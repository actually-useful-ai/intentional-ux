---
name: intentional-ux
description: Use when evaluating or redesigning an interface flow where a person's intended outcome, inputs, evidence of success, and avoidable interaction cost need to be made explicit.
---

# Intentional UX

Analyze an experience as a path from a person's intention to evidence that the
intended outcome occurred. Prefer evidence over impressions, and preserve
uncertainty rather than compressing it into a single UX score.

## Start with a task

State one tuple for each materially different person or input mode:

```
person/input mode -> start -> intended outcome -> success evidence
```

Examples of input mode include touch, pointer, keyboard, voice, and switch
access. “Success evidence” is the observable confirmation the person needs, not
just a system state change.

Then model the path as a state graph. Include the ordinary path plus any
confirmation, wait, correction, recovery, abandonment, and context-switch
states that can change completion or effort. See
[task graph](references/task-graph.md).

## Use a metric vector

Report a vector, not a synthetic score:

```
completion, hit, Fitts, cognitive, wait, recovery, surface, accessibility, integrity
```

Mark every finding as **Measured** (instrumented data or observed dimensions),
**Observed** (seen in research or evaluation), or **Assumed** (plausible but
unverified). Do not present an assumed value as a measured result. Apply the
definitions and measurement limits in [measurement](references/measurement.md).

## Make recommendations accountable

For each recommendation, provide:

1. the affected task tuple and state transition;
2. the intended change to one or more vector measures;
3. its evidence level and the evidence needed to raise confidence;
4. a trade-off or regression risk; and
5. an acceptance check using the stated success evidence.

Route semantic and assistive-technology compliance questions to an accessibility
review, and route accessibility findings back into this task graph when they
change a path, outcome, or success evidence.

Fewer visible controls improve surface economy only when discovery, keyboard
access, recovery, and user control remain equal or better. A smaller surface is
not, by itself, a better experience.

## Attribution

Created by Luke Steuber.
