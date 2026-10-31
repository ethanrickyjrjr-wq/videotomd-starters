"""PostToolUse adapter: report handoff validation; do not claim to block earlier edits."""
import json
from pathlib import Path
import sys
from check_handoff import check

try:
    event = json.load(sys.stdin)
    if not isinstance(event, dict):
        raise ValueError("Expected an event object")
    # Keep this starter confined to the handoff beside this script, independent of cwd.
    target = Path(__file__).resolve().parent / "handoff.json"
    errors = check(target)
    message = "Handoff check: " + ("; ".join(errors) if errors else "structure passed; verify the recorded evidence")
    print(json.dumps({"systemMessage": message}))
except (ValueError, TypeError, OSError) as error:
    print(f"Hook input failed: {type(error).__name__}", file=sys.stderr)
    sys.exit(1)
