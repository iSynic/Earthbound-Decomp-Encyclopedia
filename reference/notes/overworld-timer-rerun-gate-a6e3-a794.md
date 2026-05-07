# Overworld Timer Rerun Gate (`C0:A6E3..A753`, `C0:A794`)

This note captures the safest current patch experiment for the remaining overworld walking microstutter after the strip-dedupe patch.

See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).
See also [overworld-walking-stutter-producer-split-c01558-c01ca8.md](notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md).

## Main result

The safest next experiment is no longer "touch the generic queue core" and no longer "dedupe more strip uploads."

The best current patch seam is the timer-only rerun leg in `C0:A6E3..A753`.

Current strongest local model:

- movement or composite-state changes still deserve the ordinary immediate `A794` rerun
- the timer-only leg at `C0:A723..A750` can rerun `A794` even when the larger descriptor-source fields have not changed
- on that timer-only leg, the most likely redundant work is the companion visual descriptor family in the `0x4000+` VRAM band

So the safest first experiment is:

1. stay inside the timer-only leg only
2. derive the post-toggle `A794` raw descriptor header
3. compare it against the already-cached header at `$341A`
4. if equal, skip the timer-driven `JSR A794`
5. do **not** suppress the earlier movement-change reruns
6. do **not** touch `A56E`, `8643`, `865F`, or `8677`

## Locally proved

### `C0:A6E3..A753` splits movement-change reruns from timer-only reruns

Legacy decode plus local tracing gives the cleanest structure:

- `A6E3..A6F7`: cache composite state from `$2C22` high byte plus `$2AF6`; on change, store into `$3456` and immediately `JSR A794`
- `A6FB..A717`: other control branches that can still fall through to the common `A750` call
- `A717..A750`: timer-only leg
  - skip if `$5D60 != 0`
  - `DEC $0ED6,X`
  - when expired, reload from `$0F12,X`
  - toggle `$10F2,X ^= 2`
  - optionally run the `ABE0` side effect when the new `$10F2` is zero and the same small follow-on conditions pass
  - then fall into the common `JSR A794`

So there is a real, naturally narrow patch seam:

- only the timer-expiry subpath inside `A723..A750`

### `A794` queue output is determined by a narrow derived signature

Direct local proof from `A794 -> A56E -> 8643/865F`:

- transfer count: `$2ABA,Y -> $00`
- transfer size: `$2A7E,Y -> $0092`
- VRAM base: `$298E,Y -> $0097`
- pointer bank seed: `$2A06,Y -> $04`
- effective descriptor selector:
  - `$29CA,Y`
  - `+ 4*DATA_C0A623[$2AF6,Y]`
  - `+ $10F2,Y`
- raw descriptor header: `[$02]`
- source bank: `$2A42,Y -> $0096`
- auxiliary prepasses gated by:
  - raw-header bit `1`
  - `$2BAA` bits `3/2`

### `$341A` already caches the raw descriptor header

`A794` does:

- `LDA [$02]`
- `STA $341A,Y`

before masking the main source base and entering the main `A56E` loop.

So the engine already keeps the exact raw-header word we need for a skip test.

## Decomp-backed and locally consistent

### Why `$341A` alone is sufficient for the first timer-only experiment

This is the key design call.

For the timer-only rerun leg, the broader descriptor-source fields are currently understood to stay unchanged:

- `$2ABA`
- `$2A7E`
- `$298E`
- `$2A42`
- `$29CA`
- `$2AF6`
- `$2BAA`

What the timer leg explicitly changes is:

- `$0ED6` reload from `$0F12`
- `$10F2 ^= 2`

Given that local model, the queued output can only differ through the new effective descriptor selector and therefore the new raw descriptor header.

That makes the minimal first compare tuple:

- current live entry index
- newly derived raw header from the post-toggle selector
- cached previous raw header at `$341A`

Why this is enough for v1:

- transfer count, transfer size, VRAM base, source bank, and prepass-control word are locally consistent as unchanged on this leg
- prepass behavior depends on raw-header bit `1` plus stable `$2BAA` bits `3/2`
- if the raw header is unchanged, then the main masked source base and the prepass decision also remain unchanged

So the first experiment does **not** need a patch-private cache of:

- `$2ABA`
- `$2A7E`
- `$298E`
- `$2A42`
- `$2BAA`

for this one timer-only gate.

## Still uncertain

### Whether an asynchronous writer can mutate the "stable" fields between timer reruns

Current local work says the large descriptor-source fields are init/setup seeded and stable across the timer-only rerun.

That is healthy enough for a first experiment, but still one notch short of absolute proof against every possible asynchronous writer.

If the first timer-only gate causes visual desync, the next conservative expansion would be:

- keep the same timer-only seam
- add a patch-private cached tuple updated after each successful `A794` run:
  - `$341A`
  - `$2ABA`
  - `$2A7E`
  - `$298E`
  - `$2A42`
  - maybe `$2BAA & #$000C`

That would still be much safer than touching the queue core.

## Recommended first patch

### Patch seam

Hook the timer-only leg at `C0:A723`.

Replace the first two instructions:

- `LDA $0F12,X`
- `STA $0ED6,X`

with a `JSL` into an expanded-ROM helper, plus padding.

### Patch helper behavior

The helper should:

1. perform the original timer-leg reload:
   - `$0ED6 = $0F12`
2. perform the original toggle:
   - `$10F2 ^= 2`
3. preserve the original optional `ABE0` side-effect when the new `$10F2` becomes zero and the same small guards pass
4. derive the same raw descriptor header that `A794` would read:
   - seed long-pointer bank from `$2A06`
   - compute selector from `$29CA + 4*DATA_C0A623[$2AF6] + $10F2`
   - read `[$02]`
5. compare the new raw header against `$341A`
6. if equal:
   - jump directly to `A753`
7. if different:
   - `JSL C0A794`
   - jump to `A753`

This keeps the experiment narrow:

- timer-only branch only
- no generic queue changes
- no broad dedupe of every `A794` call

## Safest testing plan

1. Apply the timer-only gate **on top of** the currently stable safe dedupe baseline.
2. Test ordinary walking first:
   - single-axis outdoor walking
   - diagonal outdoor walking
3. Then test companion-heavy scenes:
   - towns
   - places with many moving or animated overworld visuals
4. Specifically look for:
   - reduced diagonal microstutter
   - frozen or under-animated companion visuals
   - phase flicker from the skipped timer reruns
5. If the visual layer regresses, fall back immediately and widen the compare tuple before touching any lower-level queue code.

## Bottom line

For the first post-dedupe experiment:

- patch only `A723..A750`
- keep all movement-change reruns intact
- use `$341A` as the compare anchor
- rely on the timer-only branch's locally stable descriptor-source fields

That is the smallest realistic experiment that directly targets the newly identified companion visual amplifier without destabilizing the generic queue machinery.
