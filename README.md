# Claude C-Suite Plugin

Executive team perspectives for any codebase. Six specialized review commands that analyze your project from different leadership viewpoints.

## Commands

| Command | Role | What it reviews |
|---------|------|-----------------|
| `/cto` | Chief Technology Officer | Tech debt, architecture, refactoring priorities, dependency risks |
| `/pm` | Product Manager | Milestone triage, issue prioritization, release planning |
| `/cdo` | Chief Design Officer | UI/UX consistency, design system health, component reuse |
| `/cso` | Chief Security Officer | Vulnerabilities, auth patterns, secret management, OWASP Top 10 |
| `/qa-lead` | QA Lead | Test coverage, quality metrics, testing strategy gaps |
| `/dx-lead` | DX Lead | Developer experience, API ergonomics, SDK usability, onboarding |

## Installation

```bash
/plugin marketplace add JFK/claude-c-suite-plugin
/plugin install claude-c-suite
```

## Usage

### Review mode

Run any command to get a full review:

```
/claude-c-suite:cto                   # Full CTO review of current repo
/claude-c-suite:cto owner/repo        # Analyze a specific repo
/claude-c-suite:cdo components        # Focus on a specific area
/claude-c-suite:cso auth              # Focus on authentication
```

### Question mode

Ask any officer a direct question — they'll answer from their perspective, grounded in your actual codebase:

```
/claude-c-suite:cto Should we migrate to a monorepo?
/claude-c-suite:pm Should we delay the launch to fix these bugs?
/claude-c-suite:cdo Should we use a modal or a drawer here?
/claude-c-suite:cso Is our JWT implementation secure?
/claude-c-suite:qa-lead Do we need E2E tests for this flow?
/claude-c-suite:dx-lead How should we structure error responses?
```

## Design Principles

- **Analysis only** — Commands recommend actions but never execute changes
- **Cross-referencing** — Run multiple commands in one session; they reference each other's findings
- **GitHub-native** — Uses `gh` CLI to gather issues, milestones, and commit history
- **Universal** — No project-specific assumptions; works with any codebase

## License

MIT
