# Map Collision Attribute Context

This context audit counts the third byte of each `.fts` arrangement cell in
actual sector scenes. The byte is still named cautiously: counts can expose
where it appears, but they do not by themselves prove collision semantics.

## Summary

- direct scenes sampled: `950`
- cells per scene: `1024`
- scene cells sampled: `972800`
- nonzero attribute cells: `603176`
- high-bit attribute cells: `522397`
- unique attribute values: `0x00`, `0x01`, `0x02`, `0x03`, `0x04`, `0x05`, `0x07`, `0x08`, `0x09`, `0x0B`, `0x0C`, `0x0D`, `0x0F`, `0x10`, `0x80`, `0x82`, `0x90`, `0x92`, `0x94`
- working model confidence: `medium-structural`
- runtime buffer anchor: `$01F800..$01FF7F current tileset collision data`

## Attribute Counts In Scene Use

| Value | Cell Count | Scene Presence |
| ---: | ---: | ---: |
| `0x00` | 369624 | 940 |
| `0x01` | 26104 | 646 |
| `0x02` | 2 | 2 |
| `0x03` | 25763 | 547 |
| `0x04` | 10879 | 54 |
| `0x05` | 198 | 25 |
| `0x07` | 10 | 5 |
| `0x08` | 9325 | 104 |
| `0x09` | 1451 | 74 |
| `0x0B` | 1660 | 60 |
| `0x0C` | 2734 | 50 |
| `0x0D` | 481 | 28 |
| `0x0F` | 1311 | 39 |
| `0x10` | 861 | 136 |
| `0x80` | 520402 | 937 |
| `0x82` | 238 | 47 |
| `0x90` | 1734 | 363 |
| `0x92` | 6 | 4 |
| `0x94` | 17 | 8 |

## Bit Family Counts

| Bit | Working Name | Cell Count | Scene Presence | Exact Values |
| ---: | --- | ---: | ---: | --- |
| `0x01` | `bit_0_low_modifier_candidate` | 56978 | 707 | `0x01`, `0x03`, `0x05`, `0x07`, `0x09`, `0x0B`, `0x0D`, `0x0F` |
| `0x02` | `bit_1_low_modifier_candidate` | 28990 | 587 | `0x02`, `0x03`, `0x07`, `0x0B`, `0x0F`, `0x82`, `0x92` |
| `0x04` | `bit_2_low_modifier_candidate` | 15630 | 99 | `0x04`, `0x05`, `0x07`, `0x0C`, `0x0D`, `0x0F`, `0x94` |
| `0x08` | `bit_3_low_modifier_candidate` | 16962 | 111 | `0x08`, `0x09`, `0x0B`, `0x0C`, `0x0D`, `0x0F` |
| `0x10` | `bit_4_special_surface_modifier_candidate` | 2618 | 416 | `0x10`, `0x90`, `0x92`, `0x94` |
| `0x80` | `bit_7_high_collision_family_candidate` | 522397 | 937 | `0x80`, `0x82`, `0x90`, `0x92`, `0x94` |

## Low-Nibble Families

| Low Nibble | Cell Count | Exact Values |
| ---: | ---: | --- |
| `0x0` | 892621 | `0x00`, `0x10`, `0x80`, `0x90` |
| `0x1` | 26104 | `0x01` |
| `0x2` | 246 | `0x02`, `0x82`, `0x92` |
| `0x3` | 25763 | `0x03` |
| `0x4` | 10896 | `0x04`, `0x94` |
| `0x5` | 198 | `0x05` |
| `0x7` | 10 | `0x07` |
| `0x8` | 9325 | `0x08` |
| `0x9` | 1451 | `0x09` |
| `0xB` | 1660 | `0x0B` |
| `0xC` | 2734 | `0x0C` |
| `0xD` | 481 | `0x0D` |
| `0xF` | 1311 | `0x0F` |

## Reference Anchors

- WRAM current tileset collision data: `$01F800..$01FF7F` (refs/community-earthbound-docs/RAM_map.txt)
- ebsrc-derived D8 collision table span: `D8:0000..D8:F05E` (notes/bank-d8-asset-data-map.md)
- Legacy ROM map also labels a bank-D8 collision-data/pointer corridor,
  but its exact end boundary overlaps later modern ebsrc assets, so this
  contract treats it as corroborating evidence rather than byte-boundary authority.

## Top Nonzero Scenes

| Scene | Sector | Tileset | Palette | Nonzero Cells | High-Bit Cells | Setting | Town Map |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| `map_scene.0184` | `5,24` | 1 | 2 | 1024 | 1024 | none | none |
| `map_scene.0203` | `6,11` | 1 | 0 | 1024 | 1004 | none | onett |
| `map_scene.0216` | `6,24` | 1 | 2 | 1024 | 1024 | none | none |
| `map_scene.0235` | `7,11` | 1 | 0 | 1024 | 1023 | none | onett |
| `map_scene.0248` | `7,24` | 1 | 2 | 1024 | 1024 | none | none |
| `map_scene.0277` | `8,21` | 6 | 0 | 1024 | 1024 | none | none |
| `map_scene.0617` | `19,9` | 0 | 1 | 1024 | 1024 | lost underworld sprites | none |
| `map_scene.0747` | `23,11` | 0 | 1 | 1024 | 1024 | lost underworld sprites | none |
| `map_scene.0867` | `27,3` | 13 | 0 | 1024 | 1024 | none | none |
| `map_scene.1124` | `35,4` | 18 | 0 | 1024 | 1024 | none | scaraba |
| `map_scene.0506` | `15,26` | 6 | 1 | 1023 | 976 | none | none |
| `map_scene.0788` | `24,20` | 7 | 0 | 1023 | 1020 | none | summers |
| `map_scene.0474` | `14,26` | 6 | 1 | 1020 | 891 | none | none |
| `map_scene.0689` | `21,17` | 7 | 0 | 1019 | 1019 | none | summers |
| `map_scene.0752` | `23,16` | 7 | 0 | 1019 | 1019 | none | summers |
| `map_scene.0889` | `27,25` | 0 | 0 | 1019 | 1018 | exit mouse usable | none |

## Strongest Setting Buckets

| Setting | Scenes | Top Attribute Counts |
| --- | ---: | --- |
| none | 743 | `0x80`:404556, `0x00`:280388, `0x03`:23452, `0x01`:22567, `0x04`:10879, `0x08`:9061 |
| indoors | 89 | `0x80`:45342, `0x00`:43146, `0x01`:1149, `0x03`:699, `0x08`:264, `0x82`:206 |
| magicant sprites | 45 | `0x00`:26597, `0x80`:16484, `0x03`:1502, `0x01`:1324, `0x90`:173 |
| lost underworld sprites | 38 | `0x80`:28279, `0x00`:10187, `0x01`:417, `0x90`:24, `0x10`:4, `0x03`:1 |
| exit mouse usable | 25 | `0x80`:17769, `0x00`:7116, `0x01`:593, `0x03`:93, `0x90`:29 |
| robot sprites | 10 | `0x80`:7972, `0x00`:2190, `0x01`:54, `0x03`:16, `0x90`:8 |

## Machine-Readable Data

`notes/map-collision-attribute-context.json` records global counts,
bit-family counts, per-tileset counts, scene-presence correlations with
coarse scene features, and the top scenes by nonzero attribute-byte cells.
