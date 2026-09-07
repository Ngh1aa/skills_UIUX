#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

REQUIRED = [
    ROOT / "RUNTIME-FOUNDATION.md",
    ROOT / "runtime" / "README.md",
    ROOT / "runtime" / "TOOL-OBSERVATION-CONTRACT.md",
    ROOT / "runtime" / "runtime-policy.json",
    ROOT / "runtime" / "agent.py",
    ROOT / "runtime" / "flow.py",
    ROOT / "runtime" / "manager.py",
    ROOT / "runtime" / "mcp_server.py",
    ROOT / "schemas" / "flow.schema.json",
    ROOT / "flows" / "professional-website-redesign.json",
    ROOT / "flows" / "existing-ui-improvement.json",
    ROOT / "scripts" / "validate-flows.py",
    ROOT / "integrations" / "playwright" / "capture.mjs",
    ROOT / "integrations" / "figma" / "component-map.example.json",
    ROOT / "vendor" / "agent-runtime-intelligence" / "SOURCE-LOCKS.md",
    ROOT / "scripts" / "build-skill-discovery-index.py",
]


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED:
        if not path.exists():
            errors.append(f"missing runtime resource: {path.relative_to(ROOT)}")

    for path in [
        ROOT / "runtime" / "runtime-policy.json",
        ROOT / "runtime" / "examples" / "read-only-plan.json",
        ROOT / "integrations" / "figma" / "component-map.example.json",
        ROOT / "schemas" / "flow.schema.json",
        ROOT / "flows" / "professional-website-redesign.json",
        ROOT / "flows" / "existing-ui-improvement.json",
    ]:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

    for path in [
        ROOT / "runtime" / "agent.py",
        ROOT / "runtime" / "flow.py",
        ROOT / "runtime" / "manager.py",
        ROOT / "runtime" / "mcp_server.py",
        ROOT / "scripts" / "context-manifest.py",
        ROOT / "scripts" / "uiux-agent.py",
        ROOT / "scripts" / "summarize-agent-trace.py",
        ROOT / "scripts" / "build-skill-discovery-index.py",
        ROOT / "scripts" / "validate-flows.py",
    ]:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, OSError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: Python syntax/read error: {exc}")

    if not errors:
        try:
            from runtime.agent import PermissionGate, ProviderNeutralAgentHarness, ToolRegistry
            from runtime.manager import DevelopmentManagerAgent

            with tempfile.TemporaryDirectory() as tmp:
                project = Path(tmp)
                harness = ProviderNeutralAgentHarness(ROOT, project)

                state = harness.create_run("runtime smoke", "implementation", "branch_write")
                for skill in ("project-context", "ai-agent-coding-guardrails"):
                    if skill not in state.context.get("selected_skills", []):
                        errors.append(f"implementation default skill not enforced: {skill}")

                state = harness.execute_plan(
                    state,
                    [
                        {"tool": "write_artifact", "args": {"path": "docs/uiux/runtime-smoke.md", "content": "ok\n"}},
                        {"handoff": "qa"},
                        {"tool": "run_validator", "args": {"name": "validate-skills"}},
                    ],
                )
                if state.state != "COMPLETED":
                    errors.append(f"runtime smoke did not complete: {state.state}")
                if state.authority != "read_only":
                    errors.append("handoff to QA did not reduce implementation authority")
                for skill in ("testing-strategy", "agent-evaluation-and-reliability"):
                    if skill not in state.context.get("selected_skills", []):
                        errors.append(f"QA default skill not activated on handoff: {skill}")
                if not (project / "docs" / "uiux" / "runtime-smoke.md").exists():
                    errors.append("runtime smoke did not create scoped artifact")
                if harness.resume(state.run_id).completed_actions != state.completed_actions:
                    errors.append("checkpoint resume does not preserve completed actions")

                invalid = harness.create_run("illegal handoff smoke", "qa", "read_only")
                try:
                    harness.execute_plan(invalid, [{"handoff": "qa"}])
                    errors.append("runtime allowed a handoff target not declared by source role")
                except ValueError as exc:
                    if "is not allowed" not in str(exc):
                        errors.append(f"illegal handoff failed for unexpected reason: {exc}")

                manager = DevelopmentManagerAgent(harness)
                managed = manager.start(
                    "redesign ecommerce",
                    {"intent": "redesign", "website_type": "ecommerce", "mode": "interactive-prototype", "risk": "standard", "features": ["search"]},
                    authority="branch_write",
                )
                if managed.flow.id != "professional-website-redesign":
                    errors.append(f"development manager resolved wrong flow: {managed.flow.id}")
                research_stage = next(stage for stage in managed.flow.stages if stage.id == "research")
                if "ecommerce-website" not in research_stage.skills:
                    errors.append("development manager failed ecommerce domain skill routing")
                research_run = manager.start_stage(managed, "research")
                if research_run.authority != "read_only":
                    errors.append("research stage did not honor role max_authority")
                decision = manager.replan(managed, signal="GATE_FAIL", current_stage="qa", replan_count=0)
                if not decision.accepted or decision.target_stage != "implementation":
                    errors.append("development manager QA replan smoke failed")

                registry = ToolRegistry(ROOT, project)
                gate = PermissionGate(ROOT / "runtime" / "runtime-policy.json")
                allowed, _ = gate.authorize(registry.specs["release_action"], "branch_write")
                if allowed:
                    errors.append("critical release boundary incorrectly allows branch_write")
        except Exception as exc:
            errors.append(f"runtime smoke exception: {type(exc).__name__}: {exc}")

    if not errors:
        result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / "validate-flows.py")], cwd=ROOT, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            errors.append("flow validator failed: " + (result.stderr.strip() or result.stdout.strip()))

    try:
        node = subprocess.run(["node", "--check", str(ROOT / "integrations" / "playwright" / "capture.mjs")], cwd=ROOT, capture_output=True, text=True)
        if node.returncode != 0:
            errors.append(f"playwright adapter syntax check failed: {node.stderr.strip()}")
    except FileNotFoundError:
        print("WARNING: node not available; Playwright adapter syntax check skipped")

    if not errors:
        try:
            with tempfile.TemporaryDirectory() as tmp:
                discovery = subprocess.run(
                    [sys.executable, "-B", str(ROOT / "scripts" / "build-skill-discovery-index.py"), "--output", tmp, "--base-url", "https://example.invalid/skills"],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    timeout=120,
                )
                if discovery.returncode != 0:
                    errors.append("skill discovery index smoke failed: " + (discovery.stderr.strip() or discovery.stdout.strip()))
                else:
                    index_path = Path(tmp) / "index.json"
                    if not index_path.exists():
                        errors.append("skill discovery index smoke did not create index.json")
                    else:
                        index = json.loads(index_path.read_text(encoding="utf-8"))
                        skills = index.get("skills", [])
                        expected = sum(1 for path in ROOT.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())
                        if len(skills) != expected:
                            errors.append(f"skill discovery index count mismatch: expected {expected}, got {len(skills)}")
                        if any(not str(item.get("digest", "")).startswith("sha256:") for item in skills):
                            errors.append("skill discovery index has missing/invalid SHA-256 digest")
        except Exception as exc:
            errors.append(f"skill discovery smoke exception: {type(exc).__name__}: {exc}")

    print("Agent runtime foundation validation")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Runtime foundation passed: Flow OS + enforced role defaults/handoffs + context/permissions/trace/checkpoint + adapter/discovery syntax")
    print("NOTE: provider reasoning and external integrations still require environment-specific end-to-end verification before production claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
