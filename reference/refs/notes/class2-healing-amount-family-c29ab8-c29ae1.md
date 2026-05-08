# Class2 Healing Amount Family C29AB8 C29AE1

This note captures the strongest current local model for the healing-amount helper at `C2:9AB8` and its four thin wrappers `C2:9AC6`, `C2:9ACF`, `C2:9AD8`, and `C2:9AE1`.

See also [class2-d57b68-battle-action-table-match.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-late-stat-and-resource-family-c28e42-c29e38.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-late-stat-and-resource-family-c28e42-c29e38.md).

## Main result

`C2:9AB8` is not best read as a timer or duration helper.

The stronger local model is:

- `C2:9AB8` = common healing-amount wrapper
- `C2:9AC6` = passes `0x0064`
- `C2:9ACF` = passes `0x012C`
- `C2:9AD8` = passes `0x2710`
- `C2:9AE1` = passes `0x0190`

Those values are then routed through `C2:6AFD` and handed to `C2:7294`, which behaves like a battler HP-target recovery helper with the usual consciousness and collapse-side guards.

## Why `C2:9AB8` is a healing helper

The body is compact and consistent:

- incoming `A` is copied to `X`
- `C2:6AFD` converts that fixed literal into the effective amount
- the current target row base from `$A972` is loaded into `A`
- `C2:7294` is called with the target row plus the computed amount

That shape is much more naturally read as "restore this much HP to the current battler" than as any timer-style helper.

## `C2:7294` behaves like the real HP recovery worker

`C2:7294` now has a stronger local read than before.

The body:

- requires battler `consciousness` at row `+0x0C` to be the live value `1`
- rejects battler affliction byte `+0x1D == 1`, the collapse or unconscious side
- adds the requested amount to battler `hp_target` at row `+0x13`
- clamps against battler `hp_max` at row `+0x15`
- writes the resulting value back through `C2:7126 / C2:7191`
- prints either a full-heal style message through `C1:DC1C` or an amount-bearing heal message through `C1:DC66`

That is a strong local fit for an HP recovery family rather than a generic state helper.

## Early action-table quartet

The strongest current action-table anchors are the early PSI entries:

- entry `32` -> `C2:9AC6` -> one-target PSI, cost `5`
- entry `33` -> `C2:9ACF` -> one-target PSI, cost `8`
- entry `34` -> `C2:9AD8` -> one-target PSI, cost `13`
- entry `35` -> `C2:9AE1` -> all-target PSI, cost `24`

That metadata progression is an unusually clean fit for the canonical `Lifeup` quartet:

- alpha = `100`
- beta = `300`
- gamma = effectively full heal via `10000`
- omega = `400`, all-target

Together with the `ebsrc` action files `lifeup_alpha.asm`, `lifeup_beta.asm`, `lifeup_gamma.asm`, and `lifeup_omega.asm`, this is strong enough to treat these as the best current local fits for the `Lifeup` family.

## Later table reuses

This helper family is not PSI-only.

Later table entries also reuse the same wrappers:

- entry `99` -> `C2:9AD8` -> one-target `other` full-heal reuse with the fuel-supply text `EF:7E88`
- entry `139` -> `C2:9AC6` -> one-target `item` healing reuse through the generic item-use script `C9:7B6B`
- entry `140` -> `C2:9AD8` -> one-target `item` full-heal reuse through the named-item wrapper `EF:8E27`
- entry `141` -> `C2:9AE1` -> all-target `item` healing reuse through the generic item-use script `C9:7B6B`

So the safest wording is not "the wrappers are Lifeup routines" in a global sense. The safer statement is:

- entries `32..35` are the canonical PSI-side `Lifeup` uses of the family
- later `other` and `item` entries reuse the same healing core with different presentation wrappers
- entry `99` is now a concrete full-heal reuse with the player-facing text "replenished a fuel supply!"
- entries `139`, `140`, and `141` are concrete item-side healing reuses, with `140` using the direct named-item text path and `139/141` using the broader food-or-item script at `C9:7B6B`

## Current safest interpretation

The safest current interpretation is:

- `C2:9AB8` is the common fixed-amount healing wrapper
- `C2:7294` is the corresponding HP recovery worker
- `C2:9AC6 / 9ACF / 9AD8 / 9AE1` are fixed-amount entry wrappers over that common helper
- early action-table entries `32..35` are the strongest current local fits for `Lifeup alpha / beta / gamma / omega`

## What is still open

Still open:

- the exact role of `C2:6AFD` in shaping the incoming literal before the heal is applied
- whether the later non-PSI reuses should be split into a distinct item-healing subfamily note later
- the exact role of the fuel-supply flavored full-heal reuse at entry `99` inside the broader enemy-action taxonomy

## Current takeaway

The safest current takeaway is:

- the older "timer-driven" wording for `C2:9AB8` was too weak and slightly misleading
- this family is better understood now as a real healing core
- the early PSI quartet around entries `32..35` is now in good enough shape to treat as the local `Lifeup` ladder

## Best next target

The best next move is to identify the later non-PSI reuses of `9AC6 / 9AD8 / 9AE1`, especially entry `99`, so the shared healing core can be cleanly split into PSI-side and item-or-other-side presentation families.

