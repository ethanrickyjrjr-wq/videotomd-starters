"""Check a small handoff artifact with any model or agent host. Python 3, no packages."""
import json
from pathlib import Path
import sys


def check(path):
    try:
        record = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        return [f"Cannot read handoff: {type(error).__name__}"]
    if not isinstance(record, dict):
        return ["Handoff must be a JSON object"]
    errors = []
    for key in ("task", "result"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            errors.append(f"Missing nonempty {key}")
    checks = record.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append("checks must contain at least one observed check")
    else:
        for item in checks:
            if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not item["name"].strip() or item.get("status") != "pass":
                errors.append("Every check needs a name and status pass")
    if not isinstance(record.get("unresolved"), list):
        errors.append("unresolved must be a list")
    elif record["unresolved"]:
        errors.append("Unresolved work remains")
    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_handoff.py handoff.json", file=sys.stderr)
        sys.exit(2)
    errors = check(sys.argv[1])
    print("\n".join(errors) if errors else "Handoff structure passed; verify the evidence behind each check.")
    sys.exit(1 if errors else 0)
