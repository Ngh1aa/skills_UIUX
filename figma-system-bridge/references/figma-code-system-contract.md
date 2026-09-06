# Figma ↔ Code System Contract — External Source Synthesis

Sources reviewed:

- OpenAI `figma-generate-library` at `openai/plugins@1e285826e604f66f7208f7ac4dba0fe8341d1f57` — `REFERENCE_ONLY` in this repository because no repository-root redistribution license was observed during review.
- Figma MCP Server Guide at `figma/mcp-server-guide@ae7e5e5f80da20f1dd7445e0c6ae5ac58a5b0bce` — Figma Developer Terms apply; beta capability guidance; `REFERENCE_ONLY`.

No upstream source text is vendored here. This is a local workflow synthesis.

## Core model

```text
project truth / code
        ↕
canonical Design Contract
        ↕
Figma variables + components + libraries
        ↕
Code Connect / implementation mapping
```

The arrows are reconciliation paths, not authority equivalence. Conflicts require an explicit decision.

## Discovery contract

Before mutation:

1. inspect code token/component sources;
2. inspect Figma pages, variables, styles and components;
3. discover libraries available to the target file when the tool supports it;
4. search existing design-system assets before creating replacements;
5. record code-only, Figma-only and conflicting items.

An empty library listing does not prove no reusable design-system asset exists if search was not performed.

## Foundation order

Prefer:

```text
primitive variables
→ semantic variables / modes
→ typography + effects
→ foundations documentation
→ components
→ component variants/properties
→ Code Connect
→ final QA
```

### Variable quality

- semantic variables should alias primitives when the design system uses that architecture;
- use explicit scopes where the platform/tool supports them;
- map code syntax to actual project token names rather than invented names;
- modes/themes should represent real project requirements, not fabricated dark mode.

## Component quality

For each component:

- auto-layout/responsive intent should be explicit;
- visual values should bind to tokens where appropriate;
- variant axes should represent meaningful component states/choices;
- use text/boolean/instance-swap style properties instead of combinatorial variants when possible;
- dependency order matters: atoms/foundations before higher-order components;
- use deterministic names and track created IDs from tool responses.

## State and resumability

Long Figma workflows can outlive one conversation context. Keep a durable state ledger with:

- run/project identifier;
- current phase/step;
- variable collections and IDs;
- pages/components/sets and IDs;
- pending validations;
- completed steps.

Never authorize deletion from a guessed/fuzzy ID.

## Tool behavior principles

When Figma MCP/connector capabilities exist:

- get structured design context for exact nodes rather than whole-file dumping;
- if response is too large, get high-level metadata then re-fetch only required nodes;
- get a screenshot for visual truth when implementing or verifying a design;
- use variable definitions/tokens rather than hardcoding values;
- reuse actual code components via Code Connect when possible;
- translate generated representation into the project's conventions instead of copying framework/style output blindly.

## QA

For Figma-generated/updated design systems verify:

- variable counts/modes/naming and unresolved bindings;
- component set/variant/property structure;
- accessibility basics such as contrast/touch/focus where applicable;
- naming consistency and duplicate objects;
- screenshots for foundations/components/pages;
- code↔Figma drift after synchronization.

A screenshot that exists but was not inspected is not visual evidence.
