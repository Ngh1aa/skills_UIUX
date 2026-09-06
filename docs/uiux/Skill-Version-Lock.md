# Skill Version Lock

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

| Source | Role | Locked ref |
|---|---|---|
| `Ngh1aa/skills_UIUX` | released cleanup state on `main` | `22ddd2ed3352316495bef7b56467caad218cb900` |
| `nextlevelbuilder/ui-ux-pro-max-skill` | vendored design-intelligence skill/data source | `314307f156aeab0c6b567bbaa1ce4e7aabd5a636` |

## Released UI UX Pro Max integration

- Released branch: `main`
- PR: `#12`
- Integration merge commit: `130b7a2181760d98fca89fe1acf26a7bbd6794f0`
- Upstream skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Vendored skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Upstream engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Vendored engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Integration post-merge validation: GitHub Actions run `34021619346` = `success`

## Released repository cleanup

- Scope: `system`
- Type: `release / post-release verification`
- Risk: `medium`
- Mode: `production`
- Cleanup baseline: `85d53ef90c56b40c6383c2e63e03ac5d2d3ab7d8`
- Cleanup branch: `chore/reorganize-clean-repo-structure`
- Cleanup PR: `#13`
- PR head at merge: `a0bef3018655a1a08d2d1457ad57764221e1aea9`
- Merge commit: `22ddd2ed3352316495bef7b56467caad218cb900`
- PR-head validation: GitHub Actions run `34024108520` = `success`
- Post-merge validation: GitHub Actions run `34024255317` = `success`
- Release authorization: explicitly authorized by user on 2026-09-06.

Upstream comparison was rechecked during cleanup and remained pinned to `314307f156aeab0c6b567bbaa1ce4e7aabd5a636`. The vendor skill/runtime trees were not mutated by the cleanup.

Change either locked ref only after reviewing migration impact and rerunning the relevant structural, vendor-integrity, retrieval, installer/bootstrap and eval verification suite.
