# Frontend integrity

Use frontend evidence to identify implementation conditions that delay, block,
or make a task outcome uncertain. The purpose is a causal finding, not an
implementation-quality score and not one UX score. Keep the metric vector in
[measurement](measurement.md) separate so a defect in one dimension cannot
mask a regression in another.

## Evidence boundary and causal finding

Record the source, location, observation, and evidence level for every check.
Do not turn a style preference or a pattern match into a defect without a
task-path consequence. A causal finding has this trace:

```
evidence -> implementation condition -> affected task state -> outcome delay or risk
```

For example, an unremoved listener is not automatically harmful. It becomes a
finding when evidence shows that it acts after teardown, duplicates an action,
or otherwise changes a person’s route to outcome or success evidence. Name the
affected people and input modes rather than treating one pointer route as
universal.

## CSS and token checks

| Check | Inspect | Make a finding when | Resist false positives by |
| --- | --- | --- | --- |
| Cascade layer order | Ordered `@layer` declarations, imports, and which layer wins for the affected element. | An unintended layer precedence changes a task-relevant state, feedback, target, or recovery control. | Do not infer precedence from stylesheet filename or source order outside the declared layers. |
| Selector duplication | Repeated selectors and overlapping declarations across files or layers. | Competing declarations produce inconsistent states or hide the intended owner of a task-relevant rule. | A repeated selector is not a defect when it intentionally supplies a variant, fallback, or documented override. Compare the winning declarations. |
| Custom-property ownership | Where a token is defined, inherited, overridden, and consumed. | An ambiguous or leaking owner changes a control’s state, contrast, spacing, or feedback on the affected path. | Do not flag an inherited property merely because its definition is distant; verify its resolved value and documented scope. |

## DOM, event, focus, and state checks

| Check | Inspect | Make a finding when | Resist false positives by |
| --- | --- | --- | --- |
| Invalid DOM | Parsed DOM, framework output, and HTML content model. | Invalid nesting or element relationships alter parsing, semantics, interaction, or a recovery path. | Validate the rendered DOM; source text that appears nested can be transformed into valid output. Route semantic and assistive-technology compliance to an accessibility review. |
| Duplicate IDs | The mounted document, including conditional views and repeated components. | A duplicate ID changes a label, fragment target, scripted lookup, or accessible relationship on the task path. | A matching string in separate documents, stories, or mutually exclusive roots is not a duplicate ID in one document. |
| Event cleanup | Listener, subscription, timer, observer, and abort lifecycle at mount, update, and teardown. | A retained handler produces duplicate actions, stale feedback, memory pressure that interrupts a task, or state updates after teardown. | Do not report a listener solely because it exists; verify its ownership and whether cleanup or an `AbortController` covers its lifetime. |
| Focus restoration | Active element before a dialog, route, or destructive action and the next useful focus target after it closes or fails. | A person cannot resume, correct, or confirm the task with the current input mode. | Do not require restoration to an element that no longer exists; verify a documented, usable fallback target. Route keyboard and assistive-technology behavior to accessibility review. |
| State/DOM drift | Application state, rendered DOM, announcement, and enabled/disabled state after action, wait, failure, undo, and recovery. | The visible or announced result disagrees with the task state, leaving the person without reliable success evidence. | Compare the same moment in the same mounted view; an intentional optimistic state is not drift when it is labelled and reconciles on completion or failure. |

## Accessibility review handoff and review sequence

1. Begin with a named task tuple and its graph; inspect only evidence relevant to
   the affected state transition.
2. Perform a static review of source, computed CSS, and rendered DOM evidence.
3. Use a runtime review when a lifecycle, focus, timing, or state transition
   cannot be established statically. Runtime review is optional when static
   evidence resolves the question.
4. Route semantic and assistive-technology compliance to accessibility review,
   then return resulting barriers and alternate paths to the task graph.
5. Write the causal finding with the required fields in the
   [report contract](report-contract.md).

## Surface-preserving redesigns

Do not present fewer controls as a win merely because the visible surface is
smaller. A change helps surface economy only when discovery, keyboard access,
recovery, and user control remain equal or improve. Preserve the before/after
task path, including success evidence and correction routes, before claiming a
surface benefit.

Created by Luke Steuber.
