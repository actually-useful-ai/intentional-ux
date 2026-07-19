#!/usr/bin/env python3
"""Fast structural checks for the Intentional UX skill contract and scenarios."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "skill": ROOT / "skills/intentional-ux/SKILL.md",
    "graph": ROOT / "skills/intentional-ux/references/task-graph.md",
    "measurement": ROOT / "skills/intentional-ux/references/measurement.md",
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
    "baseline": [
        "Scenario 1",
        "Scenario 2",
        "Required post-skill evidence",
        TUPLE,
    ],
}
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
    print("Validated 6 files: task tuple, state graph, metric contract, and two scenario artifacts.")


if __name__ == "__main__":
    main()
