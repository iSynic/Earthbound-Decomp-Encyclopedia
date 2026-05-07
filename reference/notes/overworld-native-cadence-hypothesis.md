# Overworld Native Cadence Hypothesis

This note captures the current best explanation for the remaining ordinary overworld judder after the strip and companion-family patch experiments failed to materially change the feel.

See also [overworld-stutter-current-truth-state.md](notes/overworld-stutter-current-truth-state.md).
See also [position-snapshot-and-movement-tick-c0449b-c05200.md](notes/position-snapshot-and-movement-tick-c0449b-c05200.md).
See also [overworld-timing-scroll-commit-slice-c08b20-c08284.md](notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md).
See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).

## Main result

The healthiest current interpretation is that the visible diagonal judder is mostly native to the ordinary overworld movement or snapshot cadence, not primarily a loading hitch.

This does **not** mean render workload never matters.
It does mean the consistent baseline feel in vanilla looks more like:

- discrete movement advancement
- followed by a healthy downstream camera or scroll path
- with diagonal motion making the step pattern easier to notice

## Why this is now the leading explanation

### 1. The ordinary walking path is now grounded as a tick pipeline

The best current ordinary walking chain is:

1. `C05200_Tick_OverworldPlayerPositionAndCallbacks`
2. `C04C45_Commit_PlayerPositionSnapshotTick`
3. movement body dispatch:
   - `C0449B`
   - `C047CF`
   - `C048D3`
   - `C04B53`
4. `JSL C05F82`
5. `JSL C0400E`
6. `C04010 -> C01558`
7. `C08B20..8B8D`
8. NMI commit at `C08284..82CA`

That structure reads much more like a discrete movement or snapshot tick than a fully continuous camera integrator.

### 2. The downstream camera path looks healthy when it runs

Recent emulator work found:

- orderly `C04010` inputs in the sampled walking path
- smooth writes at `C0156B / C01575`
- healthy publish at `C08B51 / C08B57`
- healthy NMI commit at `C08284`

So the camera and scroll-shadow timing path no longer looks like the main failure point.

### 3. Workload-reduction patches did not materially improve the baseline feel

The visible result stayed broadly the same across:

- vanilla
- `safe-v2`
- `safe-v4`

That makes these theories much weaker as the main explanation for the residual judder:

- redundant strip uploads
- timer-only `A794` reruns
- broader watcher-side `A794` reruns
- stale scroll publish
- queue-overflow spin-wait

### 4. Diagonal motion is the most revealing case

The user-visible behavior matches the cadence model:

- single-axis walking is less objectionable
- diagonal walking is consistently the worst-looking case

That is exactly what we would expect if both X and Y step together inside a discrete pipeline.

## What this does and does not claim

### Strong claim

The ordinary persistent diagonal judder is probably not mainly "the engine cannot keep up."

### Weaker claim

There may still be smaller additive workload hitching in some scenes.

The earlier strip and companion-family work is still useful for understanding those secondary costs.
It is just no longer the healthiest first explanation for the baseline ordinary walking feel.

## Practical implications

If the goal is to make overworld walking look smoother than vanilla, the next patch direction should probably be:

1. visual-only camera interpolation
2. camera plus visible-entity interpolation
3. only after that, more invasive movement-rate changes

The question is no longer:

- "what else can we dedupe?"

It is:

- "how do we smooth the presentation of a discrete movement cadence without breaking gameplay?"

## Bottom line

The strongest current explanation for the remaining overworld judder is native cadence in the ordinary movement or snapshot pipeline, especially visible during diagonal movement.

That shifts future patch work away from VRAM-queue pruning and toward visual smoothing.
