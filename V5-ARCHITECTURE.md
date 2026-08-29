# skills_UIUX V5 Architecture — Evidence, Measurement & Reliability

V5 adds an **evidence, measurement and reliability layer** on top of V4. It does not replace V4 audience/experience strategy, V3 research/advanced UX, or the existing domain profiles.

## Core idea

`project truth → evidence provenance → success definition → minimal capability routing → design/implementation → conformance/regression verification → multi-trial agent eval → real service outcomes → continuous learning`

## Why V5 exists

A strong framework can still fail if:
- user/research claims cannot be traced to a source;
- a prettier redesign is called an UX improvement without outcome data;
- accessibility is claimed from an automated scan or a few spot checks;
- visual/design-system drift accumulates across AI-generated changes;
- every task loads too much context;
- an agent passes once and is called reliable;
- production feedback never becomes new research, tests or regression evals.

## New capability pack

`measurement-reliability` contains:
1. `evidence-provenance-and-research-ops`
2. `journey-outcome-and-service-health`
3. `brand-recognition-validation`
4. `accessibility-conformance-evaluation`
5. `visual-regression-and-design-drift`
6. `adaptive-skill-routing-and-context-budget`
7. `agent-evaluation-and-reliability`
8. `continuous-learning-and-improvement`

## When to enable

Enable for substantial redesigns, production services, repeated AI coding workflows, regulated/high-consequence journeys, mature design systems, or projects where claims such as "improved UX", "accessible", "brand-recognizable" or "reliable" need evidence.

Do not enable the whole pack for a tiny low-risk page fix. The orchestrator should still select the smallest useful graph.

## Evidence contract

Important claims should be traceable through:

`claim → source/evidence → date/context → confidence/limitations → decision → verification/outcome`

Rules:
- never upgrade an assumption into research evidence;
- stale or contradictory evidence stays visible;
- metric definitions include numerator/denominator and journey boundary where relevant;
- conformance/reliability language is reserved for methods that justify it.

## Reliability contract

Agent quality is not a single successful run.

Use:
- a **task** with explicit success criteria;
- multiple independent **trials** when reliability matters;
- deterministic graders where possible;
- model/human graders where judgment is required;
- outcome grading over brittle tool choreography;
- capability suites for frontier quality and regression suites for backslide protection.

Track pass rate plus estimated `pass@k` / `pass^k` only with the assumptions stated.

## Accessibility contract

For formal accessibility evaluation, follow a WCAG-EM-style process:
1. define scope and conformance target;
2. explore the product;
3. select representative samples and complete processes;
4. evaluate the selected sample set with appropriate manual/automated/assistive-technology methods;
5. report findings and limitations.

A partial audit is not a conformance claim.

## Measurement contract

Define success before release where possible:

`user need → service purpose → outcome → metric → data source → segment/channel → decision threshold → review cadence`

Combine performance data with user research. Measure the whole relevant journey, including offline/human handoffs when the service continues beyond the website.

## Provider-neutral eval harness

V5 adds `scripts/eval-harness.py` for task discovery, result validation and multi-trial summary. Agent execution remains adapter/provider-specific; adapters emit the documented JSONL trial contract so the library does not lock into one model vendor.

## Backward compatibility

- V2/V2.1/V3/V4 profiles remain valid.
- Schema-version-1 and schema-version-2 project configs remain valid.
- Existing skill names are unchanged.
- V5 uses the existing generic `packs` mechanism.

## Research baseline

V5 is informed by:
- W3C/WAI WCAG-EM evaluation methodology: https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/
- GOV.UK Service Standard performance measurement: https://www.gov.uk/service-manual/service-standard/point-10-define-success-publish-performance-data
- Anthropic agent evaluation guidance: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- V4 brand-recognition research baseline and project-specific research where available.
