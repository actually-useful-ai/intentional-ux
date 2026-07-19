#!/usr/bin/env python3
"""Fast structural checks for the Intentional UX skill contract."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "skill": ROOT / "skills/intentional-ux/SKILL.md",
    "graph": ROOT / "skills/intentional-ux/references/task-graph.md",
    "measurement": ROOT / "skills/intentional-ux/references/measurement.md",
    "baseline": ROOT / "tests/fixtures/baseline.md",
}
REQUIRED = {
    "skill": [
        "name: intentional-ux",
        "person/input mode -> start -> intended outcome -> success evidence",
        "completion, hit, Fitts, cognitive, wait, recovery, surface, accessibility, integrity",
        "Measured",
        "Observed",
        "Assumed",
        "semantic and assistive-technology compliance",
        "discovery, keyboard\naccess, recovery, and user control remain equal or better",
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
        "Do not collapse the vector into a\nsingle score",
        "Accessibility",
        "Integrity",
    ],
    "baseline": [
        "Scenario 1",
        "Scenario 2",
        "Required post-skill evidence",
        "Scenario 1: pass.",
        "Scenario 2: pass.",
    ],
}


def main() -> None:
    failures = []
    for name, path in FILES.items():
        if not path.is_file():
            failures.append(f"missing {path.relative_to(ROOT)}")
            continue
        content = path.read_text(encoding="utf-8")
        for phrase in REQUIRED[name]:
            if phrase not in content:
                failures.append(f"{path.relative_to(ROOT)} missing: {phrase!r}")
    if failures:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(failures))
    print("Validated 4 files: task tuple, state graph, metric contract, and two scenarios.")


if __name__ == "__main__":
    main()
