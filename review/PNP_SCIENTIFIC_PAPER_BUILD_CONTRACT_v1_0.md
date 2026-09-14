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

### 5. Reviewer Interactive Sandbox

Develop a browser-openable interactive companion that allows reviewers to directly exercise the finite PNP mechanism rather than only reading static prose.

The sandbox should expose the reviewable semantic machinery already represented in the repository and make intermediate states inspectable.

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

The sandbox must distinguish demonstration of finite-carrier semantic correctness from the still-open conventional complexity obligations.

```text
INTERACTIVE_REVIEW_SANDBOX = REQUIRED
PRIMARY_MODE = STEP_THROUGH_FINITE_SEMANTICS
INDEPENDENT_ORACLE_COMPARISON = REQUIRED
NEGATIVE_CONTROL = REQUIRED
STANDARD_MACHINE_POLYNOMIAL_RUNTIME_PROOF = NOT_CLAIMED
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
```

The sandbox is a companion review instrument, not a substitute for the manuscript, Lean proof source, replay scripts, or verification receipts.

Preferred delivery form:

```text
REVIEWER_SANDBOX_FORMAT = SELF_CONTAINED_BROWSER_OPENABLE_HTML
REMOTE_SERVICE_DEPENDENCY = NONE_PREFERRED
REPRODUCIBLE_PRESETS = REQUIRED
SOURCE_VISIBLE_IN_REPOSITORY = REQUIRED
```

Its visual language may share the paper's notation and figure vocabulary, but interaction design should prioritize auditability over ornament.

## Construction order

```text
1. Establish manuscript section hierarchy
2. Build table of contents framework
3. Build dedicated formula page
4. Build scientific body text and equations
5. Insert explicit graphic placeholders at intended figure locations
6. Define Reviewer Interactive Sandbox interaction contract and data model
7. Resolve section references, figure references, captions, and pagination dependencies
8. Complete technical review and claim-boundary audit
9. LOCK SCIENTIFIC PAPER
10. Build splash page from the locked paper
11. Insert/finalize publication graphics against locked placeholder positions
12. Build/finalize Reviewer Interactive Sandbox against locked paper semantics
13. Cross-check sandbox outputs against archived replay/oracle evidence
14. Perform final visual/pagination and companion-artifact audit
15. Export publication artifact and reviewer companion
```

## Lock rule

The scientific paper lock freezes the substantive manuscript structure, equations, claims, section order, formula page, table-of-contents hierarchy, figure numbering, captions, and graphic placement slots.

Post-lock splash-page construction, final graphic insertion, and reviewer-sandbox presentation work may improve presentation but must not silently modify the locked mathematical argument or claim boundary.

```text
PAPER_LOCK_FREEZES_SUBSTANCE = YES
POST_LOCK_SPLASH_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_GRAPHICS_MAY_CHANGE_SUBSTANCE = NO
POST_LOCK_SANDBOX_MAY_CHANGE_SUBSTANCE = NO
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
