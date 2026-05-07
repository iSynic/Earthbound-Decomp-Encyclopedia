# Overworld Walking Stutter Producer Split (`C0:1558`, `C0:1CA8`, `C0:1E49`, `C0:A4C4/A794`, `C0:255C/25CF/2A6B/2B55`)

This note is a focused decomp investigation for the remaining overworld walking microstutter, especially the still-visible diagonal-scrolling hitch after the safe strip-dedupe patch.

See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).
See also [overworld-stutter-current-truth-state.md](notes/overworld-stutter-current-truth-state.md).
See also [bank-c0-entry-notes.md](notes/bank-c0-entry-notes.md).
See also [mushroomized-walking-builders-34de-37d0.md](notes/mushroomized-walking-builders-34de-37d0.md).
See also [secondary-visual-descriptor-c42b0d.md](notes/secondary-visual-descriptor-c42b0d.md).

## Main result

The remaining overworld stutter is no longer best modeled as "just the known strip-upload family at `0E16/0FCB`."

The strongest current local split is now:

- one movement-refresh family really does upload the known map or strip bands in the `38xx/3Cxx/58xx/5Cxx` range
- a second movement-adjacent companion family runs under the same `C0:1558` controller, funnels through `C0:2A50 -> C0:2957 -> C0:1E49`, and seeds per-entry visual tile bases in the `0x4000+` VRAM band
- that companion lane then reaches the queue in two ways:
  - a narrow direct uploader at `C0:1CA8..1D37`, which locally proves `0x4000 + offset` and `0x4100 + offset`
  - a broader descriptor-emission family at `C0:A4C4` and `C0:A794`, which read the seeded `$298E` tile-base field back into `$0097` and queue DMA descriptors through `C0:A56E -> C0:8643 -> C0:8677`
- inside that broader family, `A794` is now the stronger walking-time amplifier because it supports per-entry phase or variant bias through `$10F2`, is periodically retriggered by the `C0:A6E3..A753` watcher even when the base composite state has not changed, and therefore looks like a real residual producer after the safe strip-dedupe patch

That gives a stronger explanation for the observed transfer families:

- `58xx/5Cxx` = the known strip/tilemap refresh family
- `4040/4120/42A0` = the companion visual/entity family seeded by `C0:1E49` and later consumed by `C0:1CA8` plus `C0:A4C4/A794`

So the remaining microstutter now looks more like cumulative legitimate queue pressure from two cooperating producer families than a single missed dedupe opportunity.

## Locally proved

### `C0:1558` has two movement sublanes, and diagonal movement naturally activates both

The controller around `C0:1558` splits into:

- horizontal-side work through `C0:0BDC`, `C0:0D7E`, `C0:0FCB`, `C0:25CF`, `C0:2B55`
- vertical-side work through `C0:0AC5`, `C0:0CF3`, `C0:0E16`, `C0:255C`, `C0:2A6B`

That means diagonal scrolling is structurally the worst case: both axis lanes can contribute work in the same overall movement-refresh cycle.

### `C0:0E16` and `C0:0FCB` are the known strip-upload family

The current local read is still healthy:

- `C0:0E16` allocates scratch, builds strip payloads, and calls `C0:8616` with `0x40`-byte transfers into paired tilemap bands including `0x3800/0x3C00/0x5800/0x5C00`
- `C0:0FCB` is the sibling path for the other axis and does the same kind of `0x40`-byte queued strip copies
- the helper [summarize_transfer_to_vram_callers.py](tools/summarize_transfer_to_vram_callers.py) cleanly clusters those callers around nearby `ADC #$3800/#$3C00/#$5800/#$5C00`

So the observed `58xx/5Cxx` family still belongs to the known strip path.

### `C0:255C/25CF/2A6B/2B55` are real movement-adjacent companion producers, not cosmetic no-ops

These routines are called directly from the two `C0:1558` movement lanes and are strongly gated by movement or visibility state such as `$4A58/$4A5A`, alignment checks, and geometry-profile tests.

They do not directly call `C0:8616` themselves.

Instead, they feed a shared worker cluster:

- `C0:2A50` dispatches a small script or descriptor stream
- `C0:28E7/2957` consume those entries
- `C0:2957` calls `C0:1E49` to instantiate or refresh entity-like records and then writes active-slot state into `$0B8E/$0BCA/$2C9A/$2D12/$2D4E/$3186`
- `C0:2547` locally proves that this family also seeds per-entry mode or variant byte `$2AF6`

So the companion family is a real second producer lane under walking refresh, but its output is one step removed from direct VRAM copies.

### `C0:1E49` seeds the unknown `0x4000+` VRAM family through `$298E`

`C0:1E49` is already the strongest local fit for the sprite-pose-driven entity initializer. A useful local anchor is that it writes a per-entry word through:

- `LDA C4:2F8C,X`
- `ADC #$4000`
- `STA $298E,Y`

The source table at `C4:2F8C` is a simple tile-base ladder and directly supports values like:

- `0x4040`
- `0x4120`
- `0x42A0`

which is a very strong local match for the unexplained VRAM destinations seen at `C0:8677`.

### `C0:1CA8..1D37` directly uploads into the `0x4000` and `0x4100` bands

The helper loop at `C0:1CA8` computes a transfer size in `$02`, points at source data rooted at `C4:0BE8`, looks up a tile-base offset from `C4:2F8C`, and then issues `TRANSFER_TO_VRAM` calls with the destination set to:

- `[$0A] + 0x4000`
- `[$0A] + 0x4100`

The mixed-width decode plus the helper summary make those additions explicit.

This does not fully prove the exact `0x4200` leg yet, but it makes the `4040/4120` part of the sampled family locally real and strongly supports the same-family reading for `42A0`.

### `C0:A4C4` and `C0:A794` are the broader companion descriptor producers

This is the biggest refinement from the deeper pass.

Both routines do the same high-level setup:

- load width-like value from `$2A7E,Y` into `$0092`
- load seeded tile-base value from `$298E,Y` into `$0097`
- load a descriptor-stream base from `$29CA/Y`-relative state
- inspect per-entry control word `$2BAA`
- feed `C0:A56E`, which in turn calls `C0:8643`

Important split:

- `C0:A4C4` uses variant table `DATA_C0A60B` and the base descriptor pointer at `$29CA`
- `C0:A794` uses variant table `DATA_C0A623` and adds extra per-entry bias from `$10F2,Y` before reading the descriptor stream

So the `40xx` family is not just one tiny uploader at `1CA8`; it has a larger descriptor-production side too.

One useful refinement from the legacy cross-check is that `A4C4` is not totally separate from the same phase family. Wrapper `C0:A48F` loads `$10F2,Y` into `$2892` and then calls `A4C4`, so the simpler producer can still inherit the current phase offset through its wrapper path even though the core routine itself only reads `$2892`.

### `$2892`, `$2896`, and `$10F2` now have a cleaner local role split

This is the clearest new payoff from the second deep pass.

`$2892`:

- is read only by `C0:A4C4`
- is written by small front-end wrappers like `C0:A443`, `C0:A48F`, `C0:A4A8`, `C0:A4B2`, and `C0:AA87`
- behaves like a temporary selector or small offset into the descriptor row consumed by `A4C4`

`$2896`:

- is read only by `C0:A794`
- is written by wrappers like `C0:A6E5`, `C0:A78C`, `C0:AAA5`, and `C0:AAAE`
- behaves as the active entry selector for the `A794` producer path

`$10F2`:

- is consumed only by `C0:A794` inside this lane, where it adds a per-entry bias to the descriptor pointer before queuing
- is seeded by wrappers like `C0:AA84` or `C0:AAA2`
- is toggled by `C0:A6E3..A753` through `EOR #$0002`

So the healthiest current local read is:

- `A4C4` = simpler selector-driven descriptor producer
- `A794` = active-entry, phase-biased descriptor producer
- `$10F2` = small per-entry phase or variant offset used by `A794`

### `C0:A6E3..A753` is a real periodic retrigger path for `A794`

`C0:A6E3..A753` is now one of the most useful local anchors in the whole stutter seam.

Current locally proved behavior:

- caches a composite state from `$2C22` high byte plus `$2AF6`
- if that composite state changes, immediately reruns `A794`
- if it does not change, a timer path through `$0ED6/$0F12` can still fire
- when that timer fires, it toggles `$10F2 ^= 2` and reruns `A794`

That means `A794` is not only a movement-change producer. It is also a small periodic phase-refresh producer.

This makes it the strongest current candidate for "legitimate companion work that is still happening often enough to matter" after the safe strip dedupe.

### `$341A` is now a real descriptor-header cache, not just anonymous scratch

Both descriptor producers write a raw descriptor header word into `$341A,Y` before starting the main `A56E` loop:

- `A4C4` stores `[$02]`, then masks it with `#FFF0` for the first transfer base
- `A794` stores `[$02]`, then masks it with `#FFFE` for the first transfer base

There is also one direct reader at `C0:A3A4`, which tests bit `0` of `$341A,X` and conditionally biases `$8C` by `$2916,X` before continuing into the later queue and renderer path. So `$341A` is not throwaway scratch; it is a live cached descriptor-header field already used by the surrounding companion-display machinery.

That matters for patch design, because it makes a future "derived descriptor unchanged" gate feel healthier than a blind VRAM-destination-only gate. The engine is already caching a word from the derived stream.

### The core descriptor-stream fields are seeded at init/setup, not rebuilt from scratch every walking frame

The writer side is much healthier now.

`C0:1F90..2019` and `C0:7A90..7ACC` seed the key fields consumed later by `A4C4/A794`:

- `$298E` = tile-base field from `C4:2F8C + #$4000`
- `$2A7E` = width-like transfer size field
- `$2ABA` = transfer-count field
- `$2A42` = source bank byte
- `$2A06/$29CA` = descriptor-stream source pointer pair
- `$2C22` = high-byte state that later participates in the cached composite signature at `$3456`

That means the later walking-time producer paths are mostly consuming already-instantiated descriptor state rather than rebuilding it from first principles every frame.

This is good news for patch safety: the eventual `A794` or `A4C4` gate can key off stable per-entry initialized data plus a small set of dynamic fields, instead of trying to infer meaning from the generic DMA wrapper.

### `$0F12/$0ED6` now look like a real cadence pair, not generic scratch

`A6E3` already proved the behavioral role:

- `$0ED6` = active countdown
- `$0F12` = reload value

The writer side now makes that healthier:

- `C0:936C/9372` seed both fields from per-profile setup words at `$0A3C/$0A3E`
- broader reset paths like `C0:76B7` and `C0:76F6` mass-seed `$0F12` with small constants `8` and `5`

So the strongest current local read is that the `A794` phase-refresh traffic is driven by a real per-entry cadence system, not an ad hoc incidental timer.

That makes a second patch idea look more realistic than before:

- instead of fully suppressing `A794`, a patch could selectively reduce or defer timer-driven phase refresh cadence during ordinary walking while leaving movement-change refreshes intact

### The derived `A794` queue signature is now narrow enough to describe explicitly

`A794` itself does not queue arbitrary state. By the time it reaches `A56E`, the queued output is determined by a small derived tuple.

Direct local proof:

- `8643/865F` append four queue words: `$0091`, `$0092`, `$0094`, `$0096`, `$0097`
- `A56E` is deterministic from the initial `$0092/$0094/$0097` and only splits when the page-cross test triggers
- `A794` seeds those fields from a narrow set of inputs:
  - `$00 = $2ABA,Y` transfer-count
  - `$0092 = $2A7E,Y` transfer-size
  - `$0097 = $298E,Y` VRAM destination base
  - descriptor stream pointer `[$29CA,Y + 4*DATA_C0A623[$2AF6,Y] + $10F2,Y]`
  - raw descriptor header `[$02]`
  - `$0096 = $2A42,Y` source bank for the main loop
  - optional auxiliary prepasses gated by raw-header bit `1` clear plus `$2BAA` bits `3` and `2`, using fixed source bank `C4` and source base `C40BE8`

So the smallest patch-relevant derived signature before the main queue emission is approximately:

- transfer count `$2ABA`
- transfer size `$2A7E`
- VRAM base `$298E`
- source bank `$2A42`
- raw descriptor header `[$02]` or the cached copy at `$341A`
- effective descriptor-stream selector from `$29CA + 4*DATA_C0A623[$2AF6] + $10F2`
- auxiliary-prepass enable state from raw-header bit `1` and `$2BAA` bits `3/2`

That is much tighter than the earlier vague "companion lane somehow queues extra VRAM" model.

Practical patch implication:

- a safe `A794` gate probably does not need to compare every live companion field
- it only needs to compare the derived descriptor signature that determines the emitted `8643` descriptors
- the existing `$341A` cache is the strongest local foothold for that kind of comparison
- but `$341A + $10F2` alone is not yet a safe full proxy, because the queued output can still change through other live inputs such as `$2BAA` prepass bits, transfer count `$2ABA`, transfer size `$2A7E`, source bank `$2A42`, and the base descriptor source at `$29CA`

### `C0:A56E` can split one logical companion update into two queued descriptors

`C0:A56E` is the local bridge from the companion producer family into the queue.

Current locally proved behavior:

- it reads size-like word `$0092`
- it reads VRAM destination word `$0097`
- it tests whether the current transfer crosses a `0x0100` page boundary in VRAM destination space
- if no crossing occurs, it emits one `C0:8643` descriptor
- if a crossing occurs, it emits two `C0:8643` descriptors, adjusting `$0092/$0094/$0097` around the split

That matters for stutter: a single companion visual update can become two queued transfers when the destination crosses a page boundary.

### `C0:8643` reaches the same queue append point as `C0:8616`

`C0:8643` is not a separate sink. It is another wrapper over `C0:865F`, and therefore reaches the same queue append point at `C0:8677`.

The helper confirms that in bank `C0`, direct `C0:8643` callers are very sparse:

- `C0:A59B / A5BC / A5CE` from the `A56E` companion-split family
- `C0:85E4 / 860C` from the generic large-transfer helper around `85C0`

So the `40xx` companion traffic seen at `8677` is very plausibly coming through `C0:A56E -> C0:8643`, not only through direct `C0:8616` callers.

### `C0:1181` is still a separate strip-family pressure source

The calls at `C0:17C4` and `C0:17D3` show that `C0:1181` also participates in walking refresh around the same broader controller neighborhood. It allocates `0x40`-byte chunks and issues more `TRANSFER_TO_VRAM` calls into the same overworld strip bands rooted at `0x3800` and `0x5800`.

So even after the safe strip-dedupe patch, the strip family likely still contributes meaningful queue pressure during heavy walking states.

## Ref-backed and locally consistent

### The companion family is likely an entity or overlay visual-maintenance lane, not a second tilemap-strip builder

The broader bank-`C0` notes already had `C0:1E49` as the core entity initializer and `C0:2140` as the matching free path. The new walking-side and producer-side bridges line up with that model very well:

- walking-side companion producers instantiate or refresh transient entity-like records
- those records carry tile-base, frame, width, and descriptor-stream state in fields like `$298E/$2A7E/$29CA/$2AF6/$2BAA`
- later helpers `A4C4/A794/A56E` turn that state into queued VRAM descriptors

So the best current ref-backed and locally consistent label is: a movement-adjacent companion visual layer, probably overlay/pose/entity oriented rather than tilemap-strip oriented.

### `C0:A56E` is shared enough that it is a bad first patch target

`C0:A56E` is also called from `C4:29D3`, and `C0:8643` itself is used by other subsystems such as the already-mapped landing-display path.

So even though `A56E` is central to the companion queue behavior, it is not a safe first ROM-patch seam.

That pushes the safest patch targets outward toward `A4C4/A794` and `1CA8`, not inward toward `A56E/8643`.

### `A794` is now a better patch target than `A4C4`

This ranking is now stronger than it was earlier in the investigation.

`A4C4` is still a good upstream target, but the deeper pass made `A794` look better:

- `A794` is directly tied to `$2896`, `$10F2`, and the `A6E3..A753` timer watcher
- `A6E3` can rerun `A794` even when the base composite signature in `$3456` has not changed
- `A4C4` is simpler and still worth targeting, but it looks more like the static selector-driven sibling than the timer-amplified residual producer

So the current safest patch ranking is:

1. `C0:A794`
2. `C0:A4C4`
3. `C0:1CA8..1D37`

One more reason this ranking is stronger now: direct call shape is sparse and clean.

- `A794` has only five direct local `JSR` sites: `A6F7`, `A750`, `A78F`, `AAA8`, `AAB1`
- `A4C4` has only two direct local `JSL` sites: `A4A2` and `AA8B`

So both are much narrower than the shared queue core, and `A794` in particular has a compact caller family that is realistic to instrument or patch safely.

## Still uncertain

### Exact `0x4200` proof

The current local proof explicitly reaches:

- `0x4000 + offset`
- `0x4100 + offset`

The sampled `42A0` destination is strongly consistent with the same table-driven family, but the exact third-band instruction path has not yet been pinned in the same direct way.

### Exact player-facing identity of the companion visuals

The current best read is "entity/overlay/sprite-pose companion visuals spawned or refreshed during movement." That is structurally strong, but the exact human-facing label is still one step softer than the strip family.

### Which exact companion callers rise specifically on diagonal movement

The safest current statement is still structural:

- diagonal movement activates both axis lanes under `C0:1558`
- those lanes feed both the strip family and the companion family

But I have not yet locally pinned which exact `A4C4` versus `A794` caller mix rises specifically during diagonal walking.

### Whether the remaining hitch is entirely queue-byte pressure

The earlier breakpoint result still matters:

- the queue-overflow spin loop at `C0:8671..8673` did not trigger during visible stutter on the safe-v2 ROM

So the current best model is not literal overflow wait.

The strongest current explanation is:

- the hitch is more likely cumulative per-frame queue pressure from multiple legitimate updates, especially when strip uploads and companion `0x4000+` companion descriptors both land in the same frame
- the `A56E` page-split behavior may amplify that by turning one companion update into two queue entries
- the `A6E3` timer-driven `A794` retrigger path may further amplify that by producing phase-refresh traffic even when the base composite state has not changed
- a smaller movement/render coordination component may still exist, but it no longer looks like the main explanation

## Answers to the concrete questions

### 1. Strongest local candidates for the `40xx / 41xx / 42xx` VRAM family

Strongest candidates, in order:

1. `C0:A4C4` and `C0:A794`
   - locally proved broader descriptor producers that read `$298E` back into `$0097` and reach `C0:8677` through `A56E -> 8643`
   - within this pair, `A794` is now the stronger residual-stutter candidate because it is phase-biased and timer-retriggered
2. `C0:1CA8..1D37`
   - locally proved direct uploader into `0x4000 + offset` and `0x4100 + offset`
3. `C0:1E49` plus table `C4:2F8C`
   - locally proved seed point for `4040/4120/42A0`
4. movement companion callers `C0:255C / 25CF / 2A6B / 2B55`
   - locally proved upstream producer family that reaches `C0:1E49`

### 2. Are those updates part of the same movement refresh path as `0E16/0FCB`?

Yes, but as a separate companion lane.

Safest current statement:

- `0E16/0FCB` belong to the map-strip/tilemap refresh side
- `255C/25CF/2A6B/2B55 -> 2A50/2957 -> 1E49 -> (1CA8 and A4C4/A794)` belong to a companion visual/entity side
- both sit under the broader walking refresh umbrella, especially around `C0:1558`

So they are part of the same high-level walking refresh path, but not the same producer subfamily.

### 3. Which producers are likely active during diagonal scrolling more than single-axis scrolling?

Strongest current answer:

- both strip uploaders: `C0:0E16` and `C0:0FCB`
- both axis companion families: `C0:255C/2A6B` and `C0:25CF/2B55`
- among the later queue-facing producers, `C0:A794` is now the stronger walking-active candidate because it has live callers in the movement-timer neighborhood `C0:A6E3..A753`, a timer-driven phase toggle through `$10F2`, and explicit wrapper seeding through `C0:AA90..AAB1`

I am still keeping the exact `A4C4` versus `A794` diagonal weight one notch softer than the structural `C0:1558` split.

### 4. Most likely remaining stutter cause

Current ranked read:

1. queue-byte pressure from multiple legitimate updates
   - strongest current fit
2. companion descriptor splitting at `A56E`
   - likely amplifier when `0x0100` boundary crossings occur
3. periodic `A794` phase-refresh traffic through `$10F2`
   - likely secondary amplifier on top of ordinary movement-time companion work
4. movement/render coordination interaction
   - plausible secondary contributor because the movement controller is staged
5. literal queue-overflow spin-wait at `C0:8671`
   - currently downgraded because the breakpoint did not trigger during visible stutter on safe-v2

So the best current model is not "the queue overflowed." It is "too much valid per-frame work is still being queued, especially during diagonal movement, and part of the companion lane can split into extra descriptors or re-fire on phase updates."

### 5. Top 3 safest patch targets

#### 1. `C0:A794`

Safest and most promising single new target.

Within `A794`, the timer-only rerun path from `A6E3` now looks like the best first experiment.

Why:

- it is upstream of the shared `A56E/8643` sink
- it is already inside the companion `0x4000+` family
- it has a locally proved phase-bias input through `$10F2`
- it is the strongest current candidate for repeated companion work that is not strictly necessary every frame

Best patch idea:

- per-entry unchanged-state gate over the fully derived descriptor signature before `A56E`
- or selectively suppress timer-driven phase refreshes when movement is ordinary and the visual result would be unchanged enough to tolerate one-frame lag
- or reduce the timer-driven cadence path from A6E3 while preserving immediate reruns on real composite-state changes

#### 2. `C0:A4C4`

Best simpler upstream gate.

Why:

- narrower than the queue core
- same family as `A794` but simpler, with temporary selector `$2892` instead of per-entry phase bias

Best patch idea:

- per-entry unchanged-state gate before `A56E`

#### 3. `C0:1CA8..1D37`

Best narrow direct-uploader target.

Why:

- much narrower than the generic `C0:8616` sink
- already in the exact unexplained `0x4000+` family
- likely touches transient companion visual uploads rather than all rendering

Best patch idea:

- per-destination dedupe when the `0x4000/0x4100` tile base and source chunk are unchanged

### Patch targets that now look less safe

- `C0:A56E`
- `C0:8643`
- `C0:8616`
- `C0:865F`

These are shared enough that they look too central for a first low-risk patch.

### Strip-family target rank

The strip family is still real, but after this deeper pass it now looks like the fourth-best patch seam rather than the first:

- `C0:0E16 / 0FCB`
- `C0:1181`

## Concrete next-look suggestions

### Highest-value next addresses

- `C0:A794`
  - test a fuller compare set built around `$341A`, `$10F2`, `$2ABA`, `$2A7E`, `$298E`, `$2A42`, and the effective `$29CA/$2AF6` selector, rather than the weaker `$341A + $10F2` shortcut
- `C0:A6E3..A753`
  - treat this as the highest-value low-risk patch seam inside the broader `A794` family, especially the timer-only rerun leg after `$10F2 ^= 2`
- `C0:A4C4`
  - same as `A794`, but for the simpler selector-driven lane
- `C0:AA6E..AAB1`
  - tighten how script-side wrappers seed `$2AF6/$10F2/$2892/$2896` before the two descriptor producers
- `C0:1CA8`
  - prove whether a true third `0x4200+` band exists or whether `42A0` is always a table-driven offset within the broader companion family
- `C0:1181`
  - quantify how much residual strip pressure remains after safe-v2

### Best emulator-sampling follow-up

At `C0:8677`, separate samples by upstream caller family:

- `1CA8/1D15` direct `0x4000/0x4100` uploader
- `A56E -> 8643`, split again by whether the immediate caller was `A4C4` or `A794`
- `0E16/0FCB/1181` strip family

That should tell us quickly whether visible diagonal stutter is dominated by:

- strip uploads
- simpler companion descriptors
- phase-biased companion descriptors
- or frames where several of those land together

## Working Names

- `C0:0AC5` = `Load_VerticalMovementMapStripPayload`
- `C0:0BDC` = `Load_HorizontalMovementMapStripPayload`
- `C0:0CF3` = `Load_VerticalMovementCollisionStripPayload`
- `C0:0D7E` = `Assemble_LandingHdmaParameterBlock`
- `C0:0E16` = `Upload_VerticalMovementMapStrip`
- `C0:0FCB` = `Upload_HorizontalMovementMapStrip`
- `C0:1181` = `Upload_AuxiliaryMovementMapStrip`
- `C0:1558` = `UpdateRuntimeScrollShadowsAndIncrementalRefresh`
- `C0:1CA8` = `Upload_CompanionVisualTiles4000Band`
- `C0:1E49` = `Initialize_EntityWithSpritePose`
- `C0:8616` = `QueueVramTransfer_FromDpSource`
- `C0:8643` = `SubmitQueuedOrImmediateVramTransfer`
- `C0:2547` = `Seed_SpawnCandidateDirectionClass`
- `C0:255C` = `Run_VerticalCompanionSpawnProducer`
- `C0:25CF` = `Run_HorizontalCompanionSpawnProducer`
- `C0:28E7` = `TryPlaceSpawnCandidateFromListEntry`
- `C0:2957` = `InitializeSpawnedCandidateEntitySlot`
- `C0:2A50` = `Iterate_SpawnCandidateList`
- `C0:2A6B` = `Spawn_Horizontal`
- `C0:2B55` = `Spawn_Vertical`
- `C0:A4C4` = `RefreshSlotVisualProfileShared`
- `C0:A56E` = `Generate_RenderDmaStripDescriptors`
- `C0:A6E3` = `WatchAndRefreshCompanionVisualPhase`
- `C0:A794` = `RefreshCompanionVisualProfile_PhaseBiased`
- `C0:AA6E` = `Script_ApplyCurrentSlotVisualCountdownState`

## Source Polish Follow-Up

2026-05-06 source polish names the movement-strip and incremental-refresh call
surface across `C0:0AC5..17EA`. The vertical/horizontal strip payload loaders
now call `C0:A156` through the cached map-property lookup contract, the strip
uploaders name the shared tile-buffer allocator and EF debug overlay row
writers, and the `C0:1181`/`C0:1558` controllers now call the map-strip,
HDMA-parameter, auxiliary-strip, and companion-spawn helpers by their established
working names. The few remaining numeric calls in `C0:1181` are mixed-width
decode artifacts inside the auxiliary uploader body, not newly promoted helper
edges.





