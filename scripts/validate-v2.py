#!/usr/bin/env python3
"""Validate V2/V2.1 profiles, project configs, eval schemas and local markdown resource links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_EVAL_KEYS = {"id", "category", "prompt", "recommended_skills", "expected_outcomes", "must_not", "rubric"}
LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|#|mailto:)([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)


def load_profile(name: str, stack: tuple[str, ...] = ()) -> list[str]:
    if name in stack:
        raise ValueError("profile inheritance cycle: " + " -> ".join((*stack, name)))
    path = ROOT / "profiles" / f"{name}.json"
    if not path.exists():
        raise ValueError(f"missing parent profile {name}")
    data = json.loads(path.read_text(encoding="utf-8"))
    skills: list[str] = []
    if data.get("extends"):
        skills.extend(load_profile(data["extends"], (*stack, name)))
    skills.extend(data.get("skills", []))
    return list(dict.fromkeys(skills))


def markdown_files_for_link_check() -> list[Path]:
    files: set[Path] = set()
    for top in [ROOT / "README.md", ROOT / "V2-ARCHITECTURE.md"]:
        if top.exists():
            files.add(top)
    for pattern in [
        "*/SKILL.md", "*/references/*.md", "*/checklists/*.md", "*/examples/*.md",
        "evals/*.md", "examples/projects/*.md",
    ]:
        files.update(ROOT.glob(pattern))
    return sorted(files)


def validate_project_config(path: Path, profile_names: set[str], skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        return [f"{path.relative_to(ROOT)}: {exc}"]
    if data.get("schema_version") != 1:
        errors.append(f"{path.relative_to(ROOT)}: schema_version must be 1")
    profile = data.get("profile")
    if profile not in profile_names:
        errors.append(f"{path.relative_to(ROOT)}: unknown profile {profile}")
    for key in ("additional_skills", "exclude_skills"):
        value = data.get(key, [])
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            errors.append(f"{path.relative_to(ROOT)}: {key} must be an array of strings")
        else:
            unknown = sorted(set(value) - skill_names)
            if unknown:
                errors.append(f"{path.relative_to(ROOT)}: unknown {key} {unknown}")
    overlap = set(data.get("additional_skills", [])) & set(data.get("exclude_skills", []))
    if overlap:
        errors.append(f"{path.relative_to(ROOT)}: skills cannot be both added and excluded {sorted(overlap)}")
    for key in ("source_of_truth", "constraints"):
        value = data.get(key, [])
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            errors.append(f"{path.relative_to(ROOT)}: {key} must be an array of strings")
    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    skill_names = {p.parent.name for p in ROOT.glob("*/SKILL.md")}
    profile_paths = sorted((ROOT / "profiles").glob("*.json"))
    profile_names = {p.stem for p in profile_paths}

    for profile in profile_paths:
        try:
            data = json.loads(profile.read_text(encoding="utf-8"))
            if data.get("name") != profile.stem:
                errors.append(f"{profile.relative_to(ROOT)}: name must match filename")
            resolved = load_profile(profile.stem)
            missing = sorted(set(resolved) - skill_names)
            if missing:
                errors.append(f"{profile.relative_to(ROOT)}: missing skills {missing}")
            if len(resolved) > 30:
                warnings.append(f"{profile.relative_to(ROOT)}: resolves to {len(resolved)} skills; consider a smaller profile")
        except (ValueError, json.JSONDecodeError, OSError) as exc:
            errors.append(f"{profile.relative_to(ROOT)}: {exc}")

    project_configs = sorted(ROOT.glob("examples/projects/*/.uiux-profile.json"))
    for config in project_configs:
        errors.extend(validate_project_config(config, profile_names, skill_names))

    ids: set[str] = set()
    for task in sorted((ROOT / "evals" / "tasks").glob("*.json")):
        try:
            data = json.loads(task.read_text(encoding="utf-8"))
            missing_keys = REQUIRED_EVAL_KEYS - data.keys()
            if missing_keys:
                errors.append(f"{task.relative_to(ROOT)}: missing keys {sorted(missing_keys)}")
            task_id = data.get("id")
            if task_id in ids:
                errors.append(f"{task.relative_to(ROOT)}: duplicate eval id {task_id}")
            if task_id:
                ids.add(task_id)
            unknown = sorted(set(data.get("recommended_skills", [])) - skill_names)
            if unknown:
                errors.append(f"{task.relative_to(ROOT)}: unknown recommended skills {unknown}")
            if data.get("category") not in {"capability", "regression"}:
                errors.append(f"{task.relative_to(ROOT)}: category must be capability or regression")
            weights = data.get("rubric", {})
            if not isinstance(weights, dict) or sum(weights.values()) != 100:
                errors.append(f"{task.relative_to(ROOT)}: rubric weights must total 100")
        except (json.JSONDecodeError, OSError, TypeError) as exc:
            errors.append(f"{task.relative_to(ROOT)}: {exc}")

    for md in markdown_files_for_link_check():
        text = FENCE_RE.sub("", md.read_text(encoding="utf-8"))
        for raw in LINK_RE.findall(text):
            target = raw.split("#", 1)[0].strip()
            if not target or target.startswith("/") or any(token in target for token in ["<", ">", "{", "}"]):
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken local link -> {raw}")

    print(f"V2.1: {len(skill_names)} skills, {len(profile_paths)} profiles, {len(project_configs)} project examples, {len(ids)} eval tasks")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("V2.1 validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
