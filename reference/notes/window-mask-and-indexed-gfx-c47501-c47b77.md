# Window Mask And Indexed GFX Cluster `C4:7501-C4:7B77`

## Scope

This cluster sits between the `C4:74F6` data include and the later
`system/load_window_gfx.asm` include in the ebsrc bank04 order. The local byte
shape ties it to the C4 window/HDMA helper note rather than to generic entity
logic: the routines stage generated window-edge streams in bank `$7F`, then
start channel-4 `WH0` or channel-5 `WH2` HDMA through the already-named helpers
at `C4:245D`, `C4:2542`, `C4:25CC`, and `C4:25FD`.

The one cross-bank script clue is `C0:AA23`, the action-script wrapper just
after `ActionScript_FadeOutWithMosaic`, which calls `C4:7765`. That places at
least one member of this cluster in the mosaic/window-mask transition family.

## HDMA window-mask staging

`C4:74F6` is an 11-byte half-width/radius ramp table used by `C4:7501` while it
builds the current-entity WH window span stream:

```text
10 10 0F 0F 0E 0D 0C 0B 09 06 03
```

`C4:7501` clamps a vertical edge distance to `0..10`, indexes this table in
reverse, and uses each byte as the horizontal span radius around the current
entity's screen-relative X center. This gives the emitted WH stream a rounded or
tapered edge rather than a flat rectangle.

`C4:7501` writes a window-span byte stream to the caller-provided long pointer
in direct page `$22/$24`. The span is screen-relative: it reads the current slot
from `$1A42`, combines slot world position `$0B8E/$0BCA` with screen origin
`$0031/$0033`, clips around the byte window boundaries, and emits the resulting
edge bytes. Near the top/bottom it uses the `C4:74F6` span-radius ramp table;
the rest of the body emits full-width spans. This is the low-level current-entity
span writer used by the two per-entity HDMA starters.

`C4:76A5` double-buffers that stream in `$7F:0000` or `$7F:02FE` according to
the current slot's `$0E5E` low bit, calls `C4:7501`, starts channel-4 `WH0`
HDMA through `C4:25CC`, and increments `$0E5E`.

`C4:7705` is the channel-5 partner. It uses the same current-slot toggle field,
but stages into `$7F:05FC` or `$7F:08FA`, calls `C4:7501`, starts `WH2` HDMA
through `C4:25FD`, and increments `$0E5E`.

`C4:7765` uses a fixed `$7F:0BF8` stream buffer and then calls `C4:2542`, the
channel-4 `WH0` starter that leaves `WOBJSEL` alone. Its C0 caller context is
the fade-out-with-mosaic action-script strip, so this is best treated as a
mosaic/fade window-mask staging entry until the exact visual effect is named
from callsite behavior.

`C4:7866` is a compact coordinate clamp. `C4:7930` calls it four times to bound
incoming rectangle edges to the unsigned screen limits `#$00E0` and `#$0100`.

`C4:789E` appends one run descriptor to the long pointer in direct page
`$1F/$21`. It handles zero length, short runs, and long runs by splitting at the
`#$7F` descriptor boundary.

`C4:7930` is the higher-level rectangular mask builder. It toggles between
`$7F:0000` and `$7F:02FE` using `$9E3A`, clamps the incoming box bounds with
`C4:7866`, emits the three run descriptors through `C4:789E`, terminates the
stream, starts channel-4 `WH0` HDMA with `C4:245D`, and increments `$9E3A`.

`C4:79E9` derives a centered rectangle from the current entity's position and
screen origin, then delegates to `C4:7930`.

`C4:7A27` builds a related rectangle from the base slot in `$9889` and the
current slot. It adjusts the vertical screen origin to current-slot Y minus
`#$70`, compares the base slot against that origin, and then delegates to
`C4:7930`.

`C4:7A6B` is a small position helper, not an HDMA starter. It mirrors the
current slot's `$0BCA` Y coordinate around the current slot's `$1002` anchor or
target word.

## Indexed graphics load

`C4:7A9E` uses the current slot's `$0E5E` as an index into the pointer/table
family rooted at `$CC:2DE1`, decompresses the selected asset with
`C4:1A9E`, copies/uploads the decompressed data toward VRAM destination
`$6000`, and sets `$0030 = #$18`. The upload selector matches the existing
pattern where `$0030` requests a visual buffer transfer on the next NMI pass.

`C4:7B77` uses the same `$CC:2DE1` indexed source family, also involving the
current slot's `$0E9A`, and copies a `#$0700`-byte graphics block to `$7C00`.
It then reads the small metadata bytes at offsets `+6/+7` and returns a
variant/frame-like byte selected against `$0E9A`.

## 2026-05-06 source polish

The source comments now keep the window-mask stream contracts local to
`src/c4/window_mask_and_indexed_gfx_helpers.asm`. `$0E5E` is deliberately named
as a slot-local toggle-or-index field rather than a global animation variable:
`C4:76A5/C4:7705` use it for alternating WH0/WH2 stream buffers, while
`C4:7A9E/C4:7B77` use it as part of the indexed graphics record selection.

The adjacent `src/c4/window_gfx_load_and_flyover_undraw_helpers.asm` now carries
the same conservative boundary. `LOAD_WINDOW_GFX` is documented as a C4-owned
window-graphics cache rebuild that decompresses E0 assets into bank `$7F`,
stages/copies the tile blocks, rebuilds compact rows through the shared `$3492`
glyph scratch contract, and refreshes the palette/tile work used by later
window draws. `C4:7F87` is scoped to the `$0200` window-flavour palette block:
the lead-entity override source is `E0:2108` unless `$B4B6` suppresses it,
otherwise `$99CD` selects an `E0:1FB9` flavour row. `UNDRAW_FLYOVER_TEXT` is
limited to its local presentation side effects: BG2 screen-base queue arguments,
window graphics reload, glyph-run reset, palette refresh, and `$0030 = #$18`;
the raw `C2:038B` cleanup callee remains owned by C2.

2026-05-06 follow-up source polish: the window-mask source now carries local
names for current-slot and base-slot indexes, live world coordinates, camera
origin shadows, WH stream double buffers, box-mask toggle, `$CC:2DE1` indexed
graphics record roots, VRAM destinations, transfer sizes, and the `$0030/$003B`
presentation-refresh arguments. The C4-side contract is still intentionally
limited to generating WH0/WH2 streams and staging upload arguments; HDMA register
installation and renderer queue interpretation remain in their callee helpers.

2026-05-06 selector/latch follow-up: the indexed graphics loaders now split
the `$0030` display-selector latch from the `#$18` selector value, and rename
the local `$003B` use as a presentation-refresh latch rather than a BG-scroll
shadow. This keeps the source focused on the values C4 writes while leaving the
C0/NMI upload and refresh interpretation outside the contract.

The adjacent window-gfx source now uses the same local boundary for the cache
rebuild and flyover-undraw path: E0 source lows/banks, `$7F` work blocks,
tile-state clear/copy sizes, `$3492/$9E23/$9E25` glyph scratch fields,
window-flavour palette queue arguments, flyover BG2 screen-base values, glyph
run reset index, and `$0030 = #$18` selector write are named locally. The raw
`C2:038B` call is now a named C2 cleanup callee only in the sequencing sense;
C4 does not claim its internal cleanup contract.

2026-05-06 window-gfx selector/latch follow-up: the flyover-undraw source now
splits the `$0030` display-selector latch from the `#$18` window-gfx selector
value. `UNDRAW_FLYOVER_TEXT` still only sequences `C2:038B` before reloading the
window graphics cache; C2 owns the cleanup side effects, and C0/NMI owns the
later selector interpretation.

## Working Names

- `C4:74F6` = `WhWindowSpanRadiusRampTable`
- `C4:7501` = `WriteCurrentEntityWhWindowSpan`
- `C4:76A5` = `StageCurrentEntityWh0MaskAndStartHdma`
- `C4:7705` = `StageCurrentEntityWh2MaskAndStartHdma`
- `C4:7765` = `StageMosaicFadeWh0MaskAndStartHdma`
- `C4:7866` = `ClampCoordToUnsignedLimit`
- `C4:789E` = `AppendWhWindowRunDescriptor`
- `C4:7930` = `StageWh0BoxMaskAndStartHdma`
- `C4:79E9` = `StageCurrentEntityCenteredWh0BoxMask`
- `C4:7A27` = `StageBaseSlotRelativeWh0BoxMask`
- `C4:7A6B` = `MirrorCurrentEntityYAroundTarget1002`
- `C4:7A9E` = `LoadCurrentEntityIndexedWindowGfxToVram`
- `C4:7B77` = `LoadIndexedWindowGfxAndReadVariantByte`

## Confidence boundaries

### Locally proved

- the `C4:76A5` and `C4:7705` wrappers stage current-entity generated streams
  in bank `$7F` and start `WH0`/`WH2` HDMA respectively
- `C4:7930` generates a rectangular channel-4 `WH0` window mask stream and
  uses `C4:245D`
- `C4:7765` is reached from the mosaic fade action-script wrapper context and
  starts channel-4 `WH0` HDMA through `C4:2542`
- `C4:7A9E` and `C4:7B77` both consume the `$CC:2DE1` indexed graphics source
  family

### Still open

- the exact player-facing names of the visual effects driven by each mask
  starter
- the precise structure of the `$CC:2DE1` graphics metadata records
- whether `$0E5E` is purely a stream-buffer toggle in this family or also an
  animation/variant index for the graphics loaders
- the full C2-side cleanup behavior behind the raw flyover-undraw callee
