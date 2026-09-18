# Problem No Problem reproduction walkthrough

1. Open the [approved paper](publications/pnp-mathic/editions/20260918T220300Z/Problem_No_Problem_Paginated.pdf) and identify its finite semantic claim.
2. Inspect the [locked score and governing source](README.md#current-submission).
3. From the repository root, run `python3 publications/pnp-mathic/check_package.py` and retain the output and repository commit.
4. Read the [formal coverage table](submission/VERIFICATION.md), then follow the pinned [Lean instructions](verification/tryx-lean/README.md).
5. Compare initial and intermediate fold states using the independent oracle, and confirm that the OR-to-AND negative control is detected.

This walkthrough is not a prerecorded video. The Python command does not run Lean; semantic closure does not establish a standard-machine polynomial bound.
