from __future__ import annotations

import json
import os
import shlex
import subprocess
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Protocol


PLAN_STATUSES = {"CONTINUE", "PASS", "BLOCKED", "GATE_FAIL"}
REPLAN_SIGNALS = {
    "GATE_FAIL",
    "BLOCKED",
    "NEW_RISK",
    "INVALID_ASSUMPTION",
    "TOOL_FAILURE",
    "CONTEXT_DRIFT",
}

SKIP_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".output",
    ".turbo",
    ".uiux-agent-runs",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "vendor",
}

TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".json",
    ".md",
    ".mjs",
    ".mts",
    ".scss",
    ".ts",
    ".tsx",
    ".txt",
    ".vue",
    ".yaml",
    ".yml",
}

SENSITIVE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".env.development",
    "credentials.json",
    "id_rsa",
    "id_ed25519",
    "secrets.json",
}

TOOL_ARG_HINTS: dict[str, dict[str, Any]] = {
    "read_text": {"path": "project-relative UTF-8 file path"},
    "list_files": {"path": "project-relative directory path; default '.'"},
    "write_artifact": {
        "path": "path under docs/uiux/",
        "content": "complete UTF-8 artifact content",
    },
    "write_project_file": {
        "path": "project-relative file path outside protected runtime/secret paths",
        "content": "complete UTF-8 file content",
    },
    "delete_project_file": {
        "path": "project-relative file path outside protected runtime/secret paths"
    },
    "run_project_script": {
        "script": "one package.json script name from build/test/lint/typecheck/check/validate",
        "args": "optional string array passed after --",
    },
    "run_validator": {
        "name": "validate-skills | validate-v2 | validate-runtime | validate-flows"
    },
    "release_action": {"action": "release action description; requires release authority"},
}


class ProviderError(RuntimeError):
    pass


@dataclass(frozen=True)
class GateEvidence:
    gate_id: str
    kind: str
    ref: str
    summary: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ProviderStagePlan:
    summary: str
    status: str
    signal: str | None
    reason: str
    actions: list[dict[str, Any]] = field(default_factory=list)
    gate_evidence: list[GateEvidence] = field(default_factory=list)
    provider: str = "unknown"
    model: str = "unknown"
    request_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["gate_evidence"] = [item.to_dict() for item in self.gate_evidence]
        return payload


@dataclass(frozen=True)
class ProviderStageRequest:
    goal: str
    flow_id: str
    flow_revision: int
    stage_id: str
    agent: str
    authority: str
    purpose: str
    skills: list[str]
    gates: list[dict[str, Any]]
    task_context: dict[str, Any]
    project_root: str
    context_manifest: dict[str, Any]
    observations: list[dict[str, Any]]
    tools: list[dict[str, Any]]
    round_index: int
    max_rounds: int


class ProviderAdapter(Protocol):
    name: str
    model: str

    def plan_stage(self, request: ProviderStageRequest) -> ProviderStagePlan:
        ...


def _sensitive_path(path: Path) -> bool:
    lowered = {part.lower() for part in path.parts}
    if any(part in SKIP_DIRS for part in lowered):
        return True
    name = path.name.lower()
    if name in SENSITIVE_NAMES or name.startswith(".env."):
        return True
    return any(fragment in name for fragment in ("secret", "credential", "private-key", "private_key"))


def _read_text_bounded(path: Path, limit: int) -> tuple[str, bool]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= limit:
        return text, False
    return text[:limit], True


def _project_snapshot(project_root: Path, budget: int, max_files: int = 80) -> list[dict[str, Any]]:
    if budget <= 0 or not project_root.exists():
        return []

    candidates: list[Path] = []
    for path in project_root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        try:
            relative = path.relative_to(project_root)
        except ValueError:
            continue
        if _sensitive_path(relative):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in {
            "package.json",
            "tsconfig.json",
            "next.config.js",
            "next.config.mjs",
            "vite.config.js",
            "vite.config.ts",
        }:
            continue
        candidates.append(path)

    def priority(path: Path) -> tuple[int, int, str]:
        rel = str(path.relative_to(project_root)).replace("\\", "/")
        first = 0 if rel in {"package.json", "tsconfig.json"} else 1
        second = 0 if any(part in rel for part in ("src/", "app/", "pages/", "components/", "styles/")) else 1
        return first, second, rel

    result: list[dict[str, Any]] = []
    remaining = budget
    for path in sorted(candidates, key=priority)[:max_files]:
        if remaining <= 0:
            break
        per_file = min(16000, remaining)
        try:
            text, truncated = _read_text_bounded(path, per_file)
        except OSError:
            continue
        relative = str(path.relative_to(project_root)).replace("\\", "/")
        result.append({"path": relative, "content": text, "truncated": truncated})
        remaining -= len(text)
    return result


def _routed_context(manifest: dict[str, Any], budget: int) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    remaining = budget
    for item in manifest.get("items", []):
        if remaining <= 0:
            break
        kind = str(item.get("kind", ""))
        if kind not in {"skill", "source_of_truth", "project_config"}:
            continue
        raw_path = str(item.get("path", ""))
        path = Path(raw_path)
        if not path.is_file() or _sensitive_path(path):
            continue
        per_item = min(24000, remaining)
        try:
            text, truncated = _read_text_bounded(path, per_item)
        except OSError:
            continue
        result.append(
            {
                "kind": kind,
                "path": raw_path,
                "trust": item.get("trust"),
                "content": text,
                "truncated": truncated,
            }
        )
        remaining -= len(text)
    return result


def tool_contracts(registry: Any) -> list[dict[str, Any]]:
    contracts: list[dict[str, Any]] = []
    for name, spec in sorted(registry.specs.items()):
        contracts.append(
            {
                "name": name,
                "description": spec.description,
                "risk": spec.risk,
                "required_authority": spec.required_authority,
                "side_effect": spec.side_effect,
                "args": TOOL_ARG_HINTS.get(name, {}),
            }
        )
    return contracts


def _strip_json_fence(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    return stripped


def _parse_json_text(text: str) -> dict[str, Any]:
    stripped = _strip_json_fence(text)
    try:
        payload = json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise ProviderError(f"provider did not return valid JSON: {exc}") from exc

    if isinstance(payload, dict) and isinstance(payload.get("result"), str):
        nested = _strip_json_fence(str(payload["result"]))
        try:
            payload = json.loads(nested)
        except json.JSONDecodeError:
            pass
    if not isinstance(payload, dict):
        raise ProviderError("provider response must be one JSON object")
    return payload


def _validate_plan(
    payload: dict[str, Any],
    *,
    provider: str,
    model: str,
    request_id: str | None,
    allowed_tools: set[str],
) -> ProviderStagePlan:
    if int(payload.get("schema_version", 0)) != 1:
        raise ProviderError("provider stage plan schema_version must be 1")

    summary = str(payload.get("summary", "")).strip()
    status = str(payload.get("status", "")).strip().upper()
    signal_raw = payload.get("signal")
    signal = str(signal_raw).strip().upper() if signal_raw else None
    reason = str(payload.get("reason", "")).strip()

    if not summary:
        raise ProviderError("provider stage plan summary must be non-empty")
    if status not in PLAN_STATUSES:
        raise ProviderError(f"unknown provider stage status: {status}")
    if signal is not None and signal not in REPLAN_SIGNALS:
        raise ProviderError(f"unknown provider replanning signal: {signal}")
    if status in {"CONTINUE", "PASS"} and signal is not None:
        raise ProviderError(f"status {status} must not carry a replanning signal")
    if status == "BLOCKED" and signal is None:
        signal = "BLOCKED"
    if status == "GATE_FAIL" and signal is None:
        signal = "GATE_FAIL"

    actions_raw = payload.get("actions", [])
    if not isinstance(actions_raw, list) or len(actions_raw) > 32:
        raise ProviderError("provider actions must be an array with at most 32 items")
    actions: list[dict[str, Any]] = []
    for index, action in enumerate(actions_raw):
        if not isinstance(action, dict):
            raise ProviderError(f"provider action {index} must be an object")
        if "handoff" in action:
            raise ProviderError("provider plans cannot hand off agents; Flow/Development Manager owns routing")
        tool = str(action.get("tool", "")).strip()
        if not tool or tool not in allowed_tools:
            raise ProviderError(f"provider action {index} references unavailable tool: {tool or '(empty)'}")
        args = action.get("args", {})
        if not isinstance(args, dict):
            raise ProviderError(f"provider action {index}.args must be an object")
        actions.append({"tool": tool, "args": dict(args)})

    if status == "CONTINUE" and not actions:
        raise ProviderError("CONTINUE requires at least one executable action")

    evidence_raw = payload.get("gate_evidence", [])
    if not isinstance(evidence_raw, list):
        raise ProviderError("gate_evidence must be an array")
    evidence: list[GateEvidence] = []
    for index, item in enumerate(evidence_raw):
        if not isinstance(item, dict):
            raise ProviderError(f"gate_evidence {index} must be an object")
        kind = str(item.get("kind", "")).strip()
        if kind not in {"artifact", "tool_observation", "human"}:
            raise ProviderError(f"gate_evidence {index} has invalid kind: {kind}")
        gate_id = str(item.get("gate_id", "")).strip()
        ref = str(item.get("ref", "")).strip()
        evidence_summary = str(item.get("summary", "")).strip()
        if not gate_id or not ref or not evidence_summary:
            raise ProviderError(f"gate_evidence {index} requires gate_id/ref/summary")
        evidence.append(GateEvidence(gate_id, kind, ref, evidence_summary))

    return ProviderStagePlan(
        summary=summary,
        status=status,
        signal=signal,
        reason=reason,
        actions=actions,
        gate_evidence=evidence,
        provider=provider,
        model=model,
        request_id=request_id,
    )


SYSTEM_PROMPT = """You are one specialist execution planner inside skills_UIUX Flow Agent OS.
The Development Manager already selected the Flow, active stage, agent role and skills. You MUST NOT choose a different flow, agent, handoff or hidden skill. Use only the tools supplied by the runtime and respect their authority boundary.

Work in bounded rounds. Return exactly one JSON object matching the provider-stage-plan contract, with no markdown or prose outside JSON.

Status rules:
- CONTINUE: execute the supplied actions, then the manager will call you again with fresh project state and tool observations.
- PASS: use only when every active gate has concrete evidence. A PASS must include gate_evidence for every active gate.
- BLOCKED: use when a material blocker prevents safe progress; set signal BLOCKED unless another configured replanning signal is more accurate.
- GATE_FAIL: use when evidence shows the active stage gate failed; set signal GATE_FAIL.

Evidence rules:
- artifact: ref must be an existing project-relative file after prior tool execution.
- tool_observation: ref must be an exact successful observation id supplied in the prompt.
- human: ref must be an already approved human gate id.
Never fabricate browser/rendered evidence, production state, accessibility conformance, build success, external writes or deployment. A planned action is not evidence until its result appears in a later round.

Implementation rules:
- Use write_project_file for project code/config changes and write_artifact for docs/uiux artifacts.
- Prefer focused edits and project-native structure over replacing unrelated files.
- Use run_project_script for allowlisted build/test/lint/typecheck/check/validate scripts when they exist.
- If a required capability/tool is unavailable, report BLOCKED instead of pretending success.
"""


class BaseProviderAdapter:
    name = "base"

    def __init__(
        self,
        repo_root: Path,
        model: str,
        *,
        timeout: int = 180,
        max_tokens: int = 24000,
        context_chars: int = 140000,
    ) -> None:
        self.repo_root = repo_root.resolve()
        self.model = model
        self.timeout = timeout
        self.max_tokens = max_tokens
        self.context_chars = context_chars

    def _render_prompt(self, request: ProviderStageRequest) -> str:
        routed_budget = max(20000, int(self.context_chars * 0.55))
        project_budget = max(10000, self.context_chars - routed_budget)
        routed = _routed_context(request.context_manifest, routed_budget)
        project = _project_snapshot(Path(request.project_root), project_budget)
        contract = json.loads(
            (self.repo_root / "schemas" / "provider-stage-plan.schema.json").read_text(encoding="utf-8")
        )
        payload = {
            "goal": request.goal,
            "flow": {"id": request.flow_id, "revision": request.flow_revision},
            "stage": {
                "id": request.stage_id,
                "agent": request.agent,
                "authority": request.authority,
                "purpose": request.purpose,
                "skills": request.skills,
                "gates": request.gates,
                "round": request.round_index,
                "max_rounds": request.max_rounds,
            },
            "task_context": request.task_context,
            "allowed_tools": request.tools,
            "recent_observations": request.observations[-16:],
            "routed_context": routed,
            "project_snapshot": project,
            "output_contract": contract,
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)

    def _invoke(self, prompt: str) -> tuple[str, str | None]:
        raise NotImplementedError

    def plan_stage(self, request: ProviderStageRequest) -> ProviderStagePlan:
        text, request_id = self._invoke(self._render_prompt(request))
        payload = _parse_json_text(text)
        return _validate_plan(
            payload,
            provider=self.name,
            model=self.model,
            request_id=request_id,
            allowed_tools={str(item["name"]) for item in request.tools},
        )


def _post_json(url: str, headers: dict[str, str], payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            text = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:2000]
        raise ProviderError(f"provider HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise ProviderError(f"provider network error: {exc.reason}") from exc
    try:
        result = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ProviderError("provider HTTP response was not valid JSON") from exc
    if not isinstance(result, dict):
        raise ProviderError("provider HTTP response must be a JSON object")
    return result


class OpenAIProviderAdapter(BaseProviderAdapter):
    name = "openai"

    def __init__(self, repo_root: Path, model: str | None = None, **kwargs: Any) -> None:
        super().__init__(repo_root, model or os.getenv("UIUX_OPENAI_MODEL", "gpt-5.6-sol"), **kwargs)
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        if not self.api_key:
            raise ProviderError("OPENAI_API_KEY is required for the openai provider")
        self.base_url = os.getenv("UIUX_OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")

    def _invoke(self, prompt: str) -> tuple[str, str | None]:
        schema = json.loads(
            (self.repo_root / "schemas" / "provider-stage-plan.schema.json").read_text(encoding="utf-8")
        )
        payload = {
            "model": self.model,
            "instructions": SYSTEM_PROMPT,
            "input": prompt,
            "max_output_tokens": self.max_tokens,
            "store": False,
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "uiux_stage_plan",
                    "schema": schema,
                    "strict": False,
                }
            },
        }
        result = _post_json(
            f"{self.base_url}/responses",
            {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            payload,
            self.timeout,
        )
        chunks: list[str] = []
        for item in result.get("output", []):
            if not isinstance(item, dict) or item.get("type") != "message":
                continue
            for content in item.get("content", []):
                if isinstance(content, dict) and content.get("type") == "output_text":
                    chunks.append(str(content.get("text", "")))
        text = "".join(chunks).strip()
        if not text and isinstance(result.get("output_text"), str):
            text = str(result["output_text"]).strip()
        if not text:
            raise ProviderError("OpenAI response did not contain output_text")
        return text, str(result.get("id")) if result.get("id") else None


class AnthropicProviderAdapter(BaseProviderAdapter):
    name = "anthropic"

    def __init__(self, repo_root: Path, model: str | None = None, **kwargs: Any) -> None:
        super().__init__(repo_root, model or os.getenv("UIUX_ANTHROPIC_MODEL", "claude-sonnet-5"), **kwargs)
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "")
        if not self.api_key:
            raise ProviderError("ANTHROPIC_API_KEY is required for the anthropic provider")
        self.base_url = os.getenv("UIUX_ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")

    def _invoke(self, prompt: str) -> tuple[str, str | None]:
        payload = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "system": SYSTEM_PROMPT,
            "messages": [{"role": "user", "content": prompt}],
        }
        result = _post_json(
            f"{self.base_url}/v1/messages",
            {
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            payload,
            self.timeout,
        )
        chunks: list[str] = []
        for block in result.get("content", []):
            if isinstance(block, dict) and block.get("type") == "text":
                chunks.append(str(block.get("text", "")))
        text = "".join(chunks).strip()
        if not text:
            raise ProviderError("Anthropic response did not contain a text block")
        return text, str(result.get("id")) if result.get("id") else None


class CommandProviderAdapter(BaseProviderAdapter):
    name = "command"

    def __init__(
        self,
        repo_root: Path,
        command: str | None = None,
        model: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(repo_root, model or os.getenv("UIUX_PROVIDER_MODEL", "command"), **kwargs)
        self.command = command or os.getenv("UIUX_PROVIDER_COMMAND", "")
        if not self.command:
            raise ProviderError("UIUX_PROVIDER_COMMAND or --provider-command is required for command provider")

    def _invoke(self, prompt: str) -> tuple[str, str | None]:
        argv = shlex.split(self.command)
        if not argv:
            raise ProviderError("provider command is empty")
        result = subprocess.run(
            argv,
            input=SYSTEM_PROMPT + "\n\n" + prompt,
            capture_output=True,
            text=True,
            timeout=self.timeout,
        )
        if result.returncode != 0:
            stderr = result.stderr[-2000:].strip()
            raise ProviderError(f"provider command failed ({result.returncode}): {stderr}")
        output = result.stdout.strip()
        if not output:
            raise ProviderError("provider command returned empty stdout")
        return output, None


class MockProviderAdapter:
    """Deterministic CI-only adapter. Never use it as production evidence."""

    name = "mock"
    model = "deterministic-ci"

    def plan_stage(self, request: ProviderStageRequest) -> ProviderStagePlan:
        stage = request.stage_id
        if request.round_index == 1:
            if stage == "research":
                actions = [
                    {
                        "tool": "write_artifact",
                        "args": {
                            "path": "docs/uiux/provider-research-smoke.md",
                            "content": "# Provider research smoke\n\nProject truth and IA evidence fixture.\n",
                        },
                    }
                ]
            elif stage == "design":
                actions = [
                    {
                        "tool": "write_artifact",
                        "args": {
                            "path": "docs/uiux/design-contract.md",
                            "content": "# Design Contract\n\nDeterministic provider smoke fixture.\n",
                        },
                    }
                ]
            elif stage == "implementation":
                actions = [
                    {
                        "tool": "write_project_file",
                        "args": {
                            "path": "src/uiux-provider-smoke.txt",
                            "content": "provider auto execution ok\n",
                        },
                    }
                ]
            else:
                actions = [{"tool": "read_text", "args": {"path": "src/uiux-provider-smoke.txt"}}]
            return ProviderStagePlan(
                summary=f"mock {stage} execution round",
                status="CONTINUE",
                signal=None,
                reason="execute one deterministic smoke action before gate evidence",
                actions=actions,
                provider=self.name,
                model=self.model,
            )

        observations = [item for item in request.observations if item.get("status") == "success"]
        last_observation = str(observations[-1].get("id")) if observations else ""
        artifact_by_stage = {
            "research": "docs/uiux/provider-research-smoke.md",
            "design": "docs/uiux/design-contract.md",
            "implementation": "src/uiux-provider-smoke.txt",
        }
        evidence: list[GateEvidence] = []
        for gate in request.gates:
            gate_id = str(gate.get("id", ""))
            if stage in artifact_by_stage:
                evidence.append(
                    GateEvidence(
                        gate_id,
                        "artifact",
                        artifact_by_stage[stage],
                        "deterministic smoke artifact exists",
                    )
                )
            else:
                evidence.append(
                    GateEvidence(
                        gate_id,
                        "tool_observation",
                        last_observation,
                        "deterministic smoke read completed",
                    )
                )
        return ProviderStagePlan(
            summary=f"mock {stage} gates satisfied",
            status="PASS",
            signal=None,
            reason="deterministic CI fixture",
            actions=[],
            gate_evidence=evidence,
            provider=self.name,
            model=self.model,
        )


def create_provider(
    name: str,
    repo_root: Path,
    *,
    model: str | None = None,
    command: str | None = None,
    timeout: int = 180,
    max_tokens: int = 24000,
    context_chars: int = 140000,
) -> ProviderAdapter:
    requested = (name or "auto").strip().lower()
    if requested == "auto":
        configured = os.getenv("UIUX_PROVIDER", "").strip().lower()
        if configured:
            requested = configured
        else:
            candidates: list[str] = []
            if os.getenv("OPENAI_API_KEY"):
                candidates.append("openai")
            if os.getenv("ANTHROPIC_API_KEY"):
                candidates.append("anthropic")
            if command or os.getenv("UIUX_PROVIDER_COMMAND"):
                candidates.append("command")
            if len(candidates) == 1:
                requested = candidates[0]
            elif len(candidates) > 1:
                raise ProviderError(
                    "multiple providers are configured; select --provider or set UIUX_PROVIDER explicitly"
                )
            else:
                raise ProviderError(
                    "no provider configured; set OPENAI_API_KEY, ANTHROPIC_API_KEY, or UIUX_PROVIDER_COMMAND"
                )

    kwargs = {
        "timeout": timeout,
        "max_tokens": max_tokens,
        "context_chars": context_chars,
    }
    if requested == "openai":
        return OpenAIProviderAdapter(repo_root, model=model, **kwargs)
    if requested == "anthropic":
        return AnthropicProviderAdapter(repo_root, model=model, **kwargs)
    if requested == "command":
        return CommandProviderAdapter(repo_root, command=command, model=model, **kwargs)
    if requested == "mock":
        return MockProviderAdapter()
    raise ProviderError(f"unknown provider: {requested}")
