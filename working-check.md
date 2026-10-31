# Make your AI check its work

## Before you start

Use a text-capable AI and Python 3 on your machine or agent host. This example validates a small completion record. It checks structure and declared status; it cannot prove that a model's recorded test actually ran.

Download `check_handoff.py` and `handoff_hook.py` from the companion links on this page. Put both in a `checks` folder in your project. No Python packages are required.

## Steps

1. Ask your AI to complete a small task and write `checks/handoff.json` using the example shape below. Require actual observed checks and list unfinished work.
2. Run `python checks/check_handoff.py checks/handoff.json`. Use `python3` or `py -3` if that is your installed Python launcher.
3. If the exit code is nonzero, fix the work or keep the task incomplete. Do not change a failed check to pass without new evidence.
4. Try the invalid fixtures below before enabling automatic execution.
5. Use the same checker from Codex, Claude Code, a local agent, a human-run terminal or CI. Connect an event hook only in a host that supports it.

```json
{
  "task": "Summarize two supplied notes",
  "result": "summary.md",
  "checks": [{"name": "Compared each claim with its cited source", "status": "pass"}],
  "unresolved": []
}
```

## Codex hook setup

Merge this object into `.codex/hooks.json`. Replace the command with your Python executable and the absolute script path, quoting paths containing spaces. Review and trust the project hook when Codex requests it. This is a post-edit report, not a pre-edit blocker. [Codex hook documentation](https://learn.chatgpt.com/docs/hooks).

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "^(apply_patch|Edit|Write)$",
      "hooks": [{"type": "command", "command": "python /absolute/project/checks/handoff_hook.py", "timeout": 10}]
    }]
  }
}
```

On Windows, use a command such as `py -3 C:/projects/demo/checks/handoff_hook.py`. In JSON, quotes inside a command string must be escaped. The adapter locates `handoff.json` beside itself, so a different session working directory does not change the file checked.

## Claude Code hook setup

Merge the same `hooks` object into `.claude/settings.json`, replacing the matcher with `^(Edit|Write)$`. Set the same absolute command path and review the script before enabling it. [Claude Code hook documentation](https://code.claude.com/docs/en/hooks).

## Open-weight models and other hosts

The checker is ordinary Python and does not call a model API. Ask your agent to run it after producing the handoff. If the host exposes a post-write callback, connect that callback to the checker and show its result to the agent. Otherwise run the command yourself or in CI. A prompt asking for a check is not an enforced event hook.

For a blocking downstream action, invoke the checker in the script that performs that action and stop on nonzero exit before acting. A post-edit hook cannot undo a write that already happened.

## Completion check

The example must exit zero. Change `status` to `fail`, add an unresolved item, remove `result`, supply invalid JSON, and point at a missing file: each must exit nonzero. Trigger an actual edit in your selected agent and confirm its hook displays the check result. Native hook setup remains unverified until that observation succeeds in your installation.
