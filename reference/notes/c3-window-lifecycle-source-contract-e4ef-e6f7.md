# C3 Window Lifecycle Source Contract `C3:E4EF..E6F7`

This note closes the `source-ready-large` caveat for the addressed include row `C3:E4EF`. The row should be emitted as one window-lifecycle source unit with two public entry labels.

## Working Names

- `C3:E4EF` = `FindFirstFreeWindowSlot`
- `C3:E521` = `CloseWindowAndReleaseTileState`

## Unit Shape

The reference include row `unknown/C3/C3E4EF.asm` spans `C3:E4EF..E6F7` and contains:

| Address | Role |
| --- | --- |
| `C3:E4EF` | public helper that scans for a free window slot |
| `C3:E521` | public helper that closes/releases a mapped window slot |
| `C3:E6F4` | shared close helper epilogue |

The source extraction queue should keep `C3:E521` as an internal/public label inside the same source file rather than trying to carve a separate include. The two helpers share the same window-record state family, and the reference bankconfig already groups them.

## `FindFirstFreeWindowSlot`

Entry:

- no meaningful input

Behavior:

- scans logical window slots `0..7`
- maps each slot through `C0:8FF7(selector = 0x52)`
- checks `$8654 + slot * 0x52`
- returns the first slot whose field is `0xFFFF`
- returns `0xFFFF` if all eight slots are occupied

Direct caller:

- `C1:0528`, in the open/create-window path

## `CloseWindowAndReleaseTileState`

Entry:

- `A` = logical window id/slot, or `0xFFFF` for no-op

Behavior:

1. Reject `0xFFFF`.
2. Map the logical window id through `$88E4`; reject unmapped entries.
3. If the window is focused in `$8958`, clear `$8958` to `0xFFFF`.
4. Call `C3:E7E3` to clear registered copy/text-entry chains.
5. Relink the open-window list rooted at `$88E0/$88E2` through record fields `$8650/$8652`.
6. Mark the record free by writing `0xFFFF` to `$8654 + record`.
7. Clear the `$88E4` logical-slot mapping for the closed id.
8. Clear the visible/content tile words for the window back to `0x0040`.
9. Clear backing tile/state words in the `$7DFE` tilemap region.
10. Call `C4:5E96`, then clear any associated `$894E` mapping referenced by record byte `$868B`.
11. Clear record byte `$868B`, set redraw/dirty flag `$9623 = 1`, and clear `$5E7A` if it points at the closed window.
12. If global close-drain latch `$5E70` is clear, tick the window system without instant printing through `C3:E4E0`, then clear instant printing through `C3:E4CA`.
13. Clear `$5E75` and return.

Known direct callers include:

- `C1:0084`, close focused window
- `C1:008E`, drain all queued/current windows
- `C1:93E7`, battle target-selection setup/cleanup path

## Source Translation Notes

This unit is large but not semantically blocked. A source version should:

- keep `FindFirstFreeWindowSlot` and `CloseWindowAndReleaseTileState` as two callable labels/functions in the same source module
- represent `0x52` as the window-record stride
- use symbolic names for `$88E0/$88E2/$88E4/$8958/$8650..` as the window-list and window-record fields where available
- leave exact final field names for `$8650` record offsets to the later window-record struct pass

The lack of final struct field names is not a source-extraction blocker because every offset touched by this unit is already locally described and the caller/side-effect shape is stable.

## Confidence

- `C3:E4EF` free-slot scan: high confidence
- `C3:E521` close/free-window lifecycle helper: high confidence
- Treating `E4EF..E6F7` as one source unit with two callable labels: high confidence
