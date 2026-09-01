# Latest 3-Prompt Redesign Pipeline

Use these versions for substantial website redesigns:

1. `MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.0.md`
2. `MASTER-PROMPT-V7.0.md`
3. `FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.0.md`

All three require `visual-redesign-delta-gate`.

## Mandatory lifecycle

```text
OLD rendered baseline
→ research/reference intelligence
→ Redesign Delta Contract
→ representative composition proofs
→ Prompt 2 structural implementation
→ OLD vs NEW same-viewport proof
→ representative PASS
→ whole-site rollout
→ Prompt 3 OLD→NEW + NEW→CONTRACT + cross-page QA
→ release/deploy
→ production smoke
```

## Non-negotiable failure rule

For a substantial redesign, **do not PASS** if the visible change is primarily:

- background/color inversion;
- font changes;
- spacing/radius/shadow updates;
- image swaps inside the same layout;
- decorative animation/gradient/glass;
- universal hero/card shell with new content.

The redesign must show useful structural change in hierarchy, composition, page-role behavior, decision-object placement and/or journey while preserving validated content, URLs, business facts and working behavior.
