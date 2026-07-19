# Baseline scenarios

These scenarios were evaluated before the `intentional-ux` skill existed. The
expected analysis contract is deliberately recorded here so the same prompts can
be checked after the skill is added.

## Scenario 1: Checkout with a visible shortcut

**Prompt:** Review a checkout that shows a one-tap express purchase button ahead
of shipping and payment details. Recommend how to make completion intentional.

**Baseline omission:** A general UX review can recommend moving or labeling the
button, but does not require a task tuple, a state graph, or completion evidence.
It may count all taps alike, omit waits and recovery, and call the reduced control
set “simpler” without checking discovery, keyboard access, recovery, or user
control. It also does not require a semantic or assistive-technology review.

## Scenario 2: Replacing a menu with a gesture

**Prompt:** Assess a mobile document editor that replaces a visible formatting
menu with a swipe gesture. Compare the experience for touch, keyboard, and
switch-access users.

**Baseline omission:** A general UX review can discuss discoverability, but does
not require input-mode-specific tasks, measured target geometry before a Fitts
claim, or an evidence level for each conclusion. It may overlook context-switch
costs, confirmation and corrective actions, and the requirement to route semantic
and assistive-technology compliance to accessibility review.

## Required post-skill evidence

For each scenario, the analysis must include:

- a `person/input mode -> start -> intended outcome -> success evidence` tuple;
- a state graph with normal, wait, confirmation, corrective, recovery, and
  context-switch paths where applicable;
- a metric vector rather than a single UX score;
- hit categories, with Fitts difficulty only if distance and effective target
  width are measured;
- evidence levels and recommendation entries that preserve uncertainty;
- an accessibility handoff for semantic and assistive-technology compliance; and
- the surface-economy condition that fewer visible controls is an improvement
  only when discovery, keyboard access, recovery, and user control remain equal
  or better.

## Post-skill recheck

**Scenario 1: pass.** The checkout analysis now separates express purchase from
the shipping-and-payment path by person and input mode, models confirmation and
recovery paths, preserves integrity trade-offs, and requires person-visible
purchase evidence before declaring completion.

**Scenario 2: pass.** The editor analysis now compares touch, keyboard, and
switch-access task tuples, records gesture discovery and context-switch costs,
allows a Fitts value only after geometry is measured, and routes semantic and
assistive-technology questions to accessibility review.
