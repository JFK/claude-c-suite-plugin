---
description: CTO-level technical health review — tech debt, architecture, refactoring priorities
arguments:
  - name: repo
    description: "Target repo (e.g., owner/repo). Defaults to current repo."
    required: false
---

Analyze the project's technical health from a CTO perspective.

## Steps

### 1. Gather current state

Run in parallel:
- `gh issue list --repo $REPO --state open --json number,title,milestone,labels,createdAt` — all open issues
- `gh issue list --repo $REPO --state open --label bug --json number,title,milestone,createdAt` — open bugs
- `gh issue list --repo $REPO --state open --search "refactor OR tech-debt OR deprecat" --json number,title,milestone` — refactoring/debt issues
- `git log --oneline -30` — recent commit activity (if in repo)
- Check for issues labeled `refactor`, `tech-debt`, `breaking-change`, or with "refactor" in title

If `$ARGUMENTS` provides a repo, use it. Otherwise use the current repo.

### 2. Tech debt assessment

Evaluate:
- **Debt accumulation**: How many refactor/tech-debt issues exist? Are they growing or shrinking?
- **Debt distribution**: Are they concentrated in one area or spread across the codebase?
- **Debt age**: How old are the oldest refactor issues? Stale debt signals avoidance
- **Debt-to-feature ratio**: Ratio of refactor issues to feature issues per milestone. If >30% of a milestone is debt cleanup, the system is already behind

### 3. Architecture risk analysis

Look for signals of architectural stress:
- **Breaking changes queued**: Issues that require API changes, migration, or deprecation
- **Cross-cutting concerns**: Issues that touch multiple modules or require coordinated changes
- **Dependency risks**: Issues related to dependency updates, supply chain, or version pinning
- **Performance/scale issues**: Issues flagging performance, scaling, or resource concerns

### 4. Documentation health

Evaluate documentation posture:
- **Doc-feature gap**: Are there features shipped without corresponding documentation?
- **Stale docs**: Are there `docs:` labeled issues piling up or docs issues older than 30 days?
- **README/CHANGELOG currency**: Is the README up to date with actual capabilities? Is there a CHANGELOG?
- **API docs**: Are public APIs documented? Are breaking changes communicated?
- **Onboarding path**: Could a new contributor get started from docs alone?

### 5. Bug health

Evaluate bug posture:
- **Bug velocity**: Are bugs being closed faster than opened?
- **Bug age**: Oldest open bugs — are any becoming chronic?
- **Bug severity**: Are bugs blocking users or just cosmetic?
- **Bugs without milestones**: Unfiled bugs signal triage gaps

### 6. Apply CTO principles

1. **Debt compounds** — 3+ refactor issues without a milestone = schedule a debt sprint before the next feature release
2. **Breaking changes need coordination** — Group breaking changes into a single release with migration guides, don't scatter them
3. **Chronic bugs erode trust** — Bugs older than 30 days need a decision: fix, wontfix, or downgrade
4. **Docs are part of the product** — Features without docs are half-shipped. Flag undocumented public APIs and features
5. **Architecture before features** — If cross-cutting concerns are piling up, pause features to stabilize foundations
6. **Dependencies are liabilities** — Flag any dependency with known CVEs or pinned due to incidents

### 7. Present findings

Structure output as:

```
## Technical Health Summary
- Overall health: [healthy / minor concerns / debt accumulating / structural risk]
- Tech debt count: N issues (N with milestone, N orphaned)
- Bug posture: N open (N critical, N chronic)

## Tech Debt Inventory
- Table: issue → area → age → milestone (or "unscheduled")
- Highlight: debt clusters in specific areas

## Documentation Health
- Doc-feature gap: features shipped without docs
- Stale doc issues
- Onboarding readiness

## Architecture Risks
- Breaking changes pending
- Cross-cutting concerns
- Dependency issues

## Recommendations
- Prioritized list of actions
- Whether a "debt sprint" is needed before the next feature release
- Specific issues that need milestone assignment or triage
```

### 7. Cross-reference with PM view

If `/pm` has been run in this session, cross-reference:
- Are milestones balanced between features and debt paydown?
- Is the release order sustainable from a technical perspective?
- Flag any milestone that is all-features-no-cleanup

Do NOT execute any changes. This is analysis only — recommend actions for the user to decide.
