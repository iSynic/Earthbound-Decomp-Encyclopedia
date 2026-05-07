# C2 Loaded Battle Background Frame Generator Runtime Polish

This note records the byte-neutral C2 loaded battle-background frame generator
polish slice. It promotes the cautious runtime contract for `C2:C92D`, the
`GENERATE_BATTLEBG_FRAME` helper that consumes loaded background structs seeded
by `LOAD_BATTLE_BG`.

Primary source modules:

- `src/c2/c2_c8c8_load_final_prayer_finale_tilemap_state.asm`
- `src/c2/c2_c92d_run_final_prayer_finale_record_player.asm`

Related evidence notes:

- `notes/c2-battle-bg-load-update-runtime-polish.md`
- `notes/c2-battle-bg-palette-runtime-polish.md`
- `notes/battle-background-scene-bundles.md`
- `notes/c2-final-prayer-runtime-polish.md`

## Display Setup Helper

`C2:C8C8` carries the inherited `LOAD_ENEMY_BATTLE_SPRITES` alias, but the
decoded body is a presentation/tilemap setup helper:

- sets BG mode `9`
- configures BG1/BG2 screen bases
- configures OBJ size/base with `0x61`
- clears a scratch byte at `$7F:8000`
- queues an 0x800-byte tilemap transfer to VRAM `$7C00`

The true enemy battle sprite loader is documented separately in
`notes/c2-battle-sprite-runtime-polish.md`.

## Frame Generator Inputs

`C2:C92D` receives:

- A = loaded background struct base (`$ADD4` or `$AE4B`)
- X = layer index used by lower C0 layer/effect helpers

The routine is called both by `LOAD_BATTLE_BG` setup paths and by the
per-frame battle-background updater. It is therefore best read as the runtime
consumer of the `loaded_bg_data` struct, not as a Final Prayer-only helper.

## Consumed Struct Fields

Promoted field roles:

- `+0x00`: target BG layer/register family
- `+0x02`: freeze or skip palette-scrolling lane
- `+0x03`: palette shifting style
- `+0x04..0x07`: palette-cycle ranges
- `+0x08..0x09`: palette-cycle indices
- `+0x0A..0x0B`: palette-change speed/duration countdown
- `+0x0C..0x2B`: current palette
- `+0x4C`: displayed palette pointer
- `+0x4E..0x52`: scrolling movement ids and index
- `+0x53`: scrolling movement duration countdown
- `+0x55..0x60`: scroll position, velocity, and acceleration fields
- `+0x61..0x65`: distortion style ids and index
- `+0x66`: distortion duration countdown
- `+0x68..0x76`: active distortion/effect parameters

The scrolling lane reads CA rows rooted at `CA:F258`. The distortion lane reads
CA rows rooted at `CA:F708`.

## Runtime Effects

The helper has three major lanes:

- palette cycling: rotates current palette slots and mirrors through the
  displayed palette pointer at struct `+0x4C`
- scrolling movement: updates position/velocity/acceleration fields and writes
  BG offset registers according to target layer
- distortion/effect: loads distortion rows, advances effect parameters, and
  calls C0 layer-effect helpers to update HDMA/effect state

This is the deeper interpreter behind the `C2:DB3F` per-frame update call to
`C2:C92D`.

## Decomp Value

This slice gives the battle-background asset contract a runtime consumer:

- `BG_DATA_TABLE` scrolling and distortion row references are now tied to the
  frame generator that advances them
- loaded-bg struct offsets have stable reader/writer roles
- palette, scroll, and distortion lanes are separated for future naming
- the misleading inherited `LOAD_ENEMY_BATTLE_SPRITES` alias at `C2:C8C8` is
  documented without renaming source labels prematurely

## Remaining Soft Spots

- exact final names for palette shifting styles
- final symbolic names for CA scrolling and distortion row formats
- precise semantics of the C0 layer-effect helpers called below `C2:C92D`
