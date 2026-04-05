# Claude C-Suite Plugin

Executive team perspectives for any codebase. Eleven specialized review commands that analyze your project from different leadership viewpoints.

## Commands

| Command | Role | What it reviews |
|---------|------|-----------------|
| `/cto` | Chief Technology Officer | Tech debt, architecture, refactoring priorities, dependency risks |
| `/pm` | Product Manager | Milestone triage, issue prioritization, release planning |
| `/cdo` | Chief Design Officer | UI/UX consistency, design system health, component reuse |
| `/cso` | Chief Security Officer | Vulnerabilities, auth patterns, secret management, OWASP Top 10 |
| `/clo` | Chief Legal Officer | License compliance, data privacy, regulatory readiness, IP protection |
| `/coo` | Chief Operating Officer | CI/CD pipelines, deployment strategy, observability, incident readiness |
| `/cmo` | Chief Marketing Officer | SEO health, Core Web Vitals, social sharing, analytics implementation |
| `/caio` | Chief AI Officer | AI/ML governance, model lifecycle, responsible AI, LLM integration patterns |
| `/cfo` | Chief Financial Officer | Cloud cost optimization, resource efficiency, billing logic, compute waste |
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
/claude-c-suite:clo licenses          # Focus on dependency licenses
/claude-c-suite:coo cicd              # Focus on CI/CD pipeline
/claude-c-suite:cmo seo               # Focus on SEO health
/claude-c-suite:caio models            # Focus on model lifecycle
/claude-c-suite:cfo costs              # Focus on cloud costs
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
/claude-c-suite:clo Can we use this GPL library in our SaaS product?
/claude-c-suite:coo Are we ready for a zero-downtime deployment?
/claude-c-suite:cmo Will this page rank well for our target keywords?
/claude-c-suite:caio Are we handling prompt injection risks?
/claude-c-suite:cfo Are we over-provisioned on our database tier?
```

## Design Principles

- **Analysis only** — Commands recommend actions but never execute changes
- **Cross-referencing** — Run multiple commands in one session; they reference each other's findings
- **GitHub-native** — Uses `gh` CLI to gather issues, milestones, and commit history
- **Universal** — No project-specific assumptions; works with any codebase

## License

MIT
