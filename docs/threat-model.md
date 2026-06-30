# Threat model

Truth-Artifact Gate is aimed at a narrow failure mode:

> An AI agent claims work was completed when no execution evidence exists.

## In scope

- Fabricated completion claims
- Missing artifacts
- Stale artifacts
- Hash mismatches
- Path mismatches
- Claim/evidence mismatch
- Confusing approval with execution
- Confusing generated narration with verified occurrence

## Out of scope for this minimal proof

- Full sandboxing
- Access control
- Secrets management
- End-to-end provenance chains
- Cryptographic signing
- Remote API receipt verification
- Model behavior evaluation
- Enterprise policy enforcement

Those belong in a larger runtime. This demo proves the smaller boundary first.

## Attacker/failure examples

### Fabricated completion

The agent says a report exists. No file exists.

Gate verdict: `INADMISSIBLE`.

### Tampered artifact

The agent says a report was created with a known hash. The file exists but content changed.

Gate verdict: `REJECTED`.

### Stale evidence

The agent references an old file unrelated to the current claim.

Gate verdict: `REJECTED` or `INADMISSIBLE`, depending on policy.

### Valid completion

The file exists and its SHA-256 hash matches the claimed artifact hash.

Gate verdict: `ADMISSIBLE`.


