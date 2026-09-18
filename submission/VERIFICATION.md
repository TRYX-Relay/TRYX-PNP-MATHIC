# PNP verification coverage and accepted baseline

This record distinguishes the preserved proof baseline from submission packaging changes. Read the Actions results for the exact commit being submitted; a badge or an earlier receipt is not a substitute for that identity.

## Audited baseline

Public commit: `fbd6c7f2789d1ea097d49bc6aef4fdfcb43b8e4f`.

- [Finite-package run 35401900978](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/runs/35401900978): PASS, job `105783413424`.
- [Lean run 35401900974](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/runs/35401900974): build PASS, job `105783413569`; independent checking PASS, job `105783914661`.
- Python replay was also rerun locally: 17,902 formulas, 53,706 folds, zero disagreements; intermediate-state oracle and negative control pass.

## Exact formal scope

| Source | Declared theorem coverage | Independent checker |
|---|---|---|
| TryxProof.lean | Three PNP semantic theorems and three historical accounting lemmas | All six named in comparator.json |
| TryxMathic.lean | 13 bridge declarations, including mirror-truth and semantic local closure | Not selected by comparator.json; Lean compilation only |

The independent proof targets are `TRYX.PNP.boolean_fold_algebra`, `TRYX.PNP.hinge_exact`, `TRYX.PNP.resolve_correct`, and the preserved `TRYX.NS.one_tension_accounting`, `TRYX.NS.v6_recorded_positive_remainder`, `TRYX.NS.v6_atomic_remainder_not_exhausted`.

The [current Lean README](../verification/tryx-lean/README.md) gives reproduction instructions. The [historical receipt](../review/PNP_LEAN_VERIFICATION.RECEIPT.md) preserves the earlier acceptance history. The 13 bridge declarations do not add a standard-machine complexity theorem.

## Submission cleanup scope

Cleanup changes navigation, authority records, completeness/integrity checks and public availability of the approved paper. `TryxProof.lean`, `TryxMathic.lean`, `TryxChallenge.lean`, `comparator.json`, the toolchain and dependency pins retain their audited bytes. The final paper, Reader Guide, score, governing source and v65 instrument are preserved byte-for-byte.

Both active workflows run for the cleanup commit. Their outputs certify only their stated checks; no new independently checked bridge theorem is claimed by this record.
