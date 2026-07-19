#!/usr/bin/env python3
"""Fast structural checks for the Intentional UX skill contract and scenarios."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "skill": ROOT / "skills/intentional-ux/SKILL.md",
    "frontend_integrity": ROOT / "skills/intentional-ux/references/frontend-integrity.md",
    "graph": ROOT / "skills/intentional-ux/references/task-graph.md",
    "measurement": ROOT / "skills/intentional-ux/references/measurement.md",
    "report_contract": ROOT / "skills/intentional-ux/references/report-contract.md",
    "baseline": ROOT / "tests/fixtures/baseline.md",
    "checkout": ROOT / "tests/fixtures/scenario-1-checkout.md",
    "editor": ROOT / "tests/fixtures/scenario-2-editor.md",
}
TUPLE = "person/input mode -> start -> outcome -> success evidence"
METRICS = (
    "Completion",
    "Hit",
    "Fitts",
    "Cognitive",
    "Wait",
    "Recovery",
    "Surface",
    "Accessibility",
    "Integrity",
)
REQUIRED = {
    "skill": [
        "name: intentional-ux",
        TUPLE,
        "completion, hit, Fitts, cognitive, wait, recovery, surface, accessibility, integrity",
        "Measured",
        "Observed",
        "Assumed",
        "semantic and assistive-technology compliance",
        "discovery, keyboard access, recovery, and user control remain equal or better",
        "frontend integrity",
        "report contract",
    ],
    "frontend_integrity": [
        "Cascade layer order",
        "Selector duplication",
        "Custom-property ownership",
        "Invalid DOM",
        "Duplicate IDs",
        "Event cleanup",
        "Focus restoration",
        "State/DOM drift",
        "causal finding",
        "Accessibility review",
    ],
    "graph": [
        "Required",
        "Redundant",
        "Corrective",
        "Confirmation",
        "Wait",
        "Context-switch",
        "Success evidence",
    ],
    "measurement": [
        "log2(D/W + 1)",
        "only when distance `D` and effective target width `W` are measured",
        "Do not collapse the vector into a single score",
        "Accessibility",
        "Integrity",
    ],
    "report_contract": [
        "Affected people",
        "Outcome delay",
        "Evidence",
        "Confidence",
        "Remediation",
        "Verification",
        "Surface-preserving before/after task path",
        "Static-review fixture",
        "Runtime-review fixture",
        "false positive",
        "optional",
    ],
    "baseline": [
        "Scenario 1",
        "Scenario 2",
        "Required post-skill evidence",
        TUPLE,
    ],
}

STATIC_FIXTURE = (
    "@layer reset, components, utilities;",
    "@layer components {",
    "--control-padding: 0.75rem;",
    "<label for=\"email\">Email</label>",
    "<input id=\"email\" type=\"email\">",
    "expect(findDuplicateIds(document)).toEqual([])",
    "expected finding: none",
)
RUNTIME_FIXTURE = (
    "Optional runtime review",
    "AbortController",
    "removeEventListener",
    "document.activeElement",
    "state/DOM drift",
    "expected finding: none",
)
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
SCENARIO_SECTIONS = (
    "## Prompt",
    "## Task tuple",
    "## State graph",
    "## Metric vector",
    "## Evidence levels",
    "## Accessibility handoff",
    "## Surface guardrail",
)
SCENARIO_PROMPTS = {
    "checkout": "one-tap express purchase button ahead of shipping and payment details",
    "editor": "replaces a visible formatting menu with a swipe gesture",
}
SCENARIO_ELEMENTS = (
    "Required",
    "Redundant",
    "Corrective",
    "Confirmation",
    "Wait",
    "Context switch",
    "Recovery",
    "Measured",
    "Observed",
    "Assumed",
    "semantic",
    "assistive-technology",
    "not calculated",
    "distance",
    "effective target width",
    "discovery, keyboard access, recovery, and user control remain equal or better",
)


def main() -> None:
    failures = []
    for name, path in FILES.items():
        if not path.is_file():
            failures.append(f"missing {path.relative_to(ROOT)}")
            continue
        content = path.read_text(encoding="utf-8")
        normalized = " ".join(content.split())
        for phrase in REQUIRED.get(name, ()):
            if phrase not in normalized:
                failures.append(f"{path.relative_to(ROOT)} missing: {phrase!r}")
        if "intended outcome" in normalized:
            failures.append(f"{path.relative_to(ROOT)} uses obsolete tuple wording")

    skill = FILES["skill"]
    if skill.is_file():
        skill_lines = skill.read_text(encoding="utf-8").splitlines()
        if not (len(skill_lines) >= 5 and skill_lines[0] == "---" and "name:" in skill_lines[1]
                and skill_lines[3] == "---"):
            failures.append("skills/intentional-ux/SKILL.md has invalid frontmatter")
        for link in ("references/frontend-integrity.md", "references/report-contract.md"):
            if link not in skill.read_text(encoding="utf-8"):
                failures.append(f"skills/intentional-ux/SKILL.md missing link: {link}")

    for fixture_name, expected in (("report_contract", STATIC_FIXTURE), ("report_contract", RUNTIME_FIXTURE)):
        path = FILES[fixture_name]
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for phrase in expected:
            if phrase not in content:
                failures.append(f"{path.relative_to(ROOT)} fixture missing: {phrase!r}")

    for path in ROOT.rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(content):
            local_target = target.split("#", maxsplit=1)[0]
            if not local_target or "://" in local_target or local_target.startswith("mailto:"):
                continue
            if not (path.parent / local_target).is_file():
                failures.append(
                    f"{path.relative_to(ROOT)} has broken local link: {target!r}"
                )

    for name in ("checkout", "editor"):
        path = FILES[name]
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        normalized = " ".join(content.split())
        for section in SCENARIO_SECTIONS:
            if section not in content:
                failures.append(f"{path.relative_to(ROOT)} missing section: {section}")
        tuple_lines = [line for line in content.splitlines() if "->" in line]
        if not any("/" in line and line.count("->") == 3 for line in tuple_lines):
            failures.append(f"{path.relative_to(ROOT)} does not instantiate a task path")
        if SCENARIO_PROMPTS[name] not in normalized:
            failures.append(f"{path.relative_to(ROOT)} does not preserve its original prompt")
        for metric in METRICS:
            if f"| {metric} |" not in content:
                failures.append(f"{path.relative_to(ROOT)} missing metric: {metric}")
        for element in SCENARIO_ELEMENTS:
            if element not in normalized:
                failures.append(f"{path.relative_to(ROOT)} missing scenario element: {element!r}")
    if failures:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(failures))
    print("Validated 8 files: references, task tuple, state graph, metric contract, and scenario artifacts.")


if __name__ == "__main__":
    main()
