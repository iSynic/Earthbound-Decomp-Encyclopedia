# Class `4` / Class `6` Surface Contexts

This note captures the current best local read for the two remaining special `$9887` surface classes after class `3` was anchored to doorway transitions.

## Bottom line

The safest current interpretation is:

- `$9887 == 6` is the stronger candidate for a stairs-style surface class.
- `$9887 == 4` is the stronger candidate for an escalator-entry-style surface class.

That is still an inference, not a fully proved local label, but the evidence is now better than a loose “some other special terrain bucket” description.

## Strongest local anchors

### 1. The adjacent WRAM block matches named stairs/escalator state

From the `ebsrc` RAM map, the local `5Dxx` block we have already been touching now crosswalks cleanly as:

- `$5DAA` = `LADDER_STAIRS_TILE_X`
- `$5DAC` = `LADDER_STAIRS_TILE_Y`
- `$5DC6` = `STAIRS_DIRECTION`
- `$5DC8` = `ESCALATOR_ENTRANCE_DIRECTION`
- `$5DCE/$5DD0` = `STAIRS_NEW_X / STAIRS_NEW_Y`
- `$5DD2/$5DD4` = `ESCALATOR_NEW_X / ESCALATOR_NEW_Y`
- `$5DD6` = `CURRENT_MAP_MUSIC_TRACK`

That crosswalk fits our local doorway result too, because `C0:068F4` / `C0:06A07` drive `$5DD6` from the door-destination family.

### 2. Class `4` and class `6` are the remaining special surface buckets in the local visual resolver

The `C0780F` resolver uses `$9887` specially only in three obvious cases:

- class `3` -> doorway / transition-cell special family
- class `6` -> force selector result `#$0007`
- class `4` -> force selector result `#$0006` only when entity-local byte `+$35` is zero

That makes class `4` and class `6` look like real surface/context categories, not random animation exceptions.

### 3. The local stair-like helpers are built around the same `5DAA/$5DAC` block

The helper family around `C05B7B`, `C057E8`, and `C0583C` works directly from:

- `$5DAA/$5DAC` as tile-like anchor coordinates
- `$5DAE` as the companion checked coordinate
- alignment tests such as `$5DAC & #$0007`

That is much more consistent with stair/escalator surface handling than with doors, combat, or ordinary flat-ground walking.

## Why class `6` now looks more like stairs

The class-`6` branch in `C0780F` is unconditional:

- if `$9887 == 6`, it immediately forces selector result `#$0007`

That makes class `6` look like a stable terrain class whose special pose/visual family should always apply when standing on that surface.

That fits stairs better than an entry-gated mechanic.

## Why class `4` now looks more like escalator entry

The class-`4` branch is conditional:

- if `$9887 == 4`, it only forces selector result `#$0006` when entity-local byte `+$35` is zero

That makes class `4` look more like a gated variant than a simple always-on surface class.

Paired with the nearby named WRAM field `ESCALATOR_ENTRANCE_DIRECTION`, the cleanest current inference is that class `4` is the escalator-entry-style surface class: the special handling depends on local entity state, probably whether the actor is in the right entry condition for the escalator presentation/movement family.

## Caution

I am not treating these names as fully proved yet.

What is proved locally:

- class `3` is special and tied to door-transition logic
- classes `4` and `6` are special non-door surface buckets
- the surrounding `5Dxx` WRAM block really is the stairs/escalator/door movement block

What is still inference:

- `4 -> escalator entry`
- `6 -> stairs`

That said, this is now the strongest current read.

## Update: the stairs half of the `5Dxx` block is now better grounded locally

The new note [stairs-escalator-state-block-5daa-5dd6.md](notes/stairs-escalator-state-block-5daa-5dd6.md) tightens one of the weaker spots from the earlier pass.

The most useful local gain is `$5DC6`: in the type-`3` movement helper at `C0:6E6E`, the low path stores the incoming selector into `$5DC6`, and the follow-up path reloads it to index the tiny tables at `C0:6E0A` and `C0:6E12` before writing a facing-like value to `$987F` and computing a staged destination. That makes `STAIRS_DIRECTION` a genuinely local fit, not just a borrowed RAM-map name.

The staged pair `$5DD0/$5DD2` is also stronger now, because `C0:6F70` stores the computed target there and `C0:6E2C` / `C0:6E4A` later commit it into live player position. So the `STAIRS_NEW_X / STAIRS_NEW_Y` reading is a good local fit too.

That makes the class split a bit healthier:

- class `6` still looks like the stronger stairs-style candidate
- class `4` still looks like the stronger escalator-entry-style candidate

The escalator side is still softer, because `$5DC8` itself does not yet have a comparably strong local consumer pinned down.

## Update: the escalator-side field names should stay provisional

One raw-ROM check tightened the caution here.

I found no direct code reference to `$5DC8` in the ROM, and the local movement callbacks clearly treat `$5DCC/$5DCE` and `$5DD0/$5DD2` as staged X/Y destination pairs. So while the surrounding `ebsrc` RAM names still make the class split plausible, the exact escalator-side per-word labels are not yet locally proved.

That means the safest wording is still:

- class `6` is the stronger stairs-style candidate
- class `4` is the stronger escalator-entry-style candidate

But the escalator field names themselves should stay provisional until we anchor a real local `$5DC8` or `$5DD2/$5DD4` consumer.

## Update: class `4` is gated by selector row id `0`

One more local constraint is worth preserving.

In `C0780F`, the class-`4` special case does **not** always force mode `#$0006`.
It only does so when entity byte `+$35` is zero.

That matters because byte `+$35` is already tied into the same higher-level visual-selector family as `0E5E / 2C22`, not an unrelated scratch state.

So the class split is now a little more precise:

- class `6` still looks like the stronger always-on stairs-style surface class
- class `4` looks more like a narrower, selector-family-specific transition case

That still fits an escalator-entry-style interpretation reasonably well, especially if that behavior only applies to one selector family, but it means class `4` should not be described as a blanket all-entities surface class.

## Update: class `4` should stay tied to row `0`, not to a named actor family

The latest pass did not prove what selector row `0` means semantically. One meaningful writer seeds `$0A38` from `TYA-1`, which means row `0` can arise as the first member of an ordinal family rather than only as a special hardcoded id.

So the safest wording is now:

- class `4` is gated by selector row `0`
- row `0` itself is not yet identified as player-only or otherwise uniquely named

That still leaves the escalator-entry reading plausible, but it should stay framed as a row-`0` special case rather than a player-only special case.

## Update: row `0` still should not be promoted to a named actor family

The latest source-side pass found two meaningful `0A38` writers:

- a local ordinal writer (`TYA-1 -> 0A38`)
- a far event-flag-gated table source (matching `D5:F645` record index -> `0A38`)

That makes row `0` look more like a selectable configuration value than a uniquely named actor-family tag. So the class-`4` gate should still be described as a row-`0` special case rather than a player-only special case.


## Update: surface probes now connect classes `2/4/6` to collision samples

The `C0:52D4-C0:5E3A` pass gives this note a better local foundation. `C0:5B7B` is the movement surface front door used by the normal step and special traversal paths; it writes candidate probe coordinates into `$5DAC/$5DAE`, samples the active `$E000` collision byte page, and dispatches by the incoming mode:

- mode `0 -> C0:57E8`, using sample mask `#$0007`
- mode `4 -> C0:583C`, using sample mask `#$0038`
- mode `6 -> C0:5890`, using sample masks around `#$0009`
- mode `2 -> C0:59EF`, using sample masks around `#$0024`

That does not fully prove the gameplay labels, but it does prove that classes `4` and `6` are interpreted through special surface-pattern decoders rather than through the generic single-mode validator at `C0:5B4E`.

The paired decoders also line up with the earlier stairs/escalator caution:

- `C0:5890` is selected for mode `6` and returns values centered around `5/7/6`.
- `C0:583C` is selected for mode `4` and maps collision-sample patterns to `3/5` or a sentinel.

So the current wording should stay: class `6` is the stronger stairs-style candidate, while class `4` remains the stronger escalator-entry-style or row-`0` transition candidate. The important improvement is that both are now tied to concrete tile-sample pattern logic in `C0:5B7B` instead of only to the visual selector behavior in `C0:780F`.
