# Scenario 2 output: replacing a menu with a gesture

## Prompt

Assess a mobile document editor that replaces a visible formatting menu with a
swipe gesture. Compare the experience for touch, keyboard, and switch-access
users.

## Task tuple

`editor/touch -> document with selected text -> formatting applied -> selected
text visibly changes and the formatting state is announced`

`editor/keyboard -> document with selected text -> formatting applied -> selected
text visibly changes and the formatting state is announced`

`editor/switch access -> document with selected text -> formatting applied ->
selected text visibly changes and the formatting state is announced`

## State graph

Touch route: `Start -> gesture discovery -> gesture attempt -> Confirmation ->
Outcome -> Success evidence`.

Keyboard route: `Start -> command discovery -> keyboard command -> Confirmation
-> Outcome -> Success evidence`.

Correction route: `gesture attempt -> Corrective -> undo -> command discovery`.

Recovery route: `interrupted edit -> Recovery -> document with selected text`.

Context switch: `gesture discovery -> help content -> Context switch -> document
with selected text`.

## Metric vector

| Measure | Scenario result | Evidence level |
| --- | --- | --- |
| Completion | Formatting is complete only when the selected text changes and its state is announced. | Assumed |
| Hit | Required: unknown; Redundant: gesture exploration; Corrective: undo; Confirmation: state feedback. | Observed |
| Fitts | Fitts difficulty is not calculated because distance and effective target width are not measured. | Assumed |
| Cognitive | An undocumented gesture adds discovery and memory demand. | Observed |
| Wait | No blocked wait is documented; measure gesture recognition delay before claiming improvement. | Assumed |
| Recovery | Preserve the selection after an interrupted gesture or undo. | Assumed |
| Surface | Removing the visible menu reduces visible controls but removes a command cue. | Observed |
| Accessibility | Keyboard and switch-access alternatives need equivalent completion evidence. | Assumed |
| Integrity | Undo must restore the prior formatting without losing selected text. | Assumed |

## Evidence levels

- **Measured:** no completion, timing, distance, or effective target width data is available.
- **Observed:** the visible menu is replaced by an undocumented gesture.
- **Assumed:** keyboard, switch-access, and undo outcomes require evaluation.

## Accessibility handoff

Send semantic and assistive-technology compliance to accessibility review: verify
the keyboard command, switch-access route, formatting-state announcement, and
focus behavior. Return any barrier or alternate route to this state graph before
comparing touch completion with keyboard or switch access.

## Surface guardrail

Fewer visible controls improve surface economy only when discovery, keyboard
access, recovery, and user control remain equal or better. Keep a discoverable
keyboard and switch-access command while evaluating the gesture.
