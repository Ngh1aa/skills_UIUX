# Skill Version Lock

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

| Source | Role | Locked ref |
|---|---|---|
| `Ngh1aa/skills_UIUX` | released external-specialist integration | `bcfecfc3d7e36314f27adad716e393c41fe2ce9b` |
| `nextlevelbuilder/ui-ux-pro-max-skill` | vendored design-intelligence skill/data source | `314307f156aeab0c6b567bbaa1ce4e7aabd5a636` |
| `anthropics/claude-plugins-official` | Frontend Design visual-taste source | `85cce0381e7860082641b59d961a2b8c368b8b79` |
| `vercel-labs/agent-skills` | Web Design Guidelines + React Best Practices source | `063bee94c3f4df8453406c830b0a7df0f2860278` |
| `vercel-labs/web-interface-guidelines` | pinned web-interface rule source | `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1` |
| `billhector/design-skills` | design extraction/audit source | `afee427d8f1e2d9deb004a96bcaa8391c572c9f5` |
| `hueyexe/frontend-agent-skills` | UX writing/content-design source | `2841c079dd8a9c634882227194dc42e25227710d` |

## Released UI UX Pro Max integration

- PR: `#12`
- Integration merge commit: `130b7a2181760d98fca89fe1acf26a7bbd6794f0`
- Upstream skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Vendored skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Upstream engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Vendored engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Integration post-merge validation: GitHub Actions run `34021619346` = `success`

## Released repository cleanup

- Cleanup PR: `#13`
- Merge commit: `22ddd2ed3352316495bef7b56467caad218cb900`
- Cleanup release verification commit: `35673d3983f51182ed2212590f55351908b36e03`
- Post-release validation: GitHub Actions run `34024338827` = `success`

## Released external specialist integration

- Scope: `system`
- Type: `research / implementation / remediation / verification / release`
- Risk: `medium`
- Mode: `production`
- PR: `#14`
- Baseline: `35673d3983f51182ed2212590f55351908b36e03`
- Final PR head: `a1cd2a22db72c73fa04a7dcc0f52ab499ece3f22`
- Merge commit: `bcfecfc3d7e36314f27adad716e393c41fe2ce9b`
- PR-head validation: GitHub Actions run `34026738306` = `success`
- Post-merge validation: GitHub Actions run `34026784186` = `success`
- Release authorization: explicitly authorized by user on 2026-09-06.

### Adoption policy

- Anthropic, Vercel, Bill Hector and Huey sources are adapted with recorded license/provenance rather than becoming parallel orchestrators.
- Figma-specific additions introduced during the initial PR #14 implementation were removed before release and are not part of this released integration.
- External pins are used for reproducibility. Do not fetch mutable upstream `main` during project execution as a substitute for a reviewed source update.
- `vendor/external-uiux/SOURCE-LOCKS.md` is the detailed source/adoption ledger.

Changing any locked external ref requires reviewing source/license/trigger/behavior changes, resolving overlap/conflict with local skills and rerunning structural/profile/install/eval verification before release.
