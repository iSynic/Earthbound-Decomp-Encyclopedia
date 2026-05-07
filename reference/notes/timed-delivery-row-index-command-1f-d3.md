# Timed Delivery Row Index Command `1F D3`

This note records the script-side command pattern that selects individual timed-delivery rows, and the newly pinned local bank-`01` handler behind it.

See also [timed-delivery-controller-499-500-common.md](notes/timed-delivery-controller-499-500-common.md).
See also [timed-delivery-system-flags-754-779.md](notes/timed-delivery-system-flags-754-779.md).
See also [timed-delivery-special-row-02a3.md](notes/timed-delivery-special-row-02a3.md).
See also [timed-event-slot-block-7440-and-c20abc.md](notes/timed-event-slot-block-7440-and-c20abc.md).
See also [timed-event-callback-invoker-c187cc.md](notes/timed-event-callback-invoker-c187cc.md).

## Main result

The extracted script byte pattern `[1F D3 xx]` now lines up cleanly with the ten rows of `D5:F645`.

The low byte `xx` is not behaving like a general event id. It behaves like a 1-based timed-delivery row selector.

That script-side read is now backed by a real local handler:

- `ebsrc` names `0x1F D3` as `EBTEXT_TRIGGER_TIMED_EVENT`
- the local `0x1F` subcommand tree compares `#$00D3` at `C1:837B`
- that branch jumps to `C1:8607`
- `C1:8607` does not write the slot directly; it returns low word `$7440` through the shared leaf-return path at `C1:866B`
- a wider bank-`01` wrapper around `C1:871F` / `C1:866D` then decides whether to reuse or allocate a managed slot and writes the current payload words into that slot record

So `[1F D3 xx]` is no longer just a script-pattern guess. It is a real bank-`01` text command, but the exact local bridge between the script byte `xx` and the later managed-slot payload still runs through an additional bank-`01` wrapper layer.

A fresh xref pass tightens the surrounding local path too:

- `C1:8607` is directly reached from `C1:8380`
- `C1:866D` is directly called from `C1:8736`
- `C1:4012` is directly called from `C1:871F`
- `C1:869D` is directly called from `C1:8B1C`

So the command now has a cleaner local pipeline: select the `D3` subcommand leaf, carry low-word payload data through the shared bank-`01` wrapper, allocate or reuse a managed slot, and later poll/promote that same slot through the shared bank-`01` machinery.

The strongest new local clue is the leaf payload itself. The low word returned by `C1:8607` is `C1:7440`, and that tiny bank-`01` routine is not data-shaped at all. We can now also place its invoker locally: `C1:87CC` uses an RTS-as-JSR trick to call the low word currently held in `Y`.

`C1:7440` itself is:

- `REP #$31`
- `TXA`
- `JSL EF:0EAD`
- `LDA #$0000`
- `RTS`

That makes `$7440` read much more strongly as a queued callback entry than as a raw control-block address. It also gives the timed-delivery family its first direct local bridge back out of bank `01`: when that callback runs, it forwards the current `X` value to `EF:0EAD`, the helper we already mapped as the chosen-row delivery sprite/placeholder instantiator.

This adapter is now source-backed in `src/c1/c1_7440_timed_delivery_row_selector_callback.asm` as `TimedDeliveryRowSelectorCallback`.

Source polish follow-up (2026-05-06): that source now calls `EF:0EAD` by the
`InstantiateDeliveryRowSpriteOrPlaceholder` helper name, matching the row
sprite/placeholder contract used by the EF delivery selector cluster.

## Row mapping

The currently pinned cases are:

- `[1F D3 01]` + `set(flag 180)` -> row `0` -> pizza
- `[1F D3 02]` + `set(flag 181)` -> row `1` -> Escargo
- `[1F D3 03]` + `set(flag 645)` -> row `2` -> alternate Escargo
- `[1F D3 04]` + `set(flag 446)` -> row `3` -> customer A
- `[1F D3 05]` + `set(flag 646)` -> row `4` -> customer B
- `[1F D3 06]` + `set(flag 647)` -> row `5` -> customer C
- `[1F D3 07]` + `set(flag 648)` -> row `6` -> customer D
- `[1F D3 08]` + `set(flag 675)` -> row `7` -> special Mach-Pizza-Guy / Zombie Paper case
- `[1F D3 09]` + `set(flag 694)` -> row `8` -> special Escargo case
- `[1F D3 0A]` + `set(flag 695)` -> row `9` -> special Escargo case

So the safest current read is:

- `[1F D3 n]` selects timed-delivery row `n - 1`

## Local handler details

The common helper at `C1:866D` is shared by several neighboring `0x1F` subcommands. In the managed-slot path we have pinned locally, it does not write directly to a hardcoded `7E:7440` control block. It writes the current payload words into the allocated `96AA + 0x1A * index` slot record, clearing `slot + 4` as part of that initialization.

For the observed timed-delivery scripts, the command is only used as `[1F D3 xx]`, so the safest current read is still:

- the script byte `xx` is a 1-based timed-delivery row selector
- the local `D3` leaf contributes callback low word `$7440` into the wider bank-`01` command wrapper
- `C1:7440` itself is a tiny adapter that forwards `X` into `EF:0EAD` and returns `0`
- the exact slot-consumer path that later invokes that callback is still unresolved locally

So the script-side row mapping is strong, but the old note that treated `$7440` as a directly observed WRAM row-selector slot was too specific.

## Why this matters

This is stronger than a thematic match because the mapping is exact across all ten row families we currently know, and the local text engine now exposes the command as a real timed-event trigger path.

That gives us a clean script-side model:

1. phone or setup script chooses a timed-delivery row with `[1F D3 xx]`
2. the bank-`01` text handler selects the `D3` leaf and feeds callback low word `$7440` into the shared wrapper path
3. the same script sets the matching row-specific pending flag
4. the same script usually also sets `flag 754` (`FLG_SYS_DISTLPT`)

That gap is now mostly closed. The bank-`01` callback setup at `C1:87A7` loads the first byte of the current callback payload stream into `$14`, and `C1:87CC` copies `$14` into `X` just before invoking `C1:7440`. So the current safest local read is: the first callback payload byte after `0x1F D3` becomes the 1-based row selector forwarded to `EF:0EAD`.

## Best current interpretation

The cleanest current interpretation is that `[1F D3 xx]` is the script command that arms or selects the active timed-delivery row, using a 1-based row number rather than a raw event id.

The exact local handler is now pinned, so the remaining uncertainty is no longer the command itself. It is the downstream consumer path that turns the queued bank-`01` slot payload into the timed-delivery controller state we see later in bank `EF`.
