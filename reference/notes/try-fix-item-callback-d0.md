# `1F D0` Try-Fix-Item Callback Family

This note captures the current local picture of the `0x1F D0` bank-`01` callback branch.

See also [timed-event-callback-family-bank01.md](notes/timed-event-callback-family-bank01.md).
See also [timed-event-callback-invoker-c187cc.md](notes/timed-event-callback-invoker-c187cc.md).
See also [jeff-repair-item-name-bridge.md](notes/jeff-repair-item-name-bridge.md).

## Main result

`0x1F D0` is now strongly anchored as the local `TRY_FIX_ITEM` branch inside the broader bank-`01` deferred text-command callback system.

The script-side proof is straightforward:

- `ebsrc` defines `EBTEXT_TRY_FIX_ITEM arg` as `.BYTE $1F, $D0, arg`.
- the `eb-decompile` script dump currently shows only two live `1F D0` uses
- both of those uses are in the Jeff-repair script family that prints `Working through the night, [Jeff] fixed the [broken item].` and `After being fixed, the [broken item] became the [fixed item].`
- the same script family sets `FLG_WINS_JEFF_REPAIR` (`flag 696`)

The two observed script calls are:

- `[1F D0 64]` in the first-time branch
- `[1F D0 19]` in the later branch reached once the Jeff-repair win flag is already set

So the safest current script-side read is: `1F D0` belongs to Jeff's broken-item repair flow, and its argument is some repair-specific parameter rather than a general row id like `1F D3`.

## Local callback bridge

The local `0x1F` subcommand tree compares `#$00D0` at `C1:8368` and branches to `C1:85E7`.

A fresh local xref pass plus the legacy disassembly address anchor show that this leaf resolves to low word `C1:63A7`, making the current callback path:

1. script uses `[1F D0 xx]`
2. the bank-`01` `0x1F` subcommand tree reaches the `D0` leaf at `C1:85E7`
3. the wider callback manager later invokes low word `C1:63A7` through the same `C1:87CC` RTS-as-JSR mechanism used by the `D3` timed-delivery branch

That makes `D0` another real member of the same callback framework, not a separate one-off text helper.

## Local state shape

The `C1:61F0 .. C1:6400+` branch family is noticeably more stateful than the tiny timed-delivery adapter at `C1:7440`.

The strongest local anchors are:

- shared byte-queue state at `$97BA / $97CA`
- helper bytes `$97BB` and `$97BC`
- a private scratch byte `$97D5`, currently only read at `C1:62F1` and written at `C1:6352` inside this branch family
- helper calls to `C4:3657`, `C4:35E4`, `C3:E4CA`, `C3:E4D4`, and `C0:D038`

That shape fits the script-side Jeff-repair reading well: this looks like a deferred broken-item resolver or repair-result builder, not a one-byte immediate action.

## Stronger local structure

The corrected ROM-level read of `C3:F1EC` plus the extracted item configuration table makes this callback family much less speculative than before.

The strongest current read is:

- `C1:63A7` calls `C3:F1EC` with the callback argument in `A`
- `C3:F1EC` resolves an item-like record through the shared `D5:5000` table using stride `0x27`
- it checks byte `+0x19` against `8`, which matches `ITEM::BROKEN` in the reference constants
- it reads bytes `+0x20` and `+0x21`, which the new table inspector confirms are the middle two bytes of the item record's `params` dword
- for broken items, those two bytes line up exactly with the extracted broken-item argument table: byte `+0x20` behaves like a repair IQ requirement and byte `+0x21` behaves like the repaired item id
- it compares byte `+0x20` against `$9AA7`, which is therefore very likely Jeff's live IQ or the immediate repair stat derived from it
- it then calls `C4:5F7B` with `A = #$0063` and compares the result against the callback argument stored in `$12`
- the immediate caller behavior now proves the paired text split: the success path feeds the broken-item id returned by `C3:F1EC` into `C1:D038`, and `C1:D038` maps it to the repaired item id through byte `+0x21`

That new item-table cross-check is especially useful because the extracted broken-item entries have the exact shape the local code suggests. For broken items, the `params` dword itself packs the bytes the local code is reading. The YAML view exposes them as four argument bytes that read naturally as:

- arg byte `0`: usually `0`
- arg byte `1`: repair IQ requirement
- arg byte `2`: resulting repaired item id
- arg byte `3`: usually `0`

So the local callback branch now looks much more like a real broken-item repair resolver than a generic Jeff-event helper. The newer C3 source-contract pass proves the split: `C3:F1EC` returns the successfully repaired broken-item id after replacing the inventory slot, and the immediate follow-up helper `C1:D038` derives the repaired item id from that broken item record for text staging.

## What is solid vs. still open

Solid now:

- `1F D0` is the `TRY_FIX_ITEM` text command
- its currently exposed script uses belong to the Jeff-repair broken-item flow
- it resolves into the same bank-`01` callback framework as the `D1`, `D2`, and `D3` branches
- `C1:63A7` is the low-word callback target for this branch
- the observed callback arguments `0x64` and `0x19` now behave very strongly like repair success thresholds
- in decimal, those are `100` and `25`, which matches the script-side first-time-versus-later split unusually well
- `C3:F1EC` now looks like the real broken-item repair core: broken-type check, IQ gate, probability gate, replace the matched inventory slot with the repaired item id, then return the original broken item id

Still open:

- the exact meanings of `$97BB`, `$97BC`, and `$97D5`
- whether `$9AA7` is literally Jeff's current IQ byte or a closely related derived repair stat
- the exact local split between the callback branch that chooses the repaired item and the later text-side branch that fills the `[1C 05 00]` placeholders
- the precise point where the callback family seeds the before-fix and after-fix item ids into the memory blocks that `SWAP_WORKING_AND_ARG_MEMORY` exchanges

## Best current interpretation

The safest current interpretation is that `1F D0` is the Jeff-repair member of the bank-`01` deferred text-command callback framework, and that `C1:63A7 -> C3:F1EC` is the core repair path. It now looks locally like: verify broken item, verify Jeff can repair it, roll a repair-success threshold from the callback argument, replace the matched inventory slot with the repaired item id on success, and return the original broken-item id. The immediate follow-up helper `C1:D038` maps that broken id back to the repaired item id for text staging. The newer text-side bridge work also makes it likely that those paired values are then consumed by the common `PRINT_ITEM_NAME 0x00` path, with `SWAP_WORKING_AND_ARG_MEMORY` providing the visible broken-item / repaired-item swap inside the Jeff-repair script.
