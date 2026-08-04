#!/usr/bin/env python3
"""Fast structural checks for the Intentional UX skill contract and scenarios."""

from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CODEX_MANIFEST = ROOT / ".codex-plugin/plugin.json"
CLAUDE_MANIFEST = ROOT / ".claude-plugin/plugin.json"
MARKETPLACE = ROOT / ".claude-plugin/marketplace.json"
LICENSE = ROOT / "LICENSE"
REPOSITORY_URL = "https://github.com/actually-useful-ai/intentional-ux"
README_INTEGRITY_METRIC = (
    "integrity across accuracy, reversibility, consent, privacy, and consequences of error."
)
README_FRONTEND_INTEGRITY = (
    "Frontend integrity is a separate causal inspection of CSS, DOM, events, focus, and state."
)
TUPLE = "person/input mode -> start -> outcome -> success evidence"
README_CONTRACT = (
    "latency between intention and outcome",
    "helps product teams, designers, and frontend developers",
    TUPLE,
    "| Measured |",
    "| Observed |",
    "| Assumed |",
    "| Affected people |",
    "| Outcome delay |",
    "| Evidence |",
    "| Confidence |",
    "| Causal finding |",
    "| Remediation |",
    "| Verification |",
    "Route semantic and assistive-technology compliance to an accessibility review.",
    "skills/intentional-ux/references/accessibility-review.md",
)
README_SECTIONS = (
    "Measure the path",
    "Worked example: checkout",
    "Recommendation record",
    "Prompts to try",
    "Repository map",
    "Scope",
    "Contributing",
    "License",
    "Validate a checkout",
    "Add to Codex",
    "Add to Claude Code",
)
NO_COMBINED_SCORE = re.compile(
    r"(?:rather than|do not|never)[^.\n]*(?:combined|single|synthetic)[^.\n]*score",
    re.IGNORECASE,
)
FITTS_MEASUREMENT_GUARD = re.compile(
    r"\|\s*Fitts\s*\|[^\n]*only when[^\n]*distance[^\n]*effective target width[^\n]*measured",
    re.IGNORECASE,
)
ILLUSTRATIVE_EXAMPLE = re.compile(
    r"\billustrative\b[^.]*\bnot\b[^.]*\b(?:real|inspected)\b[^.]*\binterface\b",
    re.IGNORECASE,
)
DIRECT_INSTALL_GUARD = re.compile(
    r'if \[ -e "\$HOME/\.agents/skills/intentional-ux" \] \|\| '
    r'\[ -L "\$HOME/\.agents/skills/intentional-ux" \]; then\s+'
    r'echo "intentional-ux is already installed; leaving it unchanged"\s+else\s+'
    r'ln -s "\$PWD/skills/intentional-ux" '
    r'"\$HOME/\.agents/skills/intentional-ux"\s+fi',
    re.MULTILINE,
)
README_PROMPTS = (
    "Map the keyboard checkout path for a returning customer and identify where success evidence becomes uncertain.",
    "Compare a visible formatting menu with a swipe gesture for a touch and keyboard task path.",
    "Inspect dialog focus restoration after a failed destructive action and write a causal finding only if the task path changes.",
    "Compare the active version of a skill across two hosts and verify which source, trigger, fallback, and task outcome each runtime uses.",
)
README_HUMANIZE_BANS = (
    "AI-powered",
    "AI-enhanced",
    "AI-driven",
)
FILES = {
    "skill": ROOT / "skills/intentional-ux/SKILL.md",
    "frontend_integrity": ROOT / "skills/intentional-ux/references/frontend-integrity.md",
    "accessibility_review": ROOT / "skills/intentional-ux/references/accessibility-review.md",
    "graph": ROOT / "skills/intentional-ux/references/task-graph.md",
    "measurement": ROOT / "skills/intentional-ux/references/measurement.md",
    "report_contract": ROOT / "skills/intentional-ux/references/report-contract.md",
    "capability_experience": ROOT / "skills/intentional-ux/references/capability-experience.md",
    "baseline": ROOT / "tests/fixtures/baseline.md",
    "checkout": ROOT / "tests/fixtures/scenario-1-checkout.md",
    "editor": ROOT / "tests/fixtures/scenario-2-editor.md",
    "capability": ROOT / "tests/fixtures/scenario-3-capability.md",
}
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
        "capability experience",
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
    "accessibility_review": [
        "WCAG 2.2",
        "Keyboard",
        "Screen reader",
        "User testing",
        "Neither proves",
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
    "capability_experience": [
        "person/runtime/host -> invoke capability -> intended package resolves -> behavior activates -> outcome -> success evidence",
        "canonical source repository, commit, or release",
        "positive trigger",
        "nearby negative trigger",
        "missing optional capability",
        "observable success evidence",
    ],
    "baseline": [
        "Scenario 1",
        "Scenario 2",
        "Required post-skill evidence",
        TUPLE,
    ],
    "capability": [
        "Luke/Codex/Mac",
        "Luke/Claude Code/server",
        "exactly one intended active package",
        "positive trigger",
        "nearby negative trigger",
        "missing-capability fallback",
        "requested task outcome",
    ],
}

STATIC_FIXTURE = (
    "@layer reset, components, utilities;",
    "@layer components {",
    "@layer utilities {",
    ".email-control {",
    "--control-padding: 0.75rem;",
    "--control-padding: 0.5rem;",
    "padding: var(--control-padding);",
    "<label for=\"email\">Email</label>",
    "<input id=\"email\" class=\"email-control\" type=\"email\">",
    "expect(findDuplicateIds(document)).toEqual([])",
    "expected finding: none",
)
STATIC_REPEAT_OVERRIDE = re.compile(
    r"@layer components \{\s+\.email-control \{\s+"
    r"--control-padding: 0\.75rem;\s+padding: var\(--control-padding\);\s+\}\s+\}"
    r"\s+@layer utilities \{\s+\.email-control \{\s+"
    r"--control-padding: 0\.5rem;\s+padding: var\(--control-padding\);\s+\}\s+\}",
    re.MULTILINE,
)
STATIC_RESOLVED_EXPECTATION = (
    "Resolved cascade: because `utilities` follows `components` in the declared layer "
    "order, its repeated `.email-control` override wins. The mounted input resolves "
    "`--control-padding` and `padding` to `0.5rem`. Expected static-review result: "
    "no finding."
)
STATIC_TOKEN_OWNERSHIP = (
    "Token ownership: `components` owns the `--control-padding` default; `utilities` "
    "provides the documented higher-layer override for the same mounted control."
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
    "capability": "active version of a skill across a Mac and a server",
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


def markdown_section(content: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^##\s|\Z)",
        content,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else ""


def markdown_table_rows(section: str) -> dict[str, tuple[str, str]]:
    rows = {}
    for line in section.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0] in {"Measure", "---"}:
            continue
        rows[cells[0]] = (cells[1], cells[2])
    return rows


def main() -> None:
    failures = []

    manifests = {}
    for name, path in (
        ("Codex manifest", CODEX_MANIFEST),
        ("Claude manifest", CLAUDE_MANIFEST),
        ("marketplace", MARKETPLACE),
    ):
        try:
            manifests[name] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"{name} is missing or invalid JSON: {error}")

    codex = manifests.get("Codex manifest", {})
    claude = manifests.get("Claude manifest", {})
    marketplace = manifests.get("marketplace", {})
    marketplace_plugins = marketplace.get("plugins", [])
    marketplace_plugin = marketplace_plugins[0] if len(marketplace_plugins) == 1 else {}
    if len(marketplace_plugins) != 1:
        failures.append("marketplace must contain exactly one plugin")
    for field in ("name", "version", "description"):
        values = {
            "Codex manifest": codex.get(field),
            "Claude manifest": claude.get(field),
            "marketplace plugin": marketplace_plugin.get(field),
        }
        if len(set(values.values())) != 1 or None in values.values():
            failures.append(f"manifest {field} values do not match: {values}")
    default_prompt = codex.get("interface", {}).get("defaultPrompt")
    if not (
        isinstance(default_prompt, list)
        and default_prompt
        and all(isinstance(prompt, str) and prompt.strip() for prompt in default_prompt)
    ):
        failures.append("Codex interface.defaultPrompt must be a non-empty string array")
    if marketplace_plugin.get("source") != "./":
        failures.append("marketplace plugin source must be './'")
    for name, manifest in (("Codex manifest", codex), ("Claude manifest", claude)):
        if manifest.get("license") != "MIT":
            failures.append(f"{name} license must be MIT")
        if manifest.get("homepage") != REPOSITORY_URL:
            failures.append(f"{name} homepage must be {REPOSITORY_URL}")
        if manifest.get("repository") != REPOSITORY_URL:
            failures.append(f"{name} repository must be {REPOSITORY_URL}")
    if marketplace_plugin.get("homepage") != REPOSITORY_URL:
        failures.append(f"marketplace plugin homepage must be {REPOSITORY_URL}")

    try:
        license_text = LICENSE.read_text(encoding="utf-8")
    except OSError as error:
        failures.append(f"LICENSE is missing: {error}")
    else:
        for phrase in ("MIT License", "Copyright (c) 2026 Luke Steuber", "Permission is hereby granted"):
            if phrase not in license_text:
                failures.append(f"LICENSE missing: {phrase!r}")

    try:
        readme = README.read_text(encoding="utf-8")
    except OSError as error:
        failures.append(f"README.md is missing: {error}")
    else:
        if "will be added in a later change" in readme:
            failures.append("README.md still claims the substantive skill is future work")
        if README_INTEGRITY_METRIC not in readme:
            failures.append(
                "README.md must define the Integrity metric as accuracy, reversibility, "
                "consent, privacy, and consequences of error"
            )
        if README_FRONTEND_INTEGRITY not in readme:
            failures.append(
                "README.md must describe frontend integrity as a separate causal inspection"
            )
        if "frontend integrity across" in readme.lower():
            failures.append(
                "README.md must not conflate frontend integrity with the Integrity metric"
            )
        for phrase in README_CONTRACT:
            if phrase not in readme:
                failures.append(f"README.md missing field-guide contract: {phrase!r}")
        for prompt in README_PROMPTS:
            if prompt not in readme:
                failures.append(f"README.md missing example prompt: {prompt!r}")
        for banned in README_HUMANIZE_BANS:
            if banned in readme:
                failures.append(f"README.md contains disallowed editorial construction: {banned!r}")

        sections = {heading: markdown_section(readme, heading) for heading in README_SECTIONS}
        for heading, content in sections.items():
            if not content:
                failures.append(f"README.md missing or empty section: {heading!r}")

        measure_section = sections["Measure the path"]
        measure_rows = markdown_table_rows(measure_section)
        worked_section = sections["Worked example: checkout"]
        worked_rows = markdown_table_rows(worked_section)
        for metric in METRICS:
            if metric not in measure_rows:
                failures.append(f"README.md measure vector missing label: {metric}")
            if metric not in worked_rows:
                failures.append(f"README.md worked example missing vector row: {metric}")
        if not NO_COMBINED_SCORE.search(measure_section):
            failures.append("README.md must reject a combined UX score")
        if not FITTS_MEASUREMENT_GUARD.search(measure_section):
            failures.append("README.md must guard Fitts calculation on measured geometry")
        if not ILLUSTRATIVE_EXAMPLE.search(worked_section):
            failures.append("README.md checkout example must be illustrative, not a real inspection")

        for metric in ("Completion", "Hit", "Cognitive", "Wait", "Recovery", "Surface", "Accessibility", "Integrity"):
            finding, evidence = worked_rows.get(metric, ("", ""))
            if evidence != "Assumed":
                failures.append(f"README.md illustrative {metric} row must use Assumed evidence")
            if not re.search(r"\bvalidate by\b", finding, re.IGNORECASE):
                failures.append(f"README.md Assumed {metric} row needs an explicit validation clause")
        fitts_finding, fitts_evidence = worked_rows.get("Fitts", ("", ""))
        if not fitts_evidence.startswith("Observed"):
            failures.append("README.md illustrative Fitts row must use Observed example-input evidence")
        if not re.search(r"geometry is absent.*no calculation", fitts_finding, re.IGNORECASE):
            failures.append("README.md illustrative Fitts row must state absent geometry and no calculation")

        validation_section = sections["Validate a checkout"]
        for command in ("python3 tests/quick_validate.py",):
            if command not in validation_section:
                failures.append(f"README.md validation section missing command: {command!r}")
        if "/Users/" in validation_section:
            failures.append("README.md validation must not contain a machine-specific path")
        if not DIRECT_INSTALL_GUARD.search(readme):
            failures.append("README.md must place ln -s in the guarded install else branch")
        if re.search(r"\bcodex\s+plugin\b", readme, re.IGNORECASE):
            failures.append("README.md must not claim a universal codex plugin CLI command")
        if "[LICENSE](LICENSE)" not in sections["License"]:
            failures.append("README.md License section must link to LICENSE")
        if "has not selected a license" in sections["License"]:
            failures.append("README.md must not claim that no license is selected")

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
        for link in (
            "references/accessibility-review.md",
            "references/frontend-integrity.md",
            "references/capability-experience.md",
            "references/report-contract.md",
        ):
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

    report_contract = FILES["report_contract"]
    if report_contract.is_file():
        content = report_contract.read_text(encoding="utf-8")
        if not STATIC_REPEAT_OVERRIDE.search(content):
            failures.append(
                "skills/intentional-ux/references/report-contract.md static fixture "
                "does not contain the intentional repeated selector/token/property override"
            )
        if STATIC_RESOLVED_EXPECTATION not in content:
            failures.append(
                "skills/intentional-ux/references/report-contract.md static fixture "
                "does not document the mounted-input cascade resolution and no-finding expectation"
            )
        if STATIC_TOKEN_OWNERSHIP not in content:
            failures.append(
                "skills/intentional-ux/references/report-contract.md static fixture "
                "does not document custom-property ownership for the repeated override"
            )

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

    for name in ("checkout", "editor", "capability"):
        path = FILES[name]
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        normalized = " ".join(content.split())
        for section in SCENARIO_SECTIONS:
            if section not in content:
                failures.append(f"{path.relative_to(ROOT)} missing section: {section}")
        tuple_lines = [line for line in content.splitlines() if "->" in line]
        if not any("/" in line and line.count("->") >= 3 for line in tuple_lines):
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
    print(
        f"Validated {len(FILES)} files: references, task tuple, state graph, "
        "metric contract, and scenario artifacts."
    )


if __name__ == "__main__":
    main()
