# Elementary Visual Sanity Gate

Use this gate for substantial visual work, multi-page/whole-site UI changes, production-candidate/release work, and any remediation caused by an obvious rendered defect that previous QA missed.

This gate exists to catch elementary failures before deeper aesthetic scoring. A page that is elegant but contains invisible text, disappearing button labels, broken focus states, or a badly cropped primary subject does **not** pass visual QA.

## 1. Surface / foreground pairing — hard gate

For every changed semantic surface (`page`, `raised`, `inverse`, `footer`, `nav`, `drawer`, `modal`, `media overlay`, etc.):

- [ ] Inspect the **actual rendered background**.
- [ ] Inspect inherited/computed foreground for body text, headings, muted text, links, icons, dividers and controls on that surface.
- [ ] If a background changes light↔dark, foreground roles are reviewed in the same change; never change only the background and assume inherited text remains valid.
- [ ] No important text may be readable only after text selection/highlight.
- [ ] No foreground/background pair may collapse to effectively identical colors (for example `1:1`).
- [ ] Normal interactive labels meet the project/accessibility contrast requirement in their rendered state. Automated contrast checks are regression signals, not a formal conformance claim.
- [ ] Disabled content may follow the project's accessibility policy, but if the label is intentionally visible it must remain perceptible and must not disappear into its surface.

### Cascade/specificity check

When computed rendering differs from the intended token/component rule:

1. inspect the winning selector/cascade layer;
2. fix the true owner/specificity conflict;
3. do not add a page-local `!important` patch unless the project contract explicitly requires it;
4. recapture the rendered state.

A rule that says `color: X` in source is not evidence if a more-specific selector wins in the browser.

## 2. Interactive-state visibility — hard gate

For every changed/shared semantic control variant, inspect applicable states on the real rendered component:

`default → hover → focus-visible → active/selected → disabled → loading → success/error`

- [ ] Label/icon remains readable in every visible state.
- [ ] A state that changes foreground also changes/retains a compatible background or border context.
- [ ] Hover must never turn a dark label white while leaving a white/light surface unchanged.
- [ ] Focus-visible remains perceivable and does not depend only on a subtle color shift.
- [ ] Selected/active state does not erase label/icon contrast.
- [ ] Disabled styling communicates disabled without becoming blank/invisible.

For production-candidate/release work, prefer a small rendered/computed-style regression for state contrast in addition to screenshots.

## 3. Shared-owner coverage — hard gate

Deep visual review may sample representative pages. **Elementary sanity for a changed shared owner may not.**

If the change touches a shared header/footer/nav/button token/theme/surface/component:

- [ ] Identify every route/template where that owner renders.
- [ ] Run route smoke + elementary visibility/state checks across **all affected routes/templates**, not only a representative sample.
- [ ] Inspect at least one real rendered instance for every semantic variant and every materially different surface context (light, dark/inverse, image/overlay, disabled, etc.).

This rule prevents a shared cascade change from silently breaking the same footer/button on an entire site.

## 4. Human-subject / focal-crop integrity — hard gate when applicable

For hero/feature media containing people or another obvious focal subject:

- [ ] Inspect the actual crop at every declared target viewport/pressure point.
- [ ] `object-fit: cover` is not proof of a valid crop.
- [ ] `object-position` must be verified against the actual asset, not guessed from a generic percentage.
- [ ] Do not cut through the face, eyes, top of head, or other primary identifying feature unless the art direction intentionally requires it and the rationale is documented.
- [ ] Ensure overlays/panels do not hide the intended focal subject.
- [ ] If one source cannot survive all target crops, use responsive art direction (`<picture>`, alternate crop/asset, or layout change) rather than forcing one `cover` crop.

## 5. Rendered evidence rule

- [ ] Screenshot/capture exists.
- [ ] Screenshot/capture was actually opened/inspected.
- [ ] Known reported defect state is explicitly recaptured after remediation.
- [ ] A clean build/CI run is not substituted for visual inspection.
- [ ] If automated sanity scan and human screenshot disagree, the broken rendered screenshot wins and the phase is BLOCKED until resolved.

## 6. Failure promotion rule

If a user or reviewer catches an obvious visibility/state/crop defect that the current QA process should have caught:

1. fix the project root cause;
2. add a project-level regression/check where feasible;
3. add/update the owning library checklist/skill;
4. add a regression eval case when the failure mode is generalizable;
5. do not close the remediation as `PASSED` until the new guard itself has been exercised.

## Minimum PASS condition

`PASS` requires zero unresolved DUE-NOW P0/P1 findings from this gate. Any invisible critical text/control, disappearing interaction label, or unjustified primary-subject crop is a blocker regardless of aesthetic score or CI/build status.
