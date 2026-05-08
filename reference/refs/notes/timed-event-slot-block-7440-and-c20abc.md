# Timed-Event Slot Block `7E:7440` And `C20ABC`

This note records the current local ROM-first picture around the managed text-event slot system that `0x1F D3` feeds, including the activation path and the bank-`02` snapshot/restore helpers.

See also [timed-delivery-row-index-command-1f-d3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-row-index-command-1f-d3.md).
See also [timed-delivery-controller-499-500-common.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-controller-499-500-common.md).
See also [timed-event-callback-family-bank01.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-family-bank01.md).
See also [timed-event-callback-invoker-c187cc.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-invoker-c187cc.md).

## Main result

The old `7E:7440` interpretation was too narrow by itself, and the exact role of low word `$7440` is still not fully settled. The bigger local picture is now:

- `0x1F D3` is a real bank-`01` text command (`C1:837B -> C1:8607`)
- `C1:8607` returns low word `$7440` through the shared leaf-return path at `C1:866B`
- a wider wrapper around `C1:871F` and `C1:866D` allocates or reuses a managed slot from a 10-entry ring at `97B8`
- those slots live at `96AA + 0x001A * index`
- the wrapper writes current payload words into the front of one of those `0x1A`-byte slot records
- a later activation branch snapshots current active-slot state into `slot + 6` and sets `slot + 4 = 1`
- once active, `C1:869D` promotes `slot + 6` into `C20ABC`

So the timed-event path is no longer just ?write something to `7440`.? It is a real queued slot workflow inside bank `01`, but the precise semantic role of the `$7440` leaf payload is still open.

The strongest new local clue is that `C1:7440` is executable code, not data. Its body is a tiny adapter that does `TXA`, calls `EF:0EAD`, then returns `0`. So the `D3` leaf now looks much more like a queued callback selector than a raw control-block base.
The manager region around `C1:80B2` also appears to choose between several sibling low-word adapters such as `61F0`, `7274`, `7440`, and `7708`, which makes this look like a small callback family rather than a one-off delivery hook.

## Xref anchors from the generic scanner

The new all-bank xref pass already tightened this model in a useful way:

- `C1:8607` is directly reached from `C1:8380`
- `C1:866D` currently has one direct local caller pinned by control-flow scan: `C1:8736`
- `C1:869D` currently has one direct local caller pinned the same way: `C1:8B1C`
- `C1:4012` is directly reached from `C1:871F`
- `C20A20` has 13 direct `JSL` callers in bank `01`
- `C20ABC` has 12 direct `JSL` callers in bank `01`

That caller spread matters because it makes the slot family look broader than the timed-delivery scripts alone. The `0x1F D3` path is using a shared bank-`01` managed text-event slot system rather than a delivery-only private queue.

## Slot allocation

`C14012` is a ring allocator:

- it increments `97B8`
- wraps it through a 10-entry range
- returns `96AA + 0x001A * index`

`C14049` is the matching reverse step that decrements the same ring index.

The slot size is therefore `0x1A` bytes.

## What `0x1F D3` contributes

The bank-`01` leaf for `0x1F D3` is still important:

- `C1:837B` compares the `0x1F` subcommand against `#$00D3`
- on match it jumps to `C1:8607`
- `C1:8607` returns callback low word `$7440` through `C1:866B`
- `C1:7440` is a tiny adapter that does `TXA ; JSL EF:0EAD ; LDA #0 ; RTS`
- the wider wrapper at `C1:871F` then allocates a managed slot and passes that slot base to `C1:866D`
- `C1:866D` writes the current payload words into `slot + 0/+2` and clears `slot + 4`

For the observed delivery scripts, the command is used as `[1F D3 xx]`, and the safest current read of the script byte is still:

- `xx` = 1-based timed-delivery row selector

The script-side row mapping is still strong, and the callback interpretation is now strong too. The remaining local gap is the exact manager path that later invokes `$7440` and supplies it with the row selector in `X`.

## What the wider wrapper adds

The newly inspected `C1:870A..8754` wrapper does more than blindly allocate a slot. It appears to do a reuse-or-queue decision over the current payload pair:

- if the current payload pair matches the already active pair, it copies that pair into `$2A/$2C` and jumps straight to the later bank-`01` handler path
- otherwise it allocates a new `0x1A` slot through `C14012`
- it writes the current payload pair into the new slot through `C1866D`
- if allocation or write returns `0`, it falls back to the older `$16/$18` pair before continuing

So this manager is not just a dumb queue. It is already trying to reuse the active payload pair before it allocates a new queued record.

## What `C1:866D` does

`C1:866D` is the generic slot-front writer shared by several neighboring `0x1F` handlers.

For an input base address `A = slot_base`, it does:

- `slot + 0` <- current payload word `1`
- `slot + 2` <- current payload word `2`
- `slot + 4` <- `0`

So this helper initializes the front of the managed slot and clears its activation word. The payload words can be the low-word values returned by the nearby `0x1F` leaf handlers, not just raw script bytes.

## The activation write we were missing

The missing `slot + 4` transition is now pinned locally.

In the bank-`01` helper at `C1:795E`:

- it takes `Y`
- computes `Y + 6`
- calls `C20A20`
- then writes `#$0001` to `slot + 4`

This is the cleanest local activation path found so far. It means the slot becomes active only after a state snapshot has been written into its back half.

## What `C20A20` does

`C20A20` is the missing snapshot helper.

For input `A = slot + 6`, it writes:

- `slot + 6 + 0` <- current `$8958`
- `slot + 6 + 2` <- current `865E+` field
- `slot + 6 + 4` <- current `8660+` field
- `slot + 6 + 6` byte <- current `8662+` field
- `slot + 6 + 7` <- current `8663+` field
- `slot + 6 + 9` <- current `8665+` field

So the back half of the `0x1A` slot record is a saved snapshot of the current active-slot/object state.

## What `C20ABC` does

`C20ABC` is the matching restore/apply helper.

When `C1:869D` sees that `slot + 4` is nonzero, it calls `C20ABC` with `A = slot + 6`.

`C20ABC` then:

- reads the saved slot id from `slot + 6 + 0`
- maps it through `$88E4` and `C08FF7` selector `#$0052`
- restores the saved snapshot fields back into the live `865E+` structure family

So `C20A20` and `C20ABC` are now a real save/restore pair over the same slot-back-half layout.

## Current slot sketch

Current best working layout for one `0x1A` record at `96AA + 0x1A * n`:

- `+0x00` = primary queued payload word, likely including callback low words for deferred `0x1F` handlers
- `+0x02` = secondary queued payload word
- `+0x04` = activation/status word
- `+0x06` = saved current slot id
- `+0x08` = saved `865E+` field
- `+0x0A` = saved `8660+` field
- `+0x0C` = saved `8662+` byte
- `+0x0D` = saved `8663+` word
- `+0x0F` = saved `8665+` word
- `+0x11..+0x19` = still unresolved in this pass

## Best current interpretation

The current safest model is:

1. `[1F D3 xx]` participates in the bank-`01` timed-event slot system
2. a `0x1A` slot is allocated from the `96AA` ring
3. the current leaf-selected payload words are written into `slot + 0/+2`
4. `C20A20` snapshots current active-slot state into `slot + 6`
5. `slot + 4` is set to `1`
6. `C1:869D` later notices the active slot and calls `C20ABC` on `slot + 6`
7. `C20ABC` restores/applies that saved state through the broader `$88E4 / $8958 / C08FF7` object system

So the remaining local gap is no longer how the slot becomes active or how callback payloads are invoked. `C1:87CC` now gives us the execution step. The next real unknown is how the manager chooses the `X` value and callback low word for each queued slot, and how those front-half callback payloads interact with the restored back-half object snapshot.

The new xref pass also makes one negative conclusion safer: whatever this family is called semantically, it is almost certainly shared infrastructure in bank `01`, not a delivery-only helper glued on top of the text engine.
