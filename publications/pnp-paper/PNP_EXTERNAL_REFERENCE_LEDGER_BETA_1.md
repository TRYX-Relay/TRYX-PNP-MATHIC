# Problem No Problem External Reference Ledger — Beta 1

Date: `2026-09-13`

Status: `ACTIVE_EXTERNAL_REFERENCE_LAYER / BETA`

Purpose: provide an outsourced scholarly reference layer for the Problem No Problem scientific paper, modeled on the Navier-Stokes ANEA reference-at-activation practice.

## Reference policy

External references support conventional foundations, historical antecedents, standard complexity definitions, related Boolean-function machinery, representation-size cautions, and known theorem boundaries.

They do **not** independently verify TRYX, ENIAD, MATHIC, the internal PNP naming system, the M0-M9 score, or the local-closure provenance unless an external source proves the same mathematical statement under equivalent hypotheses.

```text
REFERENCE_AT_ACTIVATION = REQUIRED
EXTERNAL_REFERENCE_IS_NOT_INTERNAL_AUTHORITY = YES
CITATION_DOES_NOT_PROMOTE_CLAIM = YES
TRYX_VALIDATED_BY_CITATION = NO
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

## Relationship classes

```text
FOUNDATION               = standard definition / classical theorem used directly
HISTORICAL_ANTECEDENT    = earlier Boolean or complexity framework related to the construction
INDEPENDENT_SUPPORT      = external literature supporting a conventional statement also used here
ANALOGOUS_METHOD         = mathematically related mechanism without identity claim
BOUNDARY_REFERENCE       = source clarifying what must be proved for conventional P vs NP
REPRESENTATION_CAUTION   = source showing that symbolic representation size/cost can dominate semantics
PROOF_BARRIER_CONTEXT    = broader P vs NP proof-method limitation; contextual, not a premise
```

---

# Core reference set

## R1 — Stephen A. Cook, 1971

**Stephen A. Cook.** “The Complexity of Theorem-Proving Procedures.” *Proceedings of the Third Annual ACM Symposium on Theory of Computing (STOC ’71)*, pp. 151–158, 1971. DOI: `10.1145/800157.805047`.

Relationship:

```text
FOUNDATION
NP_COMPLETENESS_ORIGIN
SAT_TAUTOLOGY_REDUCTION_CONTEXT
```

Activation points:
- conventional P/NP and polynomial-time reduction discussion;
- historical origin of NP-completeness;
- explanation of why SAT-family decision problems are central to P vs NP.

Do not use this reference to claim the PNP fold itself is new or externally verified.

## R2 — Leonid A. Levin, 1973

**L. A. Levin.** “Universal Sequential Search Problems.” *Problems of Information Transmission*, 9(3), pp. 265–266, 1973; Russian original in *Problemy Peredachi Informatsii* 9(3), pp. 115–116.

Relationship:

```text
FOUNDATION
HISTORICAL_ANTECEDENT
UNIVERSAL_SEARCH / NP_COMPLETENESS_HISTORY
```

Activation points:
- Cook-Levin historical framing;
- search/decision history where relevant.

## R3 — Richard M. Karp, 1972

**Richard M. Karp.** “Reducibility Among Combinatorial Problems.” In *Complexity of Computer Computations*, pp. 85–103, 1972. DOI: `10.1007/978-1-4684-2001-2_9`.

Relationship:

```text
FOUNDATION
POLYNOMIAL_REDUCTION_FRAMEWORK
NP_COMPLETE_PROBLEM_FAMILY
```

Activation points:
- polynomial reducibility;
- role of NP-complete problems beyond SAT;
- statement that an efficient solution to an NP-complete problem propagates through standard reductions.

## R4 — Stephen Cook / Clay Mathematics Institute P vs NP problem statement

**Stephen Cook.** “The P versus NP Problem.” Official Millennium Prize problem description, Clay Mathematics Institute.

Relationship:

```text
BOUNDARY_REFERENCE
OFFICIAL_PROBLEM_STATEMENT
STANDARD_MACHINE_COST_REFERENCE
```

Activation points:
- precise distinction between nondeterministic polynomial acceptance and deterministic polynomial-time decision;
- original-input-length polynomial-time requirement;
- public statement of the conventional Millennium problem.

This is the preferred external citation when the paper states what would actually be required to establish conventional `P = NP`.

## R5 — Sanjeev Arora and Boaz Barak, 2009

**Sanjeev Arora and Boaz Barak.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. ISBN `978-0-521-42426-4`.

Relationship:

```text
FOUNDATION
MODERN_COMPLEXITY_REFERENCE
BOUNDARY_REFERENCE
```

Activation points:
- definitions of P, NP, NP-completeness, reductions, Boolean circuits, and polynomial-time complexity;
- conventional modern notation and terminology;
- complexity-cost interpretation of representation and algorithmic execution.

## R6 — Michael R. Garey and David S. Johnson, 1979

**Michael R. Garey and David S. Johnson.** *Computers and Intractability: A Guide to the Theory of NP-Completeness.* W. H. Freeman, 1979.

Relationship:

```text
FOUNDATION
CLASSICAL_NP_COMPLETENESS_REFERENCE
```

Activation points:
- standard NP-completeness terminology;
- classical problem-reduction context;
- background reference for reviewer familiarity.

## R7 — Claude E. Shannon, 1938

**Claude E. Shannon.** “A Symbolic Analysis of Relay and Switching Circuits.” *Transactions of the American Institute of Electrical Engineers*, 57(12), pp. 713–723, 1938. DOI: `10.1109/T-AIEE.1938.5057767` (also indexed as `10.1109/EE.1938.6431064`).

Relationship:

```text
HISTORICAL_ANTECEDENT
BOOLEAN_SWITCHING_ALGEBRA
ANALOGOUS_METHOD
```

Activation points:
- Boolean algebra as a representation of switching/logical systems;
- historical context for restriction/cofactor-style reasoning.

Boundary:
- Shannon is not cited as the source of the PNP local-closure theorem;
- the exact current-state existential fold and its TRYX/ENIAD organization remain traced to the internal source and Lean formalization.

## R8 — Randal E. Bryant, 1986

**Randal E. Bryant.** “Graph-Based Algorithms for Boolean Function Manipulation.” *IEEE Transactions on Computers*, C-35(8), pp. 677–691, 1986. DOI: `10.1109/TC.1986.1676819`.

Relationship:

```text
INDEPENDENT_SUPPORT
ANALOGOUS_METHOD
REPRESENTATION_CAUTION
```

Activation points:
- symbolic manipulation of Boolean functions;
- variable-ordered Boolean-function representations;
- representation size as a genuine computational resource;
- caution that Boolean function representations may be exponential in the number of variables in the worst case.

This is especially important for the PNP paper because it independently supports the distinction between a semantically correct Boolean reduction rule and the unresolved cost of representing/manipulating the state carrying that rule.

## R9 — Lance Fortnow, 2009

**Lance Fortnow.** “The Status of the P versus NP Problem.” *Communications of the ACM*, 52(9), pp. 78–86, 2009. DOI: `10.1145/1562164.1562186`.

Relationship:

```text
BOUNDARY_REFERENCE
SURVEY / CONTEXT
```

Activation points:
- broad modern significance of P vs NP;
- historical and methodological context;
- reviewer-facing statement that semantic tractability and computational tractability are distinct questions.

## R10 — Lance Fortnow, 2021/2022 issue

**Lance Fortnow.** “Fifty Years of P vs. NP and the Possibility of the Impossible.” *Communications of the ACM*, 65(1), pp. 76–85. DOI: `10.1145/3460351`.

Relationship:

```text
BOUNDARY_REFERENCE
MODERN_STATUS_CONTEXT
```

Activation points:
- contemporary perspective on the continuing importance of NP-hardness and P vs NP;
- optional discussion section or introduction context.

---

# Optional proof-barrier context

These sources should be activated only if Beta 2 or later contains an explicit section discussing known barriers to P-vs-NP proof techniques. They are not needed to establish the current finite semantic result.

## R11 — Baker, Gill, and Solovay, 1975

**Theodore Baker, John Gill, and Robert Solovay.** “Relativizations of the P =? NP Question.” *SIAM Journal on Computing*, 4(4), pp. 431–442, 1975. DOI: `10.1137/0204037`.

Relationship:

```text
PROOF_BARRIER_CONTEXT
RELATIVIZATION
```

Use only to explain that broad classes of proof techniques can fail to resolve P vs NP; do not suggest that PNP has automatically overcome relativization.

## R12 — Razborov and Rudich, 1997

**Alexander A. Razborov and Steven Rudich.** “Natural Proofs.” *Journal of Computer and System Sciences*, 55(1), pp. 24–35, 1997. DOI: `10.1006/jcss.1997.1494`.

Relationship:

```text
PROOF_BARRIER_CONTEXT
CIRCUIT_LOWER_BOUND_CONTEXT
```

Use only if the manuscript explicitly discusses proof barriers or lower-bound methodologies. It is not presently a premise of the PNP construction.

---

# Reference-at-activation map for PNP Paper Beta 2

| Paper location | External source(s) to activate | Why |
|---|---|---|
| Abstract / opening scope | Cook/Clay; Fortnow | identify the conventional problem and publication boundary |
| §2 Problem statement | Cook 1971; Levin 1973; Karp 1972; Arora-Barak | P, NP, NP-completeness, reductions, SAT centrality |
| §3 Terminology | Arora-Barak; Cook/Clay | standard meaning of deterministic polynomial time and original-input complexity |
| §4 Formula page | Shannon only as historical Boolean antecedent, if used | Boolean switching algebra background, not PNP authority |
| §6 Current-state folding | Shannon; Bryant | Boolean cofactors/symbolic manipulation as analogous external context |
| §7 Lean formalization | no external citation needed for Lean theorem correctness | theorem authority is the checked source itself |
| §8 Benchmark | no outside source needed for the recorded counts | executable package is primary evidence |
| §10 Claim-to-source map | Cook/Clay; Arora-Barak | conventional complexity boundary |
| §11 Closed vs open | Bryant; Cook/Clay; Arora-Barak; Fortnow | representation-size and standard-machine cost distinction |
| §14 Limitations | Bryant; optional Baker-Gill-Solovay / Razborov-Rudich if barriers discussed | explicit limits of semantic closure and representation claims |
| §16 References | all activated references | normalized bibliography |

---

# Citation discipline

1. Cite an external reference when the corresponding conventional concept first activates.
2. Do not cite the same background reference in every paragraph merely because it is relevant.
3. Keep internal theorem authority separate from external scholarly context.
4. If an external source supports only an analogy, label it as analogy rather than equivalence.
5. Do not use historical similarity to claim priority, novelty, or derivation without evidence.
6. Every statement about the current PNP package should trace primarily to repository evidence, not to an outside citation.
7. Every statement about the conventional P-vs-NP standard should trace to established external literature.

```text
INTERNAL_RESULT -> INTERNAL_SOURCE / LEAN / REPLAY
CONVENTIONAL_STANDARD -> EXTERNAL_SCHOLARLY_REFERENCE
ANALOGY -> EXPLICITLY_LABEL_AS_ANALOGY
CLAIM_PROMOTION_BY_CITATION -> FORBIDDEN
```

---

# Beta 2 integration target

The next paper beta should:

```text
ADD_IN_TEXT_CITATIONS = YES
NORMALIZE_REFERENCE_STYLE = YES
REFERENCE_AT_FIRST_ACTIVATION = YES
ADD_EXTERNAL_REFERENCE_RELATION_LABELS_TO_CLAIM_MAP = YES
PRESERVE_INTERNAL_AUTHORITY_PRECEDENCE = YES
```

The bibliography should use one consistent journal style before the paper is locked. DOI identifiers should be retained wherever available.

End: `PNP_EXTERNAL_REFERENCE_LEDGER_BETA_1`
