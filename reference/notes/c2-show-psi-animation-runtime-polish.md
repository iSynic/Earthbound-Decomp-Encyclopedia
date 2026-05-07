# C2 Show PSI Animation Runtime Polish

This note records the byte-neutral C2 `SHOW_PSI_ANIMATION` setup polish slice.
It complements `notes/c2-psi-animation-runtime-polish.md`, which documents the
per-frame `C2:E6B6` consumer of the state seeded here.

Primary source module:

- `src/c2/c2_e116_run_battle_visual_flash_and_bg_effect_body.asm`

Related evidence notes:

- `notes/psi-animation-bundle-contracts.md`
- `notes/c2-psi-animation-runtime-polish.md`
- `notes/c2-battle-bg-palette-runtime-polish.md`
- `notes/c2-battle-sprite-runtime-polish.md`
- `notes/battle-visual-asset-contracts.md`

## Setup Contract

`SHOW_PSI_ANIMATION` receives a PSI animation id in A and indexes the 12-byte
`PSI_ANIM_CFG` rows rooted at `CC:F04D`.

The setup body:

- loads the compressed graphics set selected by config bytes `0..1`
- handles the 2bpp and alternate tile upload paths
- copies the selected 4-color PSI palette from `CC:F47F + id*8` into `$1BAA`
  and the displayed palette buffer rooted at `$1BCA`
- stores the decompressed arrangement stream pointer in `$1BA1/$1BA3`
- arms frame ticking by setting `$1B9E = 1`
- loads the compressed arrangement payload selected by `PSI_ANIM_POINTERS`
- dims battle-background palettes through `C2:DE0F`

## Seeded State

The promoted config/state joins are:

| Config byte | Runtime field | Role |
| ---: | --- | --- |
| `2` | `$1B9F` | frame hold reload |
| `3` | `$1BA8` | palette animation timer reload |
| `4` | `$1BA5` | palette animation first slot |
| `5` | `$1BA6` | palette animation last slot |
| `6` | `$1BA0` | frame count |
| `7` | target-mode branch | affected enemy-row selection |
| `8` | `$1BCC` | enemy-color change timer |
| `9` | `$1BCE` | enemy-color restore/alternate timer |
| `10..11` | `$1BD0/$1BD2/$1BD4` | BGR555 target color components |

The per-frame animation tick consumes `$1B9E..$1BD4`; the enemy sprite palette
wave helpers consume `$AEE7` and the color timer fields.

## Target Modes

Config byte `7` selects how the effect marks enemy sprite rows:

- `0` and `3`: center on the current enemy row position
- `1`: mark active enemies sharing the current target's row
- `2`: mark all active enemy rows with a fixed vertical offset

Marked rows receive row `+0x4B = 1` and their loaded sprite slot sets the
corresponding `$AEE7` color-wave group marker.

## Decomp Value

This slice closes the producer side of the PSI animation runtime contract:

- CC config rows now have source-commented consumers
- palette and arrangement pointer joins are tied to live state fields
- battle-background dimming and enemy sprite color-wave marking are documented
  as part of the PSI setup path
- `C2:E6B6` can be read as the frame consumer rather than the initializer

## Remaining Soft Spots

- final symbolic names for target-mode values
- exact names for the two tile upload layouts
- deeper decomposition of the alternate tile repacking loop
