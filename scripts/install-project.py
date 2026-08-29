#!/usr/bin/env python3
"""Install the correct skills_UIUX subset from a project's .uiux-profile.json.

V3 adds opt-in capability packs while preserving schema-version-1 project configs.

Examples:
  python scripts/install-project.py ../QTSC --dry-run
  python scripts/install-project.py ../QTSC
  python scripts/install-project.py ../QTSC --clean
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "profiles"
PACKS = ROOT / "packs"
CONFIG_NAME = ".uiux-profile.json"
MANIFEST_NAME = ".skills-uiux-manifest.json"
PROJECT_CONTEXT = "project-context"


def load_profile(name: str, stack: tuple[str, ...] = ()) -> list[str]:
    if name in stack:
        raise ValueError("profile inheritance cycle: " + " -> ".join((*stack, name)))
    path = PROFILES / f"{name}.json"
    if not path.exists():
        available = ", ".join(sorted(p.stem for p in PROFILES.glob("*.json")))
        raise ValueError(f"unknown profile '{name}'. Available: {available}")
    data = json.loads(path.read_text(encoding="utf-8"))
    skills: list[str] = []
    parent = data.get("extends")
    if parent:
        skills.extend(load_profile(parent, (*stack, name)))
    skills.extend(data.get("skills", []))
    return list(dict.fromkeys(skills))


def load_pack(name: str) -> list[str]:
    path = PACKS / f"{name}.json"
    if not path.exists():
        available = ", ".join(sorted(p.stem for p in PACKS.glob("*.json")))
        raise ValueError(f"unknown pack '{name}'. Available: {available}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("name") != name:
        raise ValueError(f"pack name mismatch: {name}")
    return list(dict.fromkeys(data.get("skills", [])))


def load_config(project: Path) -> dict:
    path = project / CONFIG_NAME
    if not path.exists():
        raise ValueError(f"missing {CONFIG_NAME} in {project}")
    data = json.loads(path.read_text(encoding="utf-8"))
    version = data.get("schema_version")
    if version not in {1, 2}:
        raise ValueError("schema_version must be 1 or 2")
    if not isinstance(data.get("profile"), str) or not data["profile"].strip():
        raise ValueError("profile must be a non-empty string")
    for key in ("additional_skills", "exclude_skills", "source_of_truth", "constraints"):
        value = data.get(key, [])
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"{key} must be an array of strings")
    packs = data.get("packs", [])
    if version == 1 and packs:
        raise ValueError("packs require schema_version 2")
    if not isinstance(packs, list) or not all(isinstance(item, str) for item in packs):
        raise ValueError("packs must be an array of strings")
    return data


def resolve_project_skills(config: dict) -> list[str]:
    skills = load_profile(config["profile"])
    for pack in config.get("packs", []):
        skills.extend(load_pack(pack))
    skills.extend(config.get("additional_skills", []))
    excluded = set(config.get("exclude_skills", []))
    skills = [s for s in dict.fromkeys(skills) if s not in excluded]
    if PROJECT_CONTEXT not in skills:
        skills.append(PROJECT_CONTEXT)
    if "website-delivery-pipeline" not in skills:
        raise ValueError("project profile must retain website-delivery-pipeline")
    known = {p.parent.name for p in ROOT.glob("*/SKILL.md")}
    unknown = sorted(set(skills) - known)
    if unknown:
        raise ValueError("unknown skills: " + ", ".join(unknown))
    return skills


def read_previous_manifest(destination: Path) -> set[str]:
    path = destination / MANIFEST_NAME
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return set(data.get("skills", []))
    except (json.JSONDecodeError, OSError):
        return set()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Project repository root containing .uiux-profile.json")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--clean", action="store_true", help="Remove the entire destination first, including unmanaged skills")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    config = load_config(project)
    skills = resolve_project_skills(config)
    destination = project / ".claude" / "skills"

    print(f"Project: {config.get('project', {}).get('name', project.name)}")
    print(f"Profile: {config['profile']}")
    if config.get("packs"):
        print("Packs: " + ", ".join(config["packs"]))
    print(f"Destination: {destination}")
    print(f"Skills ({len(skills)}): {', '.join(skills)}")
    if config.get("source_of_truth"):
        print("Source of truth: " + ", ".join(config["source_of_truth"]))

    if args.dry_run:
        return 0

    previous = read_previous_manifest(destination)
    if args.clean and destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)

    if not args.clean:
        for old in sorted(previous - set(skills)):
            path = destination / old
            if path.exists() and path.is_dir():
                shutil.rmtree(path)

    for skill in skills:
        src = ROOT / skill
        dst = destination / skill
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    manifest = {
        "schema_version": 2,
        "library": "Ngh1aa/skills_UIUX",
        "profile": config["profile"],
        "packs": config.get("packs", []),
        "skills": skills,
    }
    (destination / MANIFEST_NAME).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Installed successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
