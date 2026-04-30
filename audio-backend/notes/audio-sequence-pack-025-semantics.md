# Audio Sequence Pack 25 Semantics Report

Status: focused structure known; opcode meanings still need SPC700 driver-dispatch corroboration.

## Summary

- ROM range: `EC:E101..EC:EB51`
- tracks using pack: `8`
- sequence payload blocks: `8`
- block prefix shapes: `[{'top_level_words': 3, 'group_word_counts': [8, 8], 'group_active_pointer_counts': [8, 4], 'count': 8}]`
- segment kinds: `{'shared_note_motif_candidate': 24, 'phrase_or_control_candidate': 7, 'channel_init_or_phrase_candidate': 56, 'global_setup_candidate': 8, 'rest_or_tail_candidate': 1}`
- reference song payload matches: `8 / 8`
- semantic status: `focused_structure_known_opcode_meanings_pending_driver_dispatch`

## Tracks

| Track | Name | Block guess | Export class | Mode | Duration seconds |
| ---: | --- | ---: | --- | --- | ---: |
| `32` | GIANT_STEP | `0` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 21.003219 |
| `33` | LILLIPUT_STEPS | `1` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 21.004906 |
| `34` | MILKY_WELL | `2` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 21.002375 |
| `35` | RAINY_CIRCLE | `3` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 21.001938 |
| `36` | MAGNET_HILL | `4` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 21.000875 |
| `37` | PINK_CLOUD | `5` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 21.005312 |
| `38` | LUMINE_HALL | `6` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 19.2455 |
| `39` | FIRE_SPRING | `7` | `finite_or_transition_review_candidate` | `trim_candidate_after_manual_or_sequence_review` | 21.005406 |

## Block Structure

| Block | Destination | Bytes | Top words | Pointer groups | Segment kinds | Ref song | Ref payload match |
| ---: | --- | ---: | ---: | --- | --- | --- | --- |
| `0` | `0x4800` | 325 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, phrase_or_control_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-20.ebm` | `True` |
| `1` | `0x4A00` | 327 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, phrase_or_control_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-21.ebm` | `True` |
| `2` | `0x4C00` | 343 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, phrase_or_control_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-22.ebm` | `True` |
| `3` | `0x4E00` | 335 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, phrase_or_control_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-23.ebm` | `True` |
| `4` | `0x5000` | 320 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, phrase_or_control_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-24.ebm` | `True` |
| `5` | `0x5200` | 339 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, phrase_or_control_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-25.ebm` | `True` |
| `6` | `0x5400` | 337 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, rest_or_tail_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-26.ebm` | `True` |
| `7` | `0x5600` | 280 | 3 | 8 words/8 active/0 null; 8 words/4 active/4 null | shared_note_motif_candidate: 3, phrase_or_control_candidate: 1, channel_init_or_phrase_candidate: 7, global_setup_candidate: 1 | `refs/eb-decompile-4ef92/Music/Packs/19/song-27.ebm` | `True` |

## Command Candidates

| Byte | Count | Current hypothesis |
| --- | ---: | --- |
| `0xE0` | 64 | set_instrument_candidate |
| `0xE1` | 78 | set_pan_candidate |
| `0xE3` | 56 | vibrato_on_candidate |
| `0xE5` | 8 | master_volume_or_channel_state_candidate |
| `0xE7` | 8 | tempo_or_tuning_candidate |
| `0xED` | 64 | set_channel_volume_candidate |
| `0xEF` | 43 | subroutine_call_candidate |
| `0xF0` | 8 | modulation_fade_candidate |
| `0xF2` | 16 | pitch_envelope_off_candidate |
| `0xF4` | 80 | driver_toggle_or_extended_control_candidate |
| `0xF5` | 16 | echo_or_voice_param_candidate |
| `0xFA` | 8 | earthbound_extended_command_candidate |
| `0xFD` | 1 | loop_or_jump_control_candidate |
| `0xFE` | 16 | jump_or_long_control_candidate |
| `0xFF` | 8 | end_or_sentinel_candidate |

## Findings

- Pack track order matches block order for the Sanctuary melody family: tracks 32..39 map cleanly to the eight sequence blocks.
- Every block has a 3-word top-level table with two active group pointers and one null slot.
- The lower-address group has eight active pointers; the higher-address group has four active pointers followed by four null slots.
- Repeated short shared-note motifs start the lower group, while later segments carry channel setup, phrase calls, and rest/tail candidates.
- The report stores structural statistics and hashes only; it does not embed ROM-derived payload byte strings.
- The eb-decompile reference has matching binary song files for every block in this family; those files corroborate extraction, while this report adds table/group/segment semantics.

## Next Work

- tie the 3-word top-level table and two pointer groups to the SPC700 driver's track-start routine
- confirm whether the two groups represent music channels, sound-stone layer variants, or intro/body control groups
- map EF/FE/FD/FF handling in driver dispatch before promoting exact finite endings for tracks 32..39
