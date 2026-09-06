# Skill Version Lock

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

| Source | Role | Locked ref |
|---|---|---|
| `Ngh1aa/skills_UIUX` | local UI/UX operating-system cleanup baseline | `85d53ef90c56b40c6383c2e63e03ac5d2d3ab7d8` |
| `nextlevelbuilder/ui-ux-pro-max-skill` | vendored design-intelligence skill/data source | `314307f156aeab0c6b567bbaa1ce4e7aabd5a636` |

## Released UI UX Pro Max integration

- Released branch: `main`
- PR: `#12`
- Integration merge commit: `130b7a2181760d98fca89fe1acf26a7bbd6794f0`
- Upstream skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Vendored skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Upstream engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Vendored engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Post-merge validation: GitHub Actions run `34021619346` = `success`

## Repository cleanup phase

- Scope: `system`
- Type: `audit / remediation`
- Risk: `medium`
- Mode: `production_candidate`
- Working branch: `chore/reorganize-clean-repo-structure`
- Local baseline: `85d53ef90c56b40c6383c2e63e03ac5d2d3ab7d8`
- Upstream comparison checked again on 2026-09-06: `main` still resolves to `314307f156aeab0c6b567bbaa1ce4e7aabd5a636`.
- Vendor rule: do not mutate `vendor/ui-ux-pro-max/` during repository cleanup.
- Release authorization: `no_release`; cleanup may create a PR but must not merge without a later explicit instruction.

The upstream ref is immutable for this phase. Change it only after reviewing upstream code/data/license/provenance/search behavior, checking whether skill/runtime boundaries moved, recording migration impact and rerunning the integration verification suite.
