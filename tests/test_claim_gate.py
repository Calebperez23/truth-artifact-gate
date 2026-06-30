from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from claim_gate import evaluate_claim


class ClaimGateTests(unittest.TestCase):
    def load_claim(self, name: str):
        return json.loads((ROOT / "examples" / name).read_text(encoding="utf-8-sig"))

    def test_fabricated_completion_is_inadmissible(self):
        result = evaluate_claim(self.load_claim("fabricated_completion.json"), ROOT)
        self.assertEqual(result.verdict, "INADMISSIBLE")
        self.assertIn("no execution artifact", result.reason)

    def test_valid_completion_is_admissible(self):
        result = evaluate_claim(self.load_claim("valid_completion.json"), ROOT)
        self.assertEqual(result.verdict, "ADMISSIBLE")
        self.assertEqual(result.claimed_sha256, result.actual_sha256)

    def test_stale_completion_is_rejected(self):
        result = evaluate_claim(self.load_claim("stale_completion.json"), ROOT)
        self.assertEqual(result.verdict, "REJECTED")
        self.assertIn("hash mismatch", result.reason)

    def test_path_escape_is_rejected(self):
        claim = {
            "claim_id": "escape",
            "agent_claim": "I wrote outside the repo.",
            "artifact": {"path": "../outside.txt", "sha256": "deadbeef"},
        }
        result = evaluate_claim(claim, ROOT)
        self.assertEqual(result.verdict, "REJECTED")
        self.assertIn("escapes", result.reason)


if __name__ == "__main__":
    unittest.main()


