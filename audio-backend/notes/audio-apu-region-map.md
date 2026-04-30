# Audio APU Region Map

Status: derived from the audio-pack contract; no ROM-derived payload bytes are included.

This map summarizes where EarthBound audio packs write inside SPC/APU RAM. It is meant to guide driver, sample, and sequence-state work before a renderer backend starts consuming the generated RAM seeds.

## Summary

- audio packs: `169`
- payload writes: `323`
- payload bytes across all pack streams: `874945`
- destination span: `0x0500..0xE6E0`
- destination role counts: `{'brr_sample_or_high_apu_payload': 152, 'main_spc700_driver_or_driver_overlay': 1, 'sequence_or_runtime_tables': 69, 'music_sequence_or_sample_directory': 101}`

## Regions By Role

| Role guess | Writes | Payload bytes | Lowest destination | Highest end | Unique destinations | Largest write |
| --- | ---: | ---: | --- | --- | ---: | --- |
| `brr_sample_or_high_apu_payload` | 152 | 670636 | `0x6C00` | `0xE6E0` | 10 | `AUDIO_PACK_108 0x7000..0xE6D0` |
| `main_spc700_driver_or_driver_overlay` | 1 | 16779 | `0x0500` | `0x468B` | 1 | `AUDIO_PACK_1 0x0500..0x468B` |
| `music_sequence_or_sample_directory` | 101 | 100636 | `0x5000` | `0x690B` | 16 | `AUDIO_PACK_36 0x5800..0x6756` |
| `sequence_or_runtime_tables` | 69 | 86894 | `0x4800` | `0x69A0` | 10 | `AUDIO_PACK_109 0x4800..0x69A0` |

## Common Repeated Write Shapes

| Destination | End | Role guess | Bytes | Writes | Sample pack ids |
| --- | --- | --- | ---: | ---: | --- |
| `0x6C68` | `0x6C80` | `brr_sample_or_high_apu_payload` | 24 | 25 | `21, 27, 33, 35, 40, 44, 50, 52, 54, 56, 64, 66` |
| `0x6C68` | `0x6C90` | `brr_sample_or_high_apu_payload` | 40 | 9 | `8, 24, 37, 47, 60, 70, 84, 105, 118` |
| `0x6C68` | `0x6C70` | `brr_sample_or_high_apu_payload` | 8 | 8 | `58, 72, 74, 80, 95, 114, 161, 165` |
| `0x6E9C` | `0x6EBA` | `brr_sample_or_high_apu_payload` | 30 | 8 | `21, 27, 35, 56, 78, 92, 98, 139` |
| `0x6E9C` | `0x6EC0` | `brr_sample_or_high_apu_payload` | 36 | 7 | `33, 50, 52, 54, 64, 89, 124` |
| `0x6E9C` | `0x6EA8` | `brr_sample_or_high_apu_payload` | 12 | 6 | `58, 72, 74, 80, 95, 165` |
| `0x6E9C` | `0x6EAE` | `brr_sample_or_high_apu_payload` | 18 | 6 | `40, 44, 66, 82, 116, 156` |
| `0x6E9C` | `0x6EB4` | `brr_sample_or_high_apu_payload` | 24 | 4 | `76, 110, 126, 131` |
| `0x6E9C` | `0x6EC6` | `brr_sample_or_high_apu_payload` | 42 | 3 | `47, 60, 118` |
| `0x6E9C` | `0x6ED2` | `brr_sample_or_high_apu_payload` | 54 | 3 | `8, 24, 105` |
| `0x5800` | `0x5A61` | `music_sequence_or_sample_directory` | 609 | 2 | `14, 155` |
| `0x6C00` | `0x6C70` | `brr_sample_or_high_apu_payload` | 112 | 2 | `5, 108` |
| `0x6C2C` | `0x6C50` | `brr_sample_or_high_apu_payload` | 36 | 2 | `3, 153` |
| `0x6E00` | `0x6E1E` | `brr_sample_or_high_apu_payload` | 30 | 2 | `0, 1` |
| `0x6E9C` | `0x6EA2` | `brr_sample_or_high_apu_payload` | 6 | 2 | `114, 161` |
| `0x6E9C` | `0x6ECC` | `brr_sample_or_high_apu_payload` | 48 | 2 | `70, 84` |
| `0x95B0` | `0xE210` | `brr_sample_or_high_apu_payload` | 19552 | 2 | `37, 126` |
