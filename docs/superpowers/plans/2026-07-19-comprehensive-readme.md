# Comprehensive README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a task-first Intentional UX field guide that is accurate, practical, naturally written, and ready for repository distribution.

**Architecture:** `README.md` is the public entry point; it summarizes rather than duplicates the deeper references. `tests/quick_validate.py` enforces the README's stable public contract, while the existing reference documents remain the source of detail.

**Tech Stack:** Markdown, Python standard-library validation, Codex plugin JSON.

## Global Constraints

- Preserve `person/input mode -> start -> outcome -> success evidence` exactly.
- Keep Completion, Hit, Fitts, Cognitive, Wait, Recovery, Surface, Accessibility, and Integrity as a vector; never synthesize one score.
- Define Integrity as accuracy, reversibility, consent, privacy, and consequences of error.
- Describe frontend integrity separately as causal CSS, DOM, event, focus, and state inspection.
- Never claim Fitts's law was calculated without measured distance and effective width.
- Preserve the guarded direct-install behavior and avoid a universal `codex plugin` CLI claim.
- Credit Luke Steuber.

---

### Task 1: Expand and Humanize the public field guide

**Files:**
- Modify: `/Users/luke/intentional-ux/README.md`
- Modify: `/Users/luke/intentional-ux/tests/quick_validate.py`

**Interfaces:**
- Consumes: the task graph, measurement, frontend-integrity, and report-contract references.
- Produces: the public explanation and deterministic README acceptance checks.

- [ ] **Step 1: Add failing README contract checks**

Require the tuple, all nine metric labels, evidence levels, worked example, recommendation fields, accessibility routing, example prompts, repository map, validation commands, and Humanize-safe installation boundaries in `tests/quick_validate.py`.

- [ ] **Step 2: Run the validator and observe RED**

Run: `python3 tests/quick_validate.py`

Expected: FAIL with missing comprehensive README sections.

- [ ] **Step 3: Write the task-first field guide**

Replace the short README with the approved reading path and required sections from the design. Keep deeper implementation detail linked to `skills/intentional-ux/references/`.

- [ ] **Step 4: Run Humanize and manual editorial review**

Scan `README.md` for weak constructions, then inspect cadence, claims, code blocks, URLs, and technical terms manually. Preserve commands and the task tuple exactly.

- [ ] **Step 5: Run all validation**

Run: `python3 tests/quick_validate.py`

Run: `python3 /Users/luke/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .`

Expected: both commands exit 0.

- [ ] **Step 6: Commit**

Stage only `README.md`, `tests/quick_validate.py`, and the approved design/plan documents. Commit with `docs: publish Intentional UX field guide` and no co-author trailer.

### Task 2: Refresh installations and publish

**Files:**
- Update installed package copies under each machine's `~/plugins/intentional-ux`.

**Interfaces:**
- Consumes: the committed, validated repository tree.
- Produces: matching package fingerprints on Mac, Beast, and Drummer plus the public GitHub repository when credentials allow.

- [ ] **Step 1: Rebuild the release bundle from the committed tree**
- [ ] **Step 2: Install it locally, on Beast, and on Drummer through Beast**
- [ ] **Step 3: Verify matching full-tree, manifest, and skill hashes**
- [ ] **Step 4: Push the repository or report the exact remaining GitHub authorization blocker**
