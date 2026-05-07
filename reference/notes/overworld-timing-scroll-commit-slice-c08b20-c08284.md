# Overworld Timing And Scroll Commit Slice (`C0:1558`, `C0:8B20`, `C0:8180..8390`, `C0:8240`, `C0:834E`)

This note narrows the timing-side hypotheses for the remaining overworld walking microstutter.

See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).
See also [overworld-walking-stutter-producer-split-c01558-c01ca8.md](notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md).

## Main result

The earlier candidate timing addresses from the patch thread were not the right seam:

- `C0:8012` is startup or initialization code, not a recurring overworld frame-sync point
- `C0:834E` sits inside the NMI handler, not the main-loop wait side

The real scroll-state path now looks like this:

1. ordinary movement refresh at `C0:1558` writes per-layer runtime shadow words into `$0031/$0033/$0035/$0037/...`
2. `C0:8B20..8B8D`, specifically `C0:8B51 / C0:8B57`, snapshots those shadow words into the hardware-commit slots at `$0041/$0045/$0049/$004D/...`
3. the NMI handler at `C0:8284..82CA` writes those slots to the actual PPU scroll registers:
   - `$0041/$0042 -> $210D` BG1 HOFS
   - `$0045/$0046 -> $210E` BG1 VOFS
   - later pairs to `$210F/$2110/$2111/$2112/$2113/$2114`

The current strongest timing question is no longer "does `C0:8012` or `C0:834E` stall?"
The newer walking-stack work now makes the healthier current question:

- is the visible judder already native to the upstream movement or snapshot cadence before this timing slice even runs?
- or is there still later presentation workload layered on top of an otherwise healthy cadence?

## Locally proved

### `C0:8012` is not a recurring frame-sync point

The local decode at `C0:8000..8124` is startup-side machine initialization:

- DP and stack setup
- PPU register clears
- DMA and WRAM init
- fixed boot-state writes

So `C0:8012` should be removed from the list of likely main-loop pacing checkpoints.

### `C0:834E` is inside the NMI handler

The local decode at `C0:8180..8390` is the NMI body.

Important anchors:

- `C0:8183` reads `$4210`
- `C0:818E` increments `$002B`, the NMI heartbeat or sync byte already seen in emulator work
- `C0:8240..8276` drains the queued VRAM DMA descriptors from `$0400+`
- `C0:834E` then resets `$99` and runs additional NMI-side work before `RTI` at `C0:8390`

So `C0:834E` is an NMI-side bookkeeping point, not a main-loop wait loop.

### NMI writes the actual scroll registers from `$41/$45/...`

Inside the NMI handler:

- `C0:8284..8295` write `$41/$42` to `$210D` and `$45/$46` to `$210E`
- the same pattern continues for the later BG scroll pairs through `$4D/$4E`, `$51/$52`, `$55/$56`, `$59/$5A`, `$5D/...`

This is the strongest current local proof that `$41/$45/...` are the immediate hardware-commit shadow slots for scroll values.

### `C0:8B20..8B8D` copies runtime shadow scroll values into the NMI commit slots

`C0:8B20` is the key runtime-to-NMI handoff.

Useful local body facts:

- `AD 31 00 -> STA $0041,X`
- `AD 33 00 -> STA $0045,X`
- `AD 35 00 -> STA $0049,X`
- `AD 37 00 -> STA $004D,X`
- `AD 39 00 -> STA $0051,X`
- `AD 3B 00 -> STA $0055,X`
- `AD 3D 00 -> STA $0059,X`
- `AD 3F 00 -> STA $005D,X`

Then:

- `$002C = $002E`
- `$002E ^= 3`

So the healthiest current local read is:

- `$31/$33/...` are the runtime-side scroll shadow words
- `$41/$45/...` are the NMI-consumed hardware-copy slots
- `8B20` flips between two buffered sets using `$2C/$2E`

### `C0:8B51` and `C0:8B57` are live during overworld walking

The emulator-side follow-up confirms the buffered handoff is not hypothetical.

Observed live hits:

- `C0:8B51  STA $0041,X`
- `C0:8B57  STA $0045,X`

and the effective addresses alternate between:

- `7E:0041 / 7E:0045`
- `7E:0043 / 7E:0047`

So `8B20` really is publishing into alternating low-WRAM shadow pairs.

### `C0:1558` is the ordinary incremental movement refresh, and `C0:156B / C0:1575` are the live movement-time writers to `$31/$33`

The most useful producer-side result from the next trace pass is that the ordinary movement refresh is already in the same strip we have been patching.

Inside `C0:1558`:

- `C0:1566  STA $0035`
- `C0:156B  STA $0031`
- `C0:1570  STA $0037`
- `C0:1575  STA $0033`

Then `1558` branches into the horizontal and vertical incremental refresh lanes:

- horizontal-side body through `15B0..165D`
- vertical-side body through `166B..171A`

Those bodies call the same known producer families:

- `0BDC / 0D7E / 0FCB`
- `0AC5 / 0CF3 / 0E16`
- `25CF / 2B55`
- `255C / 2A6B`

That makes `1558` the strongest current fit for the ordinary "movement advanced, recompute runtime scroll shadows, then perform incremental visual refresh" controller.

### `C0:18A8` and `C0:4026` are the current strongest callers into `C0:1558`

The local cross-check found two clean direct callers:

- `C0:18A8  JSR $1558`
- `C0:4026  JSR $1558`

`C0:18A8` is especially informative because it updates `$4380/$4382`, compares them against `$437C/$437E`, and only calls `1558` when the scroll position has actually changed enough to require incremental refresh. So this looks like a real movement-time refresh entry, not just a setup wrapper.

### Emulator-side timing result: movement update and publish both look healthy

The recent breakpoint sequence over:

- `C0:156B / C0:1575`
- `C0:8B51 / C0:8B57`
- `C0:8284`

showed that during diagonal walking:

- `156B / 1575` fire regularly
- the values written to `$31/$33` advance smoothly
- `8B51 / 8B57` publish those values normally into the alternating shadow slots

Representative observed sequences looked like:

- `$31: 0796 -> 0794 -> 0793 -> 0792`
- `$33: 0669 -> 0668 -> 0667 -> 0666`

That makes both the "missed movement update" and "missed publish" models much weaker.

## Decomp-backed and locally consistent

### Why the original stale-commit model was plausible

Claude's newer patch-thread hypothesis was:

- the main loop may occasionally run long enough during diagonal movement that NMI commits stale scroll shadow values for one frame

This note does not prove that globally false, but it now shows that in the tested walking path:

- runtime movement writes are happening steadily
- runtime publish into the NMI shadow slots is happening steadily
- NMI is consuming those slots on its own cadence

So the pure stale-scroll-shadow explanation is no longer the healthiest leading model.

### What now looks more plausible

The current healthier read is:

- movement-time scroll state updates are healthy
- publish into the NMI shadow slots is healthy
- the remaining microstutter is more likely upstream movement cadence or later presentation workload, not missing camera-state updates

That fits the broader patch-thread evidence:

- the stable strip-dedupe patch helped somewhat
- diagonal movement is still worst
- two producer families still appear active
- the timer-only `A794` gate was safe but did not materially help
- the later `src/c0` pass now grounds ordinary walking in the discrete `C05200 -> C04C45 -> C0449B -> C0400E/4010` pipeline

## Still uncertain

### Which presentation workload dominates the visible hitch

This note narrows the problem away from movement-state and publish-state timing, but it does not yet tell us whether the visible hitch is dominated by:

- strip-family uploads in the `58xx/5Cxx` VRAM family
- companion visual/entity uploads in the `40xx/41xx/42xx` family
- or the aggregate cost of both in the same frame

### Whether the hitch is queue-drain cost, descriptor build cost, or another presentation-side coordination cost

We have largely weakened the "state did not advance" theory.
What remains open is exactly which rendering-side work is expensive enough to produce the visible jitter.

## Best next emulator workflow

### 1. Stop focusing on `C0:8012`, `C0:834E`, and the raw `8B20` entry

Those are no longer the best seams:

- `8012` is startup only
- `834E` is NMI bookkeeping only
- `8B20` entry is less useful than the specific publish instructions at `8B51 / 8B57`

### 2. Treat the timing slice as mostly cleared

The useful timing chain is now locally established as:

- `1558` writes `$31/$33`
- `8B51 / 8B57` publish those values into alternating shadow pairs
- `8284` consumes them in NMI

The recent emulator pass shows that chain behaving normally during diagonal walking.

### 3. Pivot back to presentation workload attribution

The best next investigation target is no longer camera-state timing.
It is which render-side producer family dominates the visually bad frames:

- strip-family `58xx/5Axx/5Bxx/5Cxx/5Exx`
- companion-family `4040/4120/42A0`
- or both together

## Practical patch implications

The timing slice no longer looks like the main seam for a patch.

If the recent emulator evidence holds, the next patch direction should probably be about:

- smoothing the presentation of the upstream discrete movement cadence
- and only secondarily reducing later render workload if a smaller additive hitch still remains

That is no longer a scroll-shadow timing patch.
It is more likely a visual-smoothing patch, or secondarily a workload or scheduling patch.

## Bottom line

The timing slice is much narrower now:

- `8012` is not relevant
- `834E` is NMI-side bookkeeping only
- `1558` is the ordinary incremental movement refresh that writes `$31/$33`
- `8B51 / 8B57` are the live runtime scroll-shadow publish instructions
- `8284` is the actual NMI hardware commit to `$210D/$210E`

And the latest emulator evidence says that `1558 -> 8B51/8B57 -> 8284` is behaving normally during diagonal walking.

So the next useful investigation should pivot away from scroll-shadow timing.
The healthiest current next theories are:

- native overworld cadence in the ordinary walking tick path
- visible-layer smoothing opportunities downstream of that cadence
- only after that, any smaller additive render workload

## Working Names

- `C0:1558` = `UpdateRuntimeScrollShadowsAndIncrementalRefresh`
- `C0:8B20` = `PublishRuntimeScrollShadowsToNmiBuffers`
- `C0:8180` = `NmiHandler_UpdatePpuAndQueues`
- `C0:8240` = `NmiDrainQueuedVramDmaDescriptors`
- `C0:8284` = `NmiCommitBg1ScrollRegisters`
- `C0:834E` = `NmiPostPpuBookkeeping`
