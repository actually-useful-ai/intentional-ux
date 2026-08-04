---
name: intentional-ux
description: Use when evaluating or redesigning an interface, workflow, or agent capability where a person's goal, inputs, evidence of success, and avoidable interaction cost need to be made explicit.
---

# Intentional UX

Analyze an experience as a path from a person's intention to evidence that the
named outcome occurred. Prefer evidence over impressions, and preserve
uncertainty rather than compressing it into a single UX score.

## Start with a task

State one tuple for each materially different person or input mode:

```
person/input mode -> start -> outcome -> success evidence
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

Use the [accessibility review](references/accessibility-review.md) for semantic
and assistive-technology compliance, keyboard access, perception, and motion.
Route its findings back into this task graph when they change a path, outcome,
or success evidence.

Fewer visible controls improve surface economy only when discovery, keyboard
access, recovery, and user control remain equal or better. A smaller surface is
not, by itself, a better experience.

## Inspect frontend integrity

Inspect the CSS, DOM, event, focus, state, and token evidence that may explain a
cost in a task path. Create a causal finding only when the available evidence
connects an implementation condition to a changed task state or success
evidence; otherwise record the uncertainty. Use the
[frontend integrity](references/frontend-integrity.md) reference for the checks
and handoffs.

## Inspect capability experience

Treat skills, plugins, commands, and other agent capabilities as task paths when
discovery, activation, version selection, authorization, or verification affects
the outcome. An installed package is not success evidence by itself. Verify that
the intended source and version resolved, the right behavior activated, and the
person can observe the requested result. Use the
[capability experience](references/capability-experience.md) reference for
runtime, host, trigger, fallback, and source/install checks.

## Use the report contract

Write each recommendation so a person can trace it from evidence to an affected
task path, remediation, and verification. The
[report contract](references/report-contract.md) defines the required fields,
surface-preserving before/after paths, and static and optional runtime fixtures.

## Attribution

Created by Luke Steuber.
