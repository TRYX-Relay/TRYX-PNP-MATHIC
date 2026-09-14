# Problem No Problem Scientific Paper Build Contract v1.0

Date: `2026-09-13`

Status: `ACTIVE_PAPER_BUILD_CONTRACT`

Purpose: govern construction of the scientific-paper presentation for the Problem No Problem project without disturbing the locked mathematical evidence, provenance receipts, or public-fortress claim boundary.

## Build objective

Construct the scientific paper as a controlled publication artifact with stable structure before decorative or final presentation work is introduced.

```text
PAPER_BUILD_MODE = STRUCTURE_FIRST
BETA_TO_LOCKED_VERSION_SYSTEM = ACTIVE
MATHEMATICAL_SOURCE_MUTATION = NONE
CLAIM_PROMOTION = NONE
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

## Version lifecycle

The paper follows the established project lifecycle rather than introducing a separate lock vocabulary.

```text
BETA_1
  -> BETA_2
  -> BETA_n
  -> TECHNICAL / MATHEMATICAL / PRESENTATION AUDIT
  -> LOCKED VERSION
  -> HERO POSTER
  -> SPLASH PAGE / PUBLICATION COVER ASSEMBLY
  -> PUBLICATION PACKAGE
```

Beta versions may change structure, prose, formulas-as-presentation, references, figure placeholders, captions, notation presentation, pagination, and visual composition while remaining subordinate to the locked mathematical source authority.

The locked scientific-paper version freezes the substantive paper body. Post-lock poster and splash work may package and present that body but may not change its mathematics or claim boundary.

## Required paper components

### 1. Table of contents

The paper must contain a dedicated table of contents reflecting the locked section hierarchy of the final manuscript.

```text
TABLE_OF_CONTENTS = REQUIRED
TOC_FINALIZATION = AFTER_SECTION_STRUCTURE_STABILIZES
```

### 2. Splash page

A dedicated splash / presentation page will be built only after the scientific paper itself has been completed and locked.

The splash page is presentation-layer material and must not drive manuscript structure, mathematical content, pagination decisions, or claim language during the beta build.

The PNP splash page is not an independently invented design. It is templated from the separate PNP Hero Poster, following the successful ANEA precedent in which the poster served as both release identity and publication cover.

```text
SPLASH_PAGE = REQUIRED
SPLASH_PAGE_BUILD = AFTER_PAPER_LOCK
SPLASH_PAGE_BEFORE_PAPER_LOCK = PROHIBITED
SPLASH_TEMPLATE_AUTHORITY = PNP_HERO_POSTER
SPLASH_ROLE = PUBLICATION_COVER / FRONTISPIECE
SPLASH_MAY_CHANGE_PAPER_BODY = NO
```

The preferred publication assembly model is:

```text
PAGE_1 = SPLASH / POSTER-DERIVED COVER
PAGE_2+ = LOCKED SCIENTIFIC PAPER BODY, UNCHANGED
```

### 3. Dedicated formula page

The paper must contain a dedicated formula page presenting the principal governing formula or formula set as a standalone scientific reference surface.

This page is part of the paper body, not the later splash page.

```text
DEDICATED_FORMULA_PAGE = REQUIRED
FORMULA_PAGE_ROLE = CANONICAL_EQUATION_REFERENCE
FORMULA_PAGE_STATUS = PART_OF_PAPER_BODY
```

The formula page should appear only after the reviewer has encountered enough conventional exposition, mechanism, theorem, finite evidence, and open-gate language to understand the compressed progression.

### 4. Graphic placeholders and four-illustration system

During manuscript construction, every planned graphic location must be represented by an explicit placeholder rather than by a provisional embedded graphic until its section and footprint are stable.

Each placeholder should preserve the intended location, approximate footprint, figure identifier, and caption/reference relationship so that body pagination and cross-references can stabilize before final artwork insertion.

Recommended placeholder form:

```text
[FIGURE PLACEHOLDER: Figure N]
Purpose: <graphic purpose>
Approximate footprint: <full-width / half-page / etc.>
Caption: <working caption>
Source / construction note: <reference>
```

```text
GRAPHIC_PLACEHOLDERS = REQUIRED_DURING_BUILD
PLACEHOLDER_CROSS_REFERENCES = REQUIRED
FINAL_GRAPHICS_INSERTED_BEFORE_LOCK = YES
```

The scientific paper is limited to four principal illustrations. Each must earn its place by carrying conceptual, mechanistic, evidentiary, or reviewer-interface information.

#### Figure 1 — Problem / boundary illustration

Role: visually introduce the two distinct questions at the center of the paper.

```text
FIGURE_1_ROLE = SEMANTIC_CLOSURE_VS_COMPLEXITY_BOUNDARY
PLACEMENT = EARLY_BODY_AFTER_CONVENTIONAL_PROBLEM_FRAMING
BEAUTY_ROLE = CONCEPTUAL_OPENING
PROOF_WEIGHT = EXPLANATORY_ONLY
```

Figure 1 should distinguish the verified finite semantic path from the separate conventional complexity obligation without visually implying that one automatically establishes the other.

#### Figure 2 — Mechanism illustration

Role: show the local-closure machinery after the reviewer has learned the accepted problem language.

```text
FIGURE_2_ROLE = CURRENT_STATE_HINGE_FOLD_SUCCESSOR / MATHIC_MECHANISM
PLACEMENT = MECHANISM_SECTION
BEAUTY_ROLE = SIGNATURE_INTERNAL_MECHANISM
PROOF_WEIGHT = EXPLANATORY_ONLY
```

Figure 2 should visually encode the current state, sibling restrictions, hinge/fold, successor, repeat, and terminal return using notation synchronized to the paper and Reviewer's Bench.

#### Figure 3 — Evidence illustration

Role: make the benchmark universe and independent verification path visible.

```text
FIGURE_3_ROLE = FINITE_BENCHMARK_AND_INDEPENDENT_ORACLE
PLACEMENT = FINITE_EVIDENCE_SECTION
BEAUTY_ROLE = DATA / VERIFICATION_VISUAL
PROOF_WEIGHT = REPRODUCIBILITY_PRESENTATION_ONLY
```

Figure 3 should show the exact declared benchmark scope:

```text
3 Boolean variables
  -> 26 admissible clauses
  -> all formulas containing 0-4 distinct clauses
  -> 17,902 formulas
  -> 53,706 folds
  -> replay vs independent oracle
  -> 0 disagreements
  -> negative control detected
```

#### Figure 4 — Reviewer's Bench hero

Figure 4 is the visual source object for the reviewer instrument and later publication identity.

```text
FIGURE_4_ROLE = REVIEWERS_BENCH_HERO
PLACEMENT = LATE_BODY / REVIEWER_REWARD_TRANSITION
BEAUTY_ROLE = FLAGSHIP_INSTRUMENT_IMAGE
REUSE = HERO_POSTER + SPLASH_PAGE
PROOF_WEIGHT = NONE_INDEPENDENT
```

Figure 4 should present the Reviewer's Bench as a polished scientific instrument while retaining visible cues for current state, sibling states, fold, successor, oracle comparison, negative control, and SAT/UNSAT terminal output.

The Figure 4 master artwork must be designed to support both a fully annotated paper version and a cleaner poster/splash derivation.

### 5. Figure 4 -> Hero Poster -> Splash Page lineage

The visual development order is mandatory:

```text
FIGURE_4 MASTER ART
    -> PNP HERO POSTER
    -> PNP SPLASH PAGE
```

Interpretation:

```text
FIGURE_4 = VISUAL INVENTION / REVIEWERS_BENCH HERO
HERO_POSTER = FLAGSHIP PUBLIC VISUAL EXPANSION
SPLASH_PAGE = PUBLICATION-COVER ADAPTATION OF HERO_POSTER
```

Figure 4 is finalized as part of the scientific-paper beta series before paper lock.

After the paper is locked, the Hero Poster may expand Figure 4 into the separate public visual identity. The Splash Page is then templated from the Hero Poster and appended as the publication cover/frontispiece without altering the locked scientific body.

```text
FIGURE_4_BEFORE_PAPER_LOCK = REQUIRED
HERO_POSTER_AFTER_PAPER_LOCK = REQUIRED
SPLASH_AFTER_HERO_POSTER = REQUIRED
SPLASH_BODY_MUTATION = PROHIBITED
```

### 6. Reviewer Reward / Interactive Sandbox

Develop a browser-openable interactive companion as a deliberate reward for the reviewer who has worked through the scientific paper.

The paper carries the formal argument. The interactive companion comes afterward as a small laboratory in which the reviewer can touch the mechanism, change inputs, step through folds, inspect intermediate states, test a negative control, and compare the result against an independent oracle.

The experience should feel optional, immediate, tactile, and revealing rather than like another review obligation. It is not a sales demo, a substitute for the paper, or a shortcut around the mathematical argument.

Preferred presentation identity:

```text
REVIEWER_REWARD_NAME = REVIEWER'S BENCH
REVIEWER_REWARD_PROMPT = "You've read the argument. Now try the mechanism yourself."
PRIMARY_EXPERIENCE = OPTIONAL_HANDS_ON_LAB
FORMAL_ARGUMENT_LOCATION = SCIENTIFIC_PAPER
REWARD_AFTER_READING = YES
```

Required interaction targets:

```text
INPUT_FORMULA_OR_PRESET = REQUIRED
STEP_CURRENT_HINGE = REQUIRED
SHOW_BOOLEAN_SIBLINGS = REQUIRED
SHOW_CURRENT_STATE = REQUIRED
SHOW_FOLD_RESULT = REQUIRED
SHOW_TERMINAL_SAT_UNSAT = REQUIRED
SHOW_INTERMEDIATE_STATE_HISTORY = REQUIRED
COMPARE_WITH_INDEPENDENT_ORACLE = REQUIRED
RESET_AND_REPLAY = REQUIRED
NEGATIVE_CONTROL_MODE = REQUIRED
```

The reviewer should be able to:

1. choose a small built-in Boolean/CNF example or enter a supported finite example;
2. inspect the current variable/address being eliminated;
3. see both Boolean sibling states at the hinge;
4. execute one fold at a time or run to terminal state;
5. inspect the complete sequence of intermediate states;
6. compare the primary result with an independently implemented oracle;
7. deliberately activate the preserved negative control, such as replacing OR with AND, and observe the disagreement;
8. reset and replay without reloading the page.

The reward should open into a useful state immediately. Presets should provide a fast first success, while deeper controls remain available for deliberate inspection.

```text
INTERACTIVE_REVIEW_SANDBOX = REQUIRED
REVIEWER_REWARD = REQUIRED
PRIMARY_MODE = STEP_THROUGH_FINITE_SEMANTICS
INDEPENDENT_ORACLE_COMPARISON = REQUIRED
NEGATIVE_CONTROL = REQUIRED
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_PROOF = NOT_CLAIMED
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

Preferred delivery form:

```text
REVIEWER_SANDBOX_FORMAT = SELF_CONTAINED_BROWSER_OPENABLE_HTML
REMOTE_SERVICE_DEPENDENCY = NONE_PREFERRED
REPRODUCIBLE_PRESETS = REQUIRED
SOURCE_VISIBLE_IN_REPOSITORY = REQUIRED
FAST_FIRST_INTERACTION = REQUIRED
OPTIONAL_DEEP_INSPECTION = REQUIRED
```

Its visual language must share the paper's notation and Figure 4 vocabulary, but interaction design should prioritize clarity, tactile exploration, and auditability over ornament.

## ANEA-derived presentation scaffold

The Navier-Stokes ANEA release established a successful presentation rhythm that PNP adopts as a scaffold rather than as a page-for-page copy.

The controlling sequence is:

```text
1. BEAUTY / VISUAL IDENTITY
   poster-derived splash cover

2. ORIENTATION
   title + author/date + abstract + explicit claim boundary + contents

3. CONVENTIONAL PROBLEM FIRST
   accepted P vs NP / SAT language before internal terminology

4. FIGURE 1
   conceptual difficulty / semantic-vs-complexity boundary

5. FIGURE 2
   internal mechanism after the reader understands the conventional problem

6. MATHEMATICS
   theorem / Lean correspondence allowed to breathe with minimal decorative interruption

7. FIGURE 3
   finite evidence / benchmark / independent oracle

8. OPEN GATE
   state exactly what remains unproved in conventional complexity terms

9. DEDICATED FORMULA PAGE
   compress the complete progression into a standalone mathematical visual surface

10. FIGURE 4 / REVIEWER REWARD
    Reviewer's Bench hero as late-body transition to interactive exploration

11. DISCUSSION / LIMITATIONS / NEXT PROGRAM
    explain what the framework contributes and what it still owes

12. REFERENCES + REFERENCE-ACTIVATION INDEX + CLAIM MAP
    finish with outsourced scholarship, provenance routing, and closed/open status
```

This sequence is a presentation scaffold. Exact PNP page numbers may evolve during beta builds.

```text
ANEA_PRESENTATION_SCAFFOLD = ADOPTED
ANEA_PAGE_COUNT = NOT_BINDING
PNP_VISUAL_RHYTHM = BINDING
```

### Presentation spacing rule

The paper must not place a decorative figure merely to fill a page. The central theorem / Lean material should be allowed visually quiet pages when appropriate.

```text
FIGURE_ON_EVERY_PAGE = PROHIBITED
THEOREM_BREATHING_ROOM = REQUIRED
VISUALS_MUST_EARN_PLACEMENT = YES
```

### Formula-page timing rule

The dedicated formula page should appear after the reader has encountered:

```text
CONVENTIONAL_PROBLEM
-> CORE_MECHANISM
-> VERIFIED_SEMANTICS
-> FINITE_EVIDENCE
-> OPEN_COMPLEXITY_GATE
-> FORMULA_PROGRESSION_PAGE
```

The formula page therefore acts as compression and synthesis, not as unexplained front matter.

### Reference closeout rule

The final scholarly section must include more than a detached bibliography.

Required closeout surfaces:

```text
NORMALIZED_REFERENCES = REQUIRED
REFERENCE_ACTIVATION_INDEX = REQUIRED
CLAIM_TO_SOURCE_MAP = REQUIRED
CLOSED_OPEN_STATUS = REQUIRED
```

External references support conventional complexity theory, historical antecedents, representation cautions, and theorem boundaries. They do not gain authority over internal PNP results merely by being cited.

## ANEA-derived reviewer architecture

The Navier-Stokes ANEA release established several reviewer-facing practices that transfer directly to PNP. These are mandatory for the scientific-paper build.

### A. Explicit review hierarchy

The release must tell the reviewer exactly what to open, in what order, and which surface has what authority.

Target route:

```text
README / READER'S GUIDE
  -> SCIENTIFIC PAPER
  -> DEDICATED FORMULA PAGE
  -> CANONICAL MATHIC / SOURCE AUTHORITY
  -> LEAN PROOF + VERIFICATION RECEIPT
  -> FINITE REPLAY + INDEPENDENT ORACLE
  -> REVIEWER'S BENCH
  -> PROVENANCE / DEVELOPMENT RECEIPTS
```

Review navigation order and authority precedence are different concepts.

```text
HUMAN_ENTRY_POINT = SCIENTIFIC_PAPER
CANONICAL_MATHEMATICAL_AUTHORITY = LOCKED_MATHIC / GOVERNING_SOURCE
REVIEW_NAVIGATION_ORDER_NE_AUTHORITY_PRECEDENCE = YES
```

Role taxonomy:

```text
AUTHORITATIVE_SOURCE = CANONICAL MATHIC / SOURCE AUTHORITY
SCIENTIFIC_EXPOSITION = SCIENTIFIC PAPER
FORMULA_REFERENCE = DEDICATED FORMULA PAGE
FORMAL_VERIFICATION = LEAN PROOF + RECEIPTS
REPRODUCIBILITY_EVIDENCE = REPLAY + INDEPENDENT ORACLE
INTERACTIVE_REVIEW_INSTRUMENT = REVIEWER'S BENCH
PROVENANCE_RECORD = DEVELOPMENT / ARCHIVE RECEIPTS
```

The phrase `functional ornamental` is not part of the public-facing PNP role taxonomy.

### B. Terminology boundary table

The paper must explicitly distinguish terms that a reviewer could otherwise conflate.

Minimum required entries:

```text
HINGE
BOOLEAN SIBLING STATES
CURRENT STATE
FOLD
EXISTENTIAL ELIMINATION
FINITE-CARRIER CLOSURE
SAT TERMINAL
UNSAT TERMINAL
LOCAL / INTERNAL CLOSURE
STANDARD-MACHINE POLYNOMIAL RUNTIME BOUND
CONVENTIONAL P = NP
```

The terminology section must state which terms are finite semantic or local execution properties and which are conventional complexity-theory obligations.

```text
TERMINOLOGY_BOUNDARY_TABLE = REQUIRED
AMBIGUOUS_CLOSURE_LANGUAGE = PROHIBITED
```

### C. Claim-to-source map

The scientific paper must contain a reviewer-facing map connecting important claims to their source authority and executable evidence.

Required columns or equivalent fields:

```text
PAPER_STATEMENT
CANONICAL_SOURCE_OR_FORMULA
LEAN_STATUS
REPLAY_OR_ORACLE_EVIDENCE
REVIEWER'S_BENCH_SURFACE
CLAIM_BOUNDARY
```

At minimum it must map:

1. Boolean fold identity;
2. hinge existential semantics;
3. repeated finite existential elimination;
4. finite SAT/UNSAT terminal semantics;
5. the recorded `17,902` formula / `53,706` fold benchmark;
6. the standard-machine polynomial runtime obligation as OPEN.

```text
CLAIM_TO_SOURCE_MAP = REQUIRED
TRACEABILITY_FROM_PAPER_TO_EVIDENCE = REQUIRED
```

### D. Reviewer walkthrough

Create a short reproducible reviewer walkthrough modeled on the useful ANEA demonstration layer.

Target short path:

```text
1. Open scientific paper and dedicated formula page.
2. Identify the canonical finite semantic statement.
3. Open Lean verification receipt.
4. Show source audit / machine-check status.
5. Run the package checker.
6. Show 17,902 formulas / 53,706 folds / zero disagreements.
7. Open Reviewer's Bench.
8. Run one small preset.
9. Activate the negative control.
10. Finish on the open standard-machine polynomial-runtime gate.
```

```text
REVIEWER_WALKTHROUGH = REQUIRED
SHORT_REVIEW_PATH = REQUIRED
WALKTHROUGH_MAY_PROMOTE_CLAIMS = NO
```

### E. Paper-to-Bench notation synchronization

The scientific paper and Reviewer's Bench must use the same notation, variable names, hinge labels, state labels, formula numbering, and visual vocabulary wherever the same mathematical object is being represented.

A reviewer moving from a paper figure or formula into the Bench should recognize the same mechanism immediately.

```text
PAPER_TO_BENCH_NOTATION_SYNC = REQUIRED
FORMULA_IDENTIFIER_SYNC = REQUIRED
STATE_LABEL_SYNC = REQUIRED
HINGE_LABEL_SYNC = REQUIRED
FIGURE_TO_INTERACTION_CROSS_REFERENCE = REQUIRED_WHERE_APPLICABLE
PARALLEL_DRIFTING_NOTATION = PROHIBITED
```

### F. Negative controls as a first-class review feature

The ANEA packaging demonstrated the value of deliberate corruption tests. PNP must preserve and expose the same philosophy.

The OR-to-AND mutation is the minimum interactive negative control. The paper and walkthrough should explain that this exists to demonstrate checker sensitivity, not as part of the valid mechanism.

```text
NEGATIVE_CONTROL_DOCUMENTED = REQUIRED
NEGATIVE_CONTROL_INTERACTIVE = REQUIRED
NEGATIVE_CONTROL_DISTINGUISHED_FROM_VALID_RUN = REQUIRED
```

### G. Closed-versus-open visual boundary

The paper should place the strongest established finite result adjacent to the unresolved complexity obligations rather than burying those obligations in end matter.

Required conceptual separation:

```text
CLOSED / VERIFIED:
- Boolean fold algebra
- finite-carrier existential semantics
- finite SAT/UNSAT terminal semantics
- recorded finite benchmark

OPEN:
- representation-size bound
- normalization-cost bound
- witness-reconstruction complexity
- standard-machine polynomial runtime bound
- conventional P = NP
```

The closed-versus-open distinction may be incorporated into Figure 1 and the dedicated formula page rather than consuming a fifth principal illustration.

```text
CLOSED_VS_OPEN_MAP = REQUIRED
OPEN_OBLIGATIONS_VISIBLE_NEAR_CORE_RESULT = REQUIRED
FIFTH_PRINCIPAL_ILLUSTRATION = NOT_REQUIRED
```

## Construction order

```text
1. Establish manuscript section hierarchy
2. Establish explicit review hierarchy and artifact-role taxonomy
3. Build table of contents framework
4. Build terminology boundary table
5. Build scientific body in conventional-problem-first order
6. Build outsourced reference-at-activation layer
7. Build claim-to-source map
8. Reserve the four principal figure placeholders and exact footprints
9. Build Figure 1 concept / boundary illustration
10. Build Figure 2 mechanism illustration
11. Build Figure 3 benchmark / oracle illustration
12. Develop and finalize Reviewer's Bench interaction contract and data model
13. Build Figure 4 Reviewer's Bench master hero artwork
14. Synchronize paper notation, Figure 4 notation, and Bench notation
15. Build dedicated formula page after mechanism/evidence/open-gate sections stabilize
16. Define negative-control presentation and reviewer walkthrough
17. Resolve section references, figure references, captions, formula identifiers, and pagination dependencies
18. Insert all four final paper illustrations
19. Complete technical, mathematical, reference, visual, and claim-boundary audit
20. LOCK SCIENTIFIC PAPER VERSION
21. Build PNP Hero Poster from Figure 4 master art
22. Lock / approve Hero Poster visual identity
23. Build Splash Page from Hero Poster template
24. Append Splash Page as publication cover without changing locked paper body
25. Build/finalize Reviewer's Bench against locked paper semantics and Figure 4 vocabulary
26. Cross-check Bench outputs against archived replay/oracle evidence
27. Build/finalize reviewer walkthrough
28. Perform final publication-package visual, pagination, traceability, link, and companion-artifact audit
29. Export publication artifact and reviewer companion
```

## Lock rule

The scientific paper lock freezes the substantive manuscript body, equations, claims, section order, formula page, table-of-contents hierarchy, terminology boundaries, claim-to-source map, figure numbering, final illustrations, captions, graphic placement, scholarly references, and paper-side notation used by the Reviewer's Bench.

Post-lock Hero Poster construction, Splash Page assembly, reviewer-sandbox presentation work, and walkthrough production may improve presentation but must not silently modify the locked mathematical argument or claim boundary.

```text
PAPER_LOCK_FREEZES_SUBSTANCE = YES
PAPER_LOCK_FREEZES_FIGURES = YES
POST_LOCK_HERO_POSTER_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_SPLASH_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_SANDBOX_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_WALKTHROUGH_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_CLAIM_PROMOTION = NO
```

The splash page may be appended ahead of the locked paper body as a cover/frontispiece, following the ANEA completeness-repair model, provided the locked body remains byte- or render-equivalent apart from intentional page-number offset caused by cover assembly.

## Claim firewall

This build contract governs publication construction only. It does not alter the repository's existing mathematical status.

```text
BOOLEAN_FOLD_IDENTITY = VERIFIED
FINITE_CARRIER_EXISTENTIAL_SEMANTICS = LEAN_VERIFIED
SAT_UNSAT_TERMINAL_SEMANTICS = LEAN_VERIFIED
FINITE_PACKAGE_REPLAY = VERIFIED
REPRESENTATION_SIZE_BOUND = OPEN
NORMALIZATION_COST_BOUND = OPEN
WITNESS_RECONSTRUCTION_COMPLEXITY = OPEN
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

End: `PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_0`
