# PNP Lean verification

[Current submission](../../README.md) · [Formalization scope](PNP.md) · [Verification receipt](../../submission/VERIFICATION.md)

This is the current public PNP proof project. The older private export lacks `TryxMathic.lean`; use this complete directory and its pinned dependencies for the current build.

## Coverage

| Layer | Files and statements | Verification |
|---|---|---|
| PNP semantic core | `TryxProof.lean`: `boolean_fold_algebra`, `hinge_exact`, `resolve_correct` in `TRYX.PNP` | Lean and configured Comparator/nanoda targets |
| MATHIC bridge | `TryxMathic.lean`: 13 theorem declarations in `TRYX.PNP.Mathic` | Lean compilation and selected axiom reports; not configured as Comparator targets |
| Historical accounting | Three `TRYX.NS` declarations in `TryxProof.lean` | Preserved accepted Comparator targets; not PNP premises |

The MATHIC bridge preserves native M0–M9 naming/order and formalizes selected type, rotation, mirror truth and semantic fold/closure facts. Its terminal result delegates to `resolve_correct`. It does not certify the entire notation system, a provenance implementation, a CNF evaluator or polynomial machine cost.

## Reproduce

From this directory, using the pinned toolchain:

```sh
lake exe cache get
lake build TryxProof TryxMathic
lake env lean TryxProof.lean
lake env lean TryxMathic.lean
```

Lean: `leanprover/lean4:v4.34.0-rc2`. Mathlib revision: `85e3a25e006c35636f0e53b0e9296caca2685bc0`. `lake-manifest.json` pins every package revision. The workflow checks these revisions and confirms the manifest has not changed during dependency fetch.

[The PNP workflow](../../.github/workflows/verify-pnp-lean.yml) compiles both modules, audits solution files for proof placeholders/project axioms, prints axiom reports and runs Comparator/nanoda in a separate job. `comparator.json` is authoritative for independent-check targets; it currently selects `TryxProof`, not `TryxMathic`.

`TryxChallenge.lean` intentionally contains reference-statement `sorry` placeholders. They are not proofs and are isolated from the accepted solution. Do not remove historical declarations from the accepted project as a documentation cleanup.

The earlier manual mixed-project workflow is retained as history. Current hosted results and the accepted baseline are recorded in the [verification receipt](../../submission/VERIFICATION.md).
