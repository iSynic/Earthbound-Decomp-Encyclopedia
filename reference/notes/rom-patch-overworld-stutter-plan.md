# Overworld Walking Stutter Patch Plan

This note is now the patch-thread planning baseline after the failed strip-dedupe and `A794` gate experiments and the later `src/c0` promotion pass.

See also [overworld-stutter-current-truth-state.md](notes/overworld-stutter-current-truth-state.md).
See also [overworld-native-cadence-hypothesis.md](notes/overworld-native-cadence-hypothesis.md).
See also [position-snapshot-and-movement-tick-c0449b-c05200.md](notes/position-snapshot-and-movement-tick-c0449b-c05200.md).
See also [overworld-timing-scroll-commit-slice-c08b20-c08284.md](notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md).

## Current status

The old patch-first theory was:

- the judder was mainly redundant strip traffic or companion descriptor traffic
- so workload reduction at `0E16 / 0FCB` or `A794` should materially improve the feel

That is no longer the healthiest current read.

Practical result:

- vanilla
- `safe-v2` strip dedupe
- `safe-v4` broader `A794` watcher gate

all look broadly similar by eye, especially for the remaining small, consistent diagonal judder.

So the active patch question has changed from:

- "what more can we dedupe?"

to:

- "how do we smooth a likely native movement or camera cadence without changing gameplay logic?"

## Current best explanation

The strongest current model is:

1. ordinary overworld walking advances through a discrete movement or snapshot tick pipeline
2. the downstream camera and scroll-shadow path behaves correctly when that pipeline advances
3. the remaining visible judder is therefore more likely native cadence than loading backlog
4. diagonal movement makes that cadence easier to notice because both axes step together

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

The practical consequence is:

- the old strip and companion family work still matters as mapping
- but it no longer looks like the main explanation for the ordinary vanilla judder

## Locally proved

### The scroll publish path looks healthy

Recent emulator work and the timing note support:

- `C01558` writes runtime scroll shadows in `$31/$33/...`
- `C08B51 / C08B57` publish those values into the alternating shadow pairs at `$41/$45/...`
- `C08284..82CA` commit those shadow pairs during NMI

That makes these older theories much weaker:

- stale scroll publish
- missed NMI shadow handoff
- ordinary diagonal judder as a simple scroll-commit failure

### The ordinary walking path itself is discrete

The newer `src/c0` naming makes the structure easier to read:

- `C05200` is a real installed overworld tick callback
- `C04C45` is a commit or snapshot front door
- `C0449B` is the normal accepted-input movement-step routine
- `C0400E / C04010` are downstream of that movement work, not the top of it

That is a stronger fit for a step pipeline than for a continuous camera loop.

### Workload-reduction patches did not materially improve the baseline feel

Useful negative results:

- exact strip dedupe at the overworld `C08616` callsites
- timer-only `A794` rerun gate
- broader watcher-side `A794` gate

All were useful experiments, but none materially changed the residual diagonal judder.

### Queue-overflow spin-wait is not the leading explanation

The explicit queue-overflow stall at `C08671..8673` did not become the strongest explanation for the visible baseline judder.

That, together with the failed workload patches, pushes the interpretation away from "the engine cannot keep up" and toward "the engine is stepping on a cadence the eye can see."

## Decomp-backed and locally consistent

### Two producer families are still real, but now secondary

The older work around:

- strip-family traffic in the `58xx / 5Cxx` ranges
- companion-family traffic in the `40xx / 41xx / 42xx` ranges

still looks structurally right.

But the current state says:

- those families are not the best first explanation for the persistent vanilla-like judder
- at most they now look like secondary additive workload, not the baseline cause

### Diagonal motion is where native cadence is easiest to see

The user-visible behavior fits the cadence model well:

- single-axis walking is less objectionable
- diagonal walking is consistently the worst-looking case

That is exactly what we would expect if both axes step together inside a discrete pipeline.

## Historical experiment record

These experiments are still worth keeping on the record:

### `safe-v2`

- exact duplicate strip-upload dedupe at the overworld `C08616` sites
- stable after lazy-init fixes
- no meaningful lasting improvement by eye

### `safe-v3`

- timer-only `A794` rerun gate around the `A723..A750` branch
- safe negative result

### `safe-v4`

- broader watcher-side `A794` gate at `A750`
- safe negative result

### Debug builds

The debug builds were still useful because they ruled out several earlier theories:

- split strip counters
- scheduler counters
- queue-pressure sampling

What survived that process was not "one dominant producer," but the stronger suspicion that the remaining ordinary judder is native to the movement or camera cadence itself.

## Best next patch directions

If we keep patching, the healthiest next patch family is no longer queue optimization.

It is visual smoothing.

### Best current options

1. camera-only visual interpolation
2. camera plus visible-entity interpolation
3. more invasive movement tick-rate changes only if a visual-only patch proves insufficient

### Why visual smoothing is now the right direction

The camera and scroll path look healthy when they advance.
The question is no longer how to make the engine "catch up."
It is how to make a discrete advancement cadence look smoother than vanilla.

That means the best future patch seams are likely near:

- the camera publish side after the previous and current positions are known
- or the visible entity refresh side, if background-only smoothing produces mismatch

## Practical guidance

Use the older notes as:

- subsystem mapping
- negative patch history
- evidence for what is no longer the leading theory

Do **not** use them as proof that:

- more strip dedupe is the best next experiment
- another `A794` gate is the best next experiment

Those are now historical branches, not the current recommendation.

## Bottom line

The patch-thread state is now:

- workload-reduction patches did not materially change the residual judder
- the healthiest current explanation is native overworld movement or snapshot cadence
- future patches should probably aim at visual smoothing or interpolation rather than more VRAM-queue pruning
