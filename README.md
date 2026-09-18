# Problem No Problem

**Virgil Lee Gattenby**

[![Finite package replay](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-package.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-package.yml)
[![Lean and independent checker](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-lean.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-lean.yml)

**[Read the locked paper — PDF](publications/pnp-mathic/editions/20260918T220300Z/Problem_No_Problem_Paginated.pdf)** · **[Reader Guide — PDF](review/reader-guide/v1_0/Problem_No_Problem_READERS_GUIDE_v1_0.LOCKED.pdf)**

The paper develops exact current-state existential folding on finite Boolean assignment carriers. Its semantic core is machine checked; the finite benchmark reproduces 17,902 formulas and 53,706 folds with zero disagreements. The standard-machine polynomial cost argument required for conventional P=NP remains open.

## Current submission

| Material | Where to start |
|---|---|
| Approved paper, four figures and splash | [Locked 18-page edition](publications/pnp-mathic/editions/20260918T220300Z/README.md); [editable DOCX](publications/pnp-mathic/editions/20260918T220300Z/Problem_No_Problem_Layout_Source.docx) |
| Reading routes, terminology and work metrics | [Reader Guide v1.0](review/reader-guide/v1_0/Problem_No_Problem_READERS_GUIDE_v1_0.LOCKED.pdf) |
| Mathematical authorities | [Locked MATHIC score](charts/pnp/TRYX.PNP.LOCAL.CLOSURE.MATHIC.SCORE.LYRIC.SUCCESSOR.260905.LOCKED.html) and [governing source](publications/pnp-mathic/sources/TRYX.PNP.CONTINUITY.CLOSURE.REINTRODUCTION.BENCHMARK.260831.235122Z.md) |
| Formal proof and exact checker coverage | [Lean project](verification/tryx-lean/README.md) and [current verification receipt](submission/VERIFICATION.md) |
| Reproducible benchmark | [Package instructions](publications/pnp-mathic/README.md) |
| Optional interactive supplement | [Repaired 3E6B v65](charts/pnp/PNP_CODEBREAKER_TRI_E6B_XMAS_FORMULA_PAGE_v65.LOCKED.html) — download and open the HTML |
| Submission identity and citation | [Submission manifest](submission/MANIFEST.json), [current authority record](submission/AUTHORITY.md), [citation](CITATION.cff) |

This index selects the current submission. Earlier drafts, build contracts, waypoints and release records are [historical material](archive/README.md), retained for provenance. The September 11 GitHub release `v1.0.0` is historical; it is not the September 18 paper edition. Use the paper and manifest linked above and record the Git commit used.

## Reproduce

From the repository root:

```sh
python3 publications/pnp-mathic/check_package.py
```

This validates the required submission files and their checksums, the preserved package records, the finite replay, the independent intermediate-state oracle and the OR-to-AND negative control. It does not run Lean. For the pinned formal build, follow the [Lean instructions](verification/tryx-lean/README.md).

Lean builds `TryxProof` and `TryxMathic`. Comparator/nanoda independently checks the six declarations configured in `TryxProof`, including the three PNP core theorems. The 13 MATHIC bridge declarations are Lean checked; they are not additional Comparator targets. Neither layer supplies a polynomial runtime bound.

## Build time and AI drift

AI drift is the worst part of the process, but it is manageable. I keep the accepted source fixed, compare revisions against it, and record the work needed to recover from regressions. Trust is welcome. Receipts are forever.

| Work phase | Recorded metric |
|---|---|
| Original PNP development | Approximately **53h 22m 43s** elapsed; not hands-on labor |
| E6B → 3E6B saved-build window | **71h 24m 40s**, ending at repaired v65 |
| 3E6B September 17 recovery | **6 defect areas sharing one 1h 56m 11s recovery interval** |
| Later PNP paper production | **3h 30m reported lost time**, not independently timed |

These are different clocks. Total drift and active labor remain unknown where evidence is missing; unknown is not zero. See the [work-metrics receipt](review/PNP_3E6B_WORK_METRICS_2026-09-18.md) and [original development-time record](review/PNP_ORIGINAL_DEVELOPMENT_TIME.RECEIPT_v1_0.md).

## Review and provenance

For a challenge or reproduction result, identify the exact source, theorem, input, repository commit and observed output. [Provenance](PROVENANCE.md) records the preserved source lineage and accepted verification history. Artifact locks freeze bytes; they do not expand mathematical claims.
