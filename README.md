# Intentional UX

Intentional UX examines the latency between intention and outcome. It helps product teams, designers, and frontend developers turn a journey into an inspectable task path, name avoidable interaction cost, and tie a recommendation back to its evidence.

Start with the task. Measure its path. Record the trade-offs. The deeper
implementation detail lives in the linked references.

## Reading path

1. Name the task tuple and sketch its states.
2. Report the metric vector with an evidence level for every claim.
3. Compare the current path with a proposed change, including recovery and
   success evidence.
4. Write an accountable recommendation and verify it against the named task.

## Start with a task

Use one tuple for each person or input mode when the route changes:

```text
person/input mode -> start -> outcome -> success evidence
```

Success evidence is what the person can observe to know the outcome occurred.
A completed request without visible confirmation may leave the task incomplete.

Build a state graph after naming the tuple. Include the ordinary route and any
action, wait, confirmation, corrective, recovery, context-switch, outcome,
success-evidence, or abandonment states that change effort or completion. Keep
recovery separate from correction: recovery returns a person to a usable path;
correction fixes content or a choice. The [task graph
reference](skills/intentional-ux/references/task-graph.md) covers the state and
hit categories in detail.

## Measure the path

Report a vector rather than a combined UX score. Different measures expose
different costs and trade-offs.

| Measure | Record | Limit |
| --- | --- | --- |
| Completion | Outcome reached and success evidence obtained for the task tuple. | A system action alone may not complete the person's task. |
| Hit | Required, redundant, corrective, and confirmation interactions. | Compare categories instead of treating every interaction alike. |
| Fitts | `log2(D/W + 1)` in bits. | Calculate it only when distance `D` and effective target width `W` are measured. |
| Cognitive | Decisions, memory demands, interpretation burden, and mode changes. | Do not infer it from hit count alone. |
| Wait | Duration and frequency of blocked or unproductive waiting. | Separate delay from voluntary reading or deliberation. |
| Recovery | Error, interruption, and lost-context paths. | A rare severe failure can outweigh its average rate. |
| Surface | Visible controls, hierarchy, and visual competition. | Fewer controls help only when discovery, keyboard access, recovery, and user control remain equal or better. |
| Accessibility | Barriers and alternate paths by input mode. | Bring alternate routes back into the task graph. |
| Integrity | Accuracy, reversibility, consent, privacy, and consequences of error. | Do not trade integrity away merely to reduce time or hits. |

Review integrity across accuracy, reversibility, consent, privacy, and consequences of error.

Frontend integrity is a separate causal inspection of CSS, DOM, events, focus, and state.
It connects an implementation condition to a task-path cost without redefining
the Integrity metric. Inspect a condition only when the evidence connects it to
an affected state or success evidence. See [frontend
integrity](skills/intentional-ux/references/frontend-integrity.md) for the
inspection boundary.

## State the evidence

Every finding gets one evidence level. Keep unknowns visible.

| Level | Basis | Use it when |
| --- | --- | --- |
| Measured | Instrumentation, timed observation, controlled test, or recorded dimensions. | The value has direct supporting data. |
| Observed | Research session, inspection, or documented evaluation. | The route or condition was seen without a complete metric. |
| Assumed | A plausible hypothesis without direct support. | The report says what would validate it. |

Do not present an assumed value as measured. Put Fitts's law in the report
after measurement captures the relevant geometry. The [measurement
reference](skills/intentional-ux/references/measurement.md) defines the units
and interpretation limits.

## Worked example: checkout

**Task tuple:** returning customer/keyboard -> cart -> submitted order -> order
number is visible and announced

The current graph has an address edit, a required payment confirmation, a wait
for order submission, and a recovery route if the service rejects the card.
The order number is the success evidence. A quiet page refresh after submission
would leave completion uncertain even if the request succeeded.

```text
Before: returning customer/keyboard -> cart -> payment details -> submitted order -> order number is visible and announced
After:  returning customer/keyboard -> cart -> payment details and order review -> submitted order -> order number is visible and announced
Preserved: discovery, keyboard access, recovery, user control, correction route, and success evidence
Changed: Surface competition decreases; confirmation remains; Fitts and wait stay unknown until measured.
```

| Measure | Finding | Evidence |
| --- | --- | --- |
| Completion | Unknown until the customer can see and hear the order number. | Observed |
| Hit | The required confirmation remains; an extra repeated submit is redundant. | Observed |
| Fitts | Omit the calculation until measurement captures target distance and effective width. | Assumed |
| Cognitive | A vague error message forces the customer to infer which field needs repair. | Observed |
| Wait | Submission blocks the next useful action; timing has not been recorded. | Assumed |
| Recovery | Proposed focus restoration after card rejection should preserve entered data. | Assumed |
| Surface | Keep the payment details visible while removing unrelated promotional controls. | Assumed |
| Accessibility | Keyboard and assistive-technology paths require review. | Assumed |
| Integrity | A duplicate charge risk makes the confirmation and repeat-submit guard necessary. | Observed |

Route semantic and assistive-technology compliance to an accessibility review.
Return the resulting barriers and alternate paths to the task graph, then update
the recommendation and its verification.

## Recommendation record

Each recommendation follows this record. It keeps the finding tied to people,
evidence, and an observable outcome.

| Field | Include |
| --- | --- |
| Affected people | The task tuple, input modes, and people whose route changes. |
| Outcome delay | Time, extra transitions, blocked progress, lost success evidence, or integrity risk; use `unknown` when unmeasured. |
| Evidence | Concrete source, observation, and level: Measured, Observed, or Assumed. |
| Confidence | High, medium, or low, plus what would change it. |
| Causal finding | `evidence -> implementation condition -> affected task state -> outcome delay or risk` |
| Remediation | The smallest accountable change, including ownership across design, frontend, or accessibility work. |
| Verification | An acceptance check against the stated success evidence for the listed people and input modes. |

For a control reduction, preserve a before-and-after path:

```text
Before: person/input mode -> start -> action and discovery route -> outcome -> success evidence
After:  person/input mode -> start -> action and discovery route -> outcome -> success evidence
Preserved: discovery, keyboard access, recovery, user control, correction route, and success evidence
Changed: metric-vector components, integrity trade-off, and unknowns
```

If discovery, keyboard access, recovery, or user control worsens, record the
regression instead of claiming a surface benefit. The [report
contract](skills/intentional-ux/references/report-contract.md) supplies the
full recommendation fields, fixtures, and review controls.

## Prompts to try

- Map the keyboard checkout path for a returning customer and identify where success evidence becomes uncertain.
- Compare a visible formatting menu with a swipe gesture for a touch and keyboard task path.
- Inspect dialog focus restoration after a failed destructive action and write a causal finding only if the task path changes.

## Repository map

| Path | Use |
| --- | --- |
| `skills/intentional-ux/SKILL.md` | The concise review workflow. |
| `skills/intentional-ux/references/task-graph.md` | States, transitions, and hit categories. |
| `skills/intentional-ux/references/measurement.md` | Vector definitions, units, and evidence limits. |
| `skills/intentional-ux/references/frontend-integrity.md` | Causal inspection of frontend conditions. |
| `skills/intentional-ux/references/report-contract.md` | Recommendation fields and static or runtime fixtures. |
| `tests/fixtures/` | Checkout and editor review examples. |

## Scope

Use this package to review task paths, interaction cost, evidence, and
frontend conditions that change a person's route to a confirmed outcome. It
does not replace accessibility compliance review, product research, or a
decision about integrity trade-offs.

## Contributing

Keep proposed changes traceable to a task tuple, evidence level, and success
evidence. Run the validation commands before opening a pull request.

## License

Luke has not selected a license for this repository.

## Validate a checkout

Run the structural checks and plugin validation from the repository root:

```sh
python3 tests/quick_validate.py
python3 /Users/luke/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

## Add to Codex

In the Codex app, open the Plugin Directory, choose its import option, and use
this repository's URL or a local checkout. Codex discovers the package through
`.codex-plugin/plugin.json`.

For a direct personal installation on a Codex setup that does not offer plugin
import, clone the repository, enter its directory, and create a guarded link:

```sh
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/intentional-ux" ] || [ -L "$HOME/.agents/skills/intentional-ux" ]; then
  echo "intentional-ux is already installed; leaving it unchanged"
else
  ln -s "$PWD/skills/intentional-ux" "$HOME/.agents/skills/intentional-ux"
fi
```

The guard preserves an existing file, directory, or symbolic link.

## Add to Claude Code

Add this repository as a marketplace, then install the package:

```text
/plugin marketplace add actually-useful-ai/intentional-ux
/plugin install intentional-ux@intentional-ux
```

## Attribution

Created by Luke Steuber.
