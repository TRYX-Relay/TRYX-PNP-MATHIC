# Problem No Problem — paper and reproducibility

**Virgil Lee Gattenby**

[Read the approved paper](editions/20260918T220300Z/Problem_No_Problem_Paginated.pdf) · [Edition source and lock](editions/20260918T220300Z/README.md) · [Current submission](../../README.md)

The locked September 18 edition contains the splash, four figures, and numbered pages 1–17. `MANUSCRIPT.md` is the preserved earlier manuscript; it is not the current submission paper.

## Verify from the repository root

```sh
python3 publications/pnp-mathic/check_package.py
```

Python 3 standard library only. This checks required submission roles and hashes, preserved package hashes, the finite replay and independently generated bit-mask oracle across initial and intermediate states. It also detects the OR-to-AND negative control.

Recorded result: **17,902 formulas; 53,706 folds; 16,241 SAT; 1,661 UNSAT; zero disagreements.** The clause population is the 26 nonempty clauses of widths 1–3 on three variables. Formulas use 0–4 distinct clauses.

- [Current authority record](../../submission/AUTHORITY.md)
- [Current submission manifest](../../submission/MANIFEST.json)
- [Lean project and checker coverage](../../verification/tryx-lean/README.md)
- [Current verification receipt](../../submission/VERIFICATION.md)
- [Canonical score](../../charts/pnp/TRYX.PNP.LOCAL.CLOSURE.MATHIC.SCORE.LYRIC.SUCCESSOR.260905.LOCKED.html) and [governing source](sources/TRYX.PNP.CONTINUITY.CLOSURE.REINTRODUCTION.BENCHMARK.260831.235122Z.md)
- [Replay result](replay-result.json) and [independent result](independent-result.json)
- [Citation](../../CITATION.cff) and [historical records](../../archive/README.md)

The verified semantic result and finite benchmark do not supply the standard-machine polynomial cost bound required for conventional P=NP. Historical receipts retain their original dates and scope.
