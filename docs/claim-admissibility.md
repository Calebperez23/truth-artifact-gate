# Claim admissibility

Most agent systems treat completion as language:

> "Done."

Truth-Artifact Gate treats completion as evidence:

> "Admissible only if a runtime artifact proves the claimed event occurred."

## The problem

Agents can generate fluent claims about actions they did not execute:

- "I created the file."
- "I sent the email."
- "I ran the tests."
- "I deployed the patch."
- "I updated the record."

The user sees a confident sentence. The world may contain no evidence that anything happened.

## The boundary

Truth-Artifact Gate separates three things:

1. **Permission** - the action was allowed.
2. **Execution** - the action actually occurred.
3. **Claim admissibility** - the agent may truthfully claim completion.

Approval is not execution.

Generated text is not execution.

Only evidence can make the completion claim admissible.

## Evidence examples

A completion claim may be admitted if evidence exists, such as:

- file path + SHA-256 hash + timestamp
- command trace + exit code + captured output hash
- sent-message receipt
- ticket ID + API response
- deployment ID + provider receipt
- ledger entry + readback confirmation

The evidence must be specific enough to distinguish a real event from a plausible sentence.

## Verdicts

- `INADMISSIBLE`: no artifact or insufficient evidence.
- `ADMISSIBLE`: artifact exists and matches claimed evidence.
- `REJECTED`: artifact is missing, stale, tampered, mismatched, or outside scope.

## Principle

The action is not the only thing that needs governance.

The claim about the action needs admissibility.
