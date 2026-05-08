# Visual Selector Family (`0E5E` / `2C22` / `C0780F` / `C3:F2B5`)

This note captures the strongest current local read for the higher-level visual selector that feeds the sprite-pose cache path.

See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [secondary-visual-descriptor-c42b0d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/secondary-visual-descriptor-c42b0d.md).

## Main result

A useful layer boundary is much clearer now.

`2C22` is not a final pose id. It is the live copy of the same higher-level selector family that earlier setup paths persist in `0E5E`.

The strongest current local read is:

- `0E5E` = per-entity visual selector row id
- `2C22` = live cached copy of that same selector for the current entity slot
- `C0780F` = resolver that turns `(selector row id, local bucket state)` into a concrete pose-table index
- `C3:F2B5` = 8-entry-per-row pose resolution table used by that resolver

That is materially better than the older wording that treated `2C22` as only a vague "major visual-state selector."

## Why `0E5E` and `2C22` now look like the same family

The persistence path is strong.

A setup path copies scratch values into the per-entity block like this:

- `0A38 -> 0E5E`
- `0A3A -> 0E9A`
- `0A42 -> 0F8A`
- and several neighboring fields in the same block

Later refresh paths read `0E5E` back and feed it straight into `C07A56`.

Inside `C07A56` itself:

- caller `A` is passed to `C0780F`
- that same caller value is stored to `2C22`
- the resolved pose-table index returned by `C0780F` is what drives the later `EF:133F` lookup

So the strongest current statement is:

- `0E5E` is the persistent selector row id
- `2C22` is the active cached copy of that selector row id during visual refresh

## `C0780F` is a row resolver, not a direct-id pass-through

`C0780F` does not simply echo the selector.

It takes:

- selector row id in `A`
- current entity/context pointer in `X`
- target slot index in `Y`

and resolves a concrete pose index through several layers of control flow.

The local logic shape is:

1. Apply a few hard special overrides.
2. Clear or set bits in `2E7A` based on entity bytes `+0E/+0F`.
3. Choose a small bucket index `Y`.
4. Return a word from `DATA_C3F2B5` using the selector row id plus that bucket.

The strongest current bucket rule is:

- base buckets `0..3` are selected when current selector `$12` is in one of four small groups
- if `$9887 == 3`, the resolver shifts into alternate buckets `4..7`
- if `$9887 == 5` and the base bucket would have been `0`, it instead uses bucket `6`

That means the selector family is row-based, while the concrete pose index comes from a second local state bucket.

## Concrete row lookup shape

The return path in `C0780F` is:

- `TYA`
- `ASL`
- store to scratch
- `LDA selector`
- `ASL` four times
- `ADC bucket_word_offset`
- `TAX`
- `LDA.l DATA_C3F2B5,X`

So the table is indexed as:

- row stride = `0x10` bytes = 8 words per selector row
- column = bucket `0..7`

That is exact local proof that the selector is not itself a final pose index.

## Sample rows from `C3:F2B5`

The ROM bytes at `C3:F2B5` begin like this:

- row `0`: `0001 0008 0011 0015 001B 0022 0005 FFFF`
- row `1`: `0002 0009 0012 0016 001C 0022 0019 FFFF`
- row `2`: `0003 000A 0013 0017 001D 0022 0019 FFFF`
- row `3`: `0004 000B 0014 0018 001E 0022 0019 FFFF`
- row `4`: `002C 002C 002C 002C 002C 002C 002C FFFF`
- row `5`: `002D 002D 002D 002D 002D 002D 002D FFFF`
- row `6`: `0028 0028 002A 002B 0028 0028 0028 FFFF`
- row `7`: `00B6 00B6 00B6 00B6 00B6 00B6 00B6 FFFF`

This looks exactly like a row selector feeding multiple stance/facing/state buckets, not a table of unrelated ids.

Rows `0..3` clearly behave like one shared family with different row ids. Rows `4..7` look more like special fixed families.

## What the bucket choices currently look like

The current best local read is:

- buckets `0..3` are the ordinary resolved variants for four small current-state groups
- buckets `4..7` are alternate-mode variants reached when `$9887 == 3`
- bucket `6` is also reused by the `$9887 == 5` special case
- `FFFF` remains the cleanest current marker for "no valid pose for this bucket"

I am still keeping the exact player-facing names for those bucket families cautious because the resolver also depends on globals like `$9840`, `$9887`, `$9F71`, and some entity-local bytes.

## Why this matters for `2C22`

This finally makes the `2C22:2AF6 -> 3456` fingerprint compare easier to talk about.

The safest current layered model is now:

- `2C22` = high-level visual selector row id
- `2AF6` = lower-level pose/frame selector used within that row family
- `3456` = cached visual fingerprint word combining both layers

So when the refresh path compares `2C22` and `2AF6` against `3456`, it is not comparing two unrelated state words. It is comparing a row-level visual family selector plus a lower-level per-family pose/frame selector.

## Relationship to `0E9A`

`0E9A` still looks like a neighboring but separate selector family.

It is often loaded beside `0E5E`, and one common path immediately does:

- `LDA 0E9A`
- `ASL`
- `TAX`
- `LDA DATA_C3E09A,X`

That looks like a second table-driven selector layer, but the current pass did not pin its exact semantic name yet.

So the safest statement is:

- `0E5E/2C22` resolve the pose-family row
- `0E9A` remains a nearby secondary selector family that often participates in the same visual setup path

## Best current name

The cleanest current local name is:

- `0E5E` / `2C22` = visual selector row id

A stronger but still slightly interpretive name would be:

- pose-family selector

I would keep the more cautious wording for now, because the resolver mixes ordinary buckets, alternate-mode buckets, and a few hard overrides.

## Best next target

The best next move is to pin what the bucket families mean in gameplay or animation terms, especially the `$9887 == 3` alternate set and the `$9887 == 5` reuse of bucket `6`. That should let us rename the selector from a structural name to a player-visible one.

## Update: `$9887` now looks position-derived

The current best follow-up is in [position-derived-visual-context-class-9887.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/position-derived-visual-context-class-9887.md).

The useful correction is that `$9887` no longer looks like a free-running animation mode. It now reads much more like a position-derived visual context class from `C00AA1`'s packed `D7:B200` lookup. That class then chooses whether `C0780F` stays in its ordinary bucket family or switches into alternate special-case columns, especially for class `3`.

## Update: class `4` is narrower than it first looked

A useful refinement from the latest pass: the class-`4` special case in `C0780F` only forces mode `#$0006` when entity byte `+$35` is zero. That byte already belongs to the same higher-level selector family as `0E5E / 2C22`, so class `4` is not a blanket terrain override for every selector family.

That keeps the escalator-entry-style reading plausible, but it means the special handling is selector-family-specific rather than universal.

## Update: selector row `0` is not yet semantically identified

A useful caution from the latest pass: I do not yet have good local proof that selector row `0` means "player" or any other single semantic family.

One meaningful writer seeds `$0A38` from `TYA-1` in the `C03770` path, and that value is later copied into `0E5E`. So row `0` can arise as the first member of a small ordinal family, not only as a special hardcoded semantic id.

That means the safest current statement is still just:

- class `4` is gated by selector row `0`
- selector row `0` itself is not yet semantically named

The new focused note is [selector-row-zero-caveat.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/selector-row-zero-caveat.md).

## Update: the selector rows are sourced from setup metadata in more than one way

A useful source-side refinement from the latest pass: `0A38` is not only copied from an existing persistent selector. I now have two stronger source families.

- In the local `C03770` path, `TYA-1` is stored to `0A38`, so row `0` can arise as the first member of an ordinal family.
- In the far `EF:0EE8` setup family, the matching index of a 10-entry event-flag-gated table at `D5:F645` is stored to `0A38` after record word `1` at offset `+0x02` passes `C21628`.

That strengthens the current reading that the selector rows are setup-chosen configuration values, not yet locally proved semantic actor labels.

## Update: the far selector source is a 10-entry event-flag-gated table

One source-side refinement is materially stronger now.

The `EF:0EE8` family does not appear to translate an arbitrary metadata byte through `C21628`. Instead it loops over a 10-entry, 20-byte-per-record ROM table at `D5:F645`, passes record word `1` at offset `+0x02` to `C21628`, and if that event-flag test succeeds it stores the **record index** to `0A38`.

That means the source picture is now:

- local ordinal source: `TYA-1 -> 0A38`
- far table source: matching `D5:F645` record index -> `0A38`

So the selector rows still look like setup-chosen row ids, but the far path is now better described as an event-flag-gated selector table than as a generic “validated config value.”

The focused note is [selector-row-config-family-ef0ee8.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/selector-row-config-family-ef0ee8.md).


