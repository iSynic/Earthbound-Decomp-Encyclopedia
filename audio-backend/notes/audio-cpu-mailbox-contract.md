# Audio CPU/APU Mailbox Contract

Status: diagnostic track-command mailbox transcript pinned; ROM-derived full CHANGE_MUSIC pre-satisfied-pack bridge implemented; full scheduled CPU/APU handshake still pending.

This contract ties the CPU-side EarthBound source entry points to the APU-side command transcript observed in the ares diagnostic harness. It is the target for replacing timed command delivery with scheduled execution of the real C0 track-command sender.

## CPU Side

- send entry: `C0:ABBD` / `C0ABBD_SendApuPort0CommandByte`
- send register: `$2140/APUIO0`
- send opcode: `STA long $002140`
- send ROM bytes: `E2 20 8F 40 21 00 C2 30 6B`
- send width: `A low byte`
- command value: `one_based_track_id`
- ack read entry: `C0:AC20` / `C0AC20_ReadApuPort0Byte`
- ack read register: `$2140/APUIO0`
- stop-music ack value: `0x00`

## APU Side Target

- first command read: `0x062A` from `0x00F4`
- first ack write: `0x062A` to `0x00F4` with `0x00`
- key-on must follow command read: `True`
- diagnostic mode pinned by frontier: `on_first_port0_read`

## ares Bridge

- CPU to APU: `ares::SuperFamicom::cpu.writeAPU -> smp.portWrite(address.bit(0,1), data)`
- APU to CPU: `ares::SuperFamicom::cpu.readAPU -> smp.portRead(address.bit(0,1))`
- SMP reads CPU mailbox: `SMP::readIO(0x00f4) returns io.apu0 after synchronize(cpu)`
- SMP writes APU mailbox: `SMP::writeIO(0x00f4, data) stores io.cpu0 after synchronize(cpu)`
- implication: The current bridge can execute ROM-derived C4:FBBD CHANGE_MUSIC bytes under a documented pre-satisfied pack state, then route the C0:ABBD STA long $002140 write through WDC65816 semantics and ares' CPU/APU port path. The next accurate harness should replace the pre-satisfied pack/table stubs with real scheduled pack-loading context and produce the same mailbox transcript without timed injection.

## Current Frontier

- available: `True`
- captures: `20 / 20`
- modes: `{'on_first_port0_read': 20}`
- command reads: `20`
- commands matching track id: `20`
- zero ack writes: `20`
- key-on after command read: `20`
- first read PCs: `{'0x062A': 20}`
- first ack PCs: `{'0x062A': 20}`

## ares SMP Smoke

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after timed portWrite: `20`
- delivery mode: `ares_smp_portwrite_on_pc_062a`

## ares SMP Snapshot Rendering

- available: `True`
- rendered metrics: `20`
- render classes: `{'audible': 20}`
- versus custom last-key-on: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## ares CPU writeAPU Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after timed CPU writeAPU: `20`
- delivery mode: `ares_cpu_writeapu_2140_on_pc_062a`
- render classes: `{'audible': 20}`
- versus direct SMP portWrite: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## WDC65816 STA $2140 Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after modeled WDC65816 STA: `20`
- delivery mode: `ares_wdc65816_sta_2140_on_pc_062a`
- modeled routine: `sep_20_sta_002140_prefix_of_C0ABBD`
- render classes: `{'audible': 20}`
- versus CPU writeAPU: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## Full C0:ABBD Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after modeled C0:ABBD: `20`
- delivery mode: `ares_wdc65816_full_c0abbd_on_pc_062a`
- modeled routine: `full_C0ABBD_sep_sta_rep_rtl`
- render classes: `{'audible': 20}`
- versus WDC65816 STA $2140: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## ROM-Derived C0:ABBD Bridge

- fixture manifest available: `True`
- fixtures: `8`
- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after ROM-derived C0:ABBD: `20`
- delivery mode: `ares_wdc65816_rom_c0abbd_on_pc_062a`
- routine: `rom_fixture_C0ABBD_sep_sta_long_rep_rtl`
- render classes: `{'audible': 20}`
- versus modeled full C0:ABBD: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## ROM-Derived C0:ABBD JSL Call Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after ROM-derived C0:ABBD JSL call: `20`
- delivery mode: `ares_wdc65816_rom_c0abbd_jsl_on_pc_062a`
- routine: `rom_fixture_C0ABBD_jsl_call_context`
- call shape: `JSL $C0ABBD from modeled caller, ROM-derived bytes mapped at C0:ABBD, RTL returns through modeled stack`
- render classes: `{'audible': 20}`
- versus direct ROM-derived C0:ABBD: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## CHANGE_MUSIC Tail Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after CHANGE_MUSIC tail: `20`
- delivery mode: `ares_wdc65816_change_music_tail_on_pc_062a`
- routine: `rom_fixture_ChangeMusic_tail_to_C0ABBD`
- tail bytes: `A4 10 98 1A 22 BD AB C0 2B 6B`
- call shape: `C4:FD0E LDY $10; TYA; INC; JSL C0:ABBD; PLD; RTL with direct-page $10 preloaded to zero-based track index`
- render classes: `{'audible': 20}`
- versus ROM-derived C0:ABBD JSL call: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## Full CHANGE_MUSIC Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after full CHANGE_MUSIC: `20`
- delivery mode: `ares_wdc65816_full_change_music_on_pc_062a`
- routine: `rom_fixture_ChangeMusic_full_presatisfied_packs`
- call shape: `C4:FBBD CHANGE_MUSIC body executes from ROM-derived bytes with A seeded to the requested one-based track id, MusicDatasetTable reads served from a ROM-derived fixture, current pack variables pre-satisfied to the requested track's real table row, helper side effects stubbed, and JSL C0:ABBD mapped to ROM-derived bytes.`
- known shortcuts: `['APU RAM seed is already built for the target track before the command is delivered.', 'MusicDatasetTable bytes are real ROM-derived fixture bytes, but CurrentPrimarySamplePack, CurrentSecondarySamplePack, and CurrentSequencePack are pre-satisfied to the selected row so pack loads are skipped in this isolated CPU probe.', 'LOAD_SPC700_DATA, STOP_MUSIC, STOP_MUSIC_TRANSITION, and PLAY_SOUND_UNKNOWN0 are RTL stubs if reached.', 'The harness still times CPU delivery at the SMP $062A command-read boundary.']`
- render classes: `{'audible': 20}`
- versus CHANGE_MUSIC tail: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## Full CHANGE_MUSIC Load-Path Stub Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after full CHANGE_MUSIC load path: `20`
- delivery mode: `ares_wdc65816_full_change_music_load_stub_on_pc_062a`
- routine: `rom_fixture_ChangeMusic_full_load_path_stubbed_loader`
- call shape: `C4:FBBD CHANGE_MUSIC body executes from ROM-derived bytes with A seeded to the requested one-based track id, MusicDatasetTable and MusicPackPointerTable reads served from ROM-derived fixtures, current pack variables left unsatisfied so real pack-decision branches run, LOAD_SPC700_DATA calls recorded and stubbed, and JSL C0:ABBD mapped to ROM-derived bytes.`
- loader metrics: `{'available': True, 'job_count': 20, 'mismatch_count': 0, 'call_count_distribution': {'2': 2, '3': 18}}`
- known shortcuts: `['APU RAM seed is already built for the target track before the command is delivered.', 'MusicDatasetTable and MusicPackPointerTable bytes are real ROM-derived fixture bytes, and pack-current state is intentionally unsatisfied so the pack-decision branches execute.', 'LOAD_SPC700_DATA is an RTL stub that records A/X load-stream pointer arguments instead of streaming bytes to the APU.', 'STOP_MUSIC, STOP_MUSIC_TRANSITION, and PLAY_SOUND_UNKNOWN0 remain RTL stubs if reached.', 'The harness still times CPU delivery at the SMP $062A command-read boundary.']`
- render classes: `{'audible': 20}`
- versus pre-satisfied full CHANGE_MUSIC: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## Full CHANGE_MUSIC Load-Apply Bridge

- available: `True`
- successes: `20 / 20`
- command reads: `20`
- zero ack writes: `20`
- key-on after full CHANGE_MUSIC load apply: `20`
- delivery mode: `ares_wdc65816_full_change_music_load_apply_on_pc_062a`
- routine: `rom_fixture_ChangeMusic_full_load_path_applied_loader`
- call shape: `C4:FBBD CHANGE_MUSIC body executes from ROM-derived bytes with bootstrap-only APU RAM, real pack-decision branches, ROM-derived MusicDatasetTable and MusicPackPointerTable fixtures, and LOAD_SPC700_DATA calls that apply selected payload streams into ares APU RAM before JSL C0:ABBD sends the track command.`
- loader metrics: `{'available': True, 'job_count': 20, 'mismatch_count': 0, 'call_count_distribution': {'2': 2, '3': 18}}`
- applied stream totals: `{'streams': 58, 'blocks': 188, 'bytes': 531593, 'errors': 0}`
- known shortcuts: `['Bootstrap/common APU RAM seed is still prebuilt before the command is delivered.', 'LOAD_SPC700_DATA applies payload streams semantically from ROM bytes instead of executing the real APUIO byte handshake.', 'STOP_MUSIC, STOP_MUSIC_TRANSITION, and PLAY_SOUND_UNKNOWN0 remain RTL stubs if reached.', 'The harness still times CPU delivery at the SMP $062A command-read boundary.']`
- render classes: `{'audible': 20}`
- versus load-stub full CHANGE_MUSIC: `{'available': True, 'improved_count': 0, 'unchanged_count': 20, 'worsened_count': 0}`
- versus baseline diagnostic snapshots: `{'available': True, 'improved_count': 20, 'unchanged_count': 0, 'worsened_count': 0}`

## Replacement Target

- Use the WDC65816-modeled CPU-side $2140 write of the one-based track id instead of diagnostic APUIO0 injection.
- Until full CPU scheduling is in place, use timed WDC65816 execution of the full ROM-derived CHANGE_MUSIC body with real pack-decision branches and semantic LOAD_SPC700_DATA stream application as the current bridge step.
- Next replace semantic LOAD_SPC700_DATA application with the real APUIO byte handshake before reaching the same command send.
- Preserve the APU driver's first command read at $062A/$F4.
- Preserve the driver's immediate $00 write to $F4 as the first APUIO0 acknowledgement after command read.
- Preserve key-on after command read across the representative corpus.
- Keep the no-command $055A/zero-key-on run as the negative control.

## Evidence

| Evidence | Path | Exists | Claim |
| --- | --- | --- | --- |
| `change_music_sends_one_based_track_id` | `refs/ebsrc-main/ebsrc-main/src/audio/change_music.asm` | `yes` | CHANGE_MUSIC decrements the requested track for table lookup, then increments it and calls UNKNOWN_C0ABBD, so the mailbox command is the one-based track id. |
| `c0_abbd_writes_apuio0` | `src/c0/c0_abbd_send_apu_port0_command_byte.asm` | `yes` | Local C0 source confirms C0:ABBD stores A low byte to CPU register $002140/APUIO0 with long-addressed STA. |
| `c0_ac20_reads_apuio0` | `src/c0/c0_ac20_read_apu_port0_byte.asm` | `yes` | Local C0 source confirms C0:AC20 reads CPU register $2140/APUIO0 and masks it to one byte. |
| `stop_music_waits_for_zero_ack` | `refs/ebsrc-main/ebsrc-main/src/audio/stop_music.asm` | `yes` | STOP_MUSIC writes zero to APUIO0 and polls C0:AC20 until APUIO0 reads back zero. |
| `ares_cpu_apu_ports` | `external:ares/ares/sfc/cpu/io.cpp` | `yes` | ares CPU $2140-$2143 accesses synchronize with SMP and call smp.portRead/portWrite. |
| `ares_smp_mailbox_ports` | `external:ares/ares/sfc/smp/io.cpp` | `yes` | ares SMP $F4-$F7 accesses synchronize with CPU and expose the reciprocal APU/CPU mailbox fields. |
| `diagnostic_mailbox_frontier` | `build/audio/command-on-first-read-jobs/mailbox-frontier.json` | `yes` | Generated ignored frontier proving the current diagnostic command transcript across the representative 20-track corpus. |
| `ares_smp_mailbox_smoke` | `build/audio/ares-smp-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving timed ares::SuperFamicom::smp.portWrite delivery reaches the command read, zero ack, and key-on boundary across representative tracks. |
| `ares_smp_mailbox_spc_index` | `build/audio/ares-smp-mailbox-spc/ares-smp-mailbox-spc-snapshots.json` | `yes` | Generated ignored index of real ares SMP mailbox snapshots captured at the key-on boundary for snes_spc/libgme rendering. |
| `ares_smp_mailbox_render_metrics` | `build/audio/ares-smp-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving the ares SMP mailbox snapshots are audible across the representative track corpus. |
| `ares_cpu_writeapu_mailbox_smoke` | `build/audio/ares-cpu-writeapu-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving timed ares::SuperFamicom::cpu.writeAPU($2140, track) delivery reaches the same command read, zero ack, and key-on boundary across representative tracks. |
| `ares_cpu_writeapu_render_metrics` | `build/audio/ares-cpu-writeapu-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving CPU-side ares writeAPU mailbox snapshots are audible across the representative track corpus. |
| `ares_wdc65816_sta2140_mailbox_smoke` | `build/audio/ares-wdc65816-sta2140-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving a modeled WDC65816 execution of the C0:ABBD sep/sta $2140 prefix can deliver the track command through ares' CPU/APU bridge and reach key-on across representative tracks. |
| `ares_wdc65816_sta2140_render_metrics` | `build/audio/ares-wdc65816-sta2140-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving the WDC65816 STA $2140 bridge snapshots are audible across the representative track corpus. |
| `ares_wdc65816_full_c0abbd_mailbox_smoke` | `build/audio/ares-wdc65816-c0abbd-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving modeled execution of the full C0:ABBD routine can deliver the track command through ares' CPU/APU bridge and reach key-on across representative tracks. |
| `ares_wdc65816_full_c0abbd_render_metrics` | `build/audio/ares-wdc65816-c0abbd-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving full C0:ABBD bridge snapshots are audible across the representative track corpus. |
| `rom_c0abbd_cpu_routine_fixture` | `build/audio/cpu-routine-fixtures/audio-cpu-routine-fixtures.json` | `yes` | Generated ignored fixture manifest proving the ROM bytes at C0:ABBD are E2 20 8F 40 21 00 C2 30 6B, i.e. SEP; STA long $002140; REP; RTL. |
| `ares_wdc65816_rom_c0abbd_mailbox_smoke` | `build/audio/ares-wdc65816-rom-c0abbd-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving execution of ROM-derived C0:ABBD bytes through the WDC65816 probe reaches command read, zero ack, and key-on across representative tracks. |
| `ares_wdc65816_rom_c0abbd_render_metrics` | `build/audio/ares-wdc65816-rom-c0abbd-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving ROM-derived C0:ABBD bridge snapshots are audible across the representative track corpus. |
| `ares_wdc65816_rom_c0abbd_jsl_mailbox_smoke` | `build/audio/ares-wdc65816-rom-c0abbd-jsl-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving a real WDC65816 JSL into ROM-derived C0:ABBD reaches RTL return, command read, zero ack, and key-on across representative tracks. |
| `ares_wdc65816_rom_c0abbd_jsl_render_metrics` | `build/audio/ares-wdc65816-rom-c0abbd-jsl-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving ROM-derived C0:ABBD JSL-call snapshots are audible across the representative track corpus. |
| `ares_wdc65816_change_music_tail_mailbox_smoke` | `build/audio/ares-wdc65816-change-music-tail-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving the ROM-derived C4:FD0E CHANGE_MUSIC tail computes the one-based track command and reaches C0:ABBD, command read, zero ack, and key-on across representative tracks. |
| `ares_wdc65816_change_music_tail_render_metrics` | `build/audio/ares-wdc65816-change-music-tail-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving CHANGE_MUSIC tail snapshots are audible across the representative track corpus. |
| `ares_wdc65816_full_change_music_mailbox_smoke` | `build/audio/ares-wdc65816-full-change-music-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving the ROM-derived C4:FBBD CHANGE_MUSIC body can run under a pre-satisfied pack state, compute the one-based track command, call C0:ABBD, return, and reach key-on across representative tracks. |
| `ares_wdc65816_full_change_music_render_metrics` | `build/audio/ares-wdc65816-full-change-music-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving full CHANGE_MUSIC pre-satisfied-pack snapshots are audible across the representative track corpus. |
| `ares_wdc65816_full_change_music_load_stub_mailbox_smoke` | `build/audio/ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving the ROM-derived C4:FBBD CHANGE_MUSIC body can run its real pack-decision branches, call a stubbed LOAD_SPC700_DATA for each required pack, compute the one-based track command, call C0:ABBD, return, and reach key-on across representative tracks. |
| `ares_wdc65816_full_change_music_load_stub_metrics` | `build/audio/ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs/change-music-load-stub-metrics.json` | `yes` | Generated ignored metrics proving the LOAD_SPC700_DATA stub call arguments match MusicDatasetTable and MusicPackPointerTable for every representative track. |
| `ares_wdc65816_full_change_music_load_stub_render_metrics` | `build/audio/ares-wdc65816-full-change-music-load-stub-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving full CHANGE_MUSIC load-path-stub snapshots are audible across the representative track corpus. |
| `ares_wdc65816_full_change_music_load_apply_mailbox_smoke` | `build/audio/ares-wdc65816-full-change-music-load-apply-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json` | `yes` | Generated ignored corpus proving full CHANGE_MUSIC can start from bootstrap APU RAM, run real pack-decision branches, apply selected LOAD_SPC700_DATA payload streams into ares APU RAM, send the one-based track command, and reach key-on across representative tracks. |
| `ares_wdc65816_full_change_music_load_apply_render_metrics` | `build/audio/ares-wdc65816-full-change-music-load-apply-mailbox-render-jobs/libgme-render-metrics.json` | `yes` | Generated ignored render metrics proving full CHANGE_MUSIC load-apply snapshots are audible across the representative track corpus. |
