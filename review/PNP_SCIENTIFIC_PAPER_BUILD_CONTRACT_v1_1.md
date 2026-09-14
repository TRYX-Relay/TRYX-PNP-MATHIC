# Problem No Problem Scientific Paper Build Contract v1.1

Date: `2026-09-13`

Status: `ACTIVE_PAPER_BUILD_CONTRACT`

Supersedes: `PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_0.md`

Purpose: govern construction of the P=NP / Problem No Problem scientific paper as a human-readable publication artifact while preserving the locked mathematical evidence, Lean-verified Local Closure MATHIC, reproducibility receipts, reference boundaries, and claim firewall.

## 0. Governing build rule

The paper is built from the verified mathematical layer outward.

```text
LEAN MATHIC PASS
      ↓
MATHIC PAPER TEMPLATE
      ↓
HUMAN PRESENTATION LAYER
      ↓
SCIENTIFIC PAPER BETA
      ↓
TECHNICAL / MATHEMATICAL / FENG-SHUI AUDIT
      ↓
LOCKED SCIENTIFIC PAPER
      ↓
HERO POSTER
      ↓
SPLASH PAGE / PUBLICATION COVER
      ↓
PUBLICATION PACKAGE
```

```text
PAPER_BUILD_MODE = VERIFIED_MATH_FIRST + HUMAN_PRESENTATION_FIRST
BETA_TO_LOCKED_VERSION_SYSTEM = ACTIVE
MATHEMATICAL_SOURCE_MUTATION = NONE
CLAIM_PROMOTION = NONE
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

The scientific paper may simplify language, improve order, add exposition, and improve visual presentation. It may not silently modify the mathematics, theorem scope, benchmark population, reference meaning, or claim boundary.

---

# 1. Human presentation layer

The PNP paper follows the successful Navier-Stokes ANEA human-facing presentation model.

The reader encounters ordinary language first. Internal terminology activates only after the conventional problem and the local purpose are understandable.

```text
CONVENTIONAL_LANGUAGE_FIRST = REQUIRED
INTERNAL_JARGON_BEFORE_EXPLANATION = PROHIBITED
UNEXPLAINED_TOPOLOGY = PROHIBITED
UNEXPLAINED_LAWS = PROHIBITED
UNEXPLAINED_THEOREM_NAMES = PROHIBITED
REPOSITORY_MACHINE_IDENTIFIERS_IN_MAIN_PROSE = PROHIBITED
```

TRYX must be explained in human terms before it is used as shorthand:

```text
V = Value = current state / carried object
P = Perception = comparison / relation step
A = Action = committed operation / result
V' = next Value = successor state
```

The public paper may reference TRYX, ENIAD, and MATHIC, but those terms must function as readable instruments rather than passwords into the framework.

## Human prose rule

Paragraphs should be short enough to breathe. A reader should not encounter a solid gray wall of text.

```text
PARAGRAPH_EYE_RELIEF = REQUIRED
ONE_IDEA_PER_PARAGRAPH = PREFERRED
LONG_UNBROKEN_TEXT_BLOCKS = PROHIBITED
DENSE_MACHINE_STATUS_BLOCKS = PROHIBITED
REPOSITORY_RECEIPT_LINES_IN_BODY = PROHIBITED
```

Commit hashes, workflow run IDs, artifact IDs, raw file hashes, CI job numbers, and internal Lean source identifiers belong in repository receipts or a reviewer guide, not in the normal scientific narrative unless they are directly required for reproducibility instructions.

Example of prohibited main-body clutter:

```text
Workflow run 34795750810
commit 6c34c44d49cfa8a86c077d7174b0ab94bf92dd8d
```

The paper should instead say, in ordinary language, that the Lean/MATHIC build passed, with detailed receipts available in the repository.

---

# 2. Typography and vertical Feng Shui grid

## 2.1 Font floor

```text
DEFAULT_BODY_FONT_SIZE = 12_PT_MINIMUM
WORKING_BODY_TARGET = 13_PT
BODY_TEXT_BELOW_12_PT = PROHIBITED
```

The only routine exception is a deliberately subordinate italic explanatory line directly under a MATHIC formula row.

```text
MATHIC_ITALIC_UNDERSCORE_LINE = MAY_USE_SMALLER_TYPE
MATHIC_ITALIC_UNDERSCORE_TARGET = 10.5_PT_TO_11_PT
OTHER_SMALL_TEXT = PROHIBITED_UNLESS_EXPLICITLY_APPROVED
```

## 2.2 Line spacing

```text
BODY_LINE_SPACING = 1.0
LINE_SPACING_BELOW_1.0 = PROHIBITED
CONDENSED_LINE_SPACING_TO_FORCE_PAGE_FIT = PROHIBITED
```

Eye relief is created with paragraph spacing and page composition, not by crushing the line height.

## 2.3 Display mathematics

Display formulas are presentation objects and must be visibly larger than body prose.

```text
DISPLAY_FORMULA_SIZE > BODY_FONT_SIZE
WORKING_DISPLAY_FORMULA_TARGET = 15_PT_TO_17_PT
FORMULA_SHRINK_TO_FIT = PROHIBITED
```

## 2.4 Maximum vertical page budget

The paper uses a fixed vertical composition grid rather than subjective density guessing.

```text
MAXIMUM_PAGE_BUDGET = 48 BODY_LINE_EQUIVALENTS
PREFERRED_ORDINARY_PAGE_DENSITY = 40_TO_44 BODY_LINE_EQUIVALENTS
ONE_THIRD_PAGE = 16 BODY_LINE_EQUIVALENTS
TWO_THIRDS_PAGE = 32 BODY_LINE_EQUIVALENTS
FULL_PAGE = 48 BODY_LINE_EQUIVALENTS
```

The 48-line budget is an **absolute vertical composition budget**, not permission to fill every page with 48 literal prose lines.

Headings, displayed equations, tables, blank separation, captions, and figure zones all consume line-equivalents.

Typical accounting:

```text
SECTION_HEADING_WITH_SPACE = 2_TO_3 LINE_EQUIVALENTS
DISPLAY_EQUATION = 2_TO_3 LINE_EQUIVALENTS
LARGE_EQUATION_BLOCK = 3_TO_5 LINE_EQUIVALENTS
SHORT_CAPTION = 2_TO_3 LINE_EQUIVALENTS
PRINCIPAL_FIGURE_ZONE = 16 LINE_EQUIVALENTS
```

No page may compensate for a figure or large formula by shrinking type, reducing line spacing below 1.0, collapsing paragraph spacing, or compressing captions.

---

# 3. Figure footprint rule

The scientific paper contains exactly four principal illustrations.

Every principal figure occupies **one third of the usable page height**.

```text
PRINCIPAL_FIGURE_COUNT = 4
PRINCIPAL_FIGURE_ZONE = 16 BODY_LINE_EQUIVALENTS
PRINCIPAL_FIGURE_ZONE_FRACTION = 1/3 PAGE
MAX_TEXT_ON_FIGURE_PAGE = 32 BODY_LINE_EQUIVALENTS
FIGURE_PLUS_CAPTION_PLUS_BREATHING_ROOM <= 16 LINE_EQUIVALENTS
```

The figure zone includes:

```text
ARTWORK
+ CAPTION
+ TOP BREATHING ROOM
+ BOTTOM BREATHING ROOM
```

Recommended artwork height inside the one-third-page zone is approximately 2.5–2.8 inches, leaving sufficient room for caption and white space.

Allowed page patterns include:

```text
16 TEXT
16 FIGURE
16 TEXT
```

or

```text
16 FIGURE
32 TEXT
```

or

```text
32 TEXT
16 FIGURE
```

A principal figure may not exceed the one-third-page zone unless the user explicitly changes the contract.

```text
FIGURE_GROWTH_BY_TEXT_COMPRESSION = PROHIBITED
FIGURE_GROWTH_BY_FONT_SHRINKING = PROHIBITED
FIGURE_GROWTH_BY_LINE_SPACING_REDUCTION = PROHIBITED
```

## Figure roles

### Figure 1 — Problem / boundary

```text
ROLE = SEMANTIC_CLOSURE_VS_COMPLEXITY_BOUNDARY
PLACEMENT = EARLY_BODY_AFTER_CONVENTIONAL_PROBLEM_FRAMING
PROOF_WEIGHT = EXPLANATORY_ONLY
FOOTPRINT = 1/3 PAGE
```

### Figure 2 — Native MATHIC mechanism

```text
ROLE = M1_TO_M9_LOCAL_CLOSURE_MECHANISM
PLACEMENT = MECHANISM_SECTION
PROOF_WEIGHT = EXPLANATORY_ONLY
FOOTPRINT = 1/3 PAGE
```

Figure 2 must visibly preserve the native sequence and especially the distinction:

```text
m4. Hinge Siblings
→ m5. Mirror Closure
→ m6. Existential Fold
→ m7. Current Successor
→ m8. Ordinal Succession
```

### Figure 3 — Finite evidence

```text
ROLE = FINITE_BENCHMARK_AND_INDEPENDENT_ORACLE
PLACEMENT = FINITE_EVIDENCE_SECTION
PROOF_WEIGHT = REPRODUCIBILITY_PRESENTATION_ONLY
FOOTPRINT = 1/3 PAGE
```

Required benchmark scope:

```text
3 variables
→ 26 admissible clauses
→ formulas of size 0–4
→ 17,902 formulas
→ 53,706 folds
→ replay vs independent oracle
→ 0 disagreements
→ negative control detected
```

### Figure 4 — Reviewer’s Bench hero

```text
ROLE = REVIEWERS_BENCH_HERO
PLACEMENT = LATE_BODY / REVIEWER_REWARD_TRANSITION
PROOF_WEIGHT = NONE_INDEPENDENT
FOOTPRINT = 1/3 PAGE
REUSE = HERO_POSTER + SPLASH_PAGE
```

Visual lineage remains:

```text
FIGURE_4 MASTER
→ PNP HERO POSTER
→ PNP SPLASH PAGE
```

---

# 4. Dedicated MATHIC formula page

The paper must contain a dedicated MATHIC formula page.

This page is the canonical human-facing mathematical progression and replaces duplicated M1–M9 bullet summaries elsewhere in the paper.

```text
DEDICATED_FORMULA_PAGE = REQUIRED
M1_TO_M9_DUPLICATION_ELSEWHERE = PROHIBITED
FORMULA_PAGE_ROLE = CANONICAL_HUMAN_EQUATION_REFERENCE
```

## 4.1 Exact row presentation

Use a **two-column table**.

Left column: measure identifier and measure name on one line.

Right column: large display formula(s), followed by a small italic explanatory underscore line of no more than two lines.

Exact row naming format:

```text
m1. TYPE-SET-0 Distinction
m2. Current #
m3. VPA Rotation
m4. Hinge Siblings
m5. Mirror Closure
m6. Existential Fold
m7. Current Successor
m8. Ordinal Succession
m9. Local Closure
```

Do not split the measure number and name onto separate rows or headings.

```text
MEASURE_AND_NAME_SAME_LINE = REQUIRED
FORMULAS = LARGE_PRESENTATION_SIZE
EXPLANATORY_UNDERSCORE = SMALL_ITALIC / MAX_TWO_LINES
MATHIC_TABLE_COLUMNS = 2
```

The formula page must carry the actual mathematics, not merely descriptive bullets.

Minimum formula content:

```text
m1. Boolean carrier / 0-1 distinction
m2. current-state constitution
m3. V→P→A→V' rotation
m4. current sibling restrictions
m5. shared / left residue / right residue provenance equations
m6. existential fold a∨b = a+b-ab
m7. exact successor f_(i+1)=E_xi(f_i)
m8. current-state succession f0→f1→...→fn
m9. local closure fn=1 iff ∃a in A_n such that f0(a)=1
```

---

# 5. Theorem presentation

The scientific paper uses **human theorem names, theorem statements, and proofs**.

A theorem may not appear merely as an unexplained Lean identifier.

Prohibited public-facing form:

```text
Lean theorem: TRYX.PNP.resolve_correct
```

Required form:

```text
Theorem N (Human-readable theorem name).
<mathematical statement>

Proof.
<proof in ordinary mathematical language>
□
```

Lean names may be mentioned parenthetically after the theorem/proof if useful for traceability, but may not replace the human theorem name or proof.

```text
THEOREM_NAME = REQUIRED
THEOREM_STATEMENT = REQUIRED
THEOREM_PROOF = REQUIRED
RAW_LEAN_IDENTIFIER_AS_THEOREM_TITLE = PROHIBITED
```

The Lean section should explain what Lean checks in ordinary language. Detailed machine receipts remain in the repository verification layer.

---

# 6. Finite fixture / replay presentation

The finite benchmark is evidence and reproducibility material, not a decorative receipt card.

```text
FINITE_FIXTURE = NORMAL_PROSE + FORMULAS + FIGURE_3
FINITE_FIXTURE_BOX = PROHIBITED
RECEIPT_CARD_STYLE = PROHIBITED
```

The counts may be presented cleanly in prose, equations, or a small ordinary table where necessary. They should not become a wall of status lines.

---

# 7. Reference-at-activation policy

References activate where the cited concept becomes operational in the argument.

```text
REFERENCE_AT_ACTIVATION = REQUIRED
DETACHED_BIBLIOGRAPHY_ONLY = INSUFFICIENT
EXTERNAL_REFERENCE_IS_INTERNAL_AUTHORITY = NO
```

External sources support:

```text
CONVENTIONAL_P_VS_NP_DEFINITIONS
NP_COMPLETENESS_HISTORY
BOOLEAN_ALGEBRA_ANTECEDENTS
SYMBOLIC_BOOLEAN_REPRESENTATION_CONTEXT
REPRESENTATION_SIZE_CAUTION
COMPLEXITY_BOUNDARY
OPTIONAL_PROOF_BARRIER_CONTEXT
```

Internal PNP results trace primarily to:

```text
LOCKED_LOCAL_CLOSURE_MATHIC
GOVERNING_SOURCE
LEAN_PROOF
LEAN_MATHIC_BRIDGE
FINITE_REPLAY
INDEPENDENT_ORACLE
```

The reference-activation index remains part of the closeout.

---

# 8. Claim-map removal

The scientific paper does **not** contain a separate claim-to-source map.

The earlier v1.0 contract requirement is superseded.

```text
CLAIM_TO_SOURCE_MAP_IN_PAPER = REMOVED
CLAIM_MAP_SECTION = PROHIBITED
```

Traceability remains available through:

```text
REFERENCE_AT_ACTIVATION
THEOREM + PROOF PRESENTATION
LEAN VERIFICATION SECTION
REPLAY / ORACLE SECTION
REVIEWER WALKTHROUGH
REPOSITORY RECEIPTS
FINAL CLOSED / OPEN STATUS
```

A machine-oriented claim map may remain in repository review materials or reviewer documentation, but not as a body section in the human scientific paper.

---

# 9. Closed / open boundary

The strongest established result and the unresolved complexity obligations must remain adjacent enough that no reader can mistake one for the other.

```text
CLOSED / VERIFIED:
- Boolean fold identity
- one-step existential semantics
- repeated finite-carrier existential semantics
- SAT/UNSAT terminal semantics
- Lean MATHIC synchronization pass
- finite benchmark replay
- independent oracle agreement on declared benchmark
- negative control detection

OPEN:
- general representation-size bound
- substitution cost bound
- symbolic composition / multiplication cost bound
- normalization / canonicalization cost bound
- equality / compatibility cost bound
- witness reconstruction complexity
- standard-machine polynomial runtime bound
- conventional P = NP
```

The open obligations are not hidden in end matter.

---

# 10. Reviewer’s Bench

The browser-openable Reviewer’s Bench remains a required optional reviewer reward after the mathematical paper.

```text
REVIEWER_REWARD_NAME = REVIEWER'S BENCH
FORMAT = SELF_CONTAINED_BROWSER_OPENABLE_HTML
PROOF_WEIGHT = NONE_INDEPENDENT
```

Required visible elements:

```text
CURRENT STATE
ACTIVE M1-M9 MEASURE
BOOLEAN SIBLINGS
M5 PROVENANCE
M6 FOLD
M7 SUCCESSOR
M8 HISTORY
M9 TERMINAL
INDEPENDENT ORACLE
NEGATIVE CONTROL
OPEN COMPLEXITY GATE
```

Required actions:

```text
PRESET INPUT
SUPPORTED CUSTOM FINITE INPUT
STEP ONE MEASURE
STEP ONE FOLD
RUN TO TERMINAL
RESET
NEGATIVE CONTROL OR→AND
```

Paper notation and Bench notation must match.

---

# 11. ANEA-derived paper rhythm

The PNP paper adopts the successful ANEA rhythm, with ordinary language first and internal machinery only after orientation.

```text
1. TITLE / ABSTRACT / CLAIM BOUNDARY / CONTENTS
2. CONVENTIONAL P VS NP PROBLEM
3. TRYX EXPLAINED IN HUMAN LANGUAGE
4. FIGURE 1 — PROBLEM / BOUNDARY
5. DEDICATED MATHIC FORMULA PAGE
6. THEOREMS + PROOFS
7. LEAN VERIFICATION IN HUMAN LANGUAGE
8. FINITE EVIDENCE + FIGURE 3
9. OPEN COMPLEXITY GATE
10. REVIEWER'S BENCH + FIGURE 4
11. DISCUSSION / LIMITATIONS / HUMAN-AI NOTE
12. REFERENCES + REFERENCE-ACTIVATION INDEX + CLOSED/OPEN STATUS
```

Figure 2 may sit adjacent to the formula/mechanism discussion so long as the one-third-page figure rule is obeyed.

```text
ANEA_PAGE_COUNT = NOT_BINDING
ANEA_HUMAN_RHYTHM = BINDING
```

---

# 12. Page-break and spacing rules

Forced page breaks are used only when they serve a specific presentation purpose.

```text
FORCED_PAGE_BREAK_FOR_EVERY_SECTION = PROHIBITED
NATURAL_SECTION_FLOW = REQUIRED
ORPHAN_HALF_EMPTY_PAGE = PROHIBITED_WHEN_AVOIDABLE
WIDOW_ORPHAN_CONTROL = REQUIRED
```

Quiet pages are allowed. Cramped pages are not.

```text
THEOREM_BREATHING_ROOM = REQUIRED
FORMULA_BREATHING_ROOM = REQUIRED
FIGURE_BREATHING_ROOM = REQUIRED
WHITE_SPACE = FUNCTIONAL
```

---

# 13. Visual Feng Shui audit gate

Every DOCX beta intended for user review must be rendered before presentation.

The assistant must inspect **every rendered page**, not only page 1 or representative samples.

```text
DOCX_RENDER_BEFORE_PRESENTATION = REQUIRED
EVERY_PAGE_VISUAL_INSPECTION = REQUIRED
FENG_SHUI_AUDIT = REQUIRED
```

The audit checks:

```text
[ ] font floor respected
[ ] line spacing = 1.0
[ ] no compressed gray walls of text
[ ] paragraph eye relief present
[ ] no orphan headings
[ ] no smashed lines
[ ] no formula overflow
[ ] no table overflow
[ ] no unexplained internal identifiers
[ ] no machine receipt clutter in human prose
[ ] formula page preserves exact M1-M9 row format
[ ] principal figures reserve exactly one-third-page zones
[ ] captions fit within figure zones
[ ] no page exceeds 48 body-line equivalents
[ ] figure pages contain no more than 32 text line-equivalents
[ ] no claim-map section
[ ] finite fixture is not boxed
[ ] theorem names + statements + proofs are human-readable
[ ] reference activation remains clear
[ ] closed/open boundary remains explicit
```

A beta that fails the visual audit is not presented to the user as a review candidate.

```text
FAILED_FENG_SHUI_AUDIT = REBUILD_BEFORE_PRESENTATION
```

---

# 14. Figure 4 → Hero Poster → Splash Page lineage

The mandatory visual development order remains:

```text
FIGURE_4 MASTER ART
    → PNP HERO POSTER
    → PNP SPLASH PAGE
```

Figure 4 is finalized before paper lock.

Hero Poster and Splash Page are built only after paper lock.

```text
FIGURE_4_BEFORE_PAPER_LOCK = REQUIRED
HERO_POSTER_AFTER_PAPER_LOCK = REQUIRED
SPLASH_AFTER_HERO_POSTER = REQUIRED
SPLASH_BODY_MUTATION = PROHIBITED
```

The splash is appended as a cover/frontispiece. It does not alter the locked paper body.

---

# 15. Reviewer walkthrough

Required reviewer path:

```text
1. Open scientific paper.
2. Read conventional problem and claim boundary.
3. Read TRYX human explanation.
4. Inspect dedicated M1-M9 formula page.
5. Read theorem statements and proofs.
6. Inspect Lean verification summary.
7. Run finite replay / package checker.
8. Confirm 17,902 formulas / 53,706 folds / zero disagreements.
9. Open Reviewer's Bench.
10. Run a preset.
11. Trigger OR→AND negative control.
12. Finish on the open polynomial-runtime gate.
```

```text
REVIEWER_WALKTHROUGH = REQUIRED
WALKTHROUGH_MAY_PROMOTE_CLAIMS = NO
```

---

# 16. Construction order

```text
1. Verify Lean MATHIC pass.
2. Establish conventional problem and claim boundary.
3. Explain TRYX in human language.
4. Establish manuscript section hierarchy and TOC.
5. Reserve the four one-third-page figure zones.
6. Build the two-column M1-M9 formula page in the exact row format.
7. Write human theorem names, theorem statements, and proofs.
8. Write Lean verification section in ordinary language.
9. Write finite benchmark/oracle section without receipt boxes.
10. Write open complexity gate.
11. Integrate references at first activation.
12. Build Figure 1.
13. Build Figure 2.
14. Build Figure 3.
15. Develop Reviewer's Bench.
16. Build Figure 4 master hero.
17. Synchronize paper / figures / Bench notation.
18. Build reviewer walkthrough.
19. Render DOCX.
20. Perform every-page Feng Shui audit against the 48-line grid.
21. Repair all visual failures.
22. Perform technical / mathematical / reference / claim-boundary audit.
23. LOCK SCIENTIFIC PAPER VERSION.
24. Build Hero Poster from Figure 4.
25. Build Splash Page from Hero Poster.
26. Assemble publication package without changing locked body.
```

---

# 17. Lock rule

The scientific paper lock freezes:

```text
SUBSTANTIVE BODY
THEOREM STATEMENTS
THEOREM PROOFS
EQUATIONS
M1-M9 FORMULA PAGE
SECTION ORDER
TOC HIERARCHY
REFERENCE SET
REFERENCE-ACTIVATION INDEX
CLOSED / OPEN STATUS
FIGURES 1-4
FIGURE CAPTIONS
FIGURE PLACEMENT
PAPER-SIDE REVIEWER'S BENCH NOTATION
TYPOGRAPHIC FLOOR
VERTICAL PAGE GRID
```

The lock does **not** freeze a removed claim-map section because the claim map is no longer part of the scientific paper.

Post-lock poster, splash, sandbox, and walkthrough work may not change the mathematical substance or claim boundary.

---

# 18. Claim firewall

```text
BOOLEAN_FOLD_IDENTITY = VERIFIED
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
```

End: `PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_1`
