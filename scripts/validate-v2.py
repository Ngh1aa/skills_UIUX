#!/usr/bin/env python3
"""Validate V2 profiles, eval schemas and local markdown resource links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_EVAL_KEYS = {"id", "category", "prompt", "recommended_skills", "expected_outcomes", "must_not", "rubric"}
LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|#|mailto:)([^)]+)\)")


def load_profile(name: str, stack: tuple[str, ...] = ()) -> list[str]:
    if name in stack:
        raise ValueError(" -> ".join((*stack, name)))
    path = ROOT / "profiles" / f"{name}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    skills: list[str] = []
    if data.get("extends"):
        skills.extend(load_profile(data["extends"], (*stack, name)))
    skills.extend(data.get("skills", []))
    return list(dict.fromkeys(skills))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    skill_names = {p.parent.name for p in ROOT.glob("*/SKILL.md")}

    for profile in sorted((ROOT / "profiles").glob("*.json")):
        try:
            data = json.loads(profile.read_text(encoding="utf-8"))
            if data.get("name") != profile.stem:
                errors.append(f"{profile}: name must match filename")
            resolved = load_profile(profile.stem)
            missing = sorted(set(resolved) - skill_names)
            if missing:
                errors.append(f"{profile}: missing skills {missing}")
            if len(resolved) > 30:
                warnings.append(f"{profile}: resolves to {len(resolved)} skills; consider a smaller profile")
        except (ValueError, json.JSONDecodeError, OSError) as exc:
            errors.append(f"{profile}: {exc}")

    ids: set[str] = set()
    for task in sorted((ROOT / "evals" / "tasks").glob("*.json")):
        try:
            data = json.loads(task.read_text(encoding="utf-8"))
            missing_keys = REQUIRED_EVAL_KEYS - data.keys()
            if missing_keys:
                errors.append(f"{task}: missing keys {sorted(missing_keys)}")
            if data.get("id") in ids:
                errors.append(f"{task}: duplicate eval id {data.get('id')}")
            ids.add(data.get("id"))
            unknown = sorted(set(data.get("recommended_skills", [])) - skill_names)
            if unknown:
                errors.append(f"{task}: unknown recommended skills {unknown}")
            if data.get("category") not in {"capability", "regression"}:
                errors.append(f"{task}: category must be capability or regression")
            if sum(data.get("rubric", {}).values()) != 100:
                errors.append(f"{task}: rubric weights must total 100")
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{task}: {exc}")

    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.split("#", 1)[0]
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken local link -> {raw}")

    print(f"V2: {len(skill_names)} skills, {len(list((ROOT/'profiles').glob('*.json')))} profiles, {len(ids)} eval tasks")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("V2 validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
