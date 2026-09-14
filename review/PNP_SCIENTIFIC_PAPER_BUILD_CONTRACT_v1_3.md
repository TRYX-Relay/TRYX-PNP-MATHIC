# Problem No Problem Scientific Paper Build Contract v1.3

Date: `2026-09-13`

Status: `ACTIVE_PAPER_BUILD_CONTRACT`

Supersedes: `PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_2.md`

This contract inherits all v1.2 rules except where explicitly changed below.

## Fixed principal-figure canvas

Every principal scientific-paper figure is designed for the fixed one-third-page portrait slot.

```text
FIGURE_CANVAS_HEIGHT = 3.5_INCHES
FIGURE_CANVAS_WIDTH = 7.0_INCHES
FIGURE_CANVAS = 3.5_IN × 7.0_IN
FIGURE_ORIENTATION = HORIZONTAL_STRIP
ASPECT_RATIO = 2:1
PRINCIPAL_FIGURE_COUNT = 5
```

The artwork itself must be composed to remain legible when placed at exactly 7.0 inches wide by 3.5 inches high in the portrait paper.

```text
FIGURE_1_CANVAS = 3.5_IN × 7.0_IN
FIGURE_2_CANVAS = 3.5_IN × 7.0_IN
FIGURE_3_CANVAS = 3.5_IN × 7.0_IN
FIGURE_4_CANVAS = 3.5_IN × 7.0_IN
FIGURE_5_CANVAS = 3.5_IN × 7.0_IN
```

The existing vertical page budget remains:

```text
MAXIMUM_PAGE_BUDGET = 48 BODY_LINE_EQUIVALENTS
PRINCIPAL_FIGURE_ZONE = 16 BODY_LINE_EQUIVALENTS
MAX_TEXT_ON_FIGURE_PAGE = 32 BODY_LINE_EQUIVALENTS
```

The fixed 3.5 × 7 artwork slot is the controlling canvas. Caption and breathing room must be planned around that slot without shrinking the artwork text below legibility.

## Figure-design prohibitions

```text
FULL_PAGE_INFOGRAPHIC_COMPOSITION = PROHIBITED
TALL_POSTER_COMPOSITION = PROHIBITED
SQUARE_CANVAS_ASSUMPTION = PROHIBITED
STACKED_SECONDARY_SUPPORT_PANELS_REQUIRED_FOR_COMPREHENSION = PROHIBITED
TEXT_SHRINK_TO_FORCE_FIT = PROHIBITED
FIGURE_HEIGHT_ABOVE_3.5_INCHES = PROHIBITED
FIGURE_WIDTH_ABOVE_7.0_INCHES = PROHIBITED
```

A principal figure fails the presentation contract if it is not understandable at the fixed 3.5 × 7 inch placement size.

## Feng Shui additions

Every figure audit must verify:

```text
[ ] artwork canvas is exactly 2:1
[ ] intended paper placement is 7.0 in wide × 3.5 in high
[ ] principal information is readable without zoom
[ ] no support row is required below the main figure to explain it
[ ] caption can sit outside or directly below the artwork without enlarging the artwork slot
[ ] figure remains within its one-third-page visual allocation
```

## Mathematical status

No mathematical status changes in v1.3.

```text
CONVENTIONAL_P_EQUALS_NP = NOT_ESTABLISHED
CLAIM_PROMOTION = NONE
```

End: `PNP_SCIENTIFIC_PAPER_BUILD_CONTRACT_v1_3`
