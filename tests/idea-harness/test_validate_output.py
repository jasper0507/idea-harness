import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "validate_output.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def run_validator(name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--output", str(FIXTURES / name)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


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


if __name__ == "__main__":
    unittest.main()
