# P vs NP research — Problem No Problem Mathic and Lean 4 verification

[![Package replay](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-package.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-pnp-package.yml)
[![Lean and independent checker workflow](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-tryx-formulas.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/actions/workflows/verify-tryx-formulas.yml)

Badges show workflow status for the statements in this repository. The scope of each result is described below.

**Virgil Lee Gattenby** — TRYX / ENIAD / MATHIC

Problem No Problem Mathic: current-state existential folding and verified semantic closure.

- [Research manuscript](publications/pnp-mathic/MANUSCRIPT.md)
- [Score, source, benchmarks, and reproduction instructions](publications/pnp-mathic/README.md)
- [Citation](CITATION.cff)
- [Export provenance](PROVENANCE.md)

```sh
python3 publications/pnp-mathic/check_package.py
```

The benchmark checks 17,902 formulas and 53,706 folds with zero disagreements. The inherited Lean project proves semantic correctness on every finite Boolean assignment carrier. A standard-machine polynomial runtime bound establishing conventional P=NP is not supplied.

This standalone publication presents verified semantic closure and a reproducible local closure benchmark. The source private repository and its history are not included.

## Reproduce and inspect

Requires Git and Python 3. From a terminal:

```sh
git clone https://github.com/TRYX-Relay/TRYX-PNP-MATHIC.git
cd TRYX-PNP-MATHIC
python3 publications/pnp-mathic/check_package.py
```

The Python command checks the archived package and replay. To build the formal statements, follow the [pinned Lean project instructions](verification/tryx-lean/README.md).

[Short demonstration walkthrough](DEMONSTRATION.md) · [Citation metadata](CITATION.cff)

## Research storefronts

These public repositories share the TRYX → ENIAD → Laws → MATHIC construction order while preserving separate claim boundaries.

| Research | Current public review focus |
| --- | --- |
| [Navier–Stokes ANEA / MATHIC v7.2](https://github.com/TRYX-Relay/TRYX-Navier-Stokes-Mathic) | Canonical MATHIC review target; Lean-checked finite/algebraic and conditional score; global 3-D regularity remains open |
| **Problem No Problem / P vs NP** | Existential Boolean folding semantics and finite benchmarks; conventional polynomial-time P=NP remains unestablished |
| [Snowman / Collatz conjecture](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic) | Address reconstruction, fold identities, and local continuity checks; universal termination remains unestablished |

## Independent review

Do the existential folds preserve Boolean semantics at every intermediate state, including the negative control? Report the commit, command, input, and observed output in a [repository issue](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/issues). Please distinguish package integrity, replay results, and the exact Lean theorem statement when reporting findings.
