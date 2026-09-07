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
    ROOT / "runtime" / "runtime-policy.json",
    ROOT / "runtime" / "agent.py",
    ROOT / "runtime" / "mcp_server.py",
    ROOT / "integrations" / "playwright" / "capture.mjs",
    ROOT / "integrations" / "figma" / "component-map.example.json",
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
    ]:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

    for path in [
        ROOT / "runtime" / "agent.py",
        ROOT / "runtime" / "mcp_server.py",
        ROOT / "scripts" / "context-manifest.py",
        ROOT / "scripts" / "uiux-agent.py",
        ROOT / "scripts" / "summarize-agent-trace.py",
    ]:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, OSError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: Python syntax/read error: {exc}")

    if not errors:
        try:
            from runtime.agent import PermissionGate, ProviderNeutralAgentHarness, ToolRegistry

            with tempfile.TemporaryDirectory() as tmp:
                project = Path(tmp)
                harness = ProviderNeutralAgentHarness(ROOT, project)
                state = harness.create_run("runtime smoke", "implementation", "branch_write")
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
                if not (project / "docs" / "uiux" / "runtime-smoke.md").exists():
                    errors.append("runtime smoke did not create scoped artifact")
                if harness.resume(state.run_id).completed_actions != state.completed_actions:
                    errors.append("checkpoint resume does not preserve completed actions")

                registry = ToolRegistry(ROOT, project)
                gate = PermissionGate(ROOT / "runtime" / "runtime-policy.json")
                allowed, _ = gate.authorize(registry.specs["release_action"], "branch_write")
                if allowed:
                    errors.append("critical release boundary incorrectly allows branch_write")
        except Exception as exc:
            errors.append(f"runtime smoke exception: {type(exc).__name__}: {exc}")

    try:
        node = subprocess.run(
            ["node", "--check", str(ROOT / "integrations" / "playwright" / "capture.mjs")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if node.returncode != 0:
            errors.append(f"playwright adapter syntax check failed: {node.stderr.strip()}")
    except FileNotFoundError:
        print("WARNING: node not available; Playwright adapter syntax check skipped")

    print("Agent runtime foundation validation")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Runtime foundation passed: context + permissions + trace/checkpoint + harness + adapter syntax")
    print("NOTE: MCP/Figma/Playwright external integrations require environment-specific end-to-end verification before production claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
