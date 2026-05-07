# Audio SPC700 Dispatch Trace Frontier

Status: runtime trace hook present; current samples do not yet observe high-command dispatch.

## Summary

- trace records: `20`
- records with hits: `0`
- total hits: `0`
- total sequence reads: `82487`
- total high-byte sequence reads: `14503`
- total control-candidate sequence reads: `6424`
- fetch-like sequence reads: `69440`
- fetch-like control-candidate reads: `5520`
- command semantic statuses: `{'runtime_fetch_observed_dispatch_bridge_pending': 1, 'runtime_interpreter_read_observed_dispatch_decode_pending': 4}`
- records with sequence FF reads: `4`
- long trace records: `1`
- max long trace instruction limit: `1000000`
- semantic status: `sequence_high_bytes_observed_but_dispatch_handler_pc_not_observed`

## Trace Contract

- field: `spc700_entry_execution_probe.high_command_dispatch_trace`
- sequence read field: `spc700_entry_execution_probe.sequence_read_trace`
- sequence read window: `{'start': '0x2000', 'end_exclusive': '0x6C00'}`
- execution fetch heuristic: `pc_minus_address_between_0_and_2`
- dispatch PC: `0x12FD`
- table base: `0x16C7`
- FF target window: `{'start': '0x1A81', 'end_exclusive': '0x1ACB'}`
- mapped command rule: For high_command_dispatch_source hits, X is recorded as the table byte offset and even X values below 0x40 are mapped as 0xE0 + X/2.

## Command Semantics

| Command | Status | Seq reads | Fetch-like reads | Dispatch hits | Promotion allowed |
| --- | --- | ---: | ---: | ---: | --- |
| `0x00` | `runtime_fetch_observed_dispatch_bridge_pending` | 5931 | 5520 | 0 | `False` |
| `0xEF` | `runtime_interpreter_read_observed_dispatch_decode_pending` | 475 | 0 | 0 | `False` |
| `0xFD` | `runtime_interpreter_read_observed_dispatch_decode_pending` | 1 | 0 | 0 | `False` |
| `0xFE` | `runtime_interpreter_read_observed_dispatch_decode_pending` | 5 | 0 | 0 | `False` |
| `0xFF` | `runtime_interpreter_read_observed_dispatch_decode_pending` | 12 | 0 | 0 | `False` |

## Records

| Job | Track | Limit | Executed | Final PC | Key-ons | Dispatch hits | Seq reads | High reads | Control reads | Fetch-like control reads | Control counts |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `ares-track-001-gas_station` | `GAS_STATION` | `1000000` | `1000000` | `0x0DB9` | `3` | `0` | `13073` | `2787` | `1274` | `904` | `{'0x00': 921, '0xEF': 351, '0xFF': 2}` |
| `ares-track-002-naming_screen` | `NAMING_SCREEN` | `200000` | `200000` | `0x0565` | `5` | `0` | `7509` | `1165` | `605` | `540` | `{'0x00': 571, '0xEF': 34}` |
| `ares-track-046-onett` | `ONETT` | `200000` | `200000` | `0x0E28` | `4` | `0` | `3218` | `509` | `221` | `216` | `{'0x00': 220, '0xEF': 1}` |
| `ares-track-047-fourside` | `FOURSIDE` | `200000` | `200000` | `0x074C` | `8` | `0` | `5534` | `810` | `357` | `352` | `{'0x00': 354, '0xEF': 3}` |
| `ares-track-048-saturn_valley` | `SATURN_VALLEY` | `200000` | `200000` | `0x126D` | `7` | `0` | `5357` | `858` | `415` | `404` | `{'0x00': 415}` |
| `ares-track-083-sky_runner` | `SKY_RUNNER` | `200000` | `200000` | `0x0C4F` | `9` | `0` | `4295` | `684` | `484` | `296` | `{'0x00': 477, '0xEF': 7}` |
| `ares-track-095-smiles_and_tears` | `SMILES_AND_TEARS` | `200000` | `200000` | `0x0705` | `6` | `0` | `1763` | `328` | `117` | `104` | `{'0x00': 107, '0xEF': 1, '0xFD': 1, '0xFF': 8}` |
| `ares-track-105-pokey_means_business` | `POKEY_MEANS_BUSINESS` | `200000` | `200000` | `0x0DE6` | `6` | `0` | `3020` | `463` | `227` | `212` | `{'0x00': 225, '0xEF': 2}` |
| `ares-track-121-onett_intro` | `ONETT_INTRO` | `200000` | `200000` | `0x0703` | `9` | `0` | `3367` | `655` | `227` | `216` | `{'0x00': 226, '0xFF': 1}` |
| `ares-track-133-hidden_song` | `HIDDEN_SONG` | `200000` | `200000` | `0x0563` | `7` | `0` | `2587` | `428` | `197` | `172` | `{'0x00': 189, '0xEF': 7, '0xFE': 1}` |
| `ares-track-157-attract_mode` | `ATTRACT_MODE` | `200000` | `200000` | `0x0880` | `17` | `0` | `7939` | `1263` | `563` | `528` | `{'0x00': 534, '0xEF': 28, '0xFE': 1}` |
| `ares-track-160-soundstone_recording_giant_step` | `SOUNDSTONE_RECORDING_GIANT_STEP` | `200000` | `200000` | `0x0706` | `5` | `0` | `2181` | `480` | `149` | `140` | `{'0x00': 149}` |
| `ares-track-161-soundstone_recording_lilliput_steps` | `SOUNDSTONE_RECORDING_LILLIPUT_STEPS` | `200000` | `200000` | `0x0707` | `13` | `0` | `2894` | `554` | `188` | `180` | `{'0x00': 188}` |
| `ares-track-162-soundstone_recording_milky_well` | `SOUNDSTONE_RECORDING_MILKY_WELL` | `200000` | `200000` | `0x074F` | `11` | `0` | `3299` | `640` | `216` | `208` | `{'0x00': 216}` |
| `ares-track-163-soundstone_recording_rainy_circle` | `SOUNDSTONE_RECORDING_RAINY_CIRCLE` | `200000` | `200000` | `0x073B` | `9` | `0` | `3351` | `606` | `234` | `224` | `{'0x00': 234}` |
| `ares-track-168-soundstone_bgm` | `SOUNDSTONE_BGM` | `200000` | `200000` | `0x070E` | `2` | `0` | `2664` | `445` | `182` | `176` | `{'0x00': 179, '0xFE': 2, '0xFF': 1}` |
| `ares-track-175-title_screen` | `TITLE_SCREEN` | `200000` | `200000` | `0x0D62` | `9` | `0` | `4274` | `673` | `276` | `272` | `{'0x00': 275, '0xEF': 1}` |
| `ares-track-186-giygas_phase1` | `GIYGAS_PHASE1` | `200000` | `200000` | `0x0BC6` | `2` | `0` | `1933` | `404` | `134` | `108` | `{'0x00': 134}` |
| `ares-track-187-give_us_strength` | `GIVE_US_STRENGTH` | `200000` | `200000` | `0x0CF4` | `1` | `0` | `2580` | `426` | `234` | `168` | `{'0x00': 193, '0xEF': 40, '0xFE': 1}` |
| `ares-track-191-giygas_weakened` | `GIYGAS_WEAKENED` | `200000` | `200000` | `0x0D01` | `3` | `0` | `1649` | `325` | `124` | `100` | `{'0x00': 124}` |

## Findings

- The native ares audio harness now emits a bounded high-command dispatch trace block in each state capture.
- The native ares audio harness now also emits bounded sequence-region read traces for 0x2000..0x6BFF reads.
- The sequence read trace separates broad sequence-region reads from fetch-like reads where PC is within two bytes of the read address.
- Current sampled captures include live key-on events and thousands of sequence-region reads, including high-byte command-like values and control candidates.
- GAS_STATION and ONETT_INTRO both read 0xFF bytes from sequence/runtime RAM in the sampled windows, while GIVE_US_STRENGTH reads a 0xFE byte.
- 0x00 terminator candidates are now traced as control reads so N-SPC end-vs-return work can use runtime reader PCs.
- Despite those sequence reads, current captures still record no hits at 0x12FD, no live 0x1F opcode hits, and no hits in the provisional FF target window, so the handler bridge is still missing.
- Command-level semantic statuses are therefore pending and cannot promote exact-duration exports.

## Next Work

- narrow sequence-read tracing to the actual bytecode fetch PC/state rather than broad 0x2000..0x6BFF reads
- run a longer or later-bound trace for one finite FF candidate such as ELEVATOR_DOWN once the all-track native job path accepts per-job instruction limits
- decode 0x00 reader PCs and join them with EF context before promoting exact finite sequence duration
- only promote FF semantics after a trace records the dispatch source, X-derived command, and post-dispatch PC/state mutation
