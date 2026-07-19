# Measurement contract

Use the metric vector below to describe an experience. Report units, population,
task tuple, and evidence level with each value. Do not collapse the vector into a
single score: different measures expose different trade-offs.

| Measure | Record | Interpretation limit |
| --- | --- | --- |
| Completion | Outcome reached and success evidence obtained, by task tuple. | A completed system action without person-visible evidence may not be task completion. |
| Hit | Required, redundant, corrective, and confirmation hits. | Compare categories; do not treat every hit as equally costly. |
| Fitts | `log2(D/W + 1)` in bits. | Calculate only when distance `D` and effective target width `W` are measured for the relevant input and movement. |
| Cognitive | Decisions, memory demands, interpretation burden, and mode changes. | Describe the observed or assumed demand; do not infer it from hit count alone. |
| Wait | Duration and frequency of blocked or unproductive waiting. | Separate interface delay from voluntary reading or deliberation. |
| Recovery | Error, interruption, and lost-context paths; time and success of return. | A rare severe failure can matter more than its average rate suggests. |
| Surface | Visible controls, hierarchy, and visual competition for the task. | Fewer visible controls help only when discovery, keyboard access, recovery, and user control remain equal or better. |
| Accessibility | Barriers and alternate paths by input mode. | Route semantic and assistive-technology compliance to accessibility review. |
| Integrity | Accuracy, reversibility, consent, privacy, and consequences of error. | Do not trade integrity away merely to reduce time or hits. |

## Evidence levels

| Level | Basis | Appropriate language |
| --- | --- | --- |
| Measured | Instrumentation, timed observation, controlled test, or recorded dimensions. | “Measured completion was …” |
| Observed | Research session, inspection, or documented evaluation without a complete metric. | “Observed participants …” |
| Assumed | A stated hypothesis without direct supporting evidence. | “Assume …; validate by …” |

## Comparing alternatives

Compare alternatives against the same task tuple and success evidence. State which
vector components improve, worsen, or remain unknown, then identify the trade-off
that needs a decision. A recommendation should specify the measure it targets,
the confidence level, a regression to watch, and an acceptance check.

For example, replacing a visible command with a gesture may reduce surface
competition but can add discovery, corrective, or context-switch cost. Measure
Fitts difficulty only if its geometry is measured; otherwise label target-access
claims as observed or assumed. Include keyboard and assistive-technology paths in
the comparison through mutual accessibility review.
