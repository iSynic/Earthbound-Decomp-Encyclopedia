# Overworld A794 Watcher Gate Experiment (`safe-v4`)

This note records the next patch experiment after the timer-only `A794` gate proved safe but not impactful.

See also [overworld-companion-family-priority-a794.md](notes/overworld-companion-family-priority-a794.md).
See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).

## Main idea

The new experiment broadens the `A794`-side gate from the old timer-only branch to the common watcher-side rerun site at `C0:A750`.

This is intentionally a middle ground:

- broader than the old timer-only gate at `A723..A750`
- narrower than patching `A794` globally
- leaves the immediate state-change rerun at `C0:A6F7` untouched

That makes it a safer next step after the emulator samples showed busy `8643` traffic coming through `A56E -> A794 -> A750`.

## Hook

Patch file:

- [overworld_stutter_a794_watcher_gate_overlay.asm](asm/overworld_stutter_a794_watcher_gate_overlay.asm)

Built ROM:

- [EarthBound-overworld-stutter-safe-v4-a794-gate.sfc](build/EarthBound-overworld-stutter-safe-v4-a794-gate.sfc)

Primary hook:

- `C0:A750 -> JML Overworld_A794WatcherGate`

Support hook:

- `C0:1404 -> JSL Overworld_ClearAllCaches_And_C02194`

The refresh-side hook clears both:

- the existing strip-dedupe cache from `safe-v2`
- the new per-entry `A794` watcher cache

## Compare tuple

The watcher gate derives and compares a broader signature than the old timer-only patch:

- raw descriptor header `[$02]`
- VRAM base `$298E`
- transfer size `$2A7E`
- transfer count `$2ABA`
- packed source-bank plus auxiliary-prepass state from `$2A42` and `$2BAA`
- effective selector pointer from:
  - `$29CA + 4*DATA_C0A623[$2AF6] + $10F2`

If that full signature matches the cached signature for the same entry offset, the patch:

- skips the watcher-side rerun at `A750`
- still updates `$341A` with the current raw header
- resumes at `C0:A755`

If the signature differs, the patch:

- updates the cache
- calls the existing `C0:A780` wrapper, which in turn runs `A794`
- resumes at `C0:A755`

## Why this is safer than a full `A794` hook

This experiment still avoids the broadest-risk options:

- it does not touch `A56E`
- it does not touch `8643/865F/8677`
- it does not suppress the immediate state-change rerun at `A6F7`

So it is specifically testing whether the common watcher-side `A750` rerun is emitting redundant companion work often enough to matter.

## Current confidence

Locally proved and emulator-backed:

- `8643` busy-frame samples were dominated by `A56E -> A794` rather than `A4C4`
- `A750` is part of that hot path
- the earlier timer-only gate was too narrow to matter visibly

Still uncertain:

- whether the broader watcher-side `A750` gate is broad enough to reduce visible hitch
- whether the remaining hitch is still dominated by `A794` after the strip family is included in the same frame

## Smoke-test status

The overlay assembles cleanly on top of the stable baseline.

Smoke-test command used:

```powershell
Copy-Item 'build\EarthBound-overworld-stutter-safe-v2.sfc' 'build\EarthBound-overworld-stutter-safe-v4-a794-gate.sfc' -Force
& 'refs\earthbound-disasm-legacy\Earthbound Decomp\Global\asar.exe' 'asm\overworld_stutter_a794_watcher_gate_overlay.asm' 'build\EarthBound-overworld-stutter-safe-v4-a794-gate.sfc'
```

This does not prove gameplay correctness yet.

## Best test plan

Compare:

- [EarthBound-overworld-stutter-safe-v2.sfc](build/EarthBound-overworld-stutter-safe-v2.sfc)
- [EarthBound-overworld-stutter-safe-v4-a794-gate.sfc](build/EarthBound-overworld-stutter-safe-v4-a794-gate.sfc)

Focus on:

- diagonal outdoor walking first
- then companion-heavy town movement
- then scene transitions or map refreshes

Watch for:

- visible microstutter reduction
- missing or under-animated companion visuals
- flicker or stale companion tiles after map refresh
- any crash or black-screen regression

## Bottom line

`safe-v4` is the first post-timer experiment that still targets `A794`, but does so at the broader watcher-side rerun seam that showed up in busy `8643` samples.

So it is a materially stronger test of the current best companion-family hypothesis than the old timer-only patch.
