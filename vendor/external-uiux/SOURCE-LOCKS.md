# External UI/UX Source Locks

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

| Source | Reviewed ref | License / terms observed | Local adoption mode | Local capability |
|---|---|---|---|---|
| `anthropics/claude-plugins-official` → `frontend-design` | `85cce0381e7860082641b59d961a2b8c368b8b79` | Apache-2.0 in skill `LICENSE.txt` | `ADAPT_WITH_ATTRIBUTION` | `visual-design-direction` visual-taste calibration |
| `vercel-labs/agent-skills` → `web-design-guidelines`, `react-best-practices` | `063bee94c3f4df8453406c830b0a7df0f2860278` | repo/skill states MIT | `ADAPT_WITH_ATTRIBUTION` | `web-ui-code-review` |
| `vercel-labs/web-interface-guidelines` | `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1` | MIT | `ADAPT_WITH_ATTRIBUTION` | `web-ui-code-review` web-interface reference |
| `openai/plugins` → `figma-generate-library` | `1e285826e604f66f7208f7ac4dba0fe8341d1f57` | no repository-root redistribution license observed during this review | `REFERENCE_ONLY` | `figma-system-bridge` workflow concepts |
| `figma/mcp-server-guide` | `ae7e5e5f80da20f1dd7445e0c6ae5ac58a5b0bce` | Figma Developer Terms apply; beta MCP guidance | `REFERENCE_ONLY` | `figma-system-bridge` tool/quality contract |
| `billhector/design-skills` | `afee427d8f1e2d9deb004a96bcaa8391c572c9f5` | MIT | `ADAPT_WITH_ATTRIBUTION` | `reference-extraction-and-design-audit` |
| `hueyexe/frontend-agent-skills` → `ux-writing-content-design` | `2841c079dd8a9c634882227194dc42e25227710d` | MIT | `ADAPT_WITH_ATTRIBUTION` | `content-design-and-question-design` UX writing expansion |

## Source-specific decisions

### Anthropic Frontend Design

Adopted principles: ground visual choices in the subject matter; deliberately reject templated/generic visual defaults; treat typography and structural devices as information-bearing; use non-user-triggered motion sparingly; spend boldness in one memorable place; run a design-plan self-critique before code.

Not adopted as a separate orchestrator. The capability overlaps `visual-design-direction`, so it is integrated as a progressive reference instead of a duplicate skill.

### Vercel Web Design Guidelines + React Best Practices

The upstream `web-design-guidelines` skill fetches mutable `main` at review time. `skills_UIUX` rejects that behavior for reproducibility. Local review uses pinned principles/categories and project-specific evidence. React/Next guidance is conditional on actual stack detection and complements, rather than replaces, local accessibility/performance/architecture skills.

### Figma workflow

Only workflow concepts are adopted: inspect code and Figma before writes, variables/tokens before components, reuse existing libraries/components, map code↔Figma conflicts explicitly, keep mutations sequential, validate structure plus screenshots, and use Code Connect where available. No OpenAI/Figma source text is vendored here.

### Design Extractor/Auditor

Adopted as a source-attributed extraction/audit capability, but without Firecrawl as a mandatory dependency and without automatically converting every project to Tailwind. Extraction artifacts are evidence/candidates, not a new canonical Design Contract.

### UX Writing & Content Design

Adopted into the existing `content-design-and-question-design` capability. Words are treated as interaction design: task-first labels, consequence-revealing actions, complete state conversations, Avoid→Explain→Resolve errors, implementable accessibility/localization, and measurement only when stakes justify it.

## Update policy

Changing any pin requires:

1. inspect upstream diff, license/terms and trigger behavior;
2. review overlap/conflict with local skills;
3. record migration decision;
4. update affected local references/skills only when materially justified;
5. run structural validation and representative evals;
6. merge only after release authorization.
