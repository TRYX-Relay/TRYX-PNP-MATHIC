# PNP Figure Contract v1.0

Date: `2026-09-13`

Status: `ACTIVE / BINDING FOR ALL PNP PAPER FIGURES`

Parent paper contract:

`review/PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_3.md`

This contract governs figure identity, canvas, visual grammar, reuse boundaries, and anti-duplication. It exists specifically to prevent repeated motifs, repeated explanations, visual drift, and claim drift between figures.

---

## 1. Global figure canvas

Every principal paper figure uses the same fixed artwork canvas:

```text
WIDTH = 7.0 INCHES
HEIGHT = 3.5 INCHES
ASPECT_RATIO = 2:1
ORIENTATION = HORIZONTAL
FIGURE_COUNT = 5
```

A figure that requires more than this canvas fails before generation.

All figures must remain legible at actual paper placement size.

```text
FULL_PAGE_INFOGRAPHIC = PROHIBITED
TALL_POSTER_LAYOUT = PROHIBITED
SQUARE_LAYOUT = PROHIBITED
TEXT_SHRINK_TO_FORCE_FIT = PROHIBITED
STACKED_SUPPORT_PANEL_BELOW_ART = PROHIBITED
```

Visual style:

```text
SCIENTIFIC / JOURNAL = REQUIRED
RESTRAINED COLOR = REQUIRED
SERIF TYPOGRAPHY = PREFERRED
THIN TECHNICAL RULES = PREFERRED
CORPORATE INFOGRAPHIC STYLE = PROHIBITED
DECORATIVE COLOR CODING = MINIMIZE
```

---

## 2. One figure, one job

Each principal figure has exactly one primary explanatory job.

If material belongs to another figure's job, it is not repeated.

```text
FIGURE_1 = BOUNDARY
FIGURE_2 = VPA GRAMMAR
FIGURE_3 = ENAID TOPOLOGY / LOCAL CLOSURE
FIGURE_4 = FINITE EVIDENCE
FIGURE_5 = REVIEWER INSTRUMENT
```

No figure may become a summary poster of the entire paper.

---

## 3. Figure 1 contract

Status: `LOCKED`

Canonical title / role:

`Figure 1. Semantic closure and complexity boundary`

Primary job:

Show the separation between verified finite semantic closure and the unresolved conventional complexity obligations.

Visual grammar:

```text
SPLIT DOMAIN / BOUNDARY DIAGRAM
LEFT = FINITE SEMANTIC PATH
RIGHT = COMPLEXITY BOUNDARY
```

Required conceptual boundary:

`SEMANTIC CORRECTNESS != POLYNOMIAL COST`

Permitted content:

- finite Boolean semantic path
- SAT / UNSAT terminal semantics
- separate open complexity obligations
- representation-size bound: OPEN
- normalization-cost bound: OPEN
- witness-reconstruction complexity: OPEN
- standard-machine polynomial runtime: OPEN
- conventional P = NP: NOT ESTABLISHED

Forbidden in Figure 1:

```text
VPA CYCLE GRAPHIC = FORBIDDEN
UBIQUITY MIRROR = FORBIDDEN
FINITE REPLAY COUNTS = FORBIDDEN
REVIEWER BENCH UI = FORBIDDEN
```

Lock receipt:

`review/figures/PNP_FIGURE_1_LOCK.md`

---

## 4. Figure 2 contract

Status: `LOCKED`

Canonical role:

`TRYX local VPA cycle`

Primary job:

Teach the VPA grammar once.

Visual grammar:

```text
V -> P -> A -> V'
```

Human meanings:

```text
V = current value/state
P = comparison / perception / relation
A = committed action / operation
V' = successor value/state
```

Presentation lineage:

NS ANEA VPA audit-cell visual language.

Figure 2 is the ONLY principal figure permitted to use the VPA cycle as its main graphic.

Forbidden in Figure 2:

```text
COMPLEXITY BOUNDARY AS MAIN GRAPHIC = FORBIDDEN
UBIQUITY MIRROR TOPOLOGY = FORBIDDEN
FINITE REPLAY COUNTS = FORBIDDEN
REVIEWER BENCH UI = FORBIDDEN
```

Lock receipt:

`review/figures/PNP_FIGURE_2_LOCK.md`

---

## 5. Figure 3 contract

Status: `ACTIVE DEVELOPMENT / NOT LOCKED`

Canonical role:

`ENAID local-closure topology`

Primary topology:

`587 Ubiquity Mirror`

Notation:

`M_587` / `mathfrak{M}_{587}` where typesetting supports it.

ENAID field notation:

`Pi^ENAID_(M_587)` where useful.

Primary job:

Show the ENAID topology that carries the PNP local-closure sequence.

Required local progression:

```text
m4. Hinge Siblings
  ->
m5. Mirror Closure
  ->
m6. Existential Fold
  ->
m7. Current Successor
  ->
m8. Ordinal Succession
  ->
m9. Local Closure
```

The formula/topology is ENAID.

Naming prohibition:

```text
COLLATZ = FORBIDDEN
SNOWMAN = FORBIDDEN
COLLATZ CONJECTURE = FORBIDDEN
SNOWMAN CONJECTURE = FORBIDDEN
```

Those may be applications elsewhere, but they do not own or name this topology.

Visual grammar:

```text
TOPOLOGY / MIRROR / ADDRESS FIELD
NOT VPA CIRCLES
NOT A REPLAY BAR CHART
NOT A SOFTWARE DASHBOARD
```

Figure 3 should make the Ubiquity Mirror visually unmistakable and use the m4-m9 chain as the mechanism traversing that topology.

Forbidden in Figure 3:

```text
VPA CYCLE REDRAW = FORBIDDEN
GENERIC COMPLEXITY CURVE = FORBIDDEN
17,902 / 53,706 EVIDENCE PANEL = FORBIDDEN
REVIEWER BENCH CONTROLS = FORBIDDEN
```

---

## 6. Figure 4 contract

Status: `PENDING / ALL PRIOR DRAFTS INVALID`

Canonical role:

`Finite evidence / replay / independent oracle`

Primary job:

Present the finite benchmark as a forensic evidence chain.

Required exact evidence chain:

```text
3 variables
->
26 possible 3-literal clauses
->
17,902 formulas containing 0 through 4 distinct clauses
->
53,706 coordinate folds
->
independent replay / oracle comparison
->
0 disagreements
->
negative control detected
```

Required supporting facts:

```text
SAT = 16,241
UNSAT = 1,661
FAILURES = 0
INITIAL / INTERMEDIATE STATE DISAGREEMENTS = 0
NEGATIVE CONTROL = DETECTED
```

Visual grammar:

```text
FORENSIC EVIDENCE PIPELINE / AUDIT LEDGER
COUNTS / CHECKS / RESULT
```

No theoretical architecture needs to be redrawn here. The data is the figure.

Forbidden in Figure 4:

```text
VPA CYCLE = FORBIDDEN
UBIQUITY MIRROR = FORBIDDEN
P = NP ESTABLISHED = FORBIDDEN
POLYNOMIAL RUNTIME CLAIM = FORBIDDEN
GENERIC CERTIFICATE DIAGRAM = FORBIDDEN
REVIEWER BENCH UI = FORBIDDEN
```

Figure 4 must not imply that finite replay alone establishes conventional P = NP.

---

## 7. Figure 5 contract

Status: `PENDING / NOT LOCKED`

Canonical role:

`Reviewer's Bench hero`

Primary job:

Show the functioning review instrument used to inspect and replay the MATHIC / local-closure mechanism.

Development lineage:

```text
FUNCTIONING REVIEWER'S BENCH
-> FIGURE 5 MASTER
-> PNP HERO POSTER
-> PNP SPLASH PAGE
```

The functioning instrument comes first. Figure 5 is derived from actual working software, not from decorative concept art.

Expected capabilities of the underlying bench:

- step M1-M9
- display current state
- display sibling states
- display M5 provenance
- display M6 fold
- display M7 successor
- display M8 history
- display M9 terminal state
- independent oracle comparison
- negative-control state
- open-complexity gate / claim firewall

Visual grammar:

```text
SCIENTIFIC INSTRUMENT / BENCH / READOUT
```

Forbidden in Figure 5:

```text
VPA CYCLE AS HERO = FORBIDDEN
UBIQUITY MIRROR AS FULL REPEAT = FORBIDDEN
FINITE EVIDENCE PIPELINE AS FULL REPEAT = FORBIDDEN
CLAIM PROMOTION = FORBIDDEN
```

The bench may use compact symbols learned earlier in the paper, but it must not redraw the teaching figures.

---

## 8. Anti-repetition matrix

The following primary motif ownership is exclusive:

```text
SEMANTIC / COMPLEXITY SPLIT      -> FIGURE 1 ONLY
VPA CYCLE                        -> FIGURE 2 ONLY
587 UBIQUITY MIRROR TOPOLOGY     -> FIGURE 3 ONLY
17,902 / 53,706 FINITE EVIDENCE  -> FIGURE 4 ONLY
REVIEWER BENCH UI                -> FIGURE 5 ONLY
```

Compact notation may recur in labels or captions when mathematically necessary, but the principal visual construction may not recur.

Rule:

```text
IF A NEW FIGURE'S CENTRAL VISUAL ALREADY APPEARS IN AN EARLIER FIGURE,
THE NEW FIGURE FAILS BEFORE GENERATION.
```

---

## 9. Figure-generation preflight

Before generating or drawing any principal figure, verify all of the following:

```text
[ ] correct figure number
[ ] correct figure role
[ ] 7.0 in x 3.5 in canvas
[ ] unique visual grammar
[ ] no motif owned by another figure
[ ] no VPA cycle unless Figure 2
[ ] no Ubiquity Mirror unless Figure 3
[ ] no finite replay evidence chain unless Figure 4
[ ] no Reviewer Bench UI unless Figure 5
[ ] no Collatz / Snowman naming for ENAID topology
[ ] no conventional P = NP claim promotion
[ ] readable at actual paper size
[ ] restrained scientific styling
```

Any failed item stops generation until repaired.

---

## 10. Current figure state

```text
FIGURE_1 = LOCKED
FIGURE_2 = LOCKED
FIGURE_3 = REBUILD REQUIRED USING ENAID 587 UBIQUITY MIRROR
FIGURE_4 = PRIOR DRAFTS REJECTED / REBUILD FROM FINITE EVIDENCE ONLY
FIGURE_5 = PENDING REVIEWER'S BENCH
```

---

## 11. Claim firewall

No figure may exceed the mathematical status of the manuscript.

```text
FINITE BOOLEAN SEMANTIC RESULT = VERIFIED
FINITE BENCHMARK REPLAY = VERIFIED
INDEPENDENT STATE CHECK = VERIFIED
NEGATIVE CONTROL DETECTION = VERIFIED
STANDARD-MACHINE POLYNOMIAL RUNTIME = OPEN
REPRESENTATION-SIZE BOUND = OPEN
NORMALIZATION-COST BOUND = OPEN
WITNESS-RECONSTRUCTION COMPLEXITY = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

A visually attractive figure is not permission to strengthen a claim.

---

End: `PNP_FIGURE_CONTRACT_v1_0`
