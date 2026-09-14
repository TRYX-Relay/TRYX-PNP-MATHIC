# Problem No Problem
## Current-State Existential Folding, Native Local Closure, and Lean-Verified Finite Semantics for Boolean Satisfiability

**Scientific Paper Beta 3 — PERSONALITY PASS / NOT LOCKED**  
**Author:** Virgil Lee Gattenby  
**Project:** TRYX / ENIAD / MATHIC  
**Date:** 2026-09-13

```text
PAPER_STATUS = BETA_3_PERSONALITY_PASS
PARENT = PNP_PAPER_BETA_2.md
PAPER_TEMPLATE = Problem_No_Problem_MATHIC_PAPER_SYNC_BETA_4
NATIVE_SCORE = M0-M9_LOCAL_CLOSURE
FORMAL_CORE = TRYX.PNP
FORMAL_MATHIC_BRIDGE = TRYX.PNP.Mathic
LEAN_MATHIC_BUILD = PASS
FINITE_REPLAY = VERIFIED
INDEPENDENT_ORACLE = VERIFIED_FOR_DECLARED_BENCHMARK
PRINCIPAL_FIGURES = 4
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

> **Authority note.** This paper is the conventional scientific exposition of the Problem No Problem research package. The locked local-closure MATHIC and governing source remain the mathematical lineage authority. `TryxProof.lean` supplies the checked finite semantic core; `TryxMathic.lean` supplies the explicit M0–M9 synchronization bridge; the replay and independent checker supply finite executable evidence. The paper may have a voice. The proof still has to show its work.

---

# Contents

1. Abstract  
2. Conventional problem and scope  
3. Terminology and claim boundary  
4. Governing finite semantic formula  
5. Native Local Closure MATHIC, M0–M9  
6. Current-state existential folding  
7. Lean formalization and MATHIC correspondence  
8. Finite benchmark and independent oracle  
9. Results  
10. Standard-machine complexity gate  
11. Dedicated formula progression  
12. Claim-to-source map  
13. Reviewer’s Bench and reproducibility path  
14. Limitations and interpretation  
15. Development and provenance note  
16. Conclusion  
17. References  
18. Reference-activation index  
19. Final closed/open status

---

# 1. Abstract

Boolean satisfiability asks whether a Boolean formula admits at least one satisfying assignment. SAT sits near the center of complexity theory because it is NP-complete under standard polynomial-time reductions [1–5]. This paper presents **Problem No Problem (PNP)**, a TRYX / ENIAD / MATHIC formulation of a finite semantic elimination process for SAT. The construction acts on the **current Boolean state** rather than repeatedly returning to an immutable initial state. At each step, two Boolean sibling restrictions are formed at one selected coordinate and combined by existential OR. On Boolean values the fold is represented algebraically by

\[
a\lor b=a+b-ab.
\]

The folded result becomes the exact current successor and the process repeats until no Boolean coordinate remains. The hinge swings, the fold folds, and the successor actually succeeds something.

The semantic core is machine-checked in Lean. The formal source proves the Boolean fold identity, the exact one-step existential meaning of the current-state hinge, and correctness of repeated finite elimination over the recursively defined Boolean assignment carrier. A second Lean file explicitly synchronizes the native **M0–M9 Local Closure MATHIC** with the formal core, including a distinct M5 mirror/provenance receipt and an end-to-end `localClosureMathicPass`. The strengthened verification workflow compiles both the proof source and the MATHIC bridge successfully and audits them for `sorry`, `admit`, and project `axiom` declarations. In other words, the paper is not being asked to sing a part Lean has never rehearsed.

A separate executable benchmark enumerates a fully specified universe of 17,902 formulas over three variables, performs 53,706 existential folds, and compares every initial and intermediate state with an independently implemented bit-mask oracle. The declared benchmark contains 16,241 SAT formulas and 1,661 UNSAT formulas, with zero recorded disagreements. Replacing OR by AND is detected as a deliberate negative control. A checker should object when the operator is wrong. Otherwise it may simply be being agreeable.

These results establish a checked **finite semantic closure** for the stated carrier and execution rule. They do not establish a polynomial bound on evolving representation size, normalization, substitution, multiplication or equivalent composition, witness reconstruction, or total deterministic standard-machine runtime in the original input length. The current truth-table replay begins with \(2^n\) states and is therefore not itself a polynomial-time SAT algorithm. Accordingly, this paper does **not** claim a conventional proof that \(P=NP\). The fold may be exact. The machine bill still has to be paid.

---

# 2. Conventional problem and scope

## 2.1 SAT and the P-versus-NP boundary

For a Boolean formula \(F\) on variables \(x_1,\ldots,x_n\), satisfiability asks whether there exists an assignment

\[
a\in\{0,1\}^n
\]

such that \(F(a)=1\). Cook’s 1971 theorem established the foundational NP-completeness result for the satisfiability family, Levin independently developed the closely related universal-search formulation, and Karp’s reductions placed a broad family of combinatorial problems into the same polynomial-reduction landscape [1–3]. Modern treatments formalize the familiar consequence: a deterministic polynomial-time algorithm for an NP-complete problem such as SAT would imply \(P=NP\) [4–6].

The conventional target is therefore not merely semantic correctness. It is a machine-cost statement. A proposed SAT procedure must be realizable by a standard deterministic computational model with total running time bounded by a polynomial in the length of the original encoded input [4,5]. Intermediate representations count. So do substitution, normalization, equality testing, and any claimed witness reconstruction. Complexity theory, unlike a forgiving bartender, keeps the entire tab.

PNP separates two questions that are easy to blur:

```text
SEMANTIC QUESTION
Does repeated current-state elimination preserve exact existential truth?

COMPLEXITY QUESTION
Can every represented state and every required operation be realized with total
standard-machine cost polynomial in the original input length?
```

The present package answers the first question in the affirmative for its declared finite carrier. It leaves the second open. Two questions, two receipts.

## 2.2 Why current state matters

The PNP construction does not treat each later elimination as a fresh search from the original formula. The object of computation is the Boolean state currently present after the preceding elimination. One coordinate is exposed, its two sibling restrictions are compared, their existential union is formed, and that union becomes the next exact current state.

This is a simple rule with an important consequence: the successor is not a souvenir from the previous step. It is the next state.

Symbolic representations of Boolean functions have a long history, from Shannon’s switching algebra to later graph-based Boolean-function representations [7,8]. Such work supplies useful external context for restriction, symbolic manipulation, and representation size. It does not establish the internal PNP theorem. In particular, Bryant’s analysis of symbolic Boolean functions is a useful caution that semantically compact operations do not guarantee compact representations in the worst case [8]. A small answer can still arrive with oversized luggage.

**Figure 1 placeholder — Semantic closure versus complexity gate**  
**Location:** after §2.2.  
**Footprint:** full width, approximately one-half page.  
**Purpose:** visually separate the verified finite semantic route from the still-open standard-machine cost route.  
**Required content:** finite Boolean state → native Local Closure mechanism → SAT/UNSAT terminal on one lane; representation size / operation cost / normalization / witness reconstruction → polynomial-time gate on a separate lane.  
**Working caption:** **Figure 1. Semantic closure and the conventional complexity gate.** The finite semantic path closes. The machine-cost gate does not open merely because the mathematics reached the door.

---

# 3. Terminology and claim boundary

The paper uses a small internal vocabulary because the MATHIC score is a typed execution record. Those terms are not substitutes for standard complexity-theory definitions [4–6]. A hinge may be a hinge, but naming it one does not grant it constant-time hardware.

| Term | Meaning here | It does not establish |
|---|---|---|
| **Current state** | The exact Boolean function or finite Boolean table active at the present elimination level | A compact polynomial-size representation |
| **Sibling restrictions** | The current state restricted at the selected coordinate to false and true | Permanently queued search branches |
| **Hinge** | The local act of presenting the two sibling values for existential comparison | Constant-time computation on arbitrary encodings |
| **Mirror closure** | The M5 provenance step that retains shared lawful truth once and carries unmatched residue | A separate conventional complexity theorem |
| **Fold** | M6 existential elimination of the selected Boolean coordinate by OR | Polynomial total runtime |
| **Successor** | The folded state admitted as the next exact current state | Polynomial-size normalization |
| **Ordinal succession** | Repetition of the same lawful local measure on the current successor | A runtime bound merely from the number of levels |
| **Local closure** | Final scalar truth equals existential truth over the finite carrier | Conventional \(P=NP\) |
| **SAT terminal** | Final scalar `true` | Polynomial-time witness extraction |
| **UNSAT terminal** | Final scalar `false` | A lower-bound result or proof-system result |
| **Lean verified** | The stated Lean theorem compiles in the pinned project and is accepted by the checked formal environment | Verification of claims not present in the theorem statement |
| **Conventional \(P=NP\)** | The standard complexity-theoretic statement that deterministic polynomial time equals nondeterministic polynomial time | Any finite identity, finite replay, or number of elimination levels by itself |

The governing firewall is therefore

\[
\boxed{
\text{finite semantic closure}
\neq
\text{standard-machine polynomial-time closure}.
}
\]

That inequality is the paper’s bouncer. Attractive claims still need identification.

---

# 4. Governing finite semantic formula

Let \(f\) be the current Boolean-valued state and let \(x\) be the selected Boolean coordinate. Write the two current sibling restrictions as

\[
f_0=f\vert_{x=0},
\qquad
f_1=f\vert_{x=1}.
\]

For Boolean values \(a,b\in\{0,1\}\),

\[
\boxed{a\lor b=a+b-ab.}
\]

Accordingly,

\[
\boxed{
\mathcal E_x(f)=f_0\lor f_1
=f_0+f_1-f_0f_1.
}
\]

The algebraic form is a Boolean identity, not an efficiency claim. It tells us what the fold means, not what the fold costs. Shannon’s switching-algebra work provides historical context for algebraic handling of Boolean relations [7]; the authority for the present identity inside this package is the Lean theorem `TRYX.PNP.boolean_fold_algebra`.

Pointwise on a remaining assignment \(r\),

\[
\boxed{
\mathcal E_x(f)(r)=1
\iff
\exists b\in\{0,1\}\; f(b,r)=1.
}
\]

Thus one fold removes one Boolean coordinate while preserving exact existential truth on the remaining carrier. One coordinate leaves the stage. The truth it carried does not have to leave with it.

Define the finite assignment carrier recursively by

\[
A_0=\{()\},
\qquad
A_{n+1}=\{0,1\}\times A_n.
\]

For \(f:A_n\to\{0,1\}\), repeated current-state elimination yields

\[
\boxed{
R_n(f)=1
\iff
\exists a\in A_n\;f(a)=1.
}
\]

This is the core semantic statement formalized by `TRYX.PNP.resolve_correct`.

---

# 5. Native Local Closure MATHIC, M0–M9

The paper inherits the native score from the locked local-closure MATHIC. The measure order is not ornamental numbering. It is the declared execution order that the paper, Lean synchronization file, figures, and later Reviewer’s Bench must share.

| Measure | Native role | Paper interpretation |
|---|---|---|
| **M0 · Type-Set Zero** | base + law | admit the governing base and typed starting condition |
| **M1 · Distinction** | \(0\leftrightarrow1\) | expose the Boolean distinction |
| **M2 · Current number** | \(N_i=\langle V_i,P_i,A_i\rangle\) | constitute the exact current formula-state |
| **M3 · VPA rotation** | \(V\to P\to A\) | preserve the typed local transition |
| **M4 · Hinge siblings** | current sibling reflection | form \(f_i|_{x_i=0}\) and \(f_i|_{x_i=1}\) |
| **M5 · Mirror closure** | provenance / shared once / residue \(\Delta\) | preserve shared and unmatched truth lanes before existential collapse |
| **M6 · Existential fold** | \(a+b-ab\) | apply exact Boolean OR |
| **M7 · Current successor** | \(\sigma_{i+1}\) | admit the folded result as the next exact current state |
| **M8 · Ordinal succession** | \(\tau_i\to\tau_{i+1}\) | repeat on the current successor |
| **M9 · Local closure** | scalar terminal | return SAT/UNSAT semantic truth |

The locked lyric lines are retained as phase-recognition cues, not as proof objects:

> **M0:** Value first: hold the governing three before distinction.  
> **M1:** Perceive the distinction; let zero and one appear.  
> **M2:** Constitute the current number: Value, Perception, Action.  
> **M3:** Turn Value to Perception, Perception to Action.  
> **M4:** Present both hinge Values as siblings; compare without erasing.  
> **M5:** Cancel only the certified mirror; carry every unmatched residue.  
> **M6:** Act through Fold₀: a plus b, less their shared return.  
> **M7:** Bind the lawful successor; let the variable rank descend.  
> **M8:** What Action brings forward emerges as the next exact Value.  
> **M9:** The scalar returns T₉ to T₀; local closure, Value again.

The score has a musical vocabulary because it behaves like one: every measure has an office, every transition has timing, and skipping M5 because M6 looks more exciting still means you skipped a measure.

## 5.1 M0 and M1: typed admission and distinction

M0 admits the local score before a Boolean choice is exercised. In the formal carrier, the zero-coordinate assignment type is `Unit`. M1 activates the Boolean distinction between `false` and `true`. The corresponding Lean MATHIC bridge includes `m0_type_set_zero` and `m1_distinction`.

Shannon [7] is relevant only as historical Boolean context at M1. No outside citation is allowed to wear an internal theorem’s nametag.

## 5.2 M2 and M3: current state and typed rotation

M2 identifies the state actually being operated on now. M3 expresses the local TRYX office rotation \(V\to P\to A\), formalized in the MATHIC bridge as a three-state rotation whose third iterate is identity.

The practical rule is plain: work on what is in your hand, not what was in your hand three moves ago.

## 5.3 M4: hinge siblings

Given current state \(f_i\) and selected coordinate \(x_i\), M4 forms

\[
V_i^0=f_i\vert_{x_i=0},
\qquad
V_i^1=f_i\vert_{x_i=1}.
\]

Only the **current** state is restricted. After a successor has been produced, later sibling states derive from that successor rather than being reconstructed from the immutable bootstrap state.

The hinge does what good hinges do: it holds two sides in relation without pretending they are the same side.

## 5.4 M5: mirror closure as a distinct provenance measure

M5 is deliberately kept separate from M6. Its role is to account for shared lawful truth once and preserve unmatched residue before the existential collapse. In the Lean MATHIC bridge, a `MirrorReceipt` stores

\[
\text{shared}=a\land b,
\]

\[
\text{left residue}=a\land\neg b,
\qquad
\text{right residue}=\neg a\land b.
\]

The retained truth is the OR of those three lanes. The bridge theorem `m5_mirror_preserves_truth` verifies

\[
\text{retained truth}=a\lor b.
\]

A mirror is useful precisely because it reflects without becoming the object. M5 records provenance. M6 performs the existential action. That distinction is small on the page and large in the bookkeeping.

## 5.5 M6: exact existential fold

M6 applies existential OR to the certified sibling pair:

\[
\boxed{
\mathcal E_{x_i}(f_i)
=f_i|_{x_i=0}+f_i|_{x_i=1}
-f_i|_{x_i=0}f_i|_{x_i=1}.
}
\]

On Boolean inputs this is exactly

\[
f_i|_{x_i=0}\lor f_i|_{x_i=1}.
\]

The formal core proves both the algebraic identity and the one-step existential theorem. The MATHIC bridge additionally proves that its M6 function agrees with the underlying formal `hinge`.

This is a fold in the useful sense of the word: two exposed possibilities become one successor without losing the existential question they answered.

## 5.6 M7 and M8: exact successor and ordinal succession

M7 binds the folded state as the next exact current value. M8 repeats the same local mechanism on that successor. If the selected variable is genuinely present, one coordinate disappears semantically at each fold, so there are at most \(n\) elimination levels.

That sounds pleasantly cheap. It is not yet a receipt.

The total cost depends on how the successor is represented and manipulated. Representation size is a real computational resource [5,8]. Hence

```text
NUMBER_OF_ELIMINATION_LEVELS <= n
```

must remain paired with

```text
LEVEL_COUNT_ALONE_IMPLIES_POLYNOMIAL_RUNTIME = NO
```

Counting doors is not the same as weighing the furniture carried through them.

## 5.7 M9: local closure

After all finite Boolean coordinates have been existentially eliminated, the result is a scalar Boolean

\[
f_n\in\{0,1\}.
\]

The scalar is true exactly when the original finite state admitted at least one satisfying assignment, and false otherwise. This is the Local Closure result checked by `resolve_correct` and by `localClosureMathicPass`.

M9 closes the semantic account. It does not forge the signature on the complexity account.

**Figure 2 placeholder — Native M0–M9 Local Closure mechanism**  
**Location:** after §5.7.  
**Footprint:** approximately two-thirds page to full page.  
**Purpose:** make the complete score visible while magnifying M4→M5→M6→M7→M8.  
**Working caption:** **Figure 2. Native Problem No Problem Local Closure score.** The hinge presents, the mirror keeps the receipt, the fold acts, the successor advances, and the score turns again. M9 closes the finite semantic account, not the conventional complexity tab.

---

# 6. Current-state existential folding

Let

\[
f:\{0,1\}\times A_n\to\{0,1\}.
\]

Define

\[
H_f(a)=f(0,a)\lor f(1,a).
\]

Then

\[
H_f(a)=1
\iff
f(0,a)=1\lor f(1,a)=1
\iff
\exists b\in\{0,1\}\;f(b,a)=1.
\]

Recursive resolution is

\[
R_0(f)=f(()),
\]

\[
R_{n+1}(f)=R_n(H_f).
\]

Induction on \(n\) gives

\[
R_n(f)=1
\iff
\exists a\in A_n\;f(a)=1.
\]

The construction therefore gives an exact semantic elimination algorithm over an already represented finite Boolean function.

The phrase **already represented** earns its keep. If \(f\) is stored as its complete truth table, the initial state has \(2^n\) entries. If \(f\) is stored symbolically, the cost of producing and normalizing \(H_f\) depends on the representation. Reduced ordered binary decision diagrams, for example, can be compact for some Boolean functions and exponential for others [8]. The truth may be one bit. The road to that bit may need a moving truck.

## 6.1 Optional algebraic representation bridge

For Boolean variables one may work in

\[
\mathcal B_n=
\mathbb Z[x_1,\ldots,x_n]/\langle x_i^2-x_i\rangle.
\]

Positive and negative literals may be written

\[
L(x_i)=x_i,
\qquad
L(\neg x_i)=1-x_i.
\]

A clause \(C\) may be represented on Boolean inputs by

\[
C=1-\prod_{\ell\in C}(1-L(\ell)),
\]

and a conjunction by the product of clause values. This bridge is useful for symbolic interpretation of the Boolean fold, but no claim is made here that quotient-polynomial substitution, multiplication, canonicalization, or storage remains polynomial in the original CNF length. Algebra is allowed to be elegant. Complexity analysis is allowed to ask for the invoice.

---

# 7. Lean formalization and MATHIC correspondence

## 7.1 Formal semantic core

The formal source `TryxProof.lean` defines the assignment carrier recursively, the exact current-state hinge, and repeated finite elimination:

```lean
Assignment 0       = Unit
Assignment (n + 1) = Bool × Assignment n

hinge f a = f (false, a) || f (true, a)

resolve 0 f       = f ()
resolve (n + 1) f = resolve n (hinge f)
```

Three central theorems are checked.

### Theorem 1 — Boolean fold algebra

`TRYX.PNP.boolean_fold_algebra` proves the Boolean OR encoding

\[
a+b-ab.
\]

### Theorem 2 — One-step existential semantics

`TRYX.PNP.hinge_exact` proves

\[
\operatorname{hinge}(f,a)=\mathrm{true}
\iff
\exists b:\mathrm{Bool},\;f(b,a)=\mathrm{true}.
\]

### Theorem 3 — Repeated finite existential semantics

`TRYX.PNP.resolve_correct` proves

\[
\operatorname{resolve}(n,f)=\mathrm{true}
\iff
\exists a:\operatorname{Assignment}(n),\;f(a)=\mathrm{true}.
\]

The source audit rejects `sorry`, `admit`, and project `axiom` declarations in the checked PNP source. Lean is not impressed by confidence. This is one of its better qualities.

## 7.2 Explicit M0–M9 Lean bridge

`TryxMathic.lean` names the ten native measures explicitly and defines their order. It checks that the list has length ten and no duplicates and formalizes synchronization facts including

```text
m0_type_set_zero
m1_distinction
m2_current_exact
m3_rotate_three
m5_mirror_preserves_truth
m6_matches_hinge
m6_existential_exact
m7_successor_exact
m9_local_closure_correct
localClosureMathicPass
```

Its job is not to make the MATHIC sound formal. Its job is to make drift expensive.

## 7.3 Lean-pass build gate

The verification workflow installs the pinned Lean toolchain, verifies pinned dependencies, audits both Lean sources for placeholders and project axioms, builds both libraries, compiles the MATHIC bridge directly, prints theorem axioms, and preserves verification logs.

For the paper-build gate, workflow run `34795750810` on commit `6c34c44d49cfa8a86c077d7174b0ab94bf92dd8d` completed the build job successfully, including the explicit `TryxMathic.lean` compile step.

The project rule is therefore

```text
NO GREEN TryxMathic.lean
        =
NO PAPER BUILD
```

Nothing ruins a beautiful paper faster than discovering the mathematics only worked in italics.

---

# 8. Finite benchmark and independent oracle

Formal proof and executable evidence answer different questions. Lean establishes the quantified semantic statement. The benchmark exercises a concrete CNF universe and checks the implementation state by state.

## 8.1 Exact benchmark universe

The benchmark uses three Boolean variables

\[
\{x_1,x_2,x_3\}.
\]

For each variable a clause may contain the positive literal, the negative literal, or no literal. Excluding the all-absent choice gives

\[
3^3-1=26
\]

distinct nonempty non-tautological clauses.

Every set of zero through four distinct clauses is enumerated:

\[
\sum_{k=0}^{4}\binom{26}{k}=17,902.
\]

Every formula has three Boolean coordinates, so the replay performs

\[
17,902\times3=53,706
\]

folds.

## 8.2 Primary replay and independent oracle

The replay lane evaluates the complete eight-entry truth table and folds

\[
8\to4\to2\to1.
\]

The independent lane separately regenerates clauses, evaluates literals, constructs assignment masks, and derives expected states by direct quantification.

```text
LANE A
CNF -> truth table -> current-state fold

LANE B
CNF -> independent evaluator -> assignment mask -> direct quantified state
```

Two roads are more interesting when they did not secretly share the same map.

## 8.3 Negative control

The package replaces OR by AND in a deliberate corruption test. The mutation must disagree.

```text
NEGATIVE_CONTROL = OR_TO_AND
EXPECTED = DETECTED
RECORDED = DETECTED
```

The checker flinched. Good.

## 8.4 Recorded counts

```text
FORMULAS = 17,902
FOLDS = 53,706
SAT = 16,241
UNSAT = 1,661
FAILURES = 0
INDEPENDENT_STATE_DISAGREEMENTS = 0
NEGATIVE_CONTROL = DETECTED
```

**Figure 3 placeholder — The 17,902 field**  
**Location:** after §8.4.  
**Footprint:** full width, approximately one-half to two-thirds page.  
**Working caption:** **Figure 3. Exhaustive finite replay and independent oracle.** The two verification lanes meet at zero disagreements. The corrupted operator takes the scenic route to DETECTED.

---

# 9. Results

The present package supports six results.

1. **Exact Boolean fold identity.** `boolean_fold_algebra`. **Lean verified.**
2. **Exact one-step existential meaning.** `hinge_exact`. **Lean verified.**
3. **Exact repeated finite existential meaning.** `resolve_correct`. **Lean verified.**
4. **Native M0–M9 synchronization.** `TryxMathic.lean`. **Lean MATHIC build pass.**
5. **Declared finite replay.** 17,902 formulas, 53,706 folds, zero recorded state disagreements. **Verified for the declared benchmark.**
6. **Negative-control sensitivity.** OR→AND corruption. **Detected.**

None of these results contains a polynomial bound on the size or manipulation cost of a general compact successor representation. Six receipts are still six receipts, not a seventh theorem hiding in the envelope.

---

# 10. Standard-machine complexity gate

This is the deliberately open gate.

For an explicitly stored truth table on \(n\) variables, the initial Boolean state has

\[
2^n
\]

entries, and the successive tables have sizes

\[
2^{n-1},2^{n-2},\ldots,1.
\]

Thus the total number of sibling combinations after the full table has been materialized is

\[
2^{n-1}+2^{n-2}+\cdots+1=2^n-1.
\]

The explicit truth-table realization is therefore exponential in \(n\) and does not establish a polynomial-time SAT algorithm in ordinary CNF input length.

The fact that there are at most \(n\) elimination levels does not alter that conclusion. A short staircase can still lead through a very large building.

To promote the semantic mechanism to a conventional deterministic polynomial-time SAT algorithm, one would need polynomial bounds in original input length for at least:

1. input encoding;
2. every current-state representation size;
3. restriction or substitution;
4. multiplication or equivalent symbolic composition;
5. normalization or canonicalization;
6. equality or compatibility tests;
7. relevant storage and traversal costs;
8. terminal decision;
9. witness reconstruction, if claimed.

Current ledger:

```text
REPRESENTATION_SIZE_BOUND = OPEN
SUBSTITUTION_COST_BOUND = OPEN
MULTIPLICATION_OR_EQUIVALENT_COMPOSITION_COST_BOUND = OPEN
NORMALIZATION_COST_BOUND = OPEN
EQUALITY_OR_COMPATIBILITY_COST_BOUND = OPEN
WITNESS_RECONSTRUCTION_COMPLEXITY = OPEN
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

The machine is invited to the party. It is also expected to pay for what it orders.

---

# 11. Dedicated formula progression

### Current state

\[
f_i:A_{n-i}\to\{0,1\}.
\]

### Current siblings

\[
f_i^0=f_i\vert_{x_i=0},
\qquad
f_i^1=f_i\vert_{x_i=1}.
\]

### M5 provenance receipt

\[
\operatorname{shared}=f_i^0\land f_i^1,
\]

\[
\Delta_L=f_i^0\land\neg f_i^1,
\qquad
\Delta_R=\neg f_i^0\land f_i^1,
\]

with

\[
\operatorname{shared}\lor\Delta_L\lor\Delta_R
=f_i^0\lor f_i^1.
\]

### M6 existential fold

\[
\boxed{
\mathcal E_{x_i}(f_i)
=f_i^0\lor f_i^1
=f_i^0+f_i^1-f_i^0f_i^1.
}
\]

### One-step meaning

\[
\boxed{
\mathcal E_{x_i}(f_i)(r)=1
\iff
\exists b\in\{0,1\}\;f_i(b,r)=1.
}
\]

### M7 successor

\[
f_{i+1}=\mathcal E_{x_i}(f_i).
\]

### M8 succession

\[
f_0\to f_1\to\cdots\to f_n.
\]

### M9 terminal

\[
\boxed{
f_n=1
\iff
\exists a\in\{0,1\}^n\;f_0(a)=1.}
\]

### Open gate

\[
\boxed{
\text{semantic correctness}
\not\Rightarrow
\text{polynomial standard-machine cost}
}
\]

The formula page is where the paper shows all its cards and keeps the joker out of the deck.

---

# 12. Claim-to-source map

| Claim | Primary authority | Formal status | Executable status | External role | Current status |
|---|---|---|---|---|---|
| Boolean \(a+b-ab\) identity | locked MATHIC / governing source | `boolean_fold_algebra` | exercised | Shannon historical only | **VERIFIED** |
| One-step existential hinge | governing source | `hinge_exact` | intermediate checks | none required | **LEAN VERIFIED** |
| Repeated finite elimination | governing source | `resolve_correct` | terminal checks | none required | **LEAN VERIFIED** |
| Native M0–M9 order | locked Local Closure MATHIC | `nativeOrder` | inspection mapping | none | **SYNCED / BUILD PASS** |
| M5 retained-truth receipt | Local Closure MATHIC | `m5_mirror_preserves_truth` | represented by fold state | Bryant analogy only | **LEAN BRIDGE VERIFIED** |
| M6 agrees with formal hinge | Local Closure MATHIC | `m6_matches_hinge` | replay fold | Shannon/Bryant context | **LEAN BRIDGE VERIFIED** |
| M9 local semantic closure | Local Closure MATHIC | `localClosureMathicPass` | terminal checks | Cook/Clay defines larger boundary | **LEAN BRIDGE VERIFIED** |
| 17,902 formulas | replay package | n/a | primary evidence | none | **VERIFIED PACKAGE COUNT** |
| 53,706 folds | replay package | n/a | primary evidence | none | **VERIFIED PACKAGE COUNT** |
| zero state disagreements | independent checker | n/a | primary evidence | none | **VERIFIED DECLARED BENCHMARK** |
| OR→AND detected | independent checker | n/a | primary evidence | none | **VERIFIED** |
| polynomial representation bound | none proved | not formalized | not established | Bryant caution | **OPEN** |
| polynomial normalization cost | none proved | not formalized | not established | Arora-Barak boundary | **OPEN** |
| conventional \(P=NP\) | not asserted | not proved | not established | Cook/Clay, Arora-Barak | **NOT ESTABLISHED** |

---

# 13. Reviewer’s Bench and reproducibility path

The planned **Reviewer’s Bench** is a browser-openable companion instrument synchronized to the M0–M9 score. It is not a proof layer. It is where the reviewer gets to put fingerprints on the glass.

Required views:

```text
INPUT / PRESET
CURRENT STATE
ACTIVE M0-M9 MEASURE
M4 SIBLING 0
M4 SIBLING 1
M5 MIRROR / RESIDUE RECEIPT
M6 FOLD RESULT
M7 SUCCESSOR
M8 HISTORY
M9 SAT / UNSAT TERMINAL
INDEPENDENT ORACLE
NEGATIVE CONTROL
OPEN COMPLEXITY GATE
```

Required actions:

```text
STEP ONE NATIVE MEASURE
STEP ONE FOLD
RUN TO TERMINAL
RESET
ACTIVATE OR->AND NEGATIVE CONTROL
```

The independent oracle lane must not simply call the primary fold reducer. Two mirrors facing each other can produce a lot of images without producing another witness.

**Figure 4 placeholder — Reviewer’s Bench hero**  
**Location:** late in §13.  
**Footprint:** full width or hero-size.  
**Working caption:** **Figure 4. Reviewer’s Bench.** Step the measure, inspect the hinge, check the mirror, fold the siblings, advance the successor, compare the oracle, then break the operator on purpose. The gadget is allowed to be fun. It is not allowed to become evidence by charm.

Visual lineage:

```text
FIGURE 4 MASTER
      ↓
P=NP HERO POSTER
      ↓
PUBLICATION SPLASH PAGE
```

## 13.1 Reviewer path

1. read the conventional scope and claim boundary;
2. inspect the governing fold formula;
3. read the native M0–M9 score;
4. inspect `TryxProof.lean`;
5. inspect `TryxMathic.lean` and its build receipt;
6. run the finite replay;
7. run the independent checker;
8. activate the negative control;
9. use the Reviewer’s Bench;
10. return to §10 and make sure no open complexity obligation escaped while everyone was looking at the gadget.

---

# 14. Limitations and interpretation

## 14.1 The strongest established statement is semantic

\[
R_n(f)=1
\iff
\exists a\in A_n\;f(a)=1.
\]

Exact, useful, and narrower than conventional \(P=NP\). Precision is not a demotion.

## 14.2 Explicit truth tables are exponential

The replay materializes all \(2^n\) Boolean assignments. It is a verification realization, not a polynomial-time candidate.

## 14.3 Symbolic representation is the central technical question

A compact successor representation could change the cost picture, but only an explicit size-and-operation theorem can do that. Hope is not a compression algorithm.

## 14.4 M5 is provenance, not a secret tunnel

The M5 mirror receipt is formally synchronized and its retained truth is proved equal to sibling OR. It should not be interpreted as a complexity shortcut independent of M6. If there is a tunnel through the mountain, it still needs coordinates.

## 14.5 No claim of overcoming known proof barriers

This draft does not claim to overcome relativization, natural-proofs barriers, or other broad proof-method limitations. If those topics enter a future version, Baker–Gill–Solovay and Razborov–Rudich should be activated explicitly [11,12]. Barriers are weather reports, not trophies.

## 14.6 Novelty and priority are separate questions

External literature is used for foundation, analogy, and boundary. Similarity does not prove derivation; different terminology does not prove novelty. That particular mirror cuts both ways.

---

# 15. Development and provenance note

The current succession is

```text
LOCKED LOCAL-CLOSURE MATHIC
        ↓
PAPER-SYNC MATHIC BETA 1–4
        ↓
NATIVE M0-M9 FIDELITY RESTORATION
        ↓
TryxMathic.lean SYNCHRONIZATION BRIDGE
        ↓
LEAN MATHIC BUILD PASS
        ↓
SCIENTIFIC PAPER BETA 2
        ↓
SCIENTIFIC PAPER BETA 3 PERSONALITY PASS
```

The methodological choice is deliberate: **build from a formal pass rather than formalize after the prose has hardened**. A paper can survive a bad metaphor. It should not have to survive a theorem that never compiled.

---

# 16. Conclusion

Problem No Problem presents a finite current-state existential elimination mechanism for Boolean satisfiability. At each selected coordinate, the two sibling restrictions of the current state are exposed, the MATHIC records their provenance, and existential OR produces the next exact current state. Repetition terminates at a scalar Boolean.

The semantic statement is

\[
\boxed{
R_n(f)=1
\iff
\exists a\in\{0,1\}^n\;f(a)=1.
}
\]

The package supports this statement through the locked Local Closure MATHIC, the Lean semantic proof, the explicit M0–M9 Lean bridge, and the finite replay/oracle package. The paper’s job is to make those surfaces agree, not to let typography outrun topology.

The unresolved question is equally clear. A conventional proof that \(P=NP\) requires a deterministic standard-machine implementation with polynomial total cost in original input length. The present package does not supply the required general representation-size and operation-cost bounds. Its explicit truth-table realization is exponential.

So the present status has a clean double edge: **the semantic account closes; the complexity account remains open**. One receipt says “paid.” The other is still on the table.

---

# 17. References

[1] S. A. Cook, “The Complexity of Theorem-Proving Procedures,” *Proceedings of STOC ’71*, pp. 151–158, 1971. DOI: `10.1145/800157.805047`.

[2] L. A. Levin, “Universal Sequential Search Problems,” *Problems of Information Transmission*, 9(3), pp. 265–266, 1973.

[3] R. M. Karp, “Reducibility Among Combinatorial Problems,” in *Complexity of Computer Computations*, pp. 85–103, 1972. DOI: `10.1007/978-1-4684-2001-2_9`.

[4] S. Cook, “The P versus NP Problem,” Clay Mathematics Institute.

[5] S. Arora and B. Barak, *Computational Complexity: A Modern Approach*. Cambridge University Press, 2009.

[6] M. R. Garey and D. S. Johnson, *Computers and Intractability*. W. H. Freeman, 1979.

[7] C. E. Shannon, “A Symbolic Analysis of Relay and Switching Circuits,” *Transactions of the AIEE*, 57(12), pp. 713–723, 1938. DOI: `10.1109/T-AIEE.1938.5057767`.

[8] R. E. Bryant, “Graph-Based Algorithms for Boolean Function Manipulation,” *IEEE Transactions on Computers*, C-35(8), pp. 677–691, 1986. DOI: `10.1109/TC.1986.1676819`.

[9] L. Fortnow, “The Status of the P versus NP Problem,” *Communications of the ACM*, 52(9), pp. 78–86, 2009. DOI: `10.1145/1562164.1562186`.

[10] L. Fortnow, “Fifty Years of P vs. NP and the Possibility of the Impossible,” *Communications of the ACM*, 65(1), pp. 76–85. DOI: `10.1145/3460351`.

[11] T. Baker, J. Gill, and R. Solovay, “Relativizations of the P =? NP Question,” *SIAM Journal on Computing*, 4(4), pp. 431–442, 1975. DOI: `10.1137/0204037`.

[12] A. A. Razborov and S. Rudich, “Natural Proofs,” *Journal of Computer and System Sciences*, 55(1), pp. 24–35, 1997. DOI: `10.1006/jcss.1997.1494`.

---

# 18. Reference-activation index

| First activation | Reference(s) | Relationship |
|---|---|---|
| Abstract / SAT scope | [1]–[5] | foundation / boundary |
| §2 SAT and P vs NP | [1]–[6] | foundation |
| §2 current Boolean state | [7], [8] | historical antecedent / analogy / representation caution |
| §3 terminology | [4]–[6] | boundary / foundation |
| §4 Boolean algebra | [7] | historical antecedent only |
| §5 M2/M4 | [7], [8] | analogy only |
| §5 M5/M7/M8 | [8], then [4],[5] | representation caution / boundary |
| §5 M9 | [4],[5],[9] | conventional theorem boundary |
| §7 Lean | internal source primary | no outside theorem authority needed |
| §8 benchmark | executable package primary | no outside source needed for counts |
| §10 complexity gate | [4],[5],[8],[9],[10] | boundary / representation caution |
| §14 proof barriers | [11],[12] | contextual only |

---

# 19. Final closed/open status

```text
NATIVE_M0_M9_SCORE = RETAINED
M5_MIRROR_CLOSURE = DISTINCT
BOOLEAN_FOLD_IDENTITY = VERIFIED
ONE_STEP_EXISTENTIAL_SEMANTICS = LEAN_VERIFIED
FINITE_CARRIER_EXISTENTIAL_SEMANTICS = LEAN_VERIFIED
SAT_UNSAT_TERMINAL_SEMANTICS = LEAN_VERIFIED
LEAN_MATHIC_SYNCHRONIZATION = BUILD_PASS
FINITE_PACKAGE_REPLAY = VERIFIED
INDEPENDENT_INTERMEDIATE_STATE_CHECK = VERIFIED
NEGATIVE_CONTROL_DETECTION = VERIFIED

REPRESENTATION_SIZE_BOUND = OPEN
SUBSTITUTION_COST_BOUND = OPEN
MULTIPLICATION_OR_EQUIVALENT_COMPOSITION_COST_BOUND = OPEN
NORMALIZATION_COST_BOUND = OPEN
EQUALITY_OR_COMPATIBILITY_COST_BOUND = OPEN
WITNESS_RECONSTRUCTION_COMPLEXITY = OPEN
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE

PAPER_STATUS = BETA_3_PERSONALITY_PASS
PAPER_LOCK = NO
HERO_POSTER_BUILD = HOLD
SPLASH_PAGE_BUILD = HOLD
```

End: `PNP_PAPER_BETA_3_PERSONALITY_PASS`
