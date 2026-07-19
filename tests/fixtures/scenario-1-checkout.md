# Scenario 1 output: checkout with a visible shortcut

## Prompt

Review a checkout that shows a one-tap express purchase button ahead of shipping
and payment details. Recommend how to make completion intentional.

## Task tuple

`shopper/touch -> checkout entry -> purchase recorded -> order number, receipt,
and reversible order details are visible`

`shopper/keyboard -> checkout entry -> purchase recorded -> order number,
receipt, and reversible order details are reachable and announced`

## State graph

Normal route: `Start -> shipping and payment details -> Confirmation -> Wait ->
Outcome -> Success evidence`.

Express route: `Start -> express purchase selection -> Confirmation -> Wait ->
Outcome -> Success evidence`.

Correction route: `express purchase selection -> Corrective -> shipping and
payment details -> Confirmation`.

Recovery route: `Wait timeout -> Recovery -> shipping and payment details`.

Context switch: `shipping and payment details -> Context switch -> external
payment provider -> Recovery -> shipping and payment details`.

## Metric vector

| Measure | Scenario result | Evidence level |
| --- | --- | --- |
| Completion | Success requires a recorded purchase and person-visible receipt. | Assumed |
| Hit | Required: 3–5; Redundant: unknown; Corrective: unknown; Confirmation: 1. | Assumed |
| Fitts | Fitts difficulty is not calculated because distance and effective target width are not measured. | Assumed |
| Cognitive | Express purchase obscures shipping and payment choices before confirmation. | Observed |
| Wait | Payment authorization may block progress; duration is unmeasured. | Assumed |
| Recovery | A timeout must restore entered shipping and payment details. | Assumed |
| Surface | The express control competes with shipping and payment detail discovery. | Observed |
| Accessibility | Keyboard and assistive-technology paths require review. | Assumed |
| Integrity | Confirmation and reversibility guard against an unintended purchase. | Observed |

## Evidence levels

- **Measured:** no timing, distance, or effective target width measurements are available.
- **Observed:** the visible express control precedes shipping and payment details.
- **Assumed:** the stated recovery path and hit ranges need task research.

## Accessibility handoff

Send semantic and assistive-technology compliance to accessibility review: verify
the express control's name, role, state, keyboard order, focus recovery, and
receipt announcement. Return any barrier or alternate keyboard path to this state
graph before evaluating completion.

## Surface guardrail

Showing fewer controls improves surface economy only when discovery, keyboard
access, recovery, and user control remain equal or better. The express shortcut
must not hide the shipping, payment, cancellation, or correction path.
