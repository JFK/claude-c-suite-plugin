# Codex Adapter

Use the referenced command prompt in `../../commands/` as the authoritative
role or utility instruction.

When running inside Codex:

- Treat the user's current request, minus the explicit skill name if present, as
  the command's `$ARGUMENTS`.
- If the user invokes the skill without extra text, treat `$ARGUMENTS` as empty.
- Follow the command prompt's safety boundary, mode detection, output format,
  and analysis-only constraints.
- Do not modify the target repository unless the command prompt explicitly says
  it is a utility command that may do so and the user has requested that action.
- When the command prompt mentions Claude slash commands in examples or follow-up
  suggestions, translate them to Codex skill usage in user-facing prose.
- For language preference, check `~/.codex/claude-c-suite.json` first. If it is
  missing or malformed, fall back to `~/.claude/claude-c-suite.json`, then to
  auto-detecting the language from the user's request.
- Cite local evidence with file paths and line numbers when the command asks for
  codebase-grounded analysis.
