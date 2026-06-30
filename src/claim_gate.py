from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from artifact_store import ArtifactStore


@dataclass(frozen=True)
class GateResult:
    claim_id: str
    verdict: str
    reason: str
    checked_at: str
    claimed_path: Optional[str]
    claimed_sha256: Optional[str]
    actual_sha256: Optional[str]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def evaluate_claim(claim: Dict[str, Any], base_dir: Path) -> GateResult:
    claim_id = str(claim.get("claim_id") or "unknown")
    artifact = claim.get("artifact") or {}
    claimed_path = artifact.get("path")
    claimed_sha256 = artifact.get("sha256")

    if not claimed_path:
        return GateResult(
            claim_id=claim_id,
            verdict="INADMISSIBLE",
            reason="claim has no artifact path",
            checked_at=now_iso(),
            claimed_path=None,
            claimed_sha256=claimed_sha256,
            actual_sha256=None,
        )

    store = ArtifactStore(base_dir)
    observed = store.observe(claimed_path)

    if observed.error:
        return GateResult(
            claim_id=claim_id,
            verdict="REJECTED",
            reason=observed.error,
            checked_at=now_iso(),
            claimed_path=claimed_path,
            claimed_sha256=claimed_sha256,
            actual_sha256=None,
        )

    if not observed.exists:
        return GateResult(
            claim_id=claim_id,
            verdict="INADMISSIBLE",
            reason="no execution artifact exists at claimed path",
            checked_at=now_iso(),
            claimed_path=claimed_path,
            claimed_sha256=claimed_sha256,
            actual_sha256=None,
        )

    if not claimed_sha256:
        return GateResult(
            claim_id=claim_id,
            verdict="INADMISSIBLE",
            reason="artifact exists but claim lacks expected hash",
            checked_at=now_iso(),
            claimed_path=claimed_path,
            claimed_sha256=claimed_sha256,
            actual_sha256=observed.actual_sha256,
        )

    if observed.actual_sha256 != claimed_sha256.lower():
        return GateResult(
            claim_id=claim_id,
            verdict="REJECTED",
            reason="artifact hash mismatch; evidence is stale or tampered",
            checked_at=now_iso(),
            claimed_path=claimed_path,
            claimed_sha256=claimed_sha256,
            actual_sha256=observed.actual_sha256,
        )

    return GateResult(
        claim_id=claim_id,
        verdict="ADMISSIBLE",
        reason="artifact exists and hash matches claim",
        checked_at=now_iso(),
        claimed_path=claimed_path,
        claimed_sha256=claimed_sha256,
        actual_sha256=observed.actual_sha256,
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python src/claim_gate.py <claim.json>", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parents[1]
    claim_path = Path(argv[1])
    if not claim_path.is_absolute():
        claim_path = repo_root / claim_path

    claim = json.loads(claim_path.read_text(encoding="utf-8"))
    result = evaluate_claim(claim, repo_root)
    print(json.dumps(asdict(result), indent=2))
    return 0 if result.verdict == "ADMISSIBLE" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


