# Report contract

Use this contract for every recommendation that follows an Intentional UX
review. It preserves uncertainty, names who bears the cost, and keeps a shorter
interface from being mistaken for a better task path. Do not combine results
into one UX score; report the relevant metric-vector components and their
trade-offs instead.

## Required recommendation fields

Every recommendation must include all of these fields.

| Field | Include |
| --- | --- |
| Affected people | The task tuple, input modes, and people whose route or success evidence changes. |
| Outcome delay | Time, extra state transitions, blocked progress, loss of success evidence, or integrity risk; use `unknown` when not measured. |
| Evidence | Concrete source, observation, and level: Measured, Observed, or Assumed. |
| Confidence | High, medium, or low, plus what evidence would raise or lower it. |
| Causal finding | `evidence -> implementation condition -> affected task state -> outcome delay or risk`; do not state causation that the evidence does not support. |
| Remediation | The smallest accountable change, including ownership when it crosses design, frontend, or accessibility work. |
| Verification | An acceptance check against the stated success evidence, including the people, input modes, and color-vision modes that must pass. |

Route semantic and assistive-technology compliance to an accessibility review.
Bring barriers, alternate paths, and compliance results back into the task graph
and this recommendation; do not describe them as a generic frontend defect.

## Surface-preserving before/after task path

For a control-reduction or hierarchy change, include this exact comparison.

```
Before: person/input mode -> start -> action and discovery route -> outcome -> success evidence
After:  person/input mode -> start -> action and discovery route -> outcome -> success evidence
Preserved: discovery, keyboard access, recovery, user control, correction route, and success evidence
Changed: metric-vector components, integrity trade-off, and unknowns
```

Fewer visible controls count as an improvement only when discovery, keyboard
access, recovery, and user control stay equal or improve. If one is worse, name
the regression and do not claim a surface gain without a decision about that
trade-off.

## Report fixtures

These fixtures are review controls, not an implementation test suite. They
demonstrate that static checks need context and that runtime checks should be
used only where lifecycle or state evidence is necessary. Each includes an
`expected finding: none` control, so a broad pattern match cannot create a false
positive.

### Static-review fixture

The following complete CSS and DOM fragment has an explicit layer order, a
documented custom-property owner, valid label relationship, and one mounted ID.
It intentionally repeats `.email-control` in a higher layer so a reviewer can
distinguish a documented cascade override from an unexamined duplicate selector.

```css
@layer reset, components, utilities;
@layer components {
  .email-control { --control-padding: 0.75rem; padding: var(--control-padding); }
}
@layer utilities {
  .email-control { --control-padding: 0.5rem; padding: var(--control-padding); }
}
```

```html
<label for="email">Email</label>
<input id="email" class="email-control" type="email">
```

```js
expect(findDuplicateIds(document)).toEqual([])
// expected finding: none
```

Token ownership: `components` owns the `--control-padding` default; `utilities` provides the documented higher-layer override for the same mounted control.

Resolved cascade: because `utilities` follows `components` in the declared layer order, its repeated `.email-control` override wins. The mounted input resolves `--control-padding` and `padding` to `0.5rem`. Expected static-review result: no finding.

Static review should produce a causal finding only after this resolved cascade,
rendered DOM, and affected task state establish a real path consequence.

### Runtime-review fixture (optional)

Optional runtime review is appropriate when a static read cannot show cleanup,
focus restoration, or reconciliation after an asynchronous task. This control
uses lifecycle ownership and a focus assertion; it is not evidence of a defect.

```js
const controller = new AbortController();
window.addEventListener("resize", onResize, { signal: controller.signal });

function dispose() {
  controller.abort();
  window.removeEventListener("resize", onResize);
}

closeDialog();
expect(document.activeElement).toBe(saveButton);
expect(renderedStatus).toBe(state.status); // state/DOM drift check
// expected finding: none
```

To turn this into a finding, reproduce a stale event after `dispose`, failed
focus restoration after the relevant route, or a rendered status that diverges
from the same state transition. Then record the causal path, the evidence level,
confidence, remediation, and verification above.

Created by Luke Steuber.
