# Usage Guide

A practical guide to getting value out of Claude C-Suite Plugin in
your day-to-day work.

> Looking for installation? See [README.md](./README.md#installation).

---

## 60-second quick start

1. `cd` into any git repository
2. Run:
   ```
   /claude-c-suite:ceo
   ```
3. Read the recommendation. The CEO command will auto-diagnose your
   project, pick the 3 most relevant executive perspectives, and give
   you a prioritized action list.

That's it. **When in doubt, start with `/ceo`** — it's designed to be
the safe, always-correct entry point.

---

## "I want to..." → which command?

| Goal | Command |
|------|---------|
| Get an executive summary of the project | `/claude-c-suite:ceo` |
| Find tech debt and refactor priorities | `/claude-c-suite:cto` |
| Audit security posture / OWASP coverage | `/claude-c-suite:cso` |
| Check dependency licenses, GDPR readiness | `/claude-c-suite:clo` |
| Optimize cloud costs and resource usage | `/claude-c-suite:cfo` |
| Review data models, schemas, integrations | `/claude-c-suite:cio` |
| Triage milestones, prioritize issues | `/claude-c-suite:pm` |
| Audit CI/CD, deploy strategy, observability | `/claude-c-suite:coo` |
| Review SEO, Core Web Vitals, social meta | `/claude-c-suite:cmo` |
| Govern AI/ML lifecycle and prompt safety | `/claude-c-suite:caio` |
| Review design system and component reuse | `/claude-c-suite:cdo` |
| Find testing gaps and missing scenarios | `/claude-c-suite:qa-lead` |
| Review API ergonomics and developer experience | `/claude-c-suite:dx-lead` |

If you can't decide, run `/ceo` and let it pick.

---

## Two modes: question and review

Every command works in two modes. The plugin auto-detects which one
you want based on your input.

### Question mode

Just type a natural-language question. The role answers from its
perspective, grounded in your actual codebase.

```
/claude-c-suite:cto Should we migrate to a monorepo?
/claude-c-suite:cso Is our JWT implementation secure?
/claude-c-suite:clo Can we use this GPL library in our SaaS product?
/claude-c-suite:cfo Are we over-provisioned on the database tier?
/claude-c-suite:pm Should we delay the launch to fix these bugs?
```

The role gathers only the context needed to answer your specific
question — fast and focused.

### Review mode

Type a scope keyword (or nothing) for a structured analysis.

```
/claude-c-suite:cto                 # full review
/claude-c-suite:cto debt            # focus on tech debt
/claude-c-suite:cso auth            # focus on authentication
/claude-c-suite:clo licenses        # focus on dependency licenses
/claude-c-suite:coo cicd            # focus on CI/CD pipeline
/claude-c-suite:cmo seo             # focus on SEO health
/claude-c-suite:caio models         # focus on model lifecycle
/claude-c-suite:cfo costs           # focus on cloud costs
/claude-c-suite:cio data            # focus on data governance
```

Each command's accepted scopes are listed in its frontmatter (run
`/claude-c-suite:<role>` with no argument to see the default review).

---

## Common patterns

### Multi-role consultation

Run several roles in the same session. Each role automatically
references the findings of any peer roles you've already invoked.

**Example workflow — pre-release readiness:**

```
1. /claude-c-suite:cto       → identifies tech debt blockers
2. /claude-c-suite:cso       → notices that fixing the debt also closes auth gaps
3. /claude-c-suite:qa-lead   → finds untested code paths around the auth fix
4. /claude-c-suite:pm        → reorders the milestone with all of the above
```

By the time `/pm` runs, it has `cto`, `cso`, and `qa-lead`'s findings
in context and will prioritize accordingly.

### Let the CEO orchestrate

If you're not sure which roles to consult, run `/ceo` first. It will
pick the right 3 perspectives for your situation and synthesize them
into a unified decision. You can then drill into individual roles for
more depth.

```
/claude-c-suite:ceo Are we ready to launch?
```

Output will tell you which 3 CxOs were selected and why — a great
guide for which follow-up commands to run.

### Narrow scope to save time

For large repos, full reviews can be slow. Narrow with a scope
keyword:

```
/claude-c-suite:cso auth        # only auth code, not the whole repo
/claude-c-suite:cto debt        # only tech debt issues, not docs/bugs/arch
```

---

## Combining with other plugins

### With [claude-phd-panel](https://github.com/JFK/claude-phd-panel-plugin)

The PhD Panel adds academic depth (Distributed Systems, Statistics,
Database Theory, etc.). When you run a PhD Panel command first,
every subsequent C-Suite command will incorporate its findings.

```
1. /claude-phd-panel:dist-sys   → academic review of consensus correctness
2. /claude-c-suite:cto          → CTO incorporates the academic critique
3. /claude-c-suite:caio         → CAIO incorporates dist-sys concerns into AI rollout
```

### With [expert-craft](https://github.com/JFK/expert-craft-plugin)

Create a custom domain expert and have it cross-reference C-Suite
findings:

```
1. /expert-craft cryptographer  → create a custom crypto expert
2. /claude-c-suite:cso          → standard security review
3. /cryptographer               → deep crypto review that references the CSO findings
```

---

## What the plugin does NOT do

- **No code changes** — every command produces analysis and
  recommendations only. You decide what to act on.
- **No authoritative legal/security/financial advice** — the output
  is AI-generated. Verify critical recommendations with qualified
  domain experts before acting on them. See the disclaimer at the
  bottom of every command output.
- **No telemetry** — the plugin sends no data to any third party. It
  only invokes `gh` and `git` commands using your existing
  credentials.

---

## Troubleshooting

### "The command answered my question in review mode" (or vice versa)

The plugin auto-detects question vs review mode based on whether your
input contains question words or a `?`. If detection misfires:

- **Force review mode**: pass a scope keyword like `full`
  ```
  /claude-c-suite:cto full
  ```
- **Force question mode**: end your input with `?`
  ```
  /claude-c-suite:cto Re-review the main branch?
  ```

### "The command tried to use `--repo owner/repo` and failed"

You're on an older version. The plugin no longer accepts `owner/repo`
arguments — commands operate on the current working directory's
repository. Either `cd` into the target repo or upgrade to v1.4+.

### "The output references files that don't exist"

LLM hallucinations are possible, especially on very large codebases.
Always verify references before acting on them. If you see frequent
hallucinations, file an issue with the command name, the input you
used, and the model you ran.

### "I want a custom role that isn't in the 13"

During the v1.4 / v1.5 feature freeze, no new roles will be added to
this plugin. Use [expert-craft](https://github.com/JFK/expert-craft-plugin)
to create your own — it integrates seamlessly with C-Suite.

---

## Next steps

- Review the [SECURITY.md](./SECURITY.md) threat model before pointing
  the plugin at untrusted third-party repositories
- Read [CONTRIBUTING.md](./CONTRIBUTING.md) if you want to propose
  changes during the feature freeze
- Check [CHANGELOG.md](./CHANGELOG.md) for what's new in each release
