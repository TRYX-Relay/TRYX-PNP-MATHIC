# PNP Figure Contract v1.2

Date: `2026-09-13`

Status: `ACTIVE / BINDING FOR ALL PNP PAPER FIGURES`

Supersedes:

`review/PNP_FIGURE_CONTRACT_v1_1.md`

Parent paper contract:

`review/PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_4.md`

This revision removes the former VPA Figure 2 from the paper figure system entirely and renumbers the remaining figures with no empty slot.

---

## 1. Global figure system

```text
FIGURE_COUNT = 4
WIDTH = 7.0 INCHES
HEIGHT = 3.5 INCHES
ASPECT_RATIO = 2:1
ORIENTATION = HORIZONTAL
```

```text
FIGURE_1 = SEMANTIC / COMPLEXITY BOUNDARY
FIGURE_2 = ENAID 587 UBIQUITY MIRROR TOPOLOGY
FIGURE_3 = FINITE EVIDENCE / REPLAY / INDEPENDENT ORACLE
FIGURE_4 = REVIEWER'S BENCH
```

Former Figure 2, TRYX VPA cycle, is removed from the paper and has no replacement slot.

---

## 2. VPA removal rule

```text
VPA_PRINCIPAL_FIGURE = REMOVED
VPA_VISUAL_OCCURRENCES_ALLOWED = 0
```

Forbidden in all four principal figures:

```text
VPA CYCLE
V -> P -> A -> V'
VPA CIRCLES
VPA ICONS
VPA MINIATURES
VPA SHORTHAND
VPA RUNTIME LABEL
VPA-BASED DECORATIVE MOTIF
```

If VPA must be discussed in prose, do so textually. No principal paper figure will visualize it.

---

## 3. Figure 1 contract

Status: `LOCKED`

Role:

`Semantic closure and complexity boundary`

Primary visual grammar:

`BOUNDARY / SPLIT-DOMAIN DIAGRAM`

Forbidden:

```text
VPA
UBIQUITY MIRROR
FINITE EVIDENCE COUNTS
REVIEWER BENCH UI
```

Lock receipt:

`review/figures/PNP_FIGURE_1_LOCK.md`

---

## 4. Figure 2 contract

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

Forbidden:

```text
VPA OF ANY KIND
COLLATZ / SNOWMAN NAMING
FINITE REPLAY COUNTS
REVIEWER BENCH UI
```

The formula and topology are ENAID.

---

## 5. Figure 3 contract

Status: `PENDING / PRIOR FINITE-EVIDENCE DRAFTS REJECTED`

Role:

`Finite evidence / replay / independent oracle`

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

`FORENSIC EVIDENCE PIPELINE / AUDIT LEDGER`

Forbidden:

```text
VPA OF ANY KIND
UBIQUITY MIRROR
THEORETICAL CYCLE GRAPHICS
P = NP ESTABLISHED
POLYNOMIAL-RUNTIME CLAIM
REVIEWER BENCH UI
```

The data itself is the figure.

---

## 6. Figure 4 contract

Status: `PENDING`

Role:

`Reviewer's Bench hero`

Primary job:

Show the functioning review instrument used to inspect and replay the MATHIC / local-closure mechanism.

Development lineage:

```text
FUNCTIONING REVIEWER'S BENCH
-> FIGURE 4 MASTER
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

`SCIENTIFIC INSTRUMENT / BENCH / READOUT`

Forbidden:

```text
VPA OF ANY KIND
UBIQUITY MIRROR REDRAW
FINITE EVIDENCE PIPELINE REDRAW
CLAIM PROMOTION
```

---

## 7. Exclusive motif ownership matrix

```text
SEMANTIC / COMPLEXITY BOUNDARY     -> FIGURE 1 ONLY
587 UBIQUITY MIRROR TOPOLOGY       -> FIGURE 2 ONLY
17,902 / 53,706 EVIDENCE PIPELINE  -> FIGURE 3 ONLY
REVIEWER'S BENCH UI                -> FIGURE 4 ONLY
VPA VISUAL LANGUAGE                -> NO PRINCIPAL FIGURE
```

No visual motif may appear twice.

```text
IF THE CENTRAL OR SECONDARY VISUAL MOTIF ALREADY EXISTS IN ANOTHER FIGURE,
THE NEW FIGURE FAILS BEFORE GENERATION.
```

---

## 8. Mandatory preflight

```text
[ ] correct figure number
[ ] correct figure role
[ ] 7.0 in x 3.5 in canvas
[ ] unique visual language
[ ] no motif owned by another figure
[ ] zero VPA visualization
[ ] Ubiquity Mirror only if Figure 2
[ ] finite benchmark counts only if Figure 3
[ ] Reviewer Bench UI only if Figure 4
[ ] no Collatz / Snowman naming for ENAID topology
[ ] no conventional P = NP claim promotion
[ ] readable at actual paper size
[ ] restrained scientific styling
```

Any failed item stops generation.

---

## 9. Current state

```text
FIGURE_1 = LOCKED
FORMER_FIGURE_2_VPA = REMOVED
FIGURE_2 = ENAID 587 UBIQUITY MIRROR, REBUILD REQUIRED
FIGURE_3 = FINITE EVIDENCE, PENDING
FIGURE_4 = REVIEWER'S BENCH, PENDING
```

---

## 10. Claim firewall

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

End: `PNP_FIGURE_CONTRACT_v1_2`
