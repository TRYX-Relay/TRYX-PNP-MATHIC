# Problem No Problem Local Fortress Build v1.1 — Receipt

Date: `2026-09-13`

Status: `LOCAL_FORTRESS_BUILD = PASS`

## Build identity

```text
TARGET = TRYX-Relay/TRYX-PNP-MATHIC
BUILD_MODE = LOCAL_SUCCESSOR_OVERLAY
PINNED_PUBLIC_BASE_COMMIT = b71012c6d9570e722e86b8a9d89ac43a3a623752
PINNED_PUBLIC_BASE_TREE = e9d22cd44a16d89bc83888f4a217a20faecaeacc
MATH_SOURCE_MUTATION = NONE
LOCKED_SCORE_MUTATION = NONE
LOCKED_GOVERNING_SOURCE_MUTATION = NONE
```

The local build is an overlay on the pinned public base tree. Mathematical authorities not listed as successor files are inherited unchanged from that base at export.

## Byte-preservation checks

```text
TRYX_PROOF_LOCAL_SHA256 = 6f033b4106665a9815c44646eb82a6fbc8dae472819d87b66e365f5bfb304348
TRYX_PROOF_EXPECTED_SHA256 = 6f033b4106665a9815c44646eb82a6fbc8dae472819d87b66e365f5bfb304348
TRYX_PROOF_BYTE_PRESERVATION = PASS

LOCKED_SCORE_EXPECTED_SHA256 = 95b63f3ce280a494ac1be28d222bd03bc1da010e17ec6be3a1ba3438687073fb
GOVERNING_SOURCE_EXPECTED_SHA256 = 9a611f7c1ae0d3a1f299411d83146dfbd7ddf8b7bd693b9fddd20f7d1badaa3a
MANUSCRIPT_EXPECTED_SHA256 = 55db0ec8fdd5157b5b9dc8fde594e87d4b679f8a3e83109f975dc80c807c5154
```

The score, governing source, and manuscript are inherited from the pinned base Git tree rather than rewritten locally.

## Local finite replay

Local execution of the preserved replay algorithm produced:

```text
FORMULAS = 17902
FOLDS = 53706
SAT = 16241
UNSAT = 1661
FAILURES = 0
LOCAL_REPLAY = PASS
```

Receipt: `review/PNP_LOCAL_REPLAY_v1_1.json`.

## Local independent oracle

The independent bit-mask oracle checked every initial and intermediate benchmark state and produced:

```text
FORMULAS = 17902
FOLDS = 53706
DISAGREEMENTS = 0
INTERMEDIATE_STATE_CHECKS = PASS
NEGATIVE_CONTROL = OR replaced with AND: DETECTED
LOCAL_INDEPENDENT_ORACLE = PASS
```

Receipt: `review/PNP_LOCAL_INDEPENDENT_v1_1.json`.

## Local proof-source audit

The byte-matched `TryxProof.lean` source was scanned for project proof placeholders/declarations:

```text
SORRY = 0
ADMIT = 0
PROJECT_AXIOM_DECLARATIONS = 0
SOURCE_AUDIT = PASS
```

The local environment does not install Lean dependencies from the network. Machine proof execution is therefore anchored to the public GitHub Actions revalidation below rather than falsely described as a local kernel run.

## Public machine revalidation

```text
PUBLIC_REVALIDATION_RUN = 34790598360
BUILD_JOB = 103813972219
BUILD_JOB = PASS
INDEPENDENT_JOB = 103814291339
INDEPENDENT_JOB = PASS
COMPARATOR = PASS
NANODA = PASS
```

This public successor run executes the same pinned proof project that is preserved in the standalone repository.

## Fortress audits

```text
CANONICAL_REVIEW_ROUTE = PASS
CLAIM_FIREWALL_PRESENT = PASS
CROSS_RELEASE_REVIEW_ROUTING = NONE
OTHER_PUBLIC_RELEASE_DEPENDENCY = NONE
NEW_PUBLIC_TERMINOLOGY = TRYX / ENIAD / MATHIC
HISTORICAL_ENAID_MUTATION = NONE
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

## Terminal local state

```text
LOCAL_FORTRESS_BUILD = PASS
EXPORT_MANIFEST = READY
REPOSITORY_EXPORT = AUTHORIZED_BY_COMMANDERS_INTENT
GITHUB_UI_METADATA = SEPARATE_PATCH_SURFACE
```
