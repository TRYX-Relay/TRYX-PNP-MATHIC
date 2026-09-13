# Problem No Problem / P vs NP — standalone public review fortress

[![Finite package replay](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-package.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-package.yml)
[![PNP Lean + independent checker](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-lean.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-lean.yml)

**Virgil Lee Gattenby** — TRYX / ENIAD / MATHIC

```text
PUBLIC_OPERATING_MODE = STANDALONE_REVIEW_FORTRESS
PUBLIC_FORTRESS_TARGET = TRYX-PNP-MATHIC
CANONICAL_REVIEW_TARGET = Problem_No_Problem_MATHIC
OTHER_PUBLIC_RELEASE_DEPENDENCY = NONE
CROSS_RELEASE_REVIEW_ROUTING = NONE
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

This repository is the complete public review surface for the current Problem No Problem release. Review, reproduction, citation, audit, and challenge do not require another TRYX research repository.

## Claim firewall

The package proves the stated finite-carrier Boolean semantic result and reproduces the recorded finite benchmark. It does **not** supply the standard-machine polynomial runtime bound required to establish conventional P=NP.

Passing CI, the finite benchmark, the MATHIC score, or Lean acceptance does not promote that boundary.

## Canonical review route

1. **Canonical MATHIC score:** [TRYX.PNP.LOCAL.CLOSURE.MATHIC.SCORE.LYRIC.SUCCESSOR.260905.LOCKED.html](charts/pnp/TRYX.PNP.LOCAL.CLOSURE.MATHIC.SCORE.LYRIC.SUCCESSOR.260905.LOCKED.html)
2. **Governing source:** [TRYX.PNP.CONTINUITY.CLOSURE.REINTRODUCTION.BENCHMARK.260831.235122Z.md](publications/pnp-mathic/sources/TRYX.PNP.CONTINUITY.CLOSURE.REINTRODUCTION.BENCHMARK.260831.235122Z.md)
3. **Conventional manuscript:** [MANUSCRIPT.md](publications/pnp-mathic/MANUSCRIPT.md)
4. **Lean formalization scope:** [PNP.md](verification/tryx-lean/PNP.md)
5. **Lean proof source:** [TryxProof.lean](verification/tryx-lean/TryxProof.lean)
6. **Lean + independent-checker receipt:** [PNP_LEAN_VERIFICATION.RECEIPT.md](review/PNP_LEAN_VERIFICATION.RECEIPT.md)
7. **Finite replay evidence:** [replay-result.json](publications/pnp-mathic/replay-result.json) and [independent-result.json](publications/pnp-mathic/independent-result.json)
8. **Reviewer manifest:** [PNP_REVIEW_PACKET_v1_0.MANIFEST.md](review/PNP_REVIEW_PACKET_v1_0.MANIFEST.md)
9. **Parked release record:** [PNP_REVIEW_RELEASE_v1_0.PARKED.md](review/PNP_REVIEW_RELEASE_v1_0.PARKED.md)
10. **Fortress closeout:** [PNP_PUBLIC_FORTRESS_CLOSEOUT_v1_0.md](review/PNP_PUBLIC_FORTRESS_CLOSEOUT_v1_0.md)
11. **Citation:** [CITATION.cff](CITATION.cff)
12. **Provenance:** [PROVENANCE.md](PROVENANCE.md)

Current GitHub release: [v1.0.0 — Problem No Problem Mathic: Local Closure and Lean Verification](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/releases/tag/v1.0.0)

## Verified mathematical scope

The Lean project contains three PNP statements:

- `TRYX.PNP.boolean_fold_algebra`: Boolean OR agrees with the integer identity `a + b - ab` under Boolean encoding.
- `TRYX.PNP.hinge_exact`: one current-state hinge is true exactly when one of its two Boolean siblings is true.
- `TRYX.PNP.resolve_correct`: repeated current-state existential elimination over `Assignment n` is true exactly when a satisfying assignment exists.

The formalization is semantic. It does not bound the size or cost of the represented Boolean function, normalization, witness reconstruction, or execution on a standard machine.

```text
BOOLEAN_FOLD_IDENTITY = VERIFIED
FINITE_CARRIER_EXISTENTIAL_SEMANTICS = LEAN_VERIFIED
SAT_UNSAT_TERMINAL_SEMANTICS = LEAN_VERIFIED
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
REPRESENTATION_SIZE_BOUND = OPEN
NORMALIZATION_COST_BOUND = OPEN
WITNESS_RECONSTRUCTION_COMPLEXITY = OPEN
```

## Finite replay

From the repository root:

```sh
python3 publications/pnp-mathic/check_package.py
```

Recorded benchmark:

```text
FORMULAS = 17,902
FOLDS = 53,706
DISAGREEMENTS = 0
NEGATIVE_CONTROL = OR replaced with AND: DETECTED
```

The package checker validates source hashes, reruns the archived finite replay, compares a separately generated Boolean-mask oracle across initial and intermediate states, and confirms the negative control.

## Machine-verification boundary

Two active PNP CI paths are authoritative:

- `.github/workflows/verify-pnp-package.yml` — finite package replay, independent oracle, source-integrity checks, and negative control.
- `.github/workflows/verify-pnp-lean.yml` — pinned Lean build plus Comparator/nanoda independent checking of the accepted proof project.

The preserved `.github/workflows/verify-tryx-formulas.yml` is historical/manual only. The accepted proof project contains three older Navier-Stokes accounting statements alongside the three PNP statements because that is the byte-preserved project that received the independent checker acceptance. Those co-resident statements are not PNP results and are not a cross-release review dependency.

Accepted PNP verification source commit: `496c55eb628588d1afbb49233ab8b91ddb82a271`.

Accepted workflow run: `34445813111`.

Independent checker job: `102771173054`.

Lean toolchain: `4.34.0-rc2`.

Mathlib revision: `85e3a25e006c35636f0e53b0e9296caca2685bc0`.

See the [verification receipt](review/PNP_LEAN_VERIFICATION.RECEIPT.md) for exact pins, theorem scope, kernel acceptance, independent-checker acceptance, and audit notes.

## Independent review

A challenge to this release should identify the exact layer under review:

- locked score/source semantics;
- Lean theorem translation;
- Lean kernel acceptance;
- Comparator/nanoda independent checking;
- finite replay or negative control;
- representation-size, normalization, witness-reconstruction, or standard-machine runtime obligations.

When reporting a result, include the repository commit, command or workflow, input, and observed output. The open complexity obligations are part of the public claim boundary, not hidden assumptions.
