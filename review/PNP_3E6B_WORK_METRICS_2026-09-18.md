# PNP and 3E6B work-metrics receipt

Recorded: 18 September 2026. Status: retrospective baseline with incomplete active-time coverage.

## Recorded intervals

| Scope | Start | End | Recorded interval | Interpretation |
|---|---|---|---|---|
| Original PNP development | August 4, 2026, approximately 16:11:17 AKDT | August 6, approximately 21:34 AKDT | Approximately 53h 22m 43s | Existing reconstructed build-to-internal/local-closure elapsed span; not active labor |
| E6B → TRI-E6B / 3E6B, first saved build to v64 lock | September 14, 07:31:06.664454 UTC | September 17, 04:30:46 UTC | 68h 59m 39s | Observed artifact-to-lock interval; initial build request not recovered |
| Same instrument lineage, through v65 repair | September 14, 07:31:06.664454 UTC | September 17, 06:55:47 UTC | 71h 24m 40s | Observed delivery window including development, idle time and repairs |
| 3E6B regression recovery episode | September 17 audit response, 04:59:36 UTC | v65 repair commit, 06:55:47 UTC | 1h 56m 11s | One elapsed recovery interval; not total active drift time |
| Later PNP paper production | September 17–18; no measured start/end pair | User report recovered September 18 | 3h 30m | Author-reported lost time, counted once; not added to the original August build clock |

Times rounded to the nearest second where artifact metadata includes fractional seconds. The original PNP endpoint is reconstructed to the minute; second-level subtraction does not establish second-level certainty.

## What counts as drift

Drift is departure from an accepted instruction, source, contract or previously required behavior that creates corrective work. Requested features, intentional redesigns, ordinary aesthetic choices, routine testing, and version increments are not drift counts by themselves.

One September 17 3E6B audit identified six defect areas. Comparing archived v64 and v65 source corroborates repairs in each area:

1. Plain-text rejection: arbitrary pasted input was no longer automatically marked cipher-ready; a matching instrument receipt is required.
2. Keyless Decode direction: forward playback is explicitly selected before starting the trace.
3. Topology placement and control ownership: location and conflicting interface state were corrected.
4. Star reset: selector, decode mode, workspace, direction and topology state are reset together.
5. Paste Crypto visibility: its view binding changed from `clear-message` to `keyless-decode`.
6. Stale receipt parameters: shared receipt clearing was added before stamping and on input changes.

These six areas share one 1h56m11s episode. Do not multiply the interval by six. Detection time is from a retrieved conversation audit; the repair endpoint is GitHub's commit time. This metrics review compared source but did not rerun browser acceptance tests.

The later PNP paper record includes reported content/source omissions, formula-box and layout corrections, voice/quotation compliance, source-version concerns, and duplication of M0–M9 material. Those categories are not separately timed. The author's 3.5-hour report is one recovery-burden estimate, not independent measurements for every category. Repeated reports of that same block are not additional losses.

## Accounting limits

Original PNP development drift remains unmeasured. Total 3E6B drift and active labor for both projects remain unresolved. Unknown means unmeasured, not zero.

Do not add a user-reported labor-loss estimate to a measured elapsed recovery interval as though they were equivalent. Do not divide September paper rework by August research elapsed time to produce a drift percentage. A labor-based drift share requires non-overlapping corrective active minutes and total active minutes for the same phase.

The first saved E6B build establishes that work was already underway, not when it began. The recorded 71-hour window includes the circular codebreaker's triangular successors; it is not a standalone duration for only the triangular version. A repair commit does not establish completion of all project requirements.

Future entries should record project, phase, accepted baseline, deviation, detection time, repair start/end, acceptance time, active corrective minutes, waiting time, evidence and commit/file identity. Keep unavailable numeric values null and classify new scope separately.

## Sources

- [Existing original PNP timing receipt](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/blob/201686788695be2331e3e62d9945e6e9ed5d46c1/review/PNP_ORIGINAL_DEVELOPMENT_TIME.RECEIPT_v1_0.md): original clock, endpoint convention, and separation of elapsed time from active labor.
- Earliest recovered artifact: `PNP_CODEBREAKER_E6B_LOCAL_v0_1.html`, saved `2026-09-14T07:31:06.664454Z`; its stored metadata and HTML title were checked. Artifact identity: `libfile_c226436fe7d08191a76817d01805c8ff`.
- [v64 lock commit](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/commit/90944fec8365486c5e00f6b32d22ea62ba63a4ee), timestamp `2026-09-17T04:30:46Z`.
- [v64 lock receipt](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/blob/90944fec8365486c5e00f6b32d22ea62ba63a4ee/review/PNP_3E6B_XMAS_FORMULA_PAGE_v64.LOCK.RECEIPT.md): distinguishes structural/source checks from later visual acceptance.
- [v65 repair commit](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC/commit/a7c6e551e172553c53176283f11f7e832782a0f1), timestamp `2026-09-17T06:55:47Z`; v64/v65 source comparison.
- Conversation evidence retrieved September 18: September 17 audit at `04:59:36Z`; September 18 author report of 3.5 hours lost, attributed to PNP paper recovery. These are conversation records, not a continuous labor tracker.

This receipt records development history and recovery costs. It changes no mathematical claims, proof sources, or accepted document locks.
