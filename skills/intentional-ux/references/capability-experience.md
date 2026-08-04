# Capability experience

Use this reference when a skill, plugin, command, connector, or delegated tool
lies on the path between a person's request and the requested outcome.

## Task tuple

Name runtime and host when they can change routing:

```text
person/runtime/host -> invoke capability -> intended package resolves -> behavior activates -> outcome -> success evidence
```

Include discovery, installation, resolution, authorization, execution,
verification, failure, fallback, and recovery states that change completion or
effort. A package present on disk is an intermediate state, not the outcome.

## Metric-vector interpretation

- **Completion:** the intended behavior ran and produced observable task success.
- **Hit:** setup, selection, confirmation, retry, and corrective interactions.
- **Fitts:** relevant only for a measured graphical selection target.
- **Cognitive:** naming collisions, unclear scope, hidden activation rules, or
  uncertainty about which version ran.
- **Wait:** installation, update, startup, delegation, or retry delay.
- **Recovery:** a safe path from missing, stale, incompatible, or failed
  capability to a usable route.
- **Surface:** plugin directories, command lists, prompts, descriptions, and
  status displays that help or hinder discovery.
- **Accessibility:** equivalent discovery, invocation, status, and recovery for
  relevant input modes and assistive technology.
- **Integrity:** source provenance, version accuracy, permission boundaries,
  reversibility, secret handling, and the consequences of running the wrong
  capability.

## Evidence levels

- **Measured:** resolved path, version, content hash, trace, fixture result, or
  recorded task outcome.
- **Observed:** source tree, manifest, configuration, log, or activation behavior
  inspected without a complete end-to-end measurement.
- **Assumed:** a description appears likely to route correctly or two packages
  appear equivalent without an activation test.

Do not label declared metadata as runtime proof. A manifest can state a version
that the host never loads.

## Composition ownership

Intentional UX verifies the path from discovery through the requested outcome.
Skill Auditor owns read-only evidence about structure, routing, provenance, and
source/install drift. Skill Creator owns authorized changes to canonical source,
packaging, and installation. Exemplar may raise the quality target, but a
well-presented package is not successful until the intended behavior resolves
and produces observable task success. Chef's Choice selects capabilities; that
selection is an intermediate state rather than completion evidence.

## Acceptance checks

For each supported runtime and host, verify the checks that apply:

1. The canonical source repository, commit, or release is known.
2. Resolution finds exactly one intended active package, or a documented
   precedence rule selects the expected override.
3. The installed version or content hash matches the declared source.
4. A positive trigger, a nearby negative trigger, and an explicit invocation
   route as intended.
5. Composition with a likely neighboring capability preserves ownership and
   authorization boundaries.
6. A missing optional capability follows a named fallback or produces a useful
   recovery path.
7. The requested task produces observable success evidence.

Do not require identical packages where hosts intentionally serve different
roles. Record the variant and verify its own source, routing, and outcome.

## Causal findings

Tie implementation evidence to task cost:

```text
two active packages share one skill name
-> runtime precedence is unclear
-> invocation may load stale behavior
-> the person cannot trust or reproduce the outcome
```

Prefer the smallest repair that makes the route inspectable: one source of
truth, versioned packaging, explicit projection, collision removal, or a visible
status check. Do not solve a routing problem by copying another untracked skill.

Created by Luke Steuber.
