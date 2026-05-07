# Type 6 Door-Candidate Probe at `C0:65C2`

This note captures the current ROM-first interpretation of the helper at `C0:65C2` and the nearby queue helpers that explain why lookup type `6` matters even though `C0:6A8E` is a stub in the `C0:7526` dispatcher path.

## Main finding

The important correction is:

- type `6` is not primarily acting like a local dispatcher action code
- instead, the front-of-player interaction path uses it as a sentinel for a cached door-candidate state

That explains why `C0:6A8E` can be a no-op locally while type `6` still matters elsewhere.

## `C0:65C2` `Probe_FrontType6DoorCandidate`

What the ROM clearly shows:

- The routine is called from `C0:43B3`, inside the front-of-player interaction scan.
- It derives coarse cell coordinates from live position `$9877/$987B` using direction-dependent offset tables at `C3:E230` and `C3:E240`.
- It performs a trigger lookup through `C0:7477`.
- If that first lookup misses with `#$FF`, it retries one adjacent Y cell by incrementing the probe coordinate.
- If the resolved trigger type is anything other than `6`, it returns without caching anything.
- If the resolved trigger type is `6`, it treats `$5DBC/$5DBE` as data returned by the lookup record, resolves a pointer from the bank `CF` destination table family, stores the byte-like side value in `$5DDC`, stores the resolved pointer in `$5DDE/$5DE0`, and sets `$5D62 = #$FFFE`.

Working interpretation:

- this is a forward probe for a type-`6` movement/interaction trigger
- on success, it caches a special fallback interaction pointer rather than executing a helper immediately
- because the bank `CF` table family is the same one used by the door-oriented type `0` and type `2` helpers, the strongest current interpretation is that type `6` marks a door-like candidate reachable from the front-interaction path

## Why `#$FFFE` matters

Downstream consumers make the sentinel behavior much clearer.

In the legacy reference, the callers that inspect `$5D62` treat it like this:

- `0` -> no interaction result
- `#$FFFF` -> invalid or blocked result
- `#$FFFE` -> use cached pointer from `$5DDE/$5DE0`
- anything else -> use the normal table-driven object/interaction result path keyed by `$5D62`

That means `C0:65C2` is best read as a special-case interaction fallback loader.

## Context in the front-interaction path

A narrow legacy cross-check around `C0:43BC` is especially helpful here:

- the routine first tries the ordinary front-of-player object/tile interaction scan
- if that scan leaves `$5D62` as `0` or `#$FFFF`, it calls `C0:65C2`
- after `C0:65C2`, the caller checks `$5D62` again and can now succeed via the cached `#$FFFE` case

So `65C2` is not the main interaction scan. It is a second-stage probe that upgrades "nothing useful found" into "use this cached door-like destination instead" when a type `6` trigger is present.

## Nearby queue helpers

The surrounding `65xx` helpers also make more sense now:

- `C0:6537` peeks the current staged-movement queue entry type from `$5DEA[$5E02]`
- `C0:654E` peeks the current staged-movement queue payload pointer from `$5DEC/$5DEE[$5E02]`
- `C0:6578` pushes an `A/X` pair into a small LIFO buffer rooted at `$5E06/$5E08`, with count in `$5E36`
- `C0:65A3` flushes that LIFO buffer by repeatedly calling `JSL $C46507`

Those helpers are not the door probe itself, but they help explain why the `65xx` area mixes movement-queue state with interaction fallback preparation.

## Current best model

- type `6` is a door-candidate sentinel in at least one important call path
- `C0:65C2` performs a front-of-player trigger probe specifically to detect and cache that sentinel case
- the cached result uses `$5DDC/$5DDE/$5DE0` plus sentinel value `#$FFFE` in `$5D62`
- that is why type `6` can matter greatly even though `C0:6A8E` is a no-op in the `C0:7526` dispatcher path

## Best next target

- Trace the direct caller at `C0:43B3` and the surrounding front-interaction flow in our own notes, so we can connect type `6` cleanly to the ordinary object/tile interaction system instead of treating it as a movement-only oddity.
