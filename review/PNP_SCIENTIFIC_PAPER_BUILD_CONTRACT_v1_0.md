# Problem No Problem Scientific Paper Build Contract v1.0

Date: `2026-09-13`

Status: `ACTIVE_PAPER_BUILD_CONTRACT`

Purpose: govern construction of the scientific-paper presentation for the Problem No Problem project without disturbing the locked mathematical evidence, provenance receipts, or public-fortress claim boundary.

## Build objective

Construct the scientific paper as a controlled publication artifact with stable structure before decorative or final presentation work is introduced.

```text
PAPER_BUILD_MODE = STRUCTURE_FIRST
MATHEMATICAL_SOURCE_MUTATION = NONE
CLAIM_PROMOTION = NONE
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

## Required paper components

### 1. Table of contents

The paper must contain a dedicated table of contents reflecting the locked section hierarchy of the final manuscript.

```text
TABLE_OF_CONTENTS = REQUIRED
TOC_FINALIZATION = AFTER_SECTION_STRUCTURE_STABILIZES
```

### 2. Splash page

A dedicated splash / presentation page will be built only after the scientific paper itself has been completed and locked.

The splash page is presentation-layer material and must not drive manuscript structure, mathematical content, pagination decisions, or claim language during the build.

```text
SPLASH_PAGE = REQUIRED
SPLASH_PAGE_BUILD = AFTER_PAPER_LOCK
SPLASH_PAGE_BEFORE_PAPER_LOCK = PROHIBITED
```

### 3. Dedicated formula page

The paper must contain a dedicated formula page presenting the principal governing formula or formula set as a standalone scientific reference surface.

This page is part of the paper body, not the later splash page.

```text
DEDICATED_FORMULA_PAGE = REQUIRED
FORMULA_PAGE_ROLE = CANONICAL_EQUATION_REFERENCE
FORMULA_PAGE_STATUS = PART_OF_PAPER_BODY
```

### 4. Graphic placeholders

During manuscript construction, every planned graphic location must be represented by an explicit placeholder rather than by a provisional embedded graphic.

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
FINAL_GRAPHIC_INSERTION = AFTER_TEXT_AND_STRUCTURE_STABILIZE
PLACEHOLDER_CROSS_REFERENCES = REQUIRED
```

### 5. Reviewer Reward / Interactive Sandbox

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

Its visual language may share the paper's notation and figure vocabulary, but interaction design should prioritize clarity, tactile exploration, and auditability over ornament.

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

A dedicated figure placeholder should be reserved for this closed-versus-open map unless a superior presentation is developed before paper lock.

```text
CLOSED_VS_OPEN_MAP = REQUIRED
OPEN_OBLIGATIONS_VISIBLE_NEAR_CORE_RESULT = REQUIRED
```

## Construction order

```text
1. Establish manuscript section hierarchy
2. Establish explicit review hierarchy and artifact-role taxonomy
3. Build table of contents framework
4. Build terminology boundary table
5. Build dedicated formula page
6. Build scientific body text and equations
7. Build claim-to-source map
8. Insert explicit graphic placeholders, including closed-versus-open map placeholder
9. Define Reviewer's Bench interaction contract and data model
10. Synchronize paper notation and Bench notation
11. Define negative-control presentation and reviewer walkthrough
12. Resolve section references, figure references, captions, formula identifiers, and pagination dependencies
13. Complete technical review and claim-boundary audit
14. LOCK SCIENTIFIC PAPER
15. Build splash page from the locked paper
16. Insert/finalize publication graphics against locked placeholder positions
17. Build/finalize Reviewer's Bench against locked paper semantics
18. Cross-check Bench outputs against archived replay/oracle evidence
19. Build/finalize reviewer walkthrough
20. Perform final visual/pagination, traceability, and companion-artifact audit
21. Export publication artifact and reviewer companion
```

## Lock rule

The scientific paper lock freezes the substantive manuscript structure, equations, claims, section order, formula page, table-of-contents hierarchy, terminology boundaries, claim-to-source map, figure numbering, captions, graphic placement slots, and paper-side notation used by the Reviewer's Bench.

Post-lock splash-page construction, final graphic insertion, reviewer-sandbox presentation work, and walkthrough production may improve presentation but must not silently modify the locked mathematical argument or claim boundary.

```text
PAPER_LOCK_FREEZES_SUBSTANCE = YES
POST_LOCK_SPLASH_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_GRAPHICS_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_SANDBOX_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_WALKTHROUGH_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_CLAIM_PROMOTION = NO
```

## Claim firewall

This build contract governs publication construction only. It does not alter the repository's existing mathematical status.

```text
BOOLEAN_FOLD_IDENTITY = VERIFIED
FINITE_CARRIER_EXISTENTIAL_SEMANTICS = LEAN_VERIFIED
FINITE_PACKAGE_REPLAY = VERIFIED
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_BOUND = OPEN
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

End: `PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_0`
