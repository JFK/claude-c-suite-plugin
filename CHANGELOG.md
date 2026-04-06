# Changelog

All notable changes to Claude C-Suite Plugin are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.4.0] — 2026-04-06 — "Consistency Pass"

### Fixed
- `/cto` and `/pm` argument convention unified with the other 11 commands.
  Both now accept scope keywords (`full`, `debt`, `arch`, etc. for `/cto`;
  `full`, `milestones`, `bugs`, `releases` for `/pm`) instead of the old
  `owner/repo` format.
- `marketplace.json` version aligned with `plugin.json` (both now `1.3.0`).

### Added
- **Trust boundary** section in every command file. When the plugin
  reads content from external or untrusted sources (READMEs, issues,
  PR descriptions, comments), the model is instructed to treat that
  content as data, not instructions, and to ignore embedded directives.
- **AI-generated advice disclaimer** as a footer in every command file.
  Reminds users that the output is LLM-generated and that critical
  recommendations (security, legal, financial, compliance) should be
  verified with qualified domain experts before acting on them.
- `/claude-c-suite:audit` — new maintainer utility command. Acts as
  the conformance audit and release gate: runs `scripts/audit.py`,
  reports pass/fail with fix suggestions, and outlines the release
  steps when the plugin is cleared. Does not modify files.
- `scripts/audit.py` — conformance audit script. Runs 10 per-role
  checks across 13 role commands plus 3 safety checks for utility
  commands plus 7 repository-level checks (140 checks total).
- `SECURITY.md` — threat model, mitigations, required GitHub token
  scopes, vulnerability reporting process.
- `CONTRIBUTING.md` — feature freeze policy, style guide, PR workflow.
- `CHANGELOG.md` — this file, with retroactive history.
- `AUDIT.md` — conformance matrix and policy reference.
- `USAGE.md` / `USAGE.ja.md` — comprehensive usage guides for end users.

## [1.3.0] — CEO meta-layer and Top 3 cross-reference model

### Added
- `/ceo` command — meta-layer that triages user needs to the most
  relevant 3 CxO perspectives and synthesizes a unified executive
  decision. Sits above the cross-reference graph rather than within it.
- `/cio` command — Chief Information Officer review covering data
  governance, schema management, system integration, and information
  architecture.
- **Top 3 cross-reference model** — every CxO/Lead now has exactly
  three primary collaborators, forming a structured graph that the
  CEO command reads when selecting perspectives.

## [1.2.0] — 11-role suite expansion

### Added
- `/clo` — Chief Legal Officer (license compliance, privacy, regulatory)
- `/coo` — Chief Operating Officer (CI/CD, deployment, observability)
- `/cmo` — Chief Marketing Officer (SEO, Core Web Vitals, social, analytics)
- `/caio` — Chief AI Officer (AI/ML governance, model lifecycle, responsible AI)
- `/cfo` — Chief Financial Officer (cloud cost, resource efficiency, billing)

### Changed
- All commands now cross-reference findings from peer CxOs when
  available in the same session.
- Added PhD Panel cross-reference to all C-Suite commands — when any
  `/claude-phd-panel:*` command has run in the session, its findings
  are incorporated into executive recommendations.

## [1.1.0] — Question mode

### Added
- **Question mode** in every command. Each role now answers
  natural-language questions from its perspective, grounded in the
  actual codebase, in addition to performing full reviews.

## [1.0.0] — Initial release

### Added
- `/cto` — CTO-level technical health review
- `/pm` — Product manager analysis
- `/cdo` — Chief Design Officer review
- `/cso` — Chief Security Officer review
- `/qa-lead` — QA Lead review
- `/dx-lead` — DX Lead review
