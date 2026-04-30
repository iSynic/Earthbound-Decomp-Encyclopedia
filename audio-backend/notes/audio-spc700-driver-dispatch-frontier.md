# Audio SPC700 Driver Dispatch Frontier

Status: static dispatch targets recorded; FF runtime effect still pending.

## Summary

- driver block: pack `1` block `2` at `0x0500`, `16779` bytes
- unique indirect operands: `42`
- first-32-inside table candidates: `2`
- likely high-command table: `0x16C7`
- FF dispatch target candidate: `0x1A81`
- semantic status: `ff_driver_target_identified_but_effect_unconfirmed`

## FF Candidate

- command: `0xFF`
- hypothesis: `end_or_sentinel_candidate`
- target: `0x1A81`
- status: `driver_target_known_effect_unconfirmed`
- not promoted yet: Static table evidence identifies the target, but exact duration semantics still need an execution/disassembly pass at the target to distinguish end, return, channel stop, hold, or loop behavior.

## High Command Table

- table base: `0x16C7`
- source indirect jump addresses: `['0x12FD']`
- opcode hypothesis: 0x1F operand is treated as the SPC700 absolute indexed indirect jump shape for static triage.

| Command | Current sequence hypothesis | Driver target | Target first byte |
| --- | --- | ---: | --- |
| `0xE0` | `set_instrument_candidate` | `0x1833` | `0x04` |
| `0xE1` | `set_pan_candidate` | `0x182B` | `0x04` |
| `0xE2` | `pan_fade_candidate` | `0x183B` | `0x04` |
| `0xE3` | `vibrato_on_candidate` | `0x1843` | `0x13` |
| `0xE4` | `vibrato_off_candidate` | `0x184C` | `0x0E` |
| `0xE5` | `master_volume_or_channel_state_candidate` | `0x1858` | `0x1C` |
| `0xE6` | `volume_or_master_fade_candidate` | `0x1862` | `0x04` |
| `0xE7` | `tempo_or_tuning_candidate` | `0x186A` | `0x16` |
| `0xE8` | `tempo_fade_candidate` | `0x1872` | `0x19` |
| `0xE9` | `global_transpose_candidate` | `0x187A` | `0x11` |
| `0xEA` | `channel_transpose_candidate` | `0x1882` | `0x0D` |
| `0xEB` | `tremolo_or_modulation_on_candidate` | `0x1890` | `0x1F` |
| `0xEC` | `tremolo_or_modulation_off_candidate` | `0x1898` | `0x22` |
| `0xED` | `set_channel_volume_candidate` | `0x18A0` | `0x08` |
| `0xEE` | `channel_volume_fade_candidate` | `0x18B7` | `0x14` |
| `0xEF` | `subroutine_call_candidate` | `0x18BF` | `0x12` |
| `0xF0` | `modulation_fade_candidate` | `0x18CA` | `0x08` |
| `0xF1` | `pitch_envelope_or_portamento_candidate` | `0x18DE` | `0x1D` |
| `0xF2` | `pitch_envelope_off_candidate` | `0x18E9` | `0x16` |
| `0xF3` | `tuning_or_detune_candidate` | `0x18F1` | `0x18` |
| `0xF4` | `driver_toggle_or_extended_control_candidate` | `0x18F9` | `0x0C` |
| `0xF5` | `echo_or_voice_param_candidate` | `0x1903` | `0x02` |
| `0xF6` | `echo_off_or_effect_disable_candidate` | `0x1937` | `0x23` |
| `0xF7` | `echo_or_effect_setup_candidate` | `0x193F` | `0x0D` |
| `0xF8` | `echo_or_effect_fade_candidate` | `0x1949` | `0x0E` |
| `0xF9` | `pitch_slide_candidate` | `0x1954` | `0x18` |
| `0xFA` | `earthbound_extended_command_candidate` | `0x1967` | `0x18` |
| `0xFB` | `loop_start_or_control_candidate` | `0x197F` | `0x08` |
| `0xFC` | `loop_end_or_control_candidate` | `0x19B4` | `0x08` |
| `0xFD` | `loop_or_jump_control_candidate` | `0x19FB` | `0x14` |
| `0xFE` | `jump_or_long_control_candidate` | `0x1A32` | `0x14` |
| `0xFF` | `end_or_sentinel_candidate` | `0x1A81` | `0x0E` |

## Indirect Jump Candidates

| Operand | Candidate role | Referencing addresses | Pointer-run words | First 32 inside | First-32 target range |
| ---: | --- | --- | ---: | --- | --- |
| `0x16C7` | `likely_e0_ff_high_command_dispatch_table` | `0x12FD` | `164` | `True` | `0x182B..0x1A81` |
| `0x17C5` | `pointer_table_candidate_effect_unknown` | `0x130A` | `37` | `True` | `0x148A..0x2E0B` |
| `0x17D5` | `short_or_mixed_indirect_target_candidate` | `0x1317` | `29` | `False` | `0x148A..0x2E0B` |
| `0x125B` | `short_or_mixed_indirect_target_candidate` | `0x1258` | `10` | `False` | `0x1170..0x1A5F` |
| `0x132E` | `short_or_mixed_indirect_target_candidate` | `0x132A` | `9` | `False` | `0x1340..0x134B` |
| `0x0D0A` | `short_or_mixed_indirect_target_candidate` | `0x1F8E` | `2` | `False` | `0x14DA..0x31FB` |
| `0x0BB2` | `short_or_mixed_indirect_target_candidate` | `0x1910, 0x192B` | `1` | `False` | `0x0BC7..0x0BC7` |
| `0x180D` | `short_or_mixed_indirect_target_candidate` | `0x12F0` | `1` | `False` | `0x148A..0x148A` |
| `0x1F90` | `short_or_mixed_indirect_target_candidate` | `0x1726` | `1` | `False` | `0x140D..0x140D` |
| `0x25DC` | `short_or_mixed_indirect_target_candidate` | `0x1766` | `1` | `False` | `0x1418..0x1418` |
| `0x008D` | `operand_outside_driver_or_data_false_positive_candidate` | `0x289C, 0x28B0` | `0` | `False` | `None` |
| `0x00A8` | `operand_outside_driver_or_data_false_positive_candidate` | `0x25D0, 0x25D8` | `0` | `False` | `None` |
| `0x0440` | `operand_outside_driver_or_data_false_positive_candidate` | `0x1345` | `0` | `False` | `None` |
| `0x06A4` | `short_or_mixed_indirect_target_candidate` | `0x3E92` | `0` | `False` | `None` |
| `0x06B0` | `short_or_mixed_indirect_target_candidate` | `0x3E55, 0x3E78` | `0` | `False` | `None` |
| `0x07E1` | `short_or_mixed_indirect_target_candidate` | `0x4098` | `0` | `False` | `None` |
| `0x080A` | `short_or_mixed_indirect_target_candidate` | `0x1FD8` | `0` | `False` | `None` |
| `0x0BB4` | `short_or_mixed_indirect_target_candidate` | `0x190A, 0x1925` | `0` | `False` | `None` |
| `0x0BB7` | `short_or_mixed_indirect_target_candidate` | `0x1914, 0x192F` | `0` | `False` | `None` |
| `0x190A` | `short_or_mixed_indirect_target_candidate` | `0x1F00, 0x1F62` | `0` | `False` | `None` |
| `0x1A04` | `short_or_mixed_indirect_target_candidate` | `0x27FA` | `0` | `False` | `None` |
| `0x1B1C` | `short_or_mixed_indirect_target_candidate` | `0x1890` | `0` | `False` | `None` |
| `0x1F42` | `short_or_mixed_indirect_target_candidate` | `0x1722` | `0` | `False` | `None` |
| `0x1F64` | `short_or_mixed_indirect_target_candidate` | `0x1724` | `0` | `False` | `None` |

## Findings

- The pack-1 driver block contains a strong 0x1F indirect table candidate at $16C7 that cleanly maps 32 entries onto the E0..FF high-command byte range used by sequence payloads.
- Under that mapping, FF points at driver target $1A81, giving the FF terminator review lane a concrete address for the next SPC700 disassembly or execution trace.
- This artifact does not promote FF to an end command yet; it only names the static dispatch target and keeps the runtime effect pending.
- Several other 0x1F operands also point at driver-local tables, so the driver likely uses multiple indirect dispatch tables for lower-level music/runtime control.

## Next Work

- disassemble or trace execution at $1A81 with live channel state to determine whether FF ends a sequence, returns from EF, stops a channel, or falls into another control path
- capture a short runtime trace around the 0x1F $16C7 dispatch for at least one sequence that reaches FF
- after FF effect is confirmed, feed the result back into the FF terminator review and finite/loop metadata lanes
