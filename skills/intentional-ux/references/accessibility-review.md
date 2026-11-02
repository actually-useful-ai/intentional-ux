# Accessibility review

Build access into the task path from the first implementation. Use
[WCAG 2.2](https://www.w3.org/TR/WCAG22/) as the conformance framework, then
record user-centered evidence where a success criterion does not fully describe
whether a person can complete the task.

## Review order

1. Use native HTML semantics before Accessible Rich Internet Applications
   (ARIA). Verify names, roles, values, relationships, and state changes.
2. Complete the task with a keyboard. Check visible focus, logical order, focus
   movement, escape routes, and restoration after transient interfaces.
3. Check text alternatives, captions, contrast, non-color cues, text spacing,
   forced colors, 200% zoom, and reflow. Never let red versus green alone carry
   meaning: pair status color with text, an icon, a pattern, or position, and
   choose chart and status palettes that stay distinct under deuteranopia.
4. Prefer recognition over recall. Make state, errors, next actions, and recovery
   clear without unnecessary time pressure or interruption.
5. Respect reduced-motion preferences and provide alternatives to dragging,
   complex gestures, multiple pointers, and device motion.
6. Make consequential actions understandable, reviewable, and reversible when
   practical.

## Verification matrix

| Evidence | Check | Limitation |
| --- | --- | --- |
| Source inspection | Semantics, labels, state, focus code, hidden content, and motion. | Does not prove runtime or assistive-technology behavior. |
| Automated scan | Repeatable detectable patterns in representative states. | Cannot establish conformance or usability. |
| Keyboard | Full task with Tab, Shift+Tab, Enter, Space, Escape, and arrow keys. | Does not expose every screen-reader or visual barrier. |
| Screen reader | Names, roles, landmarks, reading order, focus, and announcements. | Results vary by browser and assistive-technology combination; record both. |
| Zoom and reflow | 200% zoom, narrow viewport, text spacing, and forced colors. | Does not assess every task or language need. |
| Color vision | Task states, charts, and errors under simulated deuteranopia, protanopia, tritanopia, and grayscale (for example, the browser's rendering emulation). Every state stays distinguishable without hue. | Simulation approximates common color vision types; it does not replace testing with people who have them. |
| User testing | Realistic tasks with disabled people using relevant input methods. | A small sample does not represent every person or context. |

## Finding record

For every barrier, record the affected people and input modes, observed
behavior, evidence type, relevant WCAG 2.2 success criterion when applicable,
classification (`normative`, `advisory`, or `supplemental`), smallest practical
remediation, and exact verification step. Mark unavailable runtime checks as
unverified.

Automated scans and source inspection provide useful evidence. Neither proves
that the experience works with assistive technology or supports a conformance
claim. Return each barrier, workaround, and alternate route to the Intentional
UX task graph.

Created by Luke Steuber.
