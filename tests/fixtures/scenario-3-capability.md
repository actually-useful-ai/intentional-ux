# Scenario 3 output: one skill across two hosts

## Prompt

Compare the active version of a skill across a Mac and a server. Verify which
source, trigger, fallback, and task outcome each runtime uses.

## Task tuple

`Luke/Codex/Mac -> invoke named skill -> intended package resolves -> behavior
activates -> requested task completes -> result and verification are visible`

`Luke/Claude Code/server -> invoke named skill -> intended package resolves ->
behavior activates -> requested task completes -> result and verification are
visible`

## State graph

Normal route: `Start -> discovery -> resolution -> authorization -> execution ->
Outcome -> Success evidence`.

Correction route: `ambiguous name -> Corrective -> inspect active roots and
precedence -> intended package resolves`.

Recovery route: `optional capability missing -> Recovery -> documented fallback
-> execution`.

Wait route: `stale package found -> Wait -> versioned install -> resolution`.

Context switch: `runtime -> plugin directory -> Context switch -> runtime`.

Composition route: `Chef's Choice selects capability -> Intentional UX verifies
resolution and task evidence -> Exemplar sets the quality target -> domain skill
executes -> Outcome -> Success evidence`.

## Metric vector

| Measure | Scenario result | Evidence level |
| --- | --- | --- |
| Completion | Each route completes only when the intended behavior produces the requested result and visible verification. | Assumed |
| Hit | Required: invocation and authorization; Redundant: duplicate selection and repeated setup; Corrective: inspect active roots; Confirmation: visible source and result. | Observed |
| Fitts | Fitts difficulty is not calculated because distance and effective target width were not measured. | Observed |
| Cognitive | Duplicate names and unclear source ownership make it hard to know which behavior ran. | Observed |
| Wait | Install and update duration remain unknown until timed. | Assumed |
| Recovery | A missing optional tool uses a documented fallback without expanding authorization. | Assumed |
| Surface | Descriptions and status output expose trigger context, source, version, and result. | Assumed |
| Accessibility | Invocation, status, and recovery need equivalent keyboard and assistive-technology routes where a graphical host is used. | Assumed |
| Integrity | Source provenance, content parity, permission boundaries, and secret handling remain visible. | Assumed |

## Evidence levels

- **Measured:** resolved paths, commits, hashes, fixture results, and completed
  task outcomes once recorded on both hosts.
- **Observed:** manifests, active roots, descriptions, and fallback instructions
  found during inspection.
- **Assumed:** trigger behavior and cross-host equivalence until each runtime is
  invoked and the result verified.

## Accessibility handoff

Send graphical discovery, invocation status, focus, and recovery behavior to an
accessibility review for semantic and assistive-technology compliance. Return
any alternate path to this state graph.

## Surface guardrail

Fewer visible skill names help only when discovery, keyboard access, recovery,
and user control remain equal or better. Hiding a collision without fixing
runtime resolution does not improve the path.

## Acceptance checks

- Record the canonical repository and commit or release.
- Resolve exactly one intended active package on each host.
- Compare installed versions or content hashes with the source.
- Run a positive trigger, nearby negative trigger, explicit invocation, and
  neighboring-skill composition case.
- Exercise the missing-capability fallback.
- Verify that Intentional UX retains task-path and evidence ownership when
  Exemplar sets the quality target.
- Verify the requested task outcome on each supported runtime and host.
