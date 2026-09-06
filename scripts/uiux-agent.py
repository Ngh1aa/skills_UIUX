#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.agent import ProviderNeutralAgentHarness


def main() -> int:
    parser = argparse.ArgumentParser(description="Provider-neutral skills_UIUX agent harness")
    parser.add_argument("--project", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--agent", choices=["research", "implementation", "qa"], default="research")
    parser.add_argument(
        "--authority",
        choices=["read_only", "branch_write", "external_write", "release"],
        default="read_only",
    )
    parser.add_argument("--skill", action="append", default=[])
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--plan", help="JSON file containing an actions array")
    parser.add_argument("--run-id")
    parser.add_argument("--resume")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    harness = ProviderNeutralAgentHarness(ROOT, Path(args.project))
    if args.resume:
        state = harness.resume(args.resume)
    else:
        state = harness.create_run(
            args.task,
            args.agent,
            args.authority,
            selected_skills=args.skill,
            explicit_sources=args.source,
            run_id=args.run_id,
        )

    actions = []
    if args.plan:
        payload = json.loads(Path(args.plan).read_text(encoding="utf-8"))
        actions = list(payload.get("actions", []))

    state = harness.execute_plan(state, actions, dry_run=args.dry_run)
    print(json.dumps(state.to_dict(), ensure_ascii=False, indent=2))
    return 0 if state.state == "COMPLETED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
