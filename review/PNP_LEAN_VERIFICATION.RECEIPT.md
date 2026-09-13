# Problem No Problem — Lean and Independent Verification Receipt

Date: `2026-09-13`

Status: `ACCEPTED_SOURCE_VERIFICATION = PASS / PUBLIC_SUCCESSOR_WORKFLOW = ACTIVE`

## Verification identity

```text
RESEARCH = Problem No Problem / P vs NP
PNP_SOURCE_COMMIT = 496c55eb628588d1afbb49233ab8b91ddb82a271
SOURCE_REPOSITORY_AT_ACCEPTANCE = TRYX-Relay/TRYX-MATHIC
ACCEPTED_WORKFLOW = Verify TRYX formulas
WORKFLOW_RUN = 34445813111
BUILD_JOB = 102770247621
INDEPENDENT_JOB = 102771173054
WORKFLOW_RESULT = SUCCESS
PUBLIC_SUCCESSOR_WORKFLOW = .github/workflows/verify-pnp-lean.yml
```

The accepted source commit was produced in the source repository before the standalone public PNP export. The exact accepted proof source and pinned dependency files are reproduced in this repository. The standalone public workflow is a successor review surface, not a claim that the historical run occurred in this public repository.

## Toolchain and dependency pins

```text
RUNNER = ubuntu-24.04
LEAN = 4.34.0-rc2
LEAN_BUILD_COMMIT = 6a10ac8c22beadecabdbb0919c2b50214762f91d
MATHLIB = 85e3a25e006c35636f0e53b0e9296caca2685bc0
COMPARATOR = 19e111e2141cf333c7daff0f64c5f24acc91dd2e
LEAN4EXPORT = cacf989bd75f608700820f6afc595f32e7a99a4d
LANDRUN = 811cfff51ceaf3d9843708aa6d22e9b84ccac8b4
NANODA = 4c544ed4099c8227f07d5de77ad1e69fb0740a27
```

The accepted workflow verified that the checked-out dependency revisions matched the pinned `lake-manifest.json`.

## Accepted PNP theorem scope

The PNP proof source contains these three public statements:

1. `TRYX.PNP.boolean_fold_algebra`
   - Boolean OR, encoded in integers as 0/1, satisfies the identity `a + b - ab`.
2. `TRYX.PNP.hinge_exact`
   - A current-state existential hinge is true exactly when one Boolean sibling evaluates true.
3. `TRYX.PNP.resolve_correct`
   - For every natural-number carrier size `n` and Boolean function `f : Assignment n → Bool`, repeated semantic elimination returns true exactly when there exists `a : Assignment n` with `f a = true`.

The accepted Lean output reports the PNP theorems as depending on Lean's standard `propext` axiom only.

## Kernel and independent checker state

The accepted build job completed successfully. The independent job built checking tools before the solution and verified that the solution object had not been precompiled at that stage.

The independent checker then reported:

```text
nanoda kernel accepts the solution
Lean default kernel accepts the solution
Your solution is okay!
Finished with result: success
```

```text
LEAN_DEFAULT_KERNEL = PASS
COMPARATOR = PASS
NANODA = PASS
INDEPENDENT_JOB = PASS
```

## `sorry` and axiom audit

`TryxProof.lean`, the solution source, contains no `sorry`, `admit`, or project `axiom` declaration. The new public successor workflow explicitly enforces that source audit before building.

`TryxChallenge.lean` intentionally contains `sorry` placeholders because it is a statement/challenge specification consumed by Comparator. The accepted independent logs show those warnings while subsequently accepting the separately checked solution with both nanoda and Lean kernels. The challenge placeholders are not solution proof gaps.

## Finite replay evidence

The standalone publication package independently records:

```text
FORMULAS = 17902
FOLDS = 53706
DISAGREEMENTS = 0
SAT = 16241
UNSAT = 1661
NEGATIVE_CONTROL = OR replaced with AND: DETECTED
INTERMEDIATE_STATE_CHECKS = PASS
```

The finite package replay is governed separately by `.github/workflows/verify-pnp-package.yml` and `publications/pnp-mathic/check_package.py`.

## Claim boundary

```text
BOOLEAN_FOLD_IDENTITY = VERIFIED
FINITE_CARRIER_EXISTENTIAL_SEMANTICS = LEAN_VERIFIED
SAT_UNSAT_TERMINAL_SEMANTICS = LEAN_VERIFIED
FINITE_PACKAGE_REPLAY = VERIFIED
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
REPRESENTATION_SIZE_BOUND = OPEN
NORMALIZATION_COST_BOUND = OPEN
WITNESS_RECONSTRUCTION_COMPLEXITY = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

The package proves the stated finite-carrier Boolean semantic result and reproduces the recorded finite benchmark. It does not supply the standard-machine polynomial runtime bound required to establish conventional P=NP.

No CI success, checker acceptance, benchmark count, or MATHIC score changes that boundary.
