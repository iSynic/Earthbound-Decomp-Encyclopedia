# C2 PSI Animation Runtime Polish

This note records the byte-neutral C2 PSI animation tick polish slice. It
promotes the runtime contract for the per-frame PSI frame/palette animator.

Primary source modules:

- `src/c2/c2_e6b3_advance_psi_animation_frame_and_palette_state.asm`
- `src/c2/c2_e6b6_advance_psi_animation_frame_and_palette_state_body.asm`

Related evidence notes:

- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`
- `notes/psi-animation-bundle-contracts.md`
- `notes/battle-visual-asset-contracts.md`

## State Block

`C2:E6B6` is the callable body. The three bytes at `C2:E6B3` are a source prefix
used by the tick body as the blank/clear tile source.

Promoted state-byte contract:

| Field | Role |
| --- | --- |
| `$1B9E` | frame timer |
| `$1B9F` | frame hold reload |
| `$1BA0` | frames remaining |
| `$1BA1` | current frame source pointer |
| `$1BA5..$1BA9` | palette animation range/index/timer fields |
| `$1BAA` | PSI palette source words |
| `$1BCA` | displayed palette buffer root |
| `$1BCC/$1BCE` | enemy-color or alternate-palette timers |

`SHOW_PSI_ANIMATION` seeds this state; the `E6B6` helper consumes it during the
battle visual tick.

## Frame Tick

When `$1B9E` is nonzero, the helper decrements it. On timer expiry:

- reload `$1B9E` from `$1B9F`
- if `$1BA0` is nonzero, upload `0x0400` bytes from the current `$1BA1` pointer
  to VRAM `$5800`
- advance the frame source pointer by `0x0400`
- decrement `$1BA0`
- if no frames remain, clear the larger `$5800` tile range and call the nearby
  visual cleanup helper

That makes this routine the frame consumer for the prepared PSI animation stream,
not the setup routine.

## Palette Tick

When `$1BA9` is nonzero, the helper decrements it. On timer expiry:

- reload the timer from `$1BA8`
- compute the inclusive palette range from `$1BA5..$1BA6`
- rotate by `$1BA7`
- copy words from `$1BAA` into the displayed palette buffer rooted at `$1BCA`
- advance and wrap `$1BA7`
- upload the changed palette range through `C0:856B(0x18)`

This ties the animation bundle palette fields to the live battle palette buffer.

## Enemy Color Timers

The final part of the helper services `$1BCC` and `$1BCE`.

- `$1BCC` expiry runs the `FAD8/FB35` helper family over active palette lanes
- `$1BCE` expiry restores active lanes through `FADE`

The exact names of those palette helpers remain intentionally provisional, but
the timer ownership and lane fanout are now source-commented.

## Decomp Value

This slice closes a runtime gap between asset contracts and battle visuals:

- `psi-animation-bundle-contracts.md` documents the extracted config rows
- source comments now document the consumer of frame hold, frame count, palette
  range, palette timer, and enemy-color timer fields
- VRAM destination `$5800` and per-frame `0x0400` source stride are explicit in
  the source module

## Remaining Soft Spots

- final symbolic names for `$1BCC/$1BCE`
- exact naming of the `FAD8/FB35/FADE` palette lane helper family
- whether the `C2:E6B3` source prefix should remain its own source-locked data
  unit or be folded into a later visual-data annotation pass
