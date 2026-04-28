import subprocess
import sys
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "validate_output.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
REPORT_KEYS = {"mode", "summary", "results"}
SUMMARY_KEYS = {"total", "passed", "failed"}
RESULT_KEYS = {"path", "expected", "valid", "passed", "errors"}


def run_validator(name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--output", str(FIXTURES / name)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def assert_json_report_contract(
    test_case: unittest.TestCase,
    report: dict[str, object],
    mode: str,
) -> None:
    test_case.assertEqual(set(report.keys()), REPORT_KEYS)
    test_case.assertEqual(report["mode"], mode)

    summary = report["summary"]
    results = report["results"]
    test_case.assertIsInstance(summary, dict)
    test_case.assertIsInstance(results, list)
    test_case.assertEqual(set(summary.keys()), SUMMARY_KEYS)

    result_rows = list(results)
    test_case.assertEqual(summary["total"], len(result_rows))
    test_case.assertEqual(
        summary["passed"],
        sum(1 for result in result_rows if result["passed"]),
    )
    test_case.assertEqual(
        summary["failed"],
        sum(1 for result in result_rows if not result["passed"]),
    )

    for result in result_rows:
        test_case.assertIsInstance(result, dict)
        test_case.assertEqual(set(result.keys()), RESULT_KEYS)
        test_case.assertIsInstance(result["path"], str)
        test_case.assertIn(result["expected"], {"valid", "invalid", "unknown"})
        test_case.assertIsInstance(result["valid"], bool)
        test_case.assertIsInstance(result["passed"], bool)
        test_case.assertIsInstance(result["errors"], list)


class ValidateOutputTests(unittest.TestCase):
    def test_accepts_valid_blocked_output(self) -> None:
        result = run_validator("valid-blocked.md")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validation passed", result.stdout)

    def test_accepts_valid_conflict_output_without_final_prompt(self) -> None:
        result = run_validator("valid-conflict-no-final-prompt.md")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_accepts_valid_execution_ready_output(self) -> None:
        result = run_validator("valid-execution-ready.md")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_accepts_valid_contract_ready_output(self) -> None:
        result = run_validator("valid-contract-ready.md")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_accepts_valid_draftable_output(self) -> None:
        result = run_validator("valid-draftable.md")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_non_execution_final_prompt(self) -> None:
        result = run_validator("invalid-blocked-final-prompt.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("must not include Final AI Execution Prompt", result.stdout)

    def test_rejects_blocked_requirement_contract(self) -> None:
        result = run_validator("invalid-blocked-contract.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("Blocked output must not include Requirement Contract", result.stdout)

    def test_rejects_confirmed_row_without_evidence(self) -> None:
        result = run_validator("invalid-confirmed-missing-evidence.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("Confirmed row has no user evidence", result.stdout)

    def test_rejects_candidate_field_in_final_prompt(self) -> None:
        result = run_validator("invalid-candidate-final-requirement.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("Unconfirmed field appears in final prompt", result.stdout)

    def test_rejects_execution_ready_without_acceptance_criteria(self) -> None:
        result = run_validator("invalid-execution-ready-no-acceptance.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("Final prompt must include acceptance criteria", result.stdout)

    def test_rejects_execution_ready_missing_gate_field(self) -> None:
        result = run_validator("invalid-execution-ready-missing-gate.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing execution gate field", result.stdout)

    def test_rejects_unconfirmed_contract_field_without_placeholder(self) -> None:
        result = run_validator("invalid-contract-unconfirmed-field.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("Unconfirmed contract field must use [NEEDS CLARIFICATION]", result.stdout)

    def test_missing_output_file_is_usage_error(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), "--output", str(FIXTURES / "missing.md")],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 2)

    def test_accepts_fixtures_directory(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), "--fixtures-dir", str(FIXTURES)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Fixture validation passed", result.stdout)

    def test_json_report_for_fixtures_directory(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), "--fixtures-dir", str(FIXTURES), "--json"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        assert_json_report_contract(self, report, "fixtures")
        self.assertGreater(report["summary"]["total"], 0)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_json_report_for_single_valid_output(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--output",
                str(FIXTURES / "valid-blocked.md"),
                "--json",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        assert_json_report_contract(self, report, "file")
        self.assertEqual(report["results"][0]["expected"], "unknown")
        self.assertTrue(report["results"][0]["valid"])
        self.assertTrue(report["results"][0]["passed"])
        self.assertEqual(report["results"][0]["errors"], [])

    def test_json_report_for_single_invalid_output(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--output",
                str(FIXTURES / "invalid-blocked-final-prompt.md"),
                "--json",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 1)
        report = json.loads(result.stdout)
        assert_json_report_contract(self, report, "file")
        self.assertFalse(report["results"][0]["valid"])
        self.assertFalse(report["results"][0]["passed"])
        self.assertIn(
            "State Blocked must not include Final AI Execution Prompt.",
            report["results"][0]["errors"],
        )

    def test_rejects_valid_fixture_that_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "valid-bad.md"
            fixture.write_text(
                "\n".join(
                    [
                        "## Idea Control Status",
                        "State: Blocked",
                        "## Evidence Ledger",
                        "| Field | Status | User Evidence | Risk |",
                        "|---|---|---|---|",
                        "| Goal | Candidate | \"x\" | High |",
                        "## Blocking Unknowns",
                        "- [NEEDS CLARIFICATION] x",
                    ]
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(VALIDATOR), "--fixtures-dir", tmp],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Expected valid fixture to pass", result.stdout)

    def test_rejects_invalid_fixture_that_passes_validation(self) -> None:
        valid_text = (FIXTURES / "valid-blocked.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "invalid-good.md"
            fixture.write_text(valid_text, encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(VALIDATOR), "--fixtures-dir", tmp],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Expected invalid fixture to fail", result.stdout)

    def test_rejects_unknown_fixture_name(self) -> None:
        valid_text = (FIXTURES / "valid-blocked.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "example.md"
            fixture.write_text(valid_text, encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(VALIDATOR), "--fixtures-dir", tmp],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Fixture filename must start with valid- or invalid-", result.stdout)

    def test_json_report_for_unknown_fixture_name(self) -> None:
        valid_text = (FIXTURES / "valid-blocked.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "example.md"
            fixture.write_text(valid_text, encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    "--fixtures-dir",
                    tmp,
                    "--json",
                ],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertEqual(result.returncode, 1)
        report = json.loads(result.stdout)
        assert_json_report_contract(self, report, "fixtures")
        self.assertEqual(report["results"][0]["expected"], "unknown")
        self.assertFalse(report["results"][0]["passed"])
        self.assertIn(
            "Fixture filename must start with valid- or invalid-: example.md.",
            report["results"][0]["errors"],
        )

    def test_rejects_empty_fixtures_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(VALIDATOR), "--fixtures-dir", tmp],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("No Markdown fixtures found", result.stdout)

    def test_json_missing_output_file_is_machine_readable(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--output",
                str(FIXTURES / "missing.md"),
                "--json",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 2)
        report = json.loads(result.stdout)
        self.assertEqual(report["mode"], "file")
        self.assertEqual(report["summary"]["failed"], 1)

    def test_output_and_fixtures_dir_are_mutually_exclusive(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--output",
                str(FIXTURES / "valid-blocked.md"),
                "--fixtures-dir",
                str(FIXTURES),
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 2)

    def test_requires_output_or_fixtures_dir(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
