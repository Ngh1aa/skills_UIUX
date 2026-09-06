# Repository Structure Cleanup Audit

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

## Phase classification

- Scope: `system`
- Type: `audit / remediation`
- Risk: `medium`
- Mode: `production_candidate`
- Local cleanup baseline: `85d53ef90c56b40c6383c2e63e03ac5d2d3ab7d8`
- Upstream UI UX Pro Max comparison ref: `314307f156aeab0c6b567bbaa1ce4e7aabd5a636`
- Working branch: `chore/reorganize-clean-repo-structure`
- Release authorization: `no_release`

## Skill Activation Plan

| Task | Trigger/risk | Skill | Expected impact | Verification |
|---|---|---|---|---|
| Preserve source truth while cleaning | system-level repository change | `project-context` | avoid deleting runtime/project truth by filename guess | inspect current main + canonical docs |
| Keep context/routing lean | root/version-history clutter | `adaptive-skill-routing-and-context-budget` | reduce ambiguous active prompt surface | current canonical entrypoints remain unique |
| Remove overlap safely | skill-library maintenance | `skill-authoring-and-governance` | remove legacy/duplicate capability prose without deleting real skill packages | SKILL structure + V5 validation |
| Preserve lifecycle contracts | prompt/governance cleanup | `website-delivery-pipeline` | keep phase-aware canonical pipeline intact | latest pipeline + eval/install smoke |

## Findings

### FACT — vendor snapshot is already correctly separated

The local vendor remains split into:

- `vendor/ui-ux-pro-max/skills` = upstream `.claude/skills` tree;
- `vendor/ui-ux-pro-max/engine` = upstream `src/ui-ux-pro-max` tree.

Current tree hashes remain:

- skills: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`;
- engine: `a393798fc862de6176d0c3422c16e0dfa3425821`.

Decision: **KEEP VERBATIM**. Cleanup does not rewrite, deduplicate or reorganize files inside the vendor snapshot.

### FACT — active root contained superseded prompt history

The cleanup baseline contained multiple generations of the same three prompt families in the active root. Current canonical orchestration explicitly names only:

- `MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.2.md`;
- `MASTER-PROMPT-V7.2.md`;
- `FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.2.md`.

Decision: superseded revisions were removed from the working tree. Git history remains the historical archive.

### DRIFT/WARNING — README pointed at an obsolete implementation prompt

The pre-cleanup README described `MASTER-PROMPT-V5.0.md` as a master orchestrator while the canonical latest redesign pipeline uses `MASTER-PROMPT-V7.2.md` for implementation and `LATEST-3-PROMPT-REDESIGN-PIPELINE.md` for orchestration.

Decision: README now distinguishes library V5 from prompt versions and names only current canonical entrypoints.

### IMPROVEMENT — local repository lacked a root `.gitignore`

The upstream comparison repo ignores common OS, Python cache, editor, dependency, build, test and environment artifacts. This repository previously had no root `.gitignore`, and prior retrieval/vendor smoke work had already shown that Python cache artifacts can be generated during execution.

Decision: add a conservative root `.gitignore` without ignoring the vendored runtime.

### FACT — unrelated/legacy standalone documents were present in root

- `Mango-Ops-Technical-Proposal.md` was project-specific and unrelated to this reusable UI/UX skill library.
- `Website-Research-Generation-Architect-Skill.md` was a legacy standalone monolith, not a packaged `<skill>/SKILL.md`, and overlapped current project-context/research/audit/reference/IA/design-system/delivery routing.

Decision: both were removed from the active working tree. Their prior content remains available in Git history.

### FACT — historical architecture prose is not a runtime compatibility contract

`V2-ARCHITECTURE.md`, `V3-ARCHITECTURE.md` and `V4-ARCHITECTURE.md` described superseded architecture generations. Backward-compatible profiles/config schemas remain implemented elsewhere.

Decision: remove these historical prose files from the active root while keeping `V5-ARCHITECTURE.md` canonical.

## Upstream comparison

Useful organization principles adopted from `nextlevelbuilder/ui-ux-pro-max-skill`:

1. keep skills/runtime in explicit source boundaries instead of mixing generated/runtime data with root documentation;
2. maintain a root `.gitignore` for common generated artifacts;
3. treat `.claude/skills` as skill source and `src/ui-ux-pro-max` as searchable runtime/data source;
4. do not copy upstream repository-maintenance/plugin metadata into the local vendor runtime unless it is required by the local consumer contract.

Not copied blindly:

- upstream CLI/package/release/plugin repository structure is specific to its npm/plugin distribution model;
- `skills_UIUX` intentionally keeps local skill folders at root because existing profiles/installers/validators resolve `<skill>/SKILL.md` there.

## Cleanup actions

### KEEP

- all root `<skill>/SKILL.md` packages;
- `README.md`, `SKILL-CATALOG.md`;
- current canonical prompt trio + latest pipeline;
- phase-aware governance docs;
- `V5-ARCHITECTURE.md` and `V5-RELEASE-NOTES.md`;
- `profiles/`, `packs/`, `evals/`, `scripts/`, `examples/`, `.github/`;
- entire `vendor/ui-ux-pro-max/` snapshot unchanged.

### DELETE FROM ACTIVE WORKING TREE

- superseded Prompt 1/2/3 versions listed in `docs/history/README.md`;
- `V2-ARCHITECTURE.md`, `V3-ARCHITECTURE.md`, `V4-ARCHITECTURE.md`;
- `Website-Research-Generation-Architect-Skill.md`;
- `Mango-Ops-Technical-Proposal.md`.

### ADD / UPDATE

- `.gitignore`;
- concise canonical `README.md`;
- `docs/history/README.md`;
- this audit;
- cleanup/version-lock/phase-state evidence.

## Verification evidence

Cleanup implementation commit: `621f9cad95b495916d0bbaaca81a37226f4cdc98`.

GitHub Actions `Validate Skills` run `34024023865` completed successfully. Verified steps include:

- `validate-skills.py` structure checks;
- V5 profiles/packs/project configs/eval/resources validation;
- vendored design-intelligence integrity;
- source retrieval smoke;
- core profile installer dry run;
- installed consumer design-intelligence dependency smoke;
- project-aware installer dry run;
- project bootstrap/sync smoke;
- provider-neutral eval harness smoke.

Post-cleanup vendor tree verification:

- `vendor/ui-ux-pro-max/skills` = `a23882a2d113b30e94adb8a5d3fc35bbc690591e`;
- `vendor/ui-ux-pro-max/engine` = `a393798fc862de6176d0c3422c16e0dfa3425821`.

No vendor blob/tree changed during cleanup.

## Requirement coverage

| ID | Requirement | OWNER_PHASE | Status | Verification |
|---|---|---|---|---|
| CLEAN-001 | Compare repository structure with current pinned upstream | audit | DONE_VERIFIED | upstream/local branch + tree inspection |
| CLEAN-002 | Preserve complete UI UX Pro Max vendor skills/runtime | remediation | DONE_VERIFIED | post-change tree hashes unchanged |
| CLEAN-003 | Remove clearly superseded prompt revisions | remediation | DONE_VERIFIED | active root contains only canonical prompt revisions |
| CLEAN-004 | Remove unrelated/legacy standalone root documents | remediation | DONE_VERIFIED | commit diff/path absence |
| CLEAN-005 | Reduce generated-artifact risk | remediation | DONE_VERIFIED | root `.gitignore` added |
| CLEAN-006 | Preserve skill/profile/install/eval behavior | verification | DONE_VERIFIED | Actions run `34024023865` = success |
| CLEAN-007 | Merge cleanup to `main` | release | PENDING_FUTURE_PHASE | explicit future authorization required |

## Phase result

`PASSED`

No runtime BUG/BLOCKER was identified. This cleanup is repository hygiene plus one concrete documentation-drift fix. The remediation phase has no due-now blocker; merge remains a separately owned future release action.
