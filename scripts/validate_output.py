import argparse
import json
import re
import sys
from pathlib import Path


VALID_STATES = {"Blocked", "Draftable", "Contract-Ready", "Execution-Ready"}
FINAL_PROMPT = "Final AI Execution Prompt"
REQUIREMENT_CONTRACT = "Requirement Contract"
ASSUMPTION_FIREWALL = "Assumption Firewall"
NEXT_BEST_QUESTION = "Next Best Question"
BASIC_HEADINGS = {
    "Idea Control Status",
    "Evidence Ledger",
    "Blocking Unknowns",
    ASSUMPTION_FIREWALL,
}

EXECUTION_GATE_FIELDS = {
    "Goal",
    "Primary user",
    "Core workflow",
    "MVP must-haves",
    "Explicit non-goals",
    "Data persistence",
    "Acceptance criteria",
}

CONTRACT_FIELD_MAP = {
    "Goal": "Goal",
    "Primary user": "Primary user",
    "Core workflow": "Core scenario",
    "MVP must-haves": "MVP must-haves",
    "Explicit non-goals": "V1 non-goals",
    "Data persistence": "Data behavior",
    "Acceptance criteria": "Acceptance criteria",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate an Idea Harness output Markdown file."
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--output", help="Path to output Markdown file")
    target.add_argument(
        "--fixtures-dir",
        help="Directory containing valid-*.md and invalid-*.md fixture files",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print a machine-readable JSON validation report",
    )
    return parser.parse_args()


def read_text(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except OSError as exc:
        return None, f"Could not read output file: {exc}"
    except UnicodeDecodeError as exc:
        return None, f"Output file is not valid UTF-8: {exc}"


def has_heading(text: str, heading: str) -> bool:
    return bool(re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE))


def section_text(text: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        return ""

    start = match.end()
    next_match = re.search(r"^##\s+.+\s*$", text[start:], re.MULTILINE)
    end = start + next_match.start() if next_match else len(text)
    return text[start:end].strip()


def parse_state(text: str) -> str | None:
    match = re.search(r"^State:\s*([A-Za-z-]+)\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def parse_ledger_rows(text: str) -> list[dict[str, str]]:
    ledger = section_text(text, "Evidence Ledger")
    rows: list[dict[str, str]] = []

    for line in ledger.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[0] == "Field" or set(cells[0]) == {"-"}:
            continue

        rows.append(
            {
                "field": cells[0],
                "status": cells[1],
                "evidence": cells[2],
                "risk": cells[3],
            }
        )

    return rows


def evidence_is_missing(evidence: str) -> bool:
    normalized = evidence.strip().strip('"').strip("'").lower()
    return normalized in {"", "none", "n/a", "na", "[needs clarification]"}


def count_questions(text: str) -> int:
    return sum(1 for line in text.splitlines() if "?" in line or "？" in line)


def field_label_appears(section: str, field: str) -> bool:
    return bool(
        re.search(rf"^\s*(?:[-*]\s*)?{re.escape(field)}\s*:", section, re.MULTILINE)
    )


def validate(text: str) -> list[str]:
    errors: list[str] = []
    state = parse_state(text)
    rows = parse_ledger_rows(text)

    if not state:
        errors.append("Missing Idea Control Status state.")
    elif state not in VALID_STATES:
        errors.append(f"Unknown Idea Control Status state: {state}.")

    for heading in sorted(BASIC_HEADINGS):
        if not has_heading(text, heading):
            errors.append(f"Output must include {heading}.")

    has_final_prompt = has_heading(text, FINAL_PROMPT)
    has_contract = has_heading(text, REQUIREMENT_CONTRACT)

    if state and state != "Execution-Ready" and has_final_prompt:
        errors.append(f"State {state} must not include Final AI Execution Prompt.")

    if state == "Execution-Ready" and not has_final_prompt:
        errors.append("Execution-Ready output must include Final AI Execution Prompt.")

    if state == "Blocked" and has_contract:
        errors.append("Blocked output must not include Requirement Contract.")

    if state == "Blocked":
        question_section = section_text(text, NEXT_BEST_QUESTION)
        if not question_section:
            errors.append("Blocked output must include Next Best Question.")
        else:
            question_count = count_questions(question_section)
            if question_count != 1:
                errors.append(
                    "Blocked output must include exactly 1 Next Best Question; "
                    f"found {question_count}."
                )

    for row in rows:
        if row["status"] == "Confirmed" and evidence_is_missing(row["evidence"]):
            errors.append(f"Confirmed row has no user evidence: {row['field']}.")

    if state == "Execution-Ready":
        row_fields = {row["field"] for row in rows}
        for field in sorted(EXECUTION_GATE_FIELDS):
            if field not in row_fields:
                errors.append(f"Execution-Ready missing execution gate field: {field}.")

        for row in rows:
            if row["field"] in EXECUTION_GATE_FIELDS and row["status"] != "Confirmed":
                errors.append(
                    "Execution-Ready requires Confirmed execution gate field: "
                    f"{row['field']}."
                )

    final_section = section_text(text, FINAL_PROMPT)
    if state == "Execution-Ready" and final_section:
        if "验收标准" not in final_section and "Acceptance criteria" not in final_section:
            errors.append("Final prompt must include acceptance criteria.")
        if "禁止假设" not in final_section and "Assumption Firewall" not in final_section:
            errors.append("Final prompt must include forbidden assumptions.")

    if final_section:
        for row in rows:
            if row["status"] in {"Candidate", "Missing", "Conflict"} and field_label_appears(
                final_section, row["field"]
            ):
                errors.append(
                    "Unconfirmed field appears in final prompt: "
                    f"{row['field']} ({row['status']})."
                )

    contract_section = section_text(text, REQUIREMENT_CONTRACT)
    if state in {"Draftable", "Contract-Ready"} and contract_section:
        for row in rows:
            contract_field = CONTRACT_FIELD_MAP.get(row["field"])
            if not contract_field or row["status"] == "Confirmed":
                continue
            line_match = re.search(
                rf"^\s*{re.escape(contract_field)}\s*:(.*)$",
                contract_section,
                re.MULTILINE,
            )
            if line_match and "[NEEDS CLARIFICATION]" not in line_match.group(1):
                errors.append(
                    "Unconfirmed contract field must use [NEEDS CLARIFICATION]: "
                    f"{contract_field}."
                )

    return errors


def expected_from_path(path: Path) -> str:
    name = path.name
    if name.startswith("valid-"):
        return "valid"
    if name.startswith("invalid-"):
        return "invalid"
    return "unknown"


def is_read_error(result: dict[str, object]) -> bool:
    prefixes = ("Could not read output file:", "Output file is not valid UTF-8:")
    return any(str(error).startswith(prefixes) for error in result["errors"])


def result_for_file(
    path: Path,
    expected: str = "unknown",
    enforce_fixture_name: bool = False,
) -> dict[str, object]:
    text, error = read_text(path)
    if error:
        errors = [error]
    else:
        assert text is not None
        errors = validate(text)

    if enforce_fixture_name and expected == "unknown":
        errors.append(
            "Fixture filename must start with valid- or invalid-: "
            f"{path.name}."
        )

    valid = not errors
    if error:
        passed = False
    elif enforce_fixture_name and expected == "unknown":
        passed = False
    elif expected == "valid":
        passed = valid
    elif expected == "invalid":
        passed = not valid
    else:
        passed = valid

    return {
        "path": str(path),
        "expected": expected,
        "valid": valid,
        "passed": passed,
        "errors": errors,
    }


def build_report(mode: str, results: list[dict[str, object]]) -> dict[str, object]:
    passed = sum(1 for result in results if result["passed"])
    failed = len(results) - passed
    return {
        "mode": mode,
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": failed,
        },
        "results": results,
    }


def print_text_report(report: dict[str, object]) -> None:
    mode = report["mode"]
    summary = report["summary"]
    results = report["results"]

    if summary["failed"] == 0:
        if mode == "fixtures":
            print(
                "Fixture validation passed: "
                f"{summary['passed']}/{summary['total']} matched expectations"
            )
        else:
            result = results[0]
            print(f"Validation passed: {result['path']}")
        return

    print("Validation failed:")
    for result in results:
        if result["passed"]:
            continue

        path = result["path"]
        expected = result["expected"]
        valid = result["valid"]
        if expected == "valid" and not valid:
            print(f"- Expected valid fixture to pass: {path}")
        elif expected == "invalid" and valid:
            print(f"- Expected invalid fixture to fail: {path}")
        else:
            print(f"- Output failed validation: {path}")

        for error_message in result["errors"]:
            print(f"  - {error_message}")


def validate_output_file(path: Path, as_json: bool) -> int:
    if not path.exists():
        error = f"Could not read output file: {path}"
        if as_json:
            report = build_report(
                "file",
                [
                    {
                        "path": str(path),
                        "expected": "unknown",
                        "valid": False,
                        "passed": False,
                        "errors": [error],
                    }
                ],
            )
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(error, file=sys.stderr)
        return 2

    result = result_for_file(path)
    report = build_report("file", [result])
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)
    if is_read_error(result):
        return 2
    return 0 if result["passed"] else 1


def validate_fixtures_dir(path: Path, as_json: bool) -> int:
    if not path.exists() or not path.is_dir():
        error = f"Could not read fixtures directory: {path}"
        if as_json:
            report = build_report(
                "fixtures",
                [
                    {
                        "path": str(path),
                        "expected": "unknown",
                        "valid": False,
                        "passed": False,
                        "errors": [error],
                    }
                ],
            )
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(error, file=sys.stderr)
        return 2

    fixture_paths = sorted(p for p in path.rglob("*.md") if p.is_file())
    if not fixture_paths:
        result = {
            "path": str(path),
            "expected": "unknown",
            "valid": False,
            "passed": False,
            "errors": ["No Markdown fixtures found."],
        }
        report = build_report("fixtures", [result])
        if as_json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print_text_report(report)
        return 1

    results = [
        result_for_file(p, expected_from_path(p), enforce_fixture_name=True)
        for p in fixture_paths
    ]
    report = build_report("fixtures", results)
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)
    if any(is_read_error(result) for result in results):
        return 2
    return 0 if report["summary"]["failed"] == 0 else 1


def main() -> int:
    args = parse_args()
    if args.output:
        return validate_output_file(Path(args.output), args.json)
    return validate_fixtures_dir(Path(args.fixtures_dir), args.json)


if __name__ == "__main__":
    raise SystemExit(main())
