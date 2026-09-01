# Latest 3-Prompt Redesign Pipeline

Use these versions for substantial website redesigns:

1. `MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.1.md`
2. `MASTER-PROMPT-V7.1.md`
3. `FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.1.md`

Mandatory hard gates:

```text
visual-redesign-delta-gate
media-crop-and-layout-integrity
```

## Mandatory lifecycle

```text
OLD rendered baseline
→ research/reference intelligence
→ asset/focal-point inventory
→ Redesign Delta Contract + Media/Focal Contract
→ representative composition proofs
→ Prompt 2 structural implementation
→ OLD vs NEW same-viewport proof
→ crop/layout integrity screenshot review
→ representative PASS
→ whole-site rollout
→ Prompt 3 OLD→NEW + NEW→CONTRACT + cross-page QA
→ human visual veto
→ release/deploy
→ production smoke
```

## Non-negotiable failure rules

For a substantial redesign, **do not PASS** if the visible change is primarily cosmetic:

- background/color inversion;
- font changes;
- spacing/radius/shadow updates;
- image swaps inside the same layout;
- decorative animation/gradient/glass;
- universal hero/card shell with new content.

Also **do not PASS** any media-heavy implementation when screenshots show:

- accidental head/face/garment crop;
- vertical slivers, stretched or squashed images;
- product text/price/CTA detached from its image;
- hero title clipped outside intended composition;
- large unexplained blank regions;
- media assigned to the wrong grid/column;
- mobile crop inherited blindly from desktop.

Automated success cannot override an obviously broken screenshot.

The redesign must show useful structural change in hierarchy, composition, page-role behavior, decision-object placement and/or journey while preserving validated content, URLs, business facts and working behavior.
