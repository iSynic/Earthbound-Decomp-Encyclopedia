# Devil's Machine Ness Transform Sprite

## Current Mapping

The Devil's Machine / Giygas cutscene does generate a dedicated overworld sprite for the Ness-like transform image.

- EBText call site: `refs/EB-M2-Listing-v1/US/bank09.txt` around `C9:C2BD`.
- Text command: `EBTEXT_GENERATE_ACTIVE_SPRITE OVERWORLD_SPRITE::GIYGAS_TO_NESS_TRANSFORM, EVENT_SCRIPT::EVENT_548, $01`.
- Sprite enum: `GIYGAS_TO_NESS_TRANSFORM ;370` in `include/constants/overworldsprites.asm`.
- Action script: `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/548.asm`.

`EVENT_548` places the sprite at `$1080,$0368`, sets priority `$03`, installs the simple physics callback, then cycles displayed poses:

1. up for 1 second
2. right for 1 second
3. down for 1 second
4. left for 1 second

That means the visible "transform" is not derived from the Devil's Machine battle background at runtime. It is an active overworld entity whose display pose is driven by normal action-script pose/direction commands.

## Palette Path

Correction: the final in-game colors are tied to the current map palette setting, not only the fixed default overworld sprite palette table.

There are two layers:

- Sprite grouping header byte `+3` carries the OAM palette selector, decoded in our notes as `(byte >> 1) & 7`.
- The loaded map palette setting carries a `Sprite Palette` / sprite-subpalette metadata value that controls which map-palette subpalette is used for sprite colors in that scene.

For Giygas's little room, EBME reports tileset `0`, palette group `0`, palette/variant `3`, with `Sprite Subpalette: 2`. Our contract agrees:

- `notes/map-fts-palette-variant-contract.json` row `03`
- `asset.da.map_data_palette_0`
- `tileset_id: 0`
- `variant: 3`
- `setting_summary.sprite_palette: 2`
- reserved metadata word `32` has `role: sprite_palette`, ROM word `2`

EBME's confusing display means "sprite subpalette value 2 selects map-palette subpalette 0" for these colors. So the transform sprite's OAM palette slot is still chosen by the overworld sprite grouping, but the actual colors in that slot come from the active map palette's sprite-subpalette selector for the final area.

### Palette Sanity Check

The extracted palette data confirms EBME's row for palette group `0`, variant `3`, subpalette `0`:

| Palette index | Hex |
| --- | --- |
| 0 | `#000000` |
| 1 | `#F7F7F7` |
| 2 | `#B58C84` |
| 3 | `#CE8CAD` |
| 4 | `#7B6B8C` |
| 5 | `#6B84EF` |
| 6 | `#420800` |
| 7 | `#C6EFC6` |
| 8 | `#B5CEAD` |
| 9 | `#ADC694` |
| 10 | `#9C8C73` |
| 11 | `#845A73` |
| 12 | `#633963` |
| 13 | `#52215A` |
| 14 | `#AD7329` |
| 15 | `#000000` |

So the blue and green entries are really present in the final room's sprite-facing map palette. However, the rendered CoilSnake group image for sprite group `370` uses default sprite palette `4` color slots `2,3,4,6,10,11,12,13`. Projected onto the final-room map palette above, those slots avoid the blue and green entries (`5`, `7`, `8`, `9`) and land on the warm/purple/brown/tan colors used by the transform art.

## Still Open

We have the call site and action script, but the generated knowledgebase does not yet expose a full art-facing frame contract for `OVERWORLD_SPRITE::GIYGAS_TO_NESS_TRANSFORM`. Map-object usage notes only cover placed NPC/object rows, so this EBText-generated sprite does not show up as a map placement.

Next useful trace:

- Decode pointer-table entry `SPRITE_GROUPING_PTR_TABLE[370]` from `EF:133F`.
- Record its grouping header, bank byte, runtime slot pointer words, size, and palette ID.
- Join those slots to the D1-D5 `SPRITE_####` payloads and generated preview PNGs.
- Teach the preview/harness path to resolve composed overworld sprite previews against the active map palette setting's `sprite_palette` metadata when a scene context is known.

## Nearby Trap

`asset.d3.sprite_0370` is a raw sprite payload at `D3:0C00..D3:0CC0`, but do not confuse that with overworld sprite/group ID `370`. The same raw asset is also used as a frame in the normal `MOM` sprite group. `GIYGAS_TO_NESS_TRANSFORM ;370` is the generated entity's sprite/group ID, while `SPRITE_0370` is one graphics payload label.
