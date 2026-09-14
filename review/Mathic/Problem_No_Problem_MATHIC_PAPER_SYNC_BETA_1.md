# Problem No Problem MATHIC — Paper-Sync Beta 1

**Status:** `BETA / NOT LOCKED / PAPER-TEMPLATE CANDIDATE`  
**Date:** `2026-09-13`  
**Author:** Virgil Lee Gattenby  
**Project:** TRYX / ENIAD / MATHIC

## 0. Authority rule

This file is a **paper-sync successor candidate**. It does not replace or mutate the currently locked local-closure score.

```text
LOCKED_PARENT_SCORE = TRYX.PNP.LOCAL.CLOSURE.MATHIC.SCORE.LYRIC.SUCCESSOR.260905.LOCKED.html
LOCKED_PARENT_SHA256 = 95b63f3ce280a494ac1be28d222bd03bc1da010e17ec6be3a1ba3438687073fb
GOVERNING_SOURCE = TRYX.PNP.CONTINUITY.CLOSURE.REINTRODUCTION.BENCHMARK.260831.235122Z.md
FORMAL_SOURCE = verification/tryx-lean/TryxProof.lean
FINITE_REPLAY = publications/pnp-mathic/replay.py
INDEPENDENT_ORACLE = publications/pnp-mathic/independent_check.py
PAPER_SYNC_BETA = THIS_FILE
LOCKED_PARENT_MUTATION = NONE
CLAIM_PROMOTION = NONE
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

The locked score remains the mathematical lineage authority. This beta reorganizes the review-facing execution into a conventional paper template while preserving the exact semantic core and the open complexity boundary.

---

# 1. Construction order

```text
TRYX
  -> ENIAD
  -> Laws
  -> MATHIC
  -> Scientific Paper
  -> Reviewer’s Bench
  -> Figure 4 Hero
  -> Hero Poster
  -> Splash Page
```

The scientific paper is downstream of the MATHIC. The paper may explain and reformat the score. It may not silently change the score’s semantic execution, theorem correspondence, benchmark population, or claim boundary.

```text
MATHIC_TEMPLATES_PAPER = YES
PAPER_TEMPLATES_MATHIC = NO
```

---

# 2. Conventional entry surface

Before internal terminology activates, the paper must establish the conventional problem.

```text
INPUT_CLASS = FINITE BOOLEAN SAT / CNF CONTEXT
CONVENTIONAL_DECISION_QUESTION = DOES_A_SATISFYING_ASSIGNMENT_EXIST
STANDARD_COMPLEXITY_GATE = DETERMINISTIC_POLYNOMIAL_TIME_IN_ORIGINAL_INPUT_LENGTH
NP_COMPLETENESS_CONTEXT = EXTERNAL_REFERENCE_AT_ACTIVATION
```

The paper must distinguish two questions immediately:

```text
Q1_SEMANTIC:
Does repeated current-state existential elimination preserve exact SAT / UNSAT meaning?

Q2_COMPLEXITY:
Can the evolving representation and every required operation be realized on a standard machine
with total cost polynomial in the original input length?
```

Current package status:

```text
Q1 = VERIFIED_WITHIN_DECLARED_SEMANTIC_SCOPE
Q2 = OPEN
```

### Lyric P01 — Two questions

> First ask whether the fold tells the truth. Then ask what it costs to carry the truth. Do not spend the same coin twice.

---

# 3. Terminology boundary

The paper inherits these meanings directly from the MATHIC execution.

```text
CURRENT_STATE = the Boolean function / table active at the present elimination level
BOOLEAN_SIBLINGS = restrictions of the current state at x=0 and x=1
HINGE = exact Boolean comparison of the two current sibling values
FOLD = existential elimination of one selected coordinate
SUCCESSOR = folded current state passed to the next level
FINITE_CARRIER_CLOSURE = terminal truth agrees with existence of a satisfying assignment
SAT_TERMINAL = scalar true terminal
UNSAT_TERMINAL = scalar false terminal
LOCAL_INTERNAL_CLOSURE = closure inside the declared PNP semantic/runtime framework
STANDARD_MACHINE_POLYNOMIAL_RUNTIME = conventional polynomial cost in original input length
CONVENTIONAL_P_EQUALS_NP = standard complexity-theoretic theorem, not established here
```

```text
AMBIGUOUS_CLOSURE_LANGUAGE = PROHIBITED
FINITE_SEMANTIC_CLOSURE_NE_CONVENTIONAL_P_EQUALS_NP = YES
```

### Lyric P02 — Name the office

> A hinge is a hinge, a fold is a fold, and a terminal is a terminal. A good name does not get promoted to a theorem by enthusiasm.

---

# 4. Canonical finite semantic formula spine

For current Boolean-valued state `f` and selected Boolean coordinate `x`, define the two current restrictions

\[
a=f\vert_{x=0},\qquad b=f\vert_{x=1}.
\]

For Boolean inputs,

\[
\boxed{a\lor b=a+b-ab}.
\]

Define the existential fold

\[
\boxed{\mathcal E_x(f)=a+b-ab=a\lor b}.
\]

Pointwise on every remaining address `r`,

\[
\boxed{
\mathcal E_x(f)(r)=1
\iff
\exists b\in\{0,1\}\;f(b,r)=1.
}
\]

Let

\[
A_0=\{()\},\qquad A_{n+1}=\{0,1\}\times A_n.
\]

Define

\[
R_0(f)=f(()),
\qquad
R_{n+1}(f)=R_n(H_f),
\]

where

\[
H_f(a)=f(0,a)\lor f(1,a).
\]

Then

\[
\boxed{
R_n(f)=1
\iff
\exists a\in A_n\;f(a)=1.
}
\]

This formula spine is the scientific-paper expression of the Lean semantic core.

```text
BOOLEAN_FOLD_IDENTITY = VERIFIED
ONE_STEP_EXISTENTIAL_MEANING = VERIFIED
REPEATED_FINITE_EXISTENTIAL_SEMANTICS = VERIFIED
```

### Lyric P03 — Current means current

> Bootstrap once. After that, fold what you actually have. The successor is not a souvenir; it is the next state.

---

# 5. Local-closure execution score — M0 through M9

The paper must preserve this order.

## M0 — Type-Set Zero

Role: admit the finite distinction-bearing carrier without importing a branch queue or hidden oracle.

```text
M0_STATUS = ADMITTED
```

## M1 — Distinction

Role: establish the Boolean distinction required for the current coordinate.

```text
DISTINCTION = {false,true}
```

## M2 — Current state / number constitution

Role: constitute the exact current state before comparison.

```text
CURRENT_STATE_REQUIRED = YES
RETURN_TO_ORIGINAL_EACH_LEVEL = NO
```

## M3 — VPA rotation / typed transition

Role: preserve the Value -> Perception -> Action -> successor discipline.

```text
VPA_TYPING = PRESERVED
```

## M4 — Current-hinge sibling reflection

Role: form the two restrictions of the **current** state at the selected coordinate.

```text
SIBLING_0 = CURRENT|x=0
SIBLING_1 = CURRENT|x=1
```

## M5 — Certified sibling comparison

Role: compare the two sibling values without erasing unmatched truth.

For existential semantics:

```text
COMPARATOR = OR
```

## M6 — Exact algebraic existential fold

Role: collapse the selected coordinate by exact Boolean OR.

\[
\boxed{a\lor b=a+b-ab}.
\]

```text
FOLD_REMOVES_ONE_COORDINATE = YES
```

## M7 — Current successor

Role: normalize the folded result only to the extent required by the declared representation, then admit it as the exact next current state.

```text
SUCCESSOR_IS_NEXT_CURRENT = YES
```

No polynomial normalization-cost claim is imported here.

## M8 — Ordinal successor repetition

Role: repeat M4-M7 on the current successor until the finite carrier is exhausted.

```text
NUMBER_OF_ELIMINATION_LEVELS = n
TOTAL_MACHINE_WORK_FROM_LEVEL_COUNT_ALONE = NOT_INFERRED
```

## M9 — Scalar terminal / typed return

Role: return the final Boolean scalar.

```text
TRUE_TERMINAL = SAT
FALSE_TERMINAL = UNSAT
LOCAL_FINITE_SEMANTIC_CLOSURE = CLOSED
```

### Lyric P04 — The return

> Remove one coordinate, keep the successor, and repeat until no coordinate remains. The final bit answers the finite semantic question and nothing larger by decree.

---

# 6. Lean execution mapping

The paper must map the MATHIC semantic spine to exactly these Lean objects.

```text
MATHIC CURRENT FINITE CARRIER -> TRYX.PNP.Assignment
M4/M5 CURRENT SIBLING HINGE -> TRYX.PNP.hinge
M6-M9 REPEATED ELIMINATION -> TRYX.PNP.resolve
BOOLEAN a+b-ab IDENTITY -> TRYX.PNP.boolean_fold_algebra
ONE-STEP EXISTENTIAL SEMANTICS -> TRYX.PNP.hinge_exact
FINITE TERMINAL CORRECTNESS -> TRYX.PNP.resolve_correct
```

Formal theorem boundary:

```text
LEAN_PROVES_BOOLEAN_FOLD_ALGEBRA = YES
LEAN_PROVES_ONE_STEP_EXISTENTIAL_SEMANTICS = YES
LEAN_PROVES_REPEATED_FINITE_EXISTENTIAL_SEMANTICS = YES
LEAN_PROVES_QUOTIENT_POLYNOMIAL_RUNTIME = NO
LEAN_PROVES_CNF_ENCODING_CORRESPONDENCE = NO
LEAN_PROVES_REPRESENTATION_SIZE_BOUND = NO
LEAN_PROVES_NORMALIZATION_COST_BOUND = NO
LEAN_PROVES_WITNESS_RECONSTRUCTION_COMPLEXITY = NO
LEAN_PROVES_STANDARD_MACHINE_POLYNOMIAL_RUNTIME = NO
LEAN_ASSERTS_THEOREM_NAMED_P_EQUALS_NP = NO
```

### Lyric P05 — Formal mirror

> Ask Lean to prove the score we actually wrote, not a more convenient song with the same chorus.

---

# 7. Finite replay / independent oracle score

The paper must state the exact benchmark universe.

```text
VARIABLES = 3
VARIABLE_SET = {x1,x2,x3}
ADMISSIBLE_NONEMPTY_CLAUSES = 26
CLAUSE_WIDTHS = 1..3
REPEATED_VARIABLE_INSIDE_CLAUSE = NO
TAUTOLOGICAL_CLAUSE = NO
FORMULA_SIZE_RANGE = 0..4 DISTINCT CLAUSES
FORMULAS = 17902
FOLDS_PER_FORMULA = 3
TOTAL_FOLDS = 53706
SAT = 16241
UNSAT = 1661
FAILURES = 0
INDEPENDENT_STATE_DISAGREEMENTS = 0
NEGATIVE_CONTROL = OR replaced with AND: DETECTED
```

Primary replay path:

```text
CNF -> explicit 8-entry truth table -> 4 -> 2 -> 1 -> terminal
```

Independent oracle path:

```text
independent clause generation
-> independent literal evaluator
-> assignment bit masks
-> direct quantified expected state at every level
-> compare with fold path
```

The two paths must remain visibly distinct in the paper and Reviewer’s Bench.

### Lyric P06 — Make the checker flinch

> A checker that agrees only when nothing is changed may be asleep. Change OR to AND and make sure it wakes up angry.

---

# 8. Open conventional complexity gate

The MATHIC paper template must put the open gate in the main spine, not in fine print.

For an explicit truth table on `n` variables,

\[
2^{n-1}+2^{n-2}+\cdots+1=2^n-1
\]

sibling combinations are required after the table has been constructed. Therefore the truth-table realization is not a polynomial-time SAT algorithm in original CNF length.

A conventional P=NP proof from a more compact realization would require a deterministic standard-machine construction and polynomial bounds, in original input length, covering at least:

```text
1. original input encoding
2. every current-state representation size
3. restriction / substitution
4. multiplication or equivalent composition
5. normalization / canonicalization
6. equality / compatibility tests required by execution
7. terminal decision
8. witness reconstruction, if claimed
```

Current status:

```text
REPRESENTATION_SIZE_BOUND = OPEN
SUBSTITUTION_COST_BOUND = OPEN
MULTIPLICATION_COST_BOUND = OPEN
NORMALIZATION_COST_BOUND = OPEN
WITNESS_RECONSTRUCTION_COMPLEXITY = OPEN
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

### Lyric P07 — Pay the machine

> The fold may be exact and the bill may still be exponential. A conventional theorem has to pay for the representation, not only count the number of doors it walks through.

---

# 9. Four-figure paper template

The updated MATHIC assigns the four principal illustration positions.

## Figure 1 — The Problem

```text
ROLE = SEMANTIC_CLOSURE_VS_COMPLEXITY_BOUNDARY
ACTIVATES_AFTER = CONVENTIONAL_PROBLEM_ENTRY
SHOW = VERIFIED_FINITE_SEMANTIC_PATH + SEPARATE_OPEN_COMPLEXITY_GATE
PROOF_WEIGHT = EXPLANATORY_ONLY
```

## Figure 2 — The Mechanism

```text
ROLE = CURRENT_STATE_HINGE_FOLD_SUCCESSOR_MECHANISM
ACTIVATES_WITH = M4-M9
SHOW = CURRENT -> SIBLINGS -> OR HINGE -> FOLD -> SUCCESSOR -> REPEAT -> TERMINAL
PROOF_WEIGHT = EXPLANATORY_ONLY
```

## Figure 3 — The Evidence

```text
ROLE = FINITE_BENCHMARK_AND_INDEPENDENT_ORACLE
ACTIVATES_WITH = FINITE_REPLAY_SECTION
SHOW = 3 VARIABLES -> 26 CLAUSES -> 17902 FORMULAS -> 53706 FOLDS -> TWO CHECKING LANES -> 0 DISAGREEMENTS
NEGATIVE_CONTROL = VISIBLE
PROOF_WEIGHT = REPRODUCIBILITY_PRESENTATION_ONLY
```

## Figure 4 — The Reward

```text
ROLE = REVIEWERS_BENCH_HERO
ACTIVATES_LATE = AFTER_FORMULA_PAGE / REVIEW_TRANSITION
SHOW = CURRENT STATE + SIBLINGS + FOLD + SUCCESSOR + ORACLE + NEGATIVE CONTROL + TERMINAL
PROOF_WEIGHT = NONE_INDEPENDENT
REUSE = HERO_POSTER + SPLASH_PAGE
```

Visual lineage:

```text
FIGURE_4 MASTER
  -> P=NP HERO POSTER
  -> PNP SPLASH PAGE / PUBLICATION COVER
```

### Lyric P08 — Earn the picture

> Use a picture where the eye can carry structure faster than prose. Do not ask a beautiful picture to pay a theorem’s debt.

---

# 10. Dedicated formula-progression page template

The paper’s standalone formula page must compress the MATHIC in this order:

```text
CONVENTIONAL SAT / BOOLEAN STATE
        ↓
CURRENT-STATE SIBLING RESTRICTIONS
        ↓
BOOLEAN HINGE / a+b-ab
        ↓
EXISTENTIAL FOLD
        ↓
CURRENT SUCCESSOR
        ↓
REPEATED FINITE ELIMINATION
        ↓
SAT / UNSAT TERMINAL SEMANTICS
        ↓
LEAN-VERIFIED CLOSURE
        ↓
FINITE REPLAY / INDEPENDENT ORACLE
        ↓
OPEN STANDARD-MACHINE POLYNOMIAL-COST GATE
```

Placement rule:

```text
FORMULA_PAGE_AFTER = MECHANISM + LEAN + FINITE_EVIDENCE + OPEN_GATE
FORMULA_PAGE_BEFORE = REVIEWERS_BENCH_HERO
```

---

# 11. External reference-at-activation template

External sources support conventional foundations, analogies, representation cautions, and theorem boundaries. They do not become internal PNP theorem authority.

Minimum activation map:

```text
COOK / LEVIN / KARP -> P, NP, SAT, NP-completeness, polynomial reductions
COOK / CLAY -> official conventional P-vs-NP problem boundary
ARORA-BARAK / GAREY-JOHNSON -> modern standard complexity terminology
SHANNON -> historical Boolean switching-algebra antecedent
BRYANT -> symbolic Boolean manipulation + representation-size caution
FORTNOW -> modern P-vs-NP context
BAKER-GILL-SOLOVAY / RAZBOROV-RUDICH -> optional proof-barrier context only
```

Reference discipline:

```text
INTERNAL_RESULT -> INTERNAL_SOURCE / LEAN / REPLAY
CONVENTIONAL_STANDARD -> EXTERNAL_REFERENCE
ANALOGY -> LABEL_AS_ANALOGY
CLAIM_PROMOTION_BY_CITATION -> FORBIDDEN
```

---

# 12. Reviewer’s Bench execution contract

The Reviewer’s Bench is the interactive manifestation of the paper-sync MATHIC.

Required two-engine architecture:

```text
ENGINE_A = CURRENT-STATE HINGE / FOLD EXECUTION
ENGINE_B = DIRECT TRUTH-TABLE / BIT-MASK ORACLE
ENGINE_B_MAY_CALL_ENGINE_A_FOLD_REDUCER = NO
```

Required controls:

```text
PRESET_INPUT
CUSTOM_SUPPORTED_FINITE_INPUT
STEP_ONE_FOLD
RUN_TO_TERMINAL
RESET
NEGATIVE_CONTROL_OR_TO_AND
```

Required readouts:

```text
CURRENT_STATE
SELECTED_COORDINATE
SIBLING_0
SIBLING_1
FOLD_RESULT
SUCCESSOR
HISTORY
PRIMARY_RESULT
ORACLE_RESULT
AGREEMENT / DISAGREEMENT
SAT / UNSAT TERMINAL
OPEN_COMPLEXITY_GATE
```

Delivery:

```text
SELF_CONTAINED_BROWSER_OPENABLE_HTML = REQUIRED
CORE_REMOTE_SERVICE_DEPENDENCY = NONE
PAPER_NOTATION_SYNC = REQUIRED
```

### Lyric P09 — Reward the reviewer

> You read the argument. Now touch the mechanism. Change the input, step the hinge, break the operator, and see whether the receipts still sing in tune.

---

# 13. Paper scaffold generated from this MATHIC

The scientific paper should inherit the following section order unless a later MATHIC successor explicitly changes it:

```text
0. Splash / poster-derived cover          [built after paper lock]
1. Title / Abstract / Claim Boundary / Contents
2. Conventional P vs NP / SAT Problem
3. Terminology and Scope Boundary
4. Figure 1 — Semantic Closure vs Complexity Boundary
5. Canonical Formula Spine
6. M0-M9 Local-Closure Mechanism
7. Figure 2 — Hinge / Fold / Successor
8. Lean Formalization and Correspondence
9. Finite Benchmark Design
10. Figure 3 — Benchmark / Independent Oracle
11. Results
12. Open Standard-Machine Complexity Gate
13. Dedicated Formula-Progression Page
14. Claim-to-Source Map
15. Figure 4 — Reviewer’s Bench Hero
16. Reproducibility / Reviewer Path
17. Development / Provenance Note
18. Limitations / Discussion / Next Program
19. References
20. Reference-Activation Index
21. Closed / Open Final Status
```

The exact page count is not fixed by this beta. The ordinal structure is.

```text
PAPER_SECTION_ORDER_TEMPLATED_BY_MATHIC = YES
PAPER_PAGE_COUNT_FIXED = NO
```

---

# 14. Claim-to-source map template

The paper must preserve at least this map:

| Statement | Internal authority | Lean | Replay/oracle | External role | Status |
|---|---|---|---|---|---|
| Boolean `a+b-ab` fold | local-closure source | `boolean_fold_algebra` | exercised | Shannon only historical/analogous | VERIFIED on Boolean inputs |
| One-step existential hinge | local-closure source | `hinge_exact` | intermediate checks | none required | VERIFIED semantic statement |
| Repeated finite elimination | local-closure source | `resolve_correct` | terminal checks | none required | VERIFIED finite semantics |
| Benchmark totals | replay package | n/a | primary evidence | none required | VERIFIED finite package |
| Independent state agreement | oracle package | n/a | primary evidence | none required | VERIFIED declared benchmark |
| Representation-size bound | none proved | OPEN | not established | Bryant / complexity texts contextual | OPEN |
| Standard-machine polynomial runtime | none proved | OPEN | not established | Cook/Clay/Arora-Barak boundary | OPEN |
| Conventional `P=NP` | not asserted by current package | NOT ESTABLISHED | not established | conventional literature defines target | NOT ESTABLISHED |

---

# 15. Beta-to-lock gate for this MATHIC

This paper-sync MATHIC may become a locked successor only after:

```text
1. locked-parent semantic correspondence audit = PASS
2. Lean correspondence audit = PASS
3. replay/oracle correspondence audit = PASS
4. external-reference activation audit = PASS
5. four-figure role audit = PASS
6. Reviewer’s Bench contract audit = PASS
7. claim-firewall exact-match audit = PASS
8. hostile overclaim audit = PASS
```

Until then:

```text
PAPER_SYNC_MATHIC_STATUS = BETA
LOCKED_PARENT_SCORE_REMAINS_ACTIVE = YES
PAPER_SHOULD_TEMPLATE_FROM_THIS_BETA = YES_FOR_DEVELOPMENT
PAPER_MAY_NOT_CITE_THIS_BETA_AS_LOCKED_AUTHORITY = YES
```

---

# 16. Claim firewall

```text
BOOLEAN_FOLD_IDENTITY = VERIFIED
FINITE_CARRIER_EXISTENTIAL_SEMANTICS = LEAN_VERIFIED
SAT_UNSAT_TERMINAL_SEMANTICS = LEAN_VERIFIED
FINITE_PACKAGE_REPLAY = VERIFIED
INDEPENDENT_INTERMEDIATE_STATE_CHECK = VERIFIED
NEGATIVE_CONTROL_DETECTION = VERIFIED
REPRESENTATION_SIZE_BOUND = OPEN
SUBSTITUTION_COST_BOUND = OPEN
MULTIPLICATION_COST_BOUND = OPEN
NORMALIZATION_COST_BOUND = OPEN
WITNESS_RECONSTRUCTION_COMPLEXITY = OPEN
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

End: `Problem_No_Problem_MATHIC_PAPER_SYNC_BETA_1`
