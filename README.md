# Truth-Artifact Gate

AI agents fabricate completion claims.

They say files were created, emails were sent, commands were run, tests passed, tickets were closed, or deployments happened — even when no execution evidence exists.

**Truth-Artifact Gate makes those claims inadmissible until execution evidence exists.**

This is not a prompt trick. It is not a model benchmark. It is not another approval layer.

It is a runtime boundary between language and evidence.

## Core rule

Generated claims are not facts.

An agent may generate a claim, but the runtime does not accept that claim as true unless it is backed by an execution artifact: a file, receipt, trace, hash, timestamp, readback, or verified side effect.

No artifact means no admissible completion.

## 60-second demo

Open `demo/index.html` in a browser. No server. No model. No dependencies.

The demo shows three cases:

1. **Fabricated completion claim** → rejected because no artifact exists.
2. **Executed completion** → admitted because an artifact, hash, and timestamp exist.
3. **Tampered / stale completion** → rejected because evidence no longer matches.

## Why this matters

Agent systems increasingly perform real work. The failure mode is no longer only "bad answer."

The dangerous failure is an agent claiming work was completed when the world contains no proof that it happened.

Truth-Artifact Gate treats completion as an evidentiary state, not a sentence.

## Quick start: browser

```text
open demo/index.html
```

## Quick start: Python

```bash
python -m unittest discover -s tests
python src/claim_gate.py examples/fabricated_completion.json
python src/claim_gate.py examples/valid_completion.json
python src/claim_gate.py examples/stale_completion.json
```

## Public positioning

Everyone gates actions.

This gates the claim.

## Repository shape

```text
truth-artifact-gate/
  README.md
  demo/
    index.html
    gate.js
    styles.css
    sample_claims.json
  src/
    claim_gate.py
    artifact_store.py
    verifier.py
  examples/
    fabricated_completion.json
    valid_completion.json
    stale_completion.json
    artifacts/
      valid_report.txt
      stale_report.txt
  tests/
    test_claim_gate.py
  docs/
    claim-admissibility.md
    provenance.md
    public-release-notes.md
    threat-model.md
```

## Status

Public-safe proof pack. It intentionally does **not** include private runtime internals, identity material, local paths, trade-secret architecture files, model prompts, or sensitive evidence archives.

## License

Copyright (c) 2026 Caleb Perez. All rights reserved.

No license is granted unless explicitly stated in `LICENSE`.



