# PNP Figure Contract v1.1

Date: `2026-09-13`

Status: `ACTIVE / BINDING FOR ALL PNP PAPER FIGURES`

Supersedes:

`review/PNP_FIGURE_CONTRACT_v1_0.md`

Parent paper contract:

`review/PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_3.md`

This revision removes all ambiguity about visual reuse. A principal motif is taught once and never redrawn in another figure.

---

## 1. Global canvas

Every principal figure uses:

```text
WIDTH = 7.0 INCHES
HEIGHT = 3.5 INCHES
ASPECT_RATIO = 2:1
ORIENTATION = HORIZONTAL
FIGURE_COUNT = 5
```

A figure that cannot be read at this size fails before generation.

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
THIN TECHNICAL RULES = PREFERRED
CORPORATE INFOGRAPHIC STYLE = PROHIBITED
```

---

## 2. One figure, one visual language

Each principal figure owns one visual language exclusively.

```text
FIGURE_1 = BOUNDARY
FIGURE_2 = VPA
FIGURE_3 = ENAID UBIQUITY MIRROR TOPOLOGY
FIGURE_4 = FINITE EVIDENCE
FIGURE_5 = REVIEWER'S BENCH
```

A figure may refer in prose to concepts already taught, but it may not redraw, restage, miniaturize, iconize, summarize, or otherwise visually repeat another figure's owned motif.

---

## 3. Absolute VPA non-repetition rule

Figure 2 owns VPA completely.

```text
VPA_VISUAL_OWNER = FIGURE_2
VPA_VISUAL_OCCURRENCES_ALLOWED = 1
```

Allowed in Figure 2 only:

```text
V -> P -> A -> V'
VPA circles
VPA arrows
VPA cycle
VPA audit-cell graphic
VPA miniatures
VPA shorthand diagrams
```

Forbidden in Figures 1, 3, 4, and 5:

```text
VPA CYCLE = FORBIDDEN
V -> P -> A -> V' = FORBIDDEN
VPA CIRCLES = FORBIDDEN
VPA ICONS = FORBIDDEN
VPA MINIATURES = FORBIDDEN
VPA SHORTHAND = FORBIDDEN
VPA RUNTIME LABEL = FORBIDDEN
VPA-BASED DECORATIVE MOTIF = FORBIDDEN
```

There is no exception for a compact reminder, corner icon, caption ornament, background watermark, or software panel.

If the reader needs VPA again, the text points back to Figure 2. The graphic itself is not repeated.

---

## 4. Figure 1 contract

Status: `LOCKED`

Role:

`Semantic closure and complexity boundary`

Primary job:

Separate finite semantic closure from unresolved conventional complexity obligations.

Visual grammar:

```text
BOUNDARY / SPLIT-DOMAIN DIAGRAM
```

Permitted content:

- finite Boolean semantic path
- SAT / UNSAT terminal semantics
- representation-size bound: OPEN
- normalization-cost bound: OPEN
- witness-reconstruction complexity: OPEN
- standard-machine polynomial runtime: OPEN
- conventional P = NP: NOT ESTABLISHED

Forbidden:

```text
VPA = FORBIDDEN
UBIQUITY MIRROR = FORBIDDEN
FINITE EVIDENCE COUNTS = FORBIDDEN
REVIEWER BENCH UI = FORBIDDEN
```

Lock receipt:

`review/figures/PNP_FIGURE_1_LOCK.md`

---

## 5. Figure 2 contract

Status: `LOCKED`

Role:

`TRYX local VPA cycle`

Primary job:

Teach the VPA grammar once and only once.

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

No other principal figure may reuse any VPA visual.

Lock receipt:

`review/figures/PNP_FIGURE_2_LOCK.md`

---

## 6. Figure 3 contract

Status: `REBUILD REQUIRED / NOT LOCKED`

Role:

`ENAID local-closure topology`

Primary topology:

`587 Ubiquity Mirror`

Notation:

`mathfrak{M}_{587}`

ENAID field notation:

`Pi^ENAID_(mathfrak{M}_{587})`

Primary job:

Show the ENAID topology carrying the local-closure mechanism.

Required progression:

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

Visual grammar:

```text
MIRROR / TOPOLOGY / ADDRESS FIELD / SUCCESSION
```

The Ubiquity Mirror must be visually unmistakable. The progression traverses the topology.

Forbidden:

```text
VPA OF ANY KIND = FORBIDDEN
V -> P -> A -> V' = FORBIDDEN
VPA LABELS = FORBIDDEN
COLLATZ / SNOWMAN NAMING = FORBIDDEN
FINITE REPLAY COUNTS = FORBIDDEN
REVIEWER BENCH UI = FORBIDDEN
```

The formula/topology is ENAID. Collatz/Snowman may use it elsewhere as an application, but do not name it here.

---

## 7. Figure 4 contract

Status: `PENDING / PRIOR DRAFTS REJECTED`

Role:

`Finite evidence / replay / independent oracle`

Primary job:

Present the finite benchmark as evidence, not theory.

Required exact chain:

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
```

Forbidden:

```text
VPA OF ANY KIND = FORBIDDEN
UBIQUITY MIRROR = FORBIDDEN
THEORETICAL CYCLE GRAPHICS = FORBIDDEN
P = NP ESTABLISHED = FORBIDDEN
POLYNOMIAL-RUNTIME CLAIM = FORBIDDEN
REVIEWER BENCH UI = FORBIDDEN
```

The data itself is the figure.

---

## 8. Figure 5 contract

Status: `PENDING`

Role:

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

Expected underlying capabilities:

- step M1-M9
- current state
- sibling states
- M5 provenance
- M6 fold
- M7 successor
- M8 history
- M9 terminal state
- independent oracle comparison
- negative control
- open-complexity gate / claim firewall

Visual grammar:

```text
SCIENTIFIC INSTRUMENT / BENCH / READOUT
```

Absolute visual prohibitions:

```text
VPA OF ANY KIND = FORBIDDEN
V -> P -> A -> V' = FORBIDDEN
VPA ICONS OR CIRCLES = FORBIDDEN
UBIQUITY MIRROR REDRAW = FORBIDDEN
FINITE EVIDENCE PIPELINE REDRAW = FORBIDDEN
```

The software may execute underlying TRYX logic internally. That is not permission to redraw Figure 2.

---

## 9. Exclusive motif ownership matrix

```text
SEMANTIC / COMPLEXITY BOUNDARY     -> FIGURE 1 ONLY
VPA VISUAL LANGUAGE                -> FIGURE 2 ONLY
587 UBIQUITY MIRROR TOPOLOGY       -> FIGURE 3 ONLY
17,902 / 53,706 EVIDENCE PIPELINE  -> FIGURE 4 ONLY
REVIEWER'S BENCH UI                -> FIGURE 5 ONLY
```

No visual motif may appear twice.

Rule:

```text
IF THE CENTRAL OR SECONDARY VISUAL MOTIF ALREADY EXISTS IN ANOTHER FIGURE,
THE NEW FIGURE FAILS BEFORE GENERATION.
```

---

## 10. Mandatory preflight before any figure generation

```text
[ ] correct figure number
[ ] correct figure role
[ ] 7.0 in x 3.5 in canvas
[ ] unique visual language
[ ] no motif owned by another figure
[ ] VPA appears only if this is Figure 2
[ ] Ubiquity Mirror appears only if this is Figure 3
[ ] finite benchmark counts appear only if this is Figure 4
[ ] Reviewer Bench UI appears only if this is Figure 5
[ ] no Collatz / Snowman naming for ENAID topology
[ ] no conventional P = NP claim promotion
[ ] readable at actual paper size
[ ] restrained scientific styling
```

Any failed item stops generation.

---

## 11. Current state

```text
FIGURE_1 = LOCKED
FIGURE_2 = LOCKED
FIGURE_3 = REBUILD REQUIRED USING ENAID 587 UBIQUITY MIRROR, ZERO VPA
FIGURE_4 = PRIOR DRAFTS REJECTED, ZERO VPA
FIGURE_5 = PENDING, ZERO VPA
```

---

## 12. Claim firewall

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

Visual design may not strengthen the mathematical claim.

---

End: `PNP_FIGURE_CONTRACT_v1_1`
