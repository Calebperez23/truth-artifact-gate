# Truth-Artifact Gate

![Tests](https://github.com/Calebperez23/truth-artifact-gate/actions/workflows/test.yml/badge.svg)

**Stop AI agents from saying "done" without proof.**

AI agents can claim files were created, refunds were issued, emails were sent, tests passed, tickets closed, or deployments completed — with no execution evidence.

Truth-Artifact Gate catches that failure.

It rejects completion claims unless the runtime can point to an artifact, receipt, trace, hash, timestamp, readback, or verified side effect.

```text
AI agent: "I issued the customer refund."
Runtime: "Where is the payment processor receipt?"
No receipt: rejected.
```

This is not a prompt trick. It is not a model benchmark. It is not another approval layer.

It is a runtime boundary between language and evidence.

## Core rule

Generated claims are not facts.

An agent may generate a claim, but the runtime does not accept that claim as true unless it is backed by execution evidence.

No artifact means no admissible completion.

## 60-second demo

Open `demo/index.html` in a browser. No server. No model. No dependencies.

Live demo after GitHub Pages is enabled:

```text
https://calebperez23.github.io/truth-artifact-gate/demo/
```

The demo shows three cases:

1. **Fabricated refund claim** -> rejected because no payment receipt exists.
2. **Executed report completion** -> admitted because an artifact, hash, and timestamp exist.
3. **Stale deployment evidence** -> rejected because evidence no longer matches.

## Why this matters

Agent systems increasingly perform real work. The failure mode is no longer only "bad answer."

The dangerous failure is an agent claiming work was completed when the world contains no proof that it happened.

Truth-Artifact Gate treats completion as an evidentiary state, not a sentence.

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

## Status

Public-safe proof pack.

It intentionally does **not** include private runtime internals, identity material, local paths, confidential implementation files, model prompts, or sensitive evidence archives.

## License

Copyright (c) 2026 Caleb Perez. All rights reserved.

No license is granted unless explicitly stated in `LICENSE`.
