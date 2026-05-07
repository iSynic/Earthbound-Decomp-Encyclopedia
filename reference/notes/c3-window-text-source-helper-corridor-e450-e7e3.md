# C3 window/text source helper corridor `E450-E7E3`

## Purpose

This pass consolidates the early C3 `source-helper` corridor from the window tick transfer helper through the window allocation/close helpers and the reflected-hit article-token resolver.

The source/data map should treat these as ordinary 65816 helper routines, not event bytecode or raw data. The nearby data islands at `C3:E44C` and `C3:E84E` remain data/frontier rows.

## `C3:E450` - window tick dynamic tile transfer

Direct caller:

- `C1:0058`, inside the frame/window tick path at `C1:004E`, calls `C3:E450` only when `$89C9` is nonzero.

Routine shape:

- reads flag bits from `$0002`
- chooses one of two row offsets, `#$0008` or `#$0028`, based on bit `#$0004`
- builds a source pointer in bank `E0` rooted at `E0:1FC8`
- folds in the active character/table index from `$99CD` through the `E0:1FB9` row-offset table
- calls `C0:8ED2` with `A = #$0228` and `X = #$0008`
- writes byte `$18` to `$0030`

This matches the earlier tile-data note: `C3:E44C` is a four-byte prelude/data island, while `C3:E450` is a real routine reached by the window tick path. The current name is still accurate enough for source extraction.

## `C3:E4CA-E4E0` - instant-printing gate

The three small helpers are source-ready:

- `C3:E4CA` clears byte `$9622`
- `C3:E4D4` sets byte `$9622`
- `C3:E4E0` wraps `C1:2DD5` between those two helpers

That makes `C3:E4E0` the "tick text/window while instant printing is disabled" wrapper. It should remain a tiny source routine rather than being folded into C1.

## `C3:E4EF` - first free window slot

Direct caller:

- `C1:0528`, in the window creation/open path, calls `C3:E4EF`; if it returns `FFFF`, the caller jumps to the open-window failure path. Otherwise the caller uses the returned slot to build and link a `$8650` window record.

Routine shape:

- scans slots `0..7`
- uses `C0:8FF7(selector #$0052)` to stride over `$8650` window records
- returns the first slot whose `$8654 + slot*0x52` field is `FFFF`
- returns `FFFF` if all eight slots are occupied

The existing `FindFirstFreeWindowSlot` name is source-ready.

## `C3:E521` and `C3:E7E3` - close/free window and registered-copy cleanup

`C3:E521` is the larger close/free path for one window id. Its local work is now clear enough for source extraction, and the source-unit shape is pinned in [c3-window-lifecycle-source-contract-e4ef-e6f7.md](notes/c3-window-lifecycle-source-contract-e4ef-e6f7.md): keep `C3:E4EF` and `C3:E521` as two callable labels in the same source module.

- reject `FFFF` input and unmapped `$88E4` entries
- clear `$8958` if the closed window was focused
- call `C3:E7E3` to clear any registered text-entry/copy chain
- unlink the window from the `$88E0/$88E2` open-window chain and neighboring `$8650/$8652` prev/next fields
- mark `$8654` and the `$88E4` slot as free by writing `FFFF`
- clear the window tile/content region back to `$0040`
- clear backing tile/state words in the `$7DFE` tilemap region
- mark the presentation layer dirty before returning

`C3:E7E3` is the focused cleanup helper it calls. Direct callers are `C1:1388` from the text-entry allocator path and `C3:E555` from `C3:E521`.

`C3:E7E3`:

- rejects input `FFFF`
- maps window id through `$88E4`, then resolves the `$8650` record with selector `#$0052`
- if record field `+2B` has a linked record index, walks the `$89D4` record chain with selector `#$002D`
- clears each record's first word
- resets window record fields `+2B/+2D/+2F` to `FFFF`
- sets fields `+31/+33` to `1`

This confirms `C3:E7E3` as registered-copy/text-entry cleanup, not a generic memory clear.

## `C3:E75D` - reflected-hit side article-token resolver

Direct callers:

- `C1:2120` calls `C3:E75D` with `A = 0`
- `C1:7EA2` calls `C3:E75D` with `A = 0`
- `C1:7EC9` calls `C3:E75D` with `A = 1`

The simple disassembler loses accumulator-width tracking in the middle of this routine, but the byte pattern and existing reflected-hit notes are consistent:

- `A = 0` selects the first-side state through `$9658` and `$5E77`
- `A = 1` selects the second-side state through `$965A` and `$5E78`
- if the selected side id is `FFFF`, the matching `$5E77/$5E78` flag is cleared
- otherwise, the selected side id is resolved through the `D5:9589` enemy descriptor table
- the routine chooses between the small `C2:0998` and `C2:099C` text fragments based on `$5E76`
- it dispatches through `C4:47FB`

That keeps `ResolveReflectedHitSideArticleTokens` as the right source-level name, while the exact text-control token semantics remain anchored in the reflected-hit token notes.

## Working Names

- `C3:E450` = `WindowTickTransferDynamicTileBlock`
- `C3:E4CA` = `ClearInstantPrinting`
- `C3:E4D4` = `SetInstantPrinting`
- `C3:E4E0` = `TickWindowWithoutInstantPrinting`
- `C3:E4EF` = `FindFirstFreeWindowSlot`
- `C3:E521` = `CloseWindowAndReleaseTileState`
- `C3:E75D` = `ResolveReflectedHitSideArticleTokens`
- `C3:E7E3` = `ClearWindowRegisteredCopyChain`

## Remaining questions

- `C3:E450` still needs the exact player-facing identity of the `E0:1FC8` tile/source region and the `E0:1FB9` row-offset table.
- The close/free path at `C3:E521` is source-ready. Final field names for `$8650` record offsets should still come from the eventual window-record struct pass, but that is no longer a source-queue blocker.
- `C3:E75D` should not be renamed more tightly until the `C4:47FB` text-control helper and the `C2:0998/C2:099C` fragments are represented in source comments.
