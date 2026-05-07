# Overworld Stutter Current Truth State

This note is the current patch-thread baseline after the later `src/c0` promotion pass and the negative results from the strip-dedupe and `A794` patch experiments.

See also [position-snapshot-and-movement-tick-c0449b-c05200.md](notes/position-snapshot-and-movement-tick-c0449b-c05200.md).
See also [overworld-timing-scroll-commit-slice-c08b20-c08284.md](notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md).
See also [overworld-live-walking-controller-c04c45-c04d33.md](notes/overworld-live-walking-controller-c04c45-c04d33.md).
See also [overworld-native-cadence-hypothesis.md](notes/overworld-native-cadence-hypothesis.md).
See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).

## Main result

The healthiest current read is no longer "one render producer is stalling the game."
It is:

- ordinary overworld walking is driven by a discrete movement or snapshot tick pipeline
- the downstream camera path is behaving cleanly when that pipeline advances
- the residual diagonal judder seen in vanilla, `safe-v2`, and `safe-v4` is therefore more likely native movement or camera cadence than a loading hitch

So the strongest current explanation is:

- we are mostly seeing the game's intended step cadence
- diagonal scrolling makes that cadence more visible because both axes step together
- pixel-art or tile-art aliasing likely amplifies the perception

This does **not** prove that render workload never contributes.
It does mean the earlier strip-first and `A794`-first patch theories are no longer the leading explanation for the consistent baseline judder.

## Locally proved

### The ordinary walking stack is now much better grounded

The `src/c0` promotion pass plus the newer note work gives a healthier live chain for normal walking:

1. `C05200_Tick_OverworldPlayerPositionAndCallbacks`
2. `C04C45_Commit_PlayerPositionSnapshotTick`
3. movement body dispatch:
   - `C0449B_Step_PlayerFromDirectionalInput`
   - `C047CF` scripted step mode
   - `C048D3` bicycle or special step mode
   - `C04B53` temporary movement modes
4. `JSL C05F82`
5. `JSL C0400E`
6. `C04010 -> C01558`
7. `C08B20..8B8D`
8. NMI-side commit at `C08284..82CA`

That is a step or tick pipeline, not a simple "camera integrates every frame independently" model.

### Movement-time camera inputs look orderly when they do advance

The emulator follow-up on `C04010` showed:

- during single-axis movement, `A` changed smoothly while `X` stayed constant
- during diagonal movement, both `A` and `X` changed smoothly in the sampled walking lane

This does not prove the routine fires every visible frame, but it does weaken the idea that the camera math itself is erratic.

### Runtime scroll shadow updates and publish look healthy

The timing slice still holds:

- `C01558` writes runtime shadow words into `$31/$33/...`
- `C08B51 / C08B57` publish those values into the alternating shadow pairs at `$41/$45/...`
- `C08284..82CA` commit those shadow pairs to the real PPU scroll registers during NMI

Recent diagonal-walk traces showed smooth advancement at:

- `C0156B / C01575`
- `C08B51 / C08B57`
- `C08284`

So the "missed movement update" and "missed publish to NMI shadow" theories are now much weaker.

### Strip dedupe and `A794` watcher gates did not materially change the visible result

The practical patch result matters here:

- vanilla
- `EarthBound-overworld-stutter-safe-v2.sfc`
- `EarthBound-overworld-stutter-safe-v4-a794-gate.sfc`

all look broadly similar by eye, with the same small but consistent diagonal judder.

That makes these older theories much weaker as dominant explanations:

- redundant strip uploads
- timer-only `A794` reruns
- broader watcher-side `A794` reruns
- stale scroll publish
- queue-overflow spin-wait at `C08671`

### The old producer-family work is still useful, but now mostly as a negative result

The strip family and companion family notes still look structurally right:

- strip-family traffic in `58xx / 5Axx / 5Bxx / 5Cxx / 5Exx`
- companion-family traffic in `4040 / 4120 / 42A0`

But because the targeted patches did not materially improve the baseline feel, those families no longer look like the main explanation for the ordinary vanilla judder the player consistently notices.

## Decomp-backed and locally consistent

### The current best explanation is native cadence, not backlog

The newer `src/c0` names make the higher-level behavior easier to read:

- `C05200` is an installed overworld tick callback
- `C04C45` is a commit or snapshot front door, not a free-running camera loop
- `C0449B` is the normal accepted-input movement-step body
- `C0400E / C04010` feed the already-smooth camera path after that movement work

That matches the current practical observation:

- the engine appears to move and snapshot on a discrete cadence
- the downstream camera and scroll path behaves correctly inside that cadence
- the eye still catches the cadence, especially on diagonal movement

### Diagonal scrolling is where that cadence is easiest to see

The current model fits the user-visible behavior well:

- single-axis scrolling looks less objectionable
- diagonal scrolling is where the constant small judder is easiest to notice

That is exactly what we would expect if:

- the movement pipeline advances on discrete ticks
- and diagonal motion changes both axes together, making the step pattern easier to see

### Pixel-art presentation probably amplifies the effect

This remains an inference, not a local proof, but it is a healthy one:

- even if the camera path is "working correctly"
- high-contrast pixel edges and tile boundaries can make stepped diagonal motion look rougher than the underlying numbers suggest

## Still uncertain

### Whether some smaller secondary workload hitch still sits on top of the native cadence

The newer conclusion is that native cadence is the best baseline explanation.
It is still possible that some scenes also have smaller additive workload jitter from:

- strip-family uploads
- companion-family updates
- follower or visible-entry refresh

But those now look secondary, not primary.

### Which visual-smoothing patch would be safest

If the goal becomes "make the game look smoother than vanilla," the healthiest next experiments are probably:

- visual-only camera interpolation
- or camera plus visible-entity interpolation

Those are different from the earlier workload-reduction patches and need their own design pass.

## Current best target ranking

### Best explanations

1. native movement or snapshot cadence in the normal overworld tick path
2. diagonal motion making that cadence more visually obvious
3. pixel-art or tile-art aliasing amplifying the perception
4. smaller secondary presentation workload on top, if any

### Best future patch directions

1. visual smoothing or interpolation experiments
2. more direct cadence measurement against NMI frames if we want harder proof
3. only after that, return to producer-family workload patches if a secondary hitch still looks worth chasing

## Practical guidance

The old strip and `A794` notes should now be read as:

- useful negative patch experiments
- useful subsystem mapping
- not the current leading cause model

If this lane stays patch-first, the healthiest next question is no longer:

- "what else can we dedupe or skip?"

It is:

- "can we smooth the presentation of a discrete movement cadence without changing gameplay logic?"

## Bottom line

The strongest current truth state is:

- ordinary overworld walking is driven by a discrete tick pipeline
- the downstream camera and scroll commit path look healthy
- the consistent remaining diagonal judder in vanilla and in the failed patch variants is most likely native cadence, not primarily loading or DMA backlog

That makes future work look more like camera or entity interpolation than queue optimization.
