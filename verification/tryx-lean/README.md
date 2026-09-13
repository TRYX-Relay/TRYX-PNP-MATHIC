# Problem No Problem Lean verification project

This directory is the preserved Lean 4 proof project used for the public Problem No Problem verification path.

The PNP-facing theorem scope is defined in [`PNP.md`](PNP.md) and implemented in [`TryxProof.lean`](TryxProof.lean). The project also contains three older Navier-Stokes accounting lemmas because the accepted source verification was performed on this combined proof project. Those co-resident lemmas are preserved provenance and are not PNP results or public-review dependencies.

## PNP theorem scope

The current PNP formalization verifies:

1. `TRYX.PNP.boolean_fold_algebra` — Boolean OR under 0/1 integer encoding satisfies `a + b - ab`.
2. `TRYX.PNP.hinge_exact` — one current-state existential hinge is true exactly when one Boolean sibling is true.
3. `TRYX.PNP.resolve_correct` — repeated current-state existential elimination over every finite typed assignment carrier is true exactly when a satisfying assignment exists.

This is a semantic theorem over finite Boolean function carriers. It does not prove a polynomial bound for representation size, substitution, multiplication, normalization, witness reconstruction, or total execution cost on a standard machine. It therefore does not establish conventional P=NP.

## Reproduce locally

The project pins Lean and its dependencies. From this directory:

```sh
lake exe cache get
lake build TryxProof
lake env lean TryxProof.lean
```

Pinned Lean toolchain:

```text
leanprover/lean4:v4.34.0-rc2
```

Pinned Mathlib revision:

```text
85e3a25e006c35636f0e53b0e9296caca2685bc0
```

## Canonical public CI

The authoritative public PNP formal-verification workflow is:

```text
.github/workflows/verify-pnp-lean.yml
```

It builds the preserved solution source, prints theorem axioms, audits `TryxProof.lean` for proof placeholders or project axiom declarations, and runs the independent Comparator + lean4export + nanoda path in a job that does not precompile the solution before Comparator checks it.

The older `.github/workflows/verify-tryx-formulas.yml` remains manual-only as a historical reproduction path for the mixed proof project.

## Accepted verification evidence

The accepted PNP source commit was:

```text
496c55eb628588d1afbb49233ab8b91ddb82a271
```

Accepted workflow run:

```text
34445813111
```

Build job: `102770247621` — success.

Independent job: `102771173054` — success.

The accepted independent job reported both:

```text
nanoda kernel accepts the solution
Lean default kernel accepts the solution
```

See [`../../review/PNP_LEAN_VERIFICATION.RECEIPT.md`](../../review/PNP_LEAN_VERIFICATION.RECEIPT.md) for the full public receipt and exact claim boundary.

## Challenge file

`TryxChallenge.lean` intentionally contains `sorry` placeholders because it specifies the statements supplied to Comparator. The solution source is `TryxProof.lean`; the public workflow audits that solution file separately. A `sorry` in the challenge specification is therefore not a proof gap in the accepted solution.
