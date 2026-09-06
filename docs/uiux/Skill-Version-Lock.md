# Skill Version Lock

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

## V5.2 agent runtime foundation candidate

- Latest observed `main` at phase start: `f098e6a94aaf3f026a810bc30073df67eb653cc2`
- `main` recovery dependency: PR `#16`, head `7373bf9201b7ad3d52eea2753a78809beb5b1562`
- Candidate branch: `feat/v5-2-agent-runtime-foundation`
- Candidate PR: `#17` (stacked on PR #16 recovery branch)
- Implementation commit: `69724b9fd65a8df0f56ae2c8231da2054da73346`
- Implementation push validation: GitHub Actions `34045466501` = `success`
- Runtime mode: provider-neutral; no model SDK required by core validation.
- MCP compatibility check: official MCP Python SDK v2 documentation reviewed 2026-09-06; candidate adapter uses `MCPServer` and keeps MCP optional.
- Figma integration check: official Figma MCP / Code Connect documentation reviewed 2026-09-06; Figma remains external context rather than project source-of-truth.
- Release authorization: `no_release`; this candidate does not change the released library lock on `main`.

## Released cross-functional intelligence upgrade

- `Ngh1aa/skills_UIUX` baseline: `279c9e01ca85779fa4af2d60551fb9b1e0d16111`
- Branch: `feat/cross-functional-product-growth-intelligence`
- PR: `#15`
- Implementation commit: `201642e6857dd26994002facfa70b029a35a1bc4`
- Final PR head: `1743c137849223fccdf0681b93fda156f652939a`
- Merge commit: `9591b238b1b0700aff6fed8deb79d13b6535d143`
- Implementation push validation: GitHub Actions `34032698500` = `success`
- Implementation PR validation: GitHub Actions `34032720908` = `success`
- Final-head push validation: GitHub Actions `34032869876` = `success`
- Final-head PR validation: GitHub Actions `34032872075` = `success`
- Post-merge validation: GitHub Actions `34033674244` = `success`
- Release authorization: explicitly authorized by user on 2026-09-06.

## External source locks

| Source | Role | Locked ref |
|---|---|---|
| `nextlevelbuilder/ui-ux-pro-max-skill` | vendored design-intelligence skill/data source | `314307f156aeab0c6b567bbaa1ce4e7aabd5a636` |
| `anthropics/claude-plugins-official` | Frontend Design visual-taste source | `85cce0381e7860082641b59d961a2b8c368b8b79` |
| `vercel-labs/agent-skills` | Web Design Guidelines + React Best Practices source | `063bee94c3f4df8453406c830b0a7df0f2860278` |
| `vercel-labs/web-interface-guidelines` | pinned web-interface rule source | `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1` |
| `billhector/design-skills` | design extraction/audit source | `afee427d8f1e2d9deb004a96bcaa8391c572c9f5` |
| `hueyexe/frontend-agent-skills` | UX writing/content-design source | `2841c079dd8a9c634882227194dc42e25227710d` |
| `assimovt/productskills` | product positioning/prioritization/scope/metrics source | `66f9cee5868d6daf9cf106b4a74090428d6fa83e` |
| `mindtheproduct/skills` | hard product-decision framing source | `3fb3d46092c4149d1653fc317aed77d63f2a98ca` |
| `ai-vita/skills` | page CRO + marketing copy source | `dda98df83ec242cf32c208a0a78b759f0b3e658b` |
| `rampstackco/claude-skills` | experimentation result-interpretation source | `a67dd34c609f034c0cfd736a348659bbdf1605bf` |
| `addyosmani/agent-skills` | coding context/planning/vertical-slice source | `48cb1168aeaaa70dfc2bbf709eddfa2a8ed8129a` |
| `mblode/agent-skills` | search-demand/content-briefing source | `0a639b1ef3b75aa6cc945e778fb1486def1d41bf` |

Detailed existing UI/UX provenance: `vendor/external-uiux/SOURCE-LOCKS.md`.
Detailed cross-functional provenance: `vendor/cross-functional-intelligence/SOURCE-LOCKS.md`.

## Released UI UX Pro Max integration

- PR: `#12`
- Integration merge commit: `130b7a2181760d98fca89fe1acf26a7bbd6794f0`
- Upstream skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Vendored skill tree: `a23882a2d113b30e94adb8a5d3fc35bbc690591e`
- Upstream engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Vendored engine tree: `a393798fc862de6176d0c3422c16e0dfa3425821`
- Integration post-merge validation: GitHub Actions `34021619346` = `success`

## Released repository cleanup

- Cleanup PR: `#13`
- Merge commit: `22ddd2ed3352316495bef7b56467caad218cb900`
- Cleanup release verification commit: `35673d3983f51182ed2212590f55351908b36e03`
- Post-release validation: GitHub Actions `34024338827` = `success`

## Released external UI/UX specialist integration

- PR: `#14`
- Baseline: `35673d3983f51182ed2212590f55351908b36e03`
- Final PR head: `a1cd2a22db72c73fa04a7dcc0f52ab499ece3f22`
- Merge commit: `bcfecfc3d7e36314f27adad716e393c41fe2ce9b`
- Release evidence docs commit: `279c9e01ca85779fa4af2d60551fb9b1e0d16111`
- PR-head validation: GitHub Actions `34026738306` = `success`
- Post-merge validation: GitHub Actions `34026784186` = `success`
- Final docs validation: GitHub Actions `34027027106` = `success`

## Adoption policy

- External repositories are pinned knowledge sources, not parallel lifecycle orchestrators.
- Prefer local synthesis/progressive disclosure and extend existing owners when overlap is high.
- Do not fetch mutable upstream `main` during normal project execution as a substitute for a reviewed source update.
- Time-sensitive product/search/platform/statistics claims require current verification when exact details matter.
- Changing any locked ref requires source/license/behavior diff review, overlap/conflict resolution and structural/profile/eval verification before release.
