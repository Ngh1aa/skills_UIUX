---
name: figma-system-bridge
description: Bridges a project's canonical Design Contract and code design system with Figma variables, components, libraries and Code Connect. Use for code↔Figma design-system synchronization, Figma library generation/update, component/token reconciliation, or design-system drift where Figma tooling is available.
---

# Figma System Bridge

## Goal

Keep **Design Contract ↔ code ↔ Figma** aligned without creating a second silent source of truth.

This skill owns synchronization/reconciliation. It does not own the project's brand, visual direction, component architecture or Figma tool syntax itself.

## Source precedence

`current user request → project truth/code → passed Design Contract → explicit Figma evidence → this bridge → external workflow guidance`

When code and Figma disagree, do not silently choose one. Record the conflict, evidence, decision and migration impact.

## Capability gate

Before claiming any Figma object was read or changed, verify a real Figma connector/MCP/tool is available and authorized.

Classify result:

- `REAL` — tool read/write actually completed and returned evidence;
- `STATIC` — only a mapping/spec was produced without Figma mutation;
- `PARTIAL` — some objects could be inspected/synced but not all;
- `UNKNOWN` — Figma state could not be verified.

Never describe a static plan as a completed Figma library.

## Workflow

### 0. Discovery — read before write

1. Read project Design Contract, token sources, components and naming conventions.
2. Inspect target Figma file when tooling permits: pages, variables, styles, components and available libraries.
3. Build a code↔Figma gap matrix:
   - exists in code only;
   - exists in Figma only;
   - exists in both and agrees;
   - exists in both and conflicts.
4. Lock exact synchronization scope before mutations.

### 1. Foundations first

For writes, synchronize in dependency order:

`primitives → semantic tokens → modes/themes → typography/effects → components`

Do not create components first and hardcode values that should bind to variables.

### 2. Reuse before create

- Discover/search file and available libraries before creating a new component.
- Reuse when component API, variable model, ownership and naming are compatible.
- Extend before duplicate.
- Rebuild only when incompatibility/ownership makes reuse unsafe.

### 3. Component synchronization

For each component family:

- map code component ↔ Figma component/set;
- define variant axes and states;
- bind applicable visual properties to variables;
- keep icon/content variation out of explosive variant matrices when instance/text properties are more appropriate;
- preserve deterministic naming for idempotency and resume.

### 4. Code Connect / implementation mapping

When supported, connect Figma components to the actual project components rather than generating parallel equivalents. Treat generated React/Tailwind representations as design evidence, not mandatory project code style.

### 5. Sequential mutation + state ledger

Figma mutations are stateful. Do not parallelize them. Track created/updated object IDs or stable names in a durable ledger for long workflows.

### 6. Validate each layer

Use structural metadata/variable inspection plus screenshots where available. Do not build later components on an unverified broken token foundation.

## Required artifact

For material work create/update `docs/uiux/Figma-System-Bridge.md`:

```text
Target Figma file:
Project commit:
Design Contract version:
Tool reality: REAL/STATIC/PARTIAL/UNKNOWN

Code ↔ Figma gap matrix
| Item | Code | Figma | Status | Decision | Evidence |

Token mapping
Component mapping
Code Connect mapping
Conflicts / decisions
Validation evidence
Remaining drift
```

## Hard rules

- Inspect before edit.
- Variables/tokens before components.
- Reuse existing library/component before duplicate.
- Do not parallelize stateful Figma writes.
- Never guess Figma node/component IDs.
- Never create placeholders when the real supplied asset/design data is available.
- Do not call Figma fidelity verified without screenshot/visual comparison when that claim is material.
- Figma-generated code does not override project architecture/tokens automatically.
- No destructive cleanup by fuzzy matching.

## Progressive reference

Read [references/figma-code-system-contract.md](references/figma-code-system-contract.md) for the externally informed workflow details and source pins.

## Acceptance criteria

- Code↔Figma conflicts are explicit.
- Tool reality is truthfully labeled.
- Token/component order is dependency-safe.
- Reuse decision is documented before new component creation.
- Material Figma writes have structural and visual verification when tools support it.
- The passed project Design Contract remains canonical after synchronization.
