# Selector Row `0` Caveat

This note records an important caution about selector row `0` in the `0E5E / 2C22 / C0780F` family.

## Main result

I do **not** yet have good local proof that selector row `0` means "player" or any other single semantic family.

The strongest current correction is that one meaningful writer seeds `$0A38` from an ordinal-style value:

- in the `C03770` path, `TYA`, then `DEC`, is stored to `$0A38`
- that value is later copied into `0E5E` by the `C092F5 -> C0933E` setup path

So row `0` can arise naturally as the first member of a small ordinal family, not only as a special hardcoded semantic id.

## Why this matters

The recent class-`4` work showed:

- `C0780F` only forces mode `#$0006` when `$9887 == 4` **and** entity byte `+$35 == 0`
- byte `+$35` is the cached copy of the same selector-row family as `0E5E / 2C22`

It would be tempting to read that as "class `4` only affects the player," but the local evidence is not strong enough for that yet.

## What is locally true

- `0E5E` / `2C22` are real selector-row ids
- row `0` is a real value in that family
- class `4` is gated on row `0`
- one writer creates row `0` from an ordinal source (`TYA-1`)

## What stays open

- whether row `0` corresponds to the player specifically
- whether row `0` is instead the first member of a broader human / party / default selector family
- whether different setup paths reuse row `0` with slightly different meanings

## Safest current wording

The safest current phrasing is:

- class `4` is gated by selector row `0`
- selector row `0` is not yet semantically identified

That is more accurate than promoting it to a player-only rule too early.

## Update: `0A38` is sourced from config/ordinal data, not a uniquely named actor id

The latest pass tightened the source side of the selector-row family.

### Source family 1: ordinal loop source

In the `C03770` path:

- `TYA`
- `DEC`
- `STA $0A38`

That means row `0` can arise as the first member of a small ordinal family.

### Source family 2: far event/config source

In the `EF:0EE8` family, after entry word `0` from a 10-entry table at `D5:F645` passes `C21628`, the code does:

- `LDA $02`
- `STA $0A38`

So `0A38` is also being sourced from the matching index of an event-flag-gated selector table, not only from a hardcoded actor-family constant.

## What this strengthens

This makes the current negative conclusion stronger:

- selector row `0` is **not yet** locally supported as a player-only tag
- the selector-row family is being fed by small configuration or ordinal values in more than one setup path

## Safest current reading

`0A38 -> 0E5E -> 2C22` still looks like a higher-level visual-selector row id family, but the row values should currently be treated as configuration values chosen by setup code, not as fully named semantic actor classes.

## Update: the far `EF:0EE8` source is a 10-entry event-flag-gated table

The latest local pass tightened the second source family substantially.

It is no longer best described as just “a small metadata/config value after validation.”

What the code now shows is:

- `EF:0EE8` loops `index = 0..9`
- each record is `20` bytes at `D5:F645 + index * 20`
- record word `0` is passed to `C21628`
- `C21628` is a direct event-flag test over the bitfield rooted at `$9C08`
- on success, the code stores the **loop index** to `$0A38`

So the strongest current statement is:

- row ids can come from ordinal sources
- row ids can also come from the matching index of a 10-entry event-flag-gated selector table
- row `0` still does **not** have good local proof as a player-only semantic id

The focused note is [selector-row-config-family-ef0ee8.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/selector-row-config-family-ef0ee8.md).


