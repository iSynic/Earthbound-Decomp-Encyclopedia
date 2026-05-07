# C3 Jeff Repair Source Contract `C3:F1EC`

This note promotes the Jeff repair helper at `C3:F1EC` into source-contract form and pairs it with the small C1 mapper at `C1:D038`.

See also [try-fix-item-callback-d0.md](notes/try-fix-item-callback-d0.md), [jeff-repair-item-name-bridge.md](notes/jeff-repair-item-name-bridge.md), and [item-byte-19-packed-class-and-slot.md](notes/item-byte-19-packed-class-and-slot.md).

## Working Names

- `C3:F1EC` = `TryRepairJeffBrokenInventoryItem`
- `C1:D038` = `MapBrokenItemToRepairedItem`

## `C3:F1EC` Entry Contract

- `A` = repair success threshold from the `1F D0 xx` callback argument

The only direct local caller is `C1:63BE`, from the `1F D0` try-fix-item callback path rooted at `C1:63A7`.

## `C3:F1EC` Behavior

The helper first checks whether party/overlay entry `3` is present through `C2:239D`. This is the Jeff-side gate: if that check returns `0`, the helper returns `0` without touching inventory.

It then scans up to 14 inventory bytes at `$9AAF..$9ABC`. For each nonzero item id, it resolves the item row in `D5:5000` using stride `0x27`.

For a candidate to repair:

- item byte `+0x19` must equal `8`, matching the broken-item type in the reference item table
- item byte `+0x20` must be less than or equal to `$9AA7`, the current best local fit for Jeff's repair IQ/stat byte
- `C4:5F7B(0x63)` must return a value strictly less than the callback threshold in `A`

On success, the helper:

1. reads repaired item id byte `+0x21` from the same item row
2. writes that repaired item id back into the matched inventory slot at `$9AAF + slot`
3. returns the original broken item id

On failure, it returns `0`.

Source contract:

- return `0` if Jeff is absent or no candidate passes the gates
- otherwise mutate the matched inventory slot from broken item id to repaired item id
- return the original broken item id

## `C1:D038` Mapper

`C1:D038` maps the original broken item id back to its repaired item id by resolving the same `D5:5000` item row:

- if item byte `+0x19 == 8`, return byte `+0x21`
- otherwise return `0`

The only direct local caller is `C1:63C8`, immediately after `C3:F1EC` returns a nonzero broken item id.

## Text Staging Flow

`C1:63A7` stages both sides of the repair result:

1. call `C3:F1EC`
2. if the result is nonzero, call `C1:D038` to recover the repaired item id
3. stage the repaired item id through `C1:045D`
4. stage the original broken item id through `C1:0489`

The community control-code documentation says `[1F D0 xx]` attempts to fix Jeff's broken items, replaces the broken item with the fixed item, and stages the broken and fixed item names into the text memory slots. The local byte flow now corroborates that description directly: the inventory mutation happens in `C3:F1EC`, while `C1:63A7` and `C1:D038` build the paired text values consumed by the Jeff repair script's repeated `PRINT_ITEM_NAME 0x00` plus `{swap}` sequence.

## Reference Cross-Check

`refs/eb-decompile-4ef92/item_configuration_table.yml` shows the broken item rows with `Type: 8` and four argument bytes. For the broken item rows, argument byte `1` matches the repair IQ requirement, and argument byte `2` matches the repaired item id that local code reads from item byte `+0x21`.

Examples:

- Broken spray can: `Argument: [0, 1, 161, 0]`
- Broken laser: `Argument: [0, 24, 41, 0]`
- Broken bazooka: `Argument: [0, 45, 134, 0]`
- Broken antenna: `Argument: [0, 65, 48, 0]`

## Confidence

- `C3:F1EC` as mutating Jeff broken-item repair core: high confidence
- `C1:D038` as broken-item to repaired-item mapper: high confidence
- item byte `+0x20` as repair IQ requirement for broken items: high confidence
- item byte `+0x21` as repaired item id for broken items: high confidence
- exact identity of `$9AA7` as Jeff's displayed IQ versus a closely related repair stat byte: medium confidence
