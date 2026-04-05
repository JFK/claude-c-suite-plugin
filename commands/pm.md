---
description: Product manager analysis — milestone triage, issue prioritization, release planning
arguments:
  - name: repo
    description: "Target repo (e.g., kagura-ai/memory-cloud). Defaults to current repo."
    required: false
---

Analyze the project's milestones and open issues from a product manager perspective.

## Steps

### 1. Gather current state

Run in parallel:
- `gh issue list --repo $REPO --state open --json number,title,milestone,labels,createdAt` — all open issues
- `gh api repos/$REPO/milestones?state=open` — open milestones with descriptions
- `gh api repos/$REPO/milestones?state=closed --jq '.[] | "\(.number) \(.title)"'` — closed milestones for version history context

If `$ARGUMENTS` provides a repo, use it. Otherwise use the current repo.

### 2. Analyze each milestone

For each open milestone, evaluate:
- **Theme coherence**: Do the issues tell a single story? Or is it a grab bag?
- **Size**: Is the milestone overloaded (>6 issues) or too thin (<2)?
- **Dependencies**: Are there issues that block others across milestones?
- **Unassigned issues**: Are there open issues with no milestone?

### 3. Evaluate release ordering

Apply these PM principles in order of priority:
1. **Trust before integration** — Users must trust the core before connecting it to other systems
2. **Control before automation** — Give users visibility and manual control before adding more automation
3. **Bugs before features** — Ship fixes first, don't let them accumulate across milestones
4. **Coherent narrative per release** — Each release should have a one-sentence theme that users understand
5. **Minimize WIP** — Prefer fewer, focused milestones over many scattered ones

For technical health analysis (tech debt, refactoring, architecture), use `/cto` instead.

### 4. Present findings

Structure your output as:

```
## Current State
- Summary of milestones, issue counts, themes

## Issues Found
- Theme incoherence, overloaded milestones, ordering problems, orphan issues

## Proposed Reorganization (if needed)
- Table: milestone → theme → issues
- One-sentence release narrative per milestone
- Dependency chain: v0.X → v0.Y → v1.0

## Recommended Actions
- Specific `gh issue edit` commands or new milestone creation needed
```

### 5. Execute (with confirmation)

If reorganization is proposed, ask the user before executing any changes.
Do NOT move issues or create/modify milestones without explicit approval.
