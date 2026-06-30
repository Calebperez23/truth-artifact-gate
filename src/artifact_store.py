from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from verifier import safe_resolve, sha256_file


@dataclass(frozen=True)
class ArtifactObservation:
    path: str
    exists: bool
    actual_sha256: Optional[str] = None
    error: Optional[str] = None


class ArtifactStore:
    """Minimal local artifact store used by the proof demo."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    def observe(self, relative_path: str) -> ArtifactObservation:
        try:
            path = safe_resolve(self.base_dir, relative_path)
        except Exception as exc:
            return ArtifactObservation(path=relative_path, exists=False, error=str(exc))

        if not path.exists() or not path.is_file():
            return ArtifactObservation(path=relative_path, exists=False)

        return ArtifactObservation(
            path=relative_path,
            exists=True,
            actual_sha256=sha256_file(path),
        )


