#!/usr/bin/env python3
"""Conformance audit for Claude C-Suite Plugin command files.

Verifies that every command file under commands/ adheres to the
conventions defined in v1.4 (Consistency Pass) and documented in
AUDIT.md and CONTRIBUTING.md.

Usage:
    python3 scripts/audit.py            # report only
    python3 scripts/audit.py --matrix   # also print the conformance matrix

Exit code 0 if all checks pass, 1 otherwise.
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CMD_DIR = os.path.join(ROOT, "commands")

# Each check is (key, label, predicate). The predicate receives the file
# content as a string and returns True if the check passes.
COMMAND_CHECKS = [
    ("frontmatter",
     "Frontmatter (description + arguments)",
     lambda c: c.startswith("---\n")
               and "description:" in c[:500]
               and "arguments:" in c[:500]),
    ("trust_boundary",
     "## Trust boundary section",
     lambda c: "## Trust boundary" in c),
    ("mode_detection",
     "## Mode detection section",
     lambda c: "## Mode detection" in c),
    ("question_mode",
     "## Question Mode section",
     lambda c: "## Question Mode" in c),
    ("review_mode",
     "## Review Mode section",
     lambda c: "## Review Mode" in c),
    ("scope_args",
     "Argument convention is scope-keyword (no owner/repo)",
     lambda c: "owner/repo" not in c),
    ("cross_reference",
     "Cross-references peer roles",
     lambda c: "cross-reference" in c.lower()),
    ("phd_panel_ref",
     "References PhD Panel plugin",
     lambda c: "claude-phd-panel" in c),
    ("ai_disclaimer",
     "AI-generated advice disclaimer footer",
     lambda c: "AI-generated advice" in c),
    ("analysis_only",
     "Analysis-only guarantee (Do NOT execute / move)",
     lambda c: "Do NOT execute" in c or "Do NOT move" in c),
]

EXPECTED_COMMANDS = {
    "ceo.md", "cto.md", "pm.md", "cdo.md", "cso.md",
    "clo.md", "coo.md", "cmo.md", "caio.md", "cfo.md",
    "cio.md", "qa-lead.md", "dx-lead.md",
}


def audit_commands() -> tuple[dict[str, dict[str, bool]], list[str]]:
    """Run all checks against every command file. Returns (results, errors)."""
    results: dict[str, dict[str, bool]] = {}
    errors: list[str] = []

    found = {f for f in os.listdir(CMD_DIR) if f.endswith(".md")}
    missing = EXPECTED_COMMANDS - found
    extra = found - EXPECTED_COMMANDS
    if missing:
        errors.append(f"Missing expected command files: {sorted(missing)}")
    if extra:
        errors.append(f"Unexpected command files: {sorted(extra)}")

    for fname in sorted(found):
        with open(os.path.join(CMD_DIR, fname)) as f:
            content = f.read()
        results[fname] = {key: predicate(content)
                          for key, _, predicate in COMMAND_CHECKS}

    return results, errors


def audit_metadata() -> list[str]:
    """Run repository-level metadata checks. Returns list of failure messages."""
    errors: list[str] = []
    plugin_path = os.path.join(ROOT, ".claude-plugin", "plugin.json")
    market_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")

    with open(plugin_path) as f:
        plugin = json.load(f)
    with open(market_path) as f:
        market = json.load(f)

    plugin_version = plugin.get("version")
    market_version = market.get("plugins", [{}])[0].get("version")
    if plugin_version != market_version:
        errors.append(
            f"plugin.json version ({plugin_version}) != "
            f"marketplace.json version ({market_version})"
        )

    for required in ("SECURITY.md", "CONTRIBUTING.md", "CHANGELOG.md",
                     "README.md", "README.ja.md", "AUDIT.md"):
        if not os.path.exists(os.path.join(ROOT, required)):
            errors.append(f"Missing required document: {required}")

    return errors


def render_matrix(results: dict[str, dict[str, bool]]) -> str:
    headers = ["Command"] + [label for _, label, _ in COMMAND_CHECKS]
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("|" + "|".join([" :--- "] + [" :-: " for _ in COMMAND_CHECKS]) + "|")
    for fname in sorted(results):
        cells = ["`/" + fname.replace(".md", "") + "`"]
        for key, _, _ in COMMAND_CHECKS:
            cells.append("✅" if results[fname][key] else "❌")
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def main() -> int:
    show_matrix = "--matrix" in sys.argv
    results, structural_errors = audit_commands()
    metadata_errors = audit_metadata()

    failures: list[str] = list(structural_errors)
    for fname, checks in results.items():
        for key, label, _ in COMMAND_CHECKS:
            if not checks[key]:
                failures.append(f"{fname}: {label}")
    failures.extend(metadata_errors)

    if show_matrix:
        print(render_matrix(results))
        print()

    if failures:
        print("AUDIT FAILED:")
        for f in failures:
            print(f"  ❌ {f}")
        return 1

    total_checks = len(results) * len(COMMAND_CHECKS) + 1 + 6  # commands + version + 6 docs
    print(f"✅ All {total_checks} conformance checks passed "
          f"({len(results)} commands × {len(COMMAND_CHECKS)} checks "
          f"+ metadata).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
