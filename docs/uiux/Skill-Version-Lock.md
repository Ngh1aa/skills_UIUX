# Skill Version Lock

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

| Source | Role | Locked ref |
|---|---|---|
| `Ngh1aa/skills_UIUX` | local UI/UX operating-system base used for the integration | `a2c4f4765144bcdf2648e7c2f32cdd01a0b52751` |
| `nextlevelbuilder/ui-ux-pro-max-skill` | vendored design-intelligence skill/data source | `314307f156aeab0c6b567bbaa1ce4e7aabd5a636` |

## Released integration

- Released branch: `main`
- PR: `#12`
- Integration merge commit: `130b7a2181760d98fca89fe1acf26a7bbd6794f0`
- Upstream skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Vendored skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Upstream engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Vendored engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Post-merge validation: GitHub Actions run `34021619346` = `success`

Upstream files are kept under `vendor/ui-ux-pro-max/`. Local routing, adapter, prompt, installer and evaluation changes live outside the vendor directory.

The upstream ref is immutable for this released integration. Change it only after reviewing upstream code/data/license/provenance/search behavior, checking whether skill/runtime boundaries moved, recording migration impact and rerunning the integration verification suite.
