# Overworld Stutter Mesen Test Results - 2026-04-30

## Harness

- Emulator: Mesen2 2.1.1, headless `--testRunner`.
- Save state: `F:\Mesen\SaveStates\EarthBound (USA)_1.mss`.
- Baseline ROM: `EarthBound (USA).sfc`.
- Formal fixed baseline: `build/test-runs/baseline-fixed/20260430-125328`.
- Strip-suppressed control: `build/test-runs/strip-suppressed/20260430-125541`.
- Dedupe candidate: `build/test-runs/dedupe-debug-v2/20260430-130058`.
- Scheduler candidate: `build/test-runs/scheduler-debug-v5/20260430-130330`.

Important harness fix: runtime patches must write to the absolute `snesPrgRom`
memory domain returned by `emu.convertAddress(...)`. Writing CPU ROM addresses in
`snesMemory` records patch metadata but does not affect execution.

## Baseline

With the corrected no-collision patch:

- `cardinal_square`: 7134 moved frames, 36 not-moved frames, max no-move run 1.
- `diagonal_square`: 7100 moved frames, 70 not-moved frames, max no-move run 1.
- `alloc_wait_86fa`, `queue_wait_8671`, and `queue_wait_869d`: all zero.
- Diagonal strip pressure is higher than cardinal:
  - cardinal strip frames: 1270
  - diagonal strip frames: 1661
  - cardinal DMA submissions: 13870
  - diagonal DMA submissions: 15260

This supports upload-pressure correlation, not NMI/allocator/queue wait as the
ordinary-walking cause.

## Strip-Suppressed Control

`-SuppressStripUploads` NOPs the six `C0:1558` strip upload call sites:

- `C0:15E7`, `C0:163B` -> `0FCB`
- `C0:16A5`, `C0:16FB` -> `0E16`
- `C0:17C4`, `C0:17D3` -> `1181`

Results:

- `cardinal_square`: 7170 moved, 0 not-moved.
- `diagonal_square`: 7170 moved, 0 not-moved.
- `diagonal_square` DMA submissions fell from 15260 to 6391.
- Wait counters stayed zero.

This is not a gameplay fix because it breaks map-edge refresh, but it proves the
upload path can account for the isolated one-frame misses in the closed-loop
tests.

## Candidate Results

### Dedupe Debug V2

Rebuilt from `asm/overworld_stutter_dedupe_debug_v2_asar.asm` onto a clean,
expanded baserom with `tools/build_overworld_candidate_rom.ps1`.

Result: reject.

- `diagonal_square`: 7092 moved, 78 not-moved.
- Baseline was 7100 moved, 70 not-moved.
- DMA submissions barely changed: 15260 -> 15250.
- No queue/allocator waits, but no improvement.

### Scheduler Debug V5

Rebuilt from `asm/overworld_stutter_scheduler_debug_v5_asar.asm`.

Result: reject.

- `diagonal_square`: 3059 moved, 4111 not-moved.
- `queue_wait_8671` became nonzero and enormous.
- Cardinal movement regressed badly too.

## Current Direction

The next source candidate should not suppress uploads entirely, and simple
payload dedupe is insufficient. A better source-level direction is to preserve
visual correctness while reducing same-frame DMA pressure from `C0:1558`, likely
by batching/scheduling strip uploads with queue-capacity awareness, then proving:

- zero `86FA`, `8671`, and `869D` waits;
- diagonal moved-frame count improves over 7100;
- cardinal movement does not regress;
- strip refresh totals remain plausible rather than zero.

## Follow-Up: Strong No-Collision And Tick-Miss Signal

The original `-NoCollision` patch only bypassed the final rejection branch at
`C0:46D3`. A stronger test-only mode now also clears the main collision probe
and avoids fallback-direction recalculation:

- `C0:460B`: `JSL $C05B7B` -> `LDA #$0000; NOP`
- `C0:4616`: `BEQ` -> `BRA`
- `C0:466E`: `JSR $5FD1` -> `LDA #$0000`

This showed that raw moved/not-moved frame counts are noisy. Some no-move frames
are normal fixed-point cadence: the active movement path runs, coordinates do
not change that frame, and the next frame catches up with a larger delta.

The better lag signal is now:

- active frames where `C0:5200` did not execute;
- active frames where `C0:449B` did not execute;
- queue/allocator waits, which remain zero in vanilla walking.

Strong no-collision baseline:

- `baseline-strong-nocollision/20260430-143214`
- `diagonal_square`: 7130 moved, 40 visible no-move, 5 no-move without tick.
- `cardinal_square`: 7139 moved, 31 visible no-move, 0 no-move without tick.

Strong no-collision strip suppression:

- `strip-suppressed-strong-nocollision/20260430-143456`
- `diagonal_square`: 7170 moved, 0 no-move, 0 tick/input misses.
- `cardinal_square`: 7170 moved, 0 no-move, 0 tick/input misses.

Dedupe v2 under strong no-collision:

- `dedupe-debug-v2-strong-nocollision/20260430-143804`
- `diagonal_square`: worsened to 7117 moved, 53 visible no-move, 18 no-move
  without tick.

Updated conclusion: the upload path is still implicated, but the candidate
acceptance metric should prioritize tick/input-step misses over raw no-move
frames.

## Follow-Up: Axis-Isolated Strip Suppression

The harness now supports `-SuppressStripMode horizontal|vertical|aux|primary|all`.

Under strong no-collision:

### Suppress Horizontal Only

- Run: `suppress-horizontal-strong-nocollision/20260430-144345`
- `diagonal_square`: 7170 moved, 0 no-move, 0 active tickless frames.
- `cardinal_square`: 7132 moved, 38 no-move, 38 active tickless frames.
- Interpretation: horizontal suppression helps the diagonal route but regresses
  cardinal movement, so it is not a good isolated source-fix target.

### Suppress Vertical Only

- Run: `suppress-vertical-strong-nocollision/20260430-144611`
- `diagonal_square`: 7167 moved, 3 no-move, 0 active tickless frames.
- `cardinal_square`: 7142 moved, 28 no-move, 0 active tickless frames.
- Interpretation: vertical suppression eliminates true tick/input-step misses in
  both primary movement routes while preserving horizontal uploads.

Current best source-level hypothesis: do not suppress strips permanently, but
make the vertical `C0:0E16` upload family deferrable or queue-aware so its DMA
work can be serviced outside the overloaded frame while keeping the map edge
visually correct.

## Follow-Up: Vertical Deferral Candidates

### Vertical Defer Debug V1

- Patch: `asm/overworld_stutter_vertical_defer_debug_v1_asar.asm`
- ROM: `build/candidate-roms/overworld_stutter_vertical_defer_debug_v1.sfc`
- Run: `vertical-defer-debug-v1-fixed/20260430-150056`

Result: reject.

This candidate deferred a vertical `C0:0E16` upload only when the same
`C0:1558` refresh had already performed horizontal `C0:0FCB` work. The full
matrix showed that this condition almost never catches the real missed-tick
cases.

- `diagonal_square`: 7129 moved, 41 visible no-move, 5 active tickless frames.
- Baseline strong no-collision was 7130 moved, 40 visible no-move, 5 active
  tickless frames.
- `VerticalDeferDeferred`: 1.
- Wait counters stayed zero, but there was no improvement.

Important correction: the first draft of this hook accidentally used a `JSR`
prologue hook at `C0:1558` while replaying long-lived `PHD/PHA` stack entries.
That malformed the stack and effectively suppressed strip work. The fixed
version uses a `JML` trampoline and rejoins at `C0:155C`.

### Vertical Defer All Debug V2

- Patch: `asm/overworld_stutter_vertical_defer_all_debug_v2_asar.asm`
- ROM: `build/candidate-roms/overworld_stutter_vertical_defer_all_debug_v2.sfc`
- Run: `vertical-defer-all-debug-v2/20260430-150602`

Result: promising, but needs visual validation.

This candidate stores every vertical `C0:0E16` request and services it at the
start of the next `C0:1558` refresh. It preserves the vertical strip calls
rather than suppressing them, but it intentionally makes vertical map-edge
updates one refresh late.

- `diagonal_square`: 7167 moved, 3 visible no-move, 0 active tickless frames.
- Strong baseline: 7130 moved, 40 visible no-move, 5 active tickless frames.
- `cardinal_square`: 7142 moved, 28 visible no-move, 0 active tickless frames.
- Strong cardinal baseline: 7139 moved, 31 visible no-move, 0 active tickless
  frames.
- Wait counters stayed zero: `86FA=0`, `8671=0`, `869D=0`.
- `diagonal_square` DMA pressure improved:
  - `SubmitDmaTotal`: 15398 -> 14350.
  - `MaxQueuePending`: 1792 -> 1280.
- Strip calls remain plausible rather than zero:
  - `VerticalStripTotal`: 896.
  - `HorizontalStripTotal`: 822.
- Deferral telemetry:
  - `VerticalDeferDeferred`: 896.
  - `VerticalDeferServed`: 896.
  - `VerticalDeferPending`: 0.

Current interpretation: timing-shifting the vertical strip family is enough to
remove the true diagonal tick misses in this route without introducing queue or
allocator waits. The risk is visual correctness: the next check should compare
screenshots/video near vertical map-edge updates and test more overworld
locations before treating this as a gameplay-safe source fix.

## Follow-Up: First Visual Probe For V2

The trace harness now supports optional screenshot capture:

- `tools/run_mesen_overworld_trace.ps1 -ScreenshotDir ... -ScreenshotFrames ...`
- Comparison helper: `tools/compare_mesen_visual_frames.ps1`

Probe:

- Baseline trace/screens:
  `build/visual-probes/vertical-defer-v2-seq/baseline/`
- V2 trace/screens:
  `build/visual-probes/vertical-defer-v2-seq/candidate/`
- Diff CSV:
  `build/visual-probes/vertical-defer-v2-seq/frame-diff.csv`
- Contact sheets:
  `build/visual-probes/vertical-defer-v2-seq/sheets/`

Important testing note: do not run paired Mesen screenshot captures in parallel.
Even though trace runs are fine, parallel screenshot capture produced misleading
palette output in the first visual probe. The sequential run is the one to use.

Initial visual result:

- Critical early deferral/service frames were exact PNG matches:
  - frame 82: baseline immediate vertical upload vs V2 deferred request.
  - frame 83: V2 serviced the pending vertical upload.
  - frame 90: second immediate-vs-deferred vertical upload.
  - frame 91: V2 service frame while baseline hit a missed tick.
- No obvious blank strip, wrong tile column/row, or map-edge tear was visible in
  the contact sheet for frames 82-92.
- Raw full-frame pixel diff is not a reliable pass/fail metric once timing
  diverges. Some same-coordinate frames differ by palette/update phase even
  where no visible map-edge corruption is apparent.

Current visual conclusion: V2 has passed the first targeted screenshot sanity
check at the earliest vertical defer/service moments, but this is not enough to
call it gameplay-safe. The next visual pass should capture more route windows,
preferably from additional save states/locations with stronger vertical tile
contrast at the screen edge.

## Follow-Up: Apparent Smoothness Is A Separate Signal

Manual testing reported that the candidate ROM still has less-than-fluid
scrolling in places, including the post-naming Onett intro pan. This is
plausible and is not contradicted by the zero tick-miss result.

New analyzer:

- `tools/analyze_mesen_scroll_cadence.ps1`

The analyzer separates actual missed game ticks from camera/scroll cadence:

- Baseline strong diagonal route:
  - `ZeroScrollFrames`: 44.
  - `NonUnitScrollFrames`: 41.
  - scroll delta `2,-2`/`2,2`: 41 frames.
  - `JerkAbsStats.average`: 0.1933.
- V2 diagonal route:
  - `ZeroScrollFrames`: 3.
  - `NonUnitScrollFrames`: 3.
  - scroll delta `2,-2`: 3 frames.
  - `JerkAbsStats.average`: 0.1492.

Interpretation: V2 removes the major catch-up scroll bursts in the formal
diagonal route, but it does not and cannot make every visual pan perceptually
smooth. There are still normal cadence changes from integer-pixel scrolling,
direction changes, and fixed-point-to-integer projection.

Intro-specific source note:

- The intro/credits-style command stream is driven by
  `src/c0/c0_f41e_frame_callback_process_command_stream.asm`.
- At `C0:F89A..C0:F8BD`, `CREDITS_SCROLL_POSITION` (`$B4EB/$B4ED`) is advanced
  by `#$4000` per frame and the integer high word is published into `$003B`.
- `$003B` is one of the runtime scroll shadows copied into NMI commit buffers by
  `C0:8B20` and is also written directly to PPU register `$2112` by `C0:AD9F`.

That means the intro pan can have an inherent fractional-scroll cadence: the
camera state advances every frame, but the visible SNES BG scroll register can
only move in whole pixels. A sub-1-pixel-per-frame pan therefore displays as
repeated pixels followed by a one-pixel step. This can look like stutter even
without CPU lag or missed logic ticks.

Current conclusion: the vertical deferral candidate addresses one real workload
stutter source in ordinary diagonal overworld scrolling. The intro smoothness
complaint appears to involve a different class of issue: perceptual cadence from
integer BG scroll and scripted fractional camera speed. It should be measured
with a save state at or just before the Onett flyover if we want hard emulator
trace data for that exact scene.

### Intro Flyover Save State Probe

State:

- `F:\Mesen\SaveStates\overworld_stutter_vertical_defer_all_debug_v2_1.mss`

Runs:

- V2 candidate:
  `build/intro-probes/v2-state1/candidate_neutral/trace.jsonl`
- Baseline ROM using the same state:
  `build/intro-probes/v2-state1/baseline_neutral/trace.jsonl`

The state successfully starts near the Onett flyover. This scene does not use
the earlier suspected `C0:F41E` command-stream scroll path; both
`intro_scroll_f41e` and `intro_scroll_commit_ad9f` stayed zero. It uses the
normal overworld tick/refresh path:

- V2 trace: `tick_5200=920`, `refresh_1558=910`.
- Baseline trace: `tick_5200=516`, `refresh_1558=510` in the shorter run.

Stable visible pan window, frames 90-850:

- Baseline and V2 have the same visible scroll cadence.
- Histogram for both:
  - `0,0`: 459 frames.
  - `-1,-1`: 302 frames.

Example cadence:

- frames 90-92: `-1,-1`
- frame 93: `0,0`
- frames 94-95: `-1,-1`
- frame 96: `0,0`
- frames 97-98: `-1,-1`
- frame 99: `0,0`

There are no queue waits or allocator waits in this window, and every sampled
frame has `tick_5200=1`/`refresh_1558=1`. The apparent unevenness is therefore
not CPU lag and is not caused by the vertical-deferral candidate. It is the
expected whole-pixel projection of a scripted subpixel pan: roughly three
one-pixel diagonal moves across every four frames, with regular repeated
screen positions.

### Intro Whole-Pixel Vector Experiment

Rejected output-forcing attempts:

- V3/V4 forced final scroll target deltas in `C0:1558`. Both produced positive
  correction frames (`+1,+1`/`+2,+2`) because the scripted movement source still
  advanced at the original fractional speed.
- V5/V6 tried to fill held integer player-coordinate frames after movement in
  `C0:4C45`. V5 had an init-width bug; V6 still produced `+1,+1` correction
  frames. Conclusion: do not patch the visible result independently of the
  movement source.

Source-level experiment:

- `asm/overworld_stutter_vertical_defer_all_intro_velocity_debug_v7_asar.asm`
- ROM:
  `build/candidate-roms/overworld_stutter_vertical_defer_all_intro_velocity_debug_v7b.sfc`
- Trace:
  `build/intro-probes/v2-state1/intro_velocity_v7b_screens/trace.jsonl`

This version keeps the V2 vertical-strip deferral, then hooks the script
movement-vector store tail at `C0:CA33`. For the observed flyover direction-7
vector only, it changes the computed active-slot velocity from
`low=$4AFB, high=$FFFF` on both axes (`~-0.707 px/frame`) to
`low=$0000, high=$FFFF` on both axes (`-1.0 px/frame`).

Measured active pan window, frames 90-515:

- Scroll delta histogram:
  - `-1,-1`: 425 frames.
- No `0,0` hold frames.
- No positive correction frames.
- Queue/allocator waits: zero.

Important caveat: this is a perception experiment, not a final design. The
flyover completes substantially earlier because the route is now faster. A real
source fix would either retime the script duration/path to preserve composition
or choose a different rational cadence/speed that looks better without changing
the scene length as dramatically.
