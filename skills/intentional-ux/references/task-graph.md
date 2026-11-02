# Task graph

Create one graph per task tuple when people or input modes materially change the
route. Use `person/input mode -> start -> outcome -> success evidence` to name
the task before graphing it. A graph has named states and directed transitions;
it should make both completion and non-completion paths inspectable.

## States to consider

| State | Include when |
| --- | --- |
| Start | The person begins the named task. |
| Action | A person provides input that advances, selects, edits, or navigates. |
| Wait | The interface delays a useful next action or result. |
| Confirmation | The interface asks the person to verify a consequential action. |
| Corrective | The person reverses, edits, or retries after a mismatch. |
| Recovery | The person returns from an error, interruption, or lost context. |
| Context switch | The task requires leaving the current context, tool, or modality. |
| Outcome | The named outcome occurs. |
| Success evidence | The person can observe or obtain evidence that the outcome occurred. |
| Abandonment | The person exits or pauses without the named outcome. |

## Hit categories

Classify every counted interaction by its role. The same physical input can have
different roles in different task paths.

| Category | Meaning |
| --- | --- |
| Required | Necessary to reach the named outcome in the supported path. |
| Redundant | Does not advance the task, duplicate a completed action, or is avoidable. |
| Corrective | Repairs a wrong, incomplete, or misunderstood action. |
| Confirmation | Verifies a consequential action before or after it takes effect. |
| Wait | Time spent unable to make useful progress while the interface responds. |
| Context-switch | Effort to move between contexts, tools, views, or input modes. |

Count required, redundant, corrective, and confirmation hits separately. Record
wait and context-switch costs separately from hit count; they are interaction
costs, not clicks. A confirmation can be justified by integrity risk, while a
corrective hit is often a signal to inspect discovery, mapping, or feedback.

## Graph review

- Ensure every outcome path reaches success evidence or explicitly lacks it.
- Confirm that each state change and its success evidence can be perceived
  without hue. A state that differs only by color is missing for people with a
  color vision deficiency; record it as a barrier on their tuple.
- Model alternate input modes when navigation, target access, or feedback differs.
- Keep recovery distinct from correction: recovery restores a usable path;
  correction fixes task content or choice.
- Send semantic and assistive-technology compliance questions to accessibility
  review. Incorporate resulting barriers and alternate paths back into this graph.
