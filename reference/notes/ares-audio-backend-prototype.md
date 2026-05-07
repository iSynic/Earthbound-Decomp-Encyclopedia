# ares Audio Backend Prototype

Status: local ares source checkout configured; core `ares` and `desktop-ui` targets built; native diagnostic harness implemented; libgme PCM/WAV rendering implemented for diagnostic and real-SMP mailbox SPC snapshots; ROM-derived C0:ABBD command-sender bytes validated; full CPU-driven track-start fidelity still pending.

The prototype checkout lives outside this repository at `<local-ares-checkout>`. It is intentionally not a submodule or vendored dependency yet. The current policy is to prove one external backend path first, then decide whether a submodule, patch queue, or separate companion repository is the cleanest long-term shape.

## Local Build State

- ares repository: `https://github.com/ares-emulator/ares.git`
- local checkout: `<local-ares-checkout>`
- observed commit: `6f6786e04`
- configured preset: `windows-msvc`
- built target: `ares`
- built core library: `<local-ares-checkout>\build_msvc\ares\RelWithDebInfo\ares.lib`
- built target: `desktop-ui`
- built executable: `<local-ares-checkout>\build_msvc\desktop-ui\rundir\ares.exe`
- executable version check: `master - (6f6786e04 - 2026-04-27)`

Check this state with:

```sh
python tools/check_ares_backend_prereq.py
```

The check writes ignored status to `build/audio/ares-backend-status.json`.

## Link Smoke

The repo includes a tiny CMake link-smoke target at `tools/ares_link_smoke`. It is meant to prove that a standalone backend executable can include the ares SFC headers, link against the locally built `ares.lib`, and touch SFC DSP/APU RAM state.

Configure/build it with:

```sh
cmake -S tools/ares_link_smoke -B build/audio/ares-link-smoke -DARES_ROOT=<local-ares-checkout>
cmake --build build/audio/ares-link-smoke --config RelWithDebInfo
```

If this works, the first true backend harness can grow out of the same shape.

Current link-smoke result:

- configured build dir: `build/audio/ares-link-smoke-msvc`
- executable: `build/audio/ares-link-smoke-msvc/RelWithDebInfo/earthbound_ares_link_smoke.exe`
- run output: `ares SFC DSP link smoke OK; apuram[0]=0`

## Backend Boundary

The repo-side backend contract supports three modes:

```sh
python tools/run_audio_backend_job.py ares-track-046-onett
python tools/run_audio_backend_job.py ares-track-046-onett --mode native-ares
python tools/run_audio_backend_batch.py --mode native-ares --force
```

The generic external harness shape remains:

```sh
python tools/run_audio_backend_job.py ares-track-046-onett --mode external --external python tools/audio_backend_stub_harness.py --job "{job}" --result "{result}"
```

A real ares harness should keep the same shape:

```sh
ares-earthbound-audio-harness --job "{job}" --result "{result}"
```

The harness consumes one generated `job.json`, reads its renderer fixture and APU RAM seed, runs or captures through ares, and writes `result.json` using schema `earthbound-decomp.audio-backend-result.v1`.

## Native Diagnostic Harness

The repo now includes a native ares-backed harness at `tools/ares_audio_harness`.

Configure/build it with:

```sh
cmake -S tools/ares_audio_harness -B build/audio/ares-audio-harness-msvc -G "Visual Studio 17 2022" -DARES_ROOT=<local-ares-checkout>
cmake --build build/audio/ares-audio-harness-msvc --config RelWithDebInfo
```

Current executable:

```text
build/audio/ares-audio-harness-msvc/RelWithDebInfo/earthbound_ares_audio_harness.exe
```

Current capability:

- consumes one backend `job.json`;
- loads the referenced renderer fixture;
- reads and SHA-1 verifies the generated 64 KiB APU RAM seed;
- imports the seed into `ares::SuperFamicom::dsp.apuram`;
- captures public SPC700 register defaults and DSP register hash/nonzero count;
- uses ares' SPC700 disassembler to probe the terminal entry point at `$0500`;
- runs a harness-only `ares::SPC700` execution probe with a RAM/IO shim, rough timer0 progress, and a diagnostic APUIO0 track-command delivery mode, enough to observe driver initialization, DSP register writes, timer setup, command recognition, and track-specific update code;
- writes an `ares-state-capture.json` output record;
- writes a diagnostic `complete_spc_snapshot` at `diagnostic-driver-state.spc` using the probe's APU RAM, SPC700 registers, and DSP registers;
- writes a diagnostic last-key-on SPC snapshot at `diagnostic-last-keyon-state.spc` when the probe reaches a nonzero DSP `KON` write;
- records instruction/sequence/shim-tick evidence for IO reads, IO writes, IO tail windows, DSP writes, diagnostic host-command injection, host-command first read, the ordered host-command IO window, and the last-key-on snapshot;
- writes a schema-valid backend `result.json`.

Representative `$0500` entry probe after importing ONETT's APU RAM seed:

```text
0x0500  clp
0x0501  ldx #$cf
0x0503  txs
0x0504  lda #$00
0x0506  tax
0x0507  sta (x++)
0x0508  cpx #$e0
0x050A  bne $0507
0x050C  jsr $16a5
0x050F  lda #$55
```

That confirms the loaded driver entry clears direct-page RAM through `$00DF`, sets the stack, then enters the driver helper at `$16A5` before beginning the CPU/APU port handshake sequence.

The execution probe is not a renderer and does not use a full SFC scheduler. Earlier versions stopped at the driver timer wait at `$0579/$057C`:

```text
0x0579  ldy $00fd
0x057C  beq $0579
```

The timer0 diagnostic shim now lets the driver escape that wait. The harness also pre-seeds the one-byte APUIO0 track command after timer enable, mirroring the high-level `CHANGE_MUSIC -> C0ABBD` handoff enough to see track-specific driver update paths. This is still diagnostic, not a real CPU/APU handshake.

Representative ONETT probe counts:

- `200000` SPC700 instructions executed;
- diagnostic APUIO0 command: `$2E`;
- final PC: `$0E28`;
- `5729` APU IO reads;
- `5019` APU IO writes;
- `2402` DSP register writes observed;
- `288` reads of timer counter `$FD`;
- first timer setup remains `$F1=$F0`, `$FA=$10`, `$F1=$01`.

This is a useful boundary: the next implementation step is not more static RAM import, a simple timer escape, or command-byte discovery, but replacing diagnostic APUIO0 command delivery with the real CPU/APU track-start handshake or a full-SMP execution path that naturally carries that handshake and timing state.

The emitted `.spc` is intentionally diagnostic. It is structurally valid and useful for `snes_spc` parser/playback experiments, but it is not yet a faithful captured runtime snapshot because the CPU/APU handshake, exact elapsed cycles, SMP timers, and DSP timing have not been produced by the full emulator path.

Current corpus result:

- `20 / 20` representative ares jobs run through `--mode native-ares`;
- all `20` results validate;
- all `20` runs now inject their own track command byte and land at track-specific final PCs/counts;
- all `20` runs emit a validated diagnostic SPC snapshot under `build/audio/backend-jobs/<job-id>/diagnostic-driver-state.spc`;
- all `20` runs emit a validated real last-key-on snapshot under `build/audio/backend-jobs/<job-id>/diagnostic-last-keyon-state.spc`;
- all `20` runs now record the diagnostic command injection and the driver's first read of that command before the last-key-on boundary;
- a stricter on-first-read command timing mode injects the diagnostic APUIO0 command only when the driver first reads port 0, still reaches `20 / 20` key-on events after command read, and still renders `20 / 20` audible tracks through libgme;
- the same on-first-read run now records an ordered command IO window; the mailbox frontier validates `20 / 20` command bytes matching track ids, `20 / 20` first APUIO0 command reads, `20 / 20` immediate zero APUIO0 acknowledgement writes, and `20 / 20` key-on-after-command-read ordering;
- `tools/collect_audio_diagnostic_spc_snapshots.py` indexes those snapshots at `build/audio/backend-jobs/diagnostic-spc-snapshots.json`;
- `tools/snes_spc_diagnostic_harness.py` exercises the lightweight backend adapter by copying those snapshots into `snes_spc` job outputs and writing readiness metadata without linking the renderer library yet;
- out-of-tree libgme at `<local-libgme-checkout>` builds SPC support into `gme.lib`;
- `tools/libgme_audio_harness` renders job-specified WAVs from the generated SPC snapshots through libgme;
- native ares diagnostic capture results remain `unsupported`, because that harness captures/imports state but does not render audio itself.

The libgme renderer result status is `ok` for the diagnostic render job itself, but that should not be confused with final audio faithfulness. It proves the WAV/export adapter path works; the remaining accuracy work is still getting the source SPC state from a real full-SMP runtime boundary.

Current libgme render metrics:

- `20 / 20` diagnostic renders produce valid WAV files.
- `12` are silent.
- `3` are click/trace-level.
- `5` are very quiet.
- `0` are confidently audible.

That baseline is valuable: future ares capture-boundary experiments should move tracks from silent/trace into audible without changing the renderer side.

The capture-side instrumentation now gives the matching explanation:

- `20 / 20` representative tracks issue DSP key-on writes during the ares diagnostic probe.
- final diagnostic SPC headers still have `KON=$00`.
- the current stop point is therefore structurally valid but musically poorly timed.

The next capture-boundary experiment was to capture the probe state at the last nonzero key-on write and render that snapshot corpus through libgme. That succeeded and became the positive control for the stricter command-timing and real-SMP mailbox work below.

## Key-On Priming Experiment

The project now has a deliberately non-faithful experiment that patches each diagnostic SPC's DSP `KON` register to the last key-on byte observed during the ares probe and clears `KOF`.

Tools:

- `tools/build_audio_keyon_primed_spc_experiment.py`
- `tools/validate_audio_keyon_primed_spc_experiment.py`
- `tools/compare_audio_render_metrics.py`
- `tools/validate_audio_render_metrics_comparison.py`

Result:

- baseline diagnostic renders: `12` silent, `3` click/trace, `5` very quiet, `0` audible.
- key-on primed renders: `3` silent, `1` click/trace, `3` very quiet, `13` audible.
- comparison: `14` tracks improved, `6` unchanged, `0` worsened.

This does not make the primed SPCs faithful. It proves the direction: we need the ares-side capture boundary to land on real key-on/runtime state rather than patching headers after the fact.

## Last-Key-On Snapshot Experiment

The native ares harness now records the complete diagnostic RAM, DSP register file, and SPC700 registers at the last nonzero DSP `KON` write observed during the probe. `tools/build_audio_last_keyon_spc_experiment.py` indexes those snapshots, and `tools/validate_audio_last_keyon_spc_experiment.py` verifies the corpus.

Result:

- `20 / 20` representative last-key-on SPC snapshots validate.
- `20 / 20` render as audible through the same libgme harness.
- `20 / 20` have matching render source SHA-1s against the last-key-on snapshot index.
- `20 / 20` record command injection, command first-read, command-read-after-injection, and key-on-after-command-read ordering.
- compared with the baseline final-state diagnostic snapshots: `20` improved, `0` unchanged, `0` worsened.
- compared with the non-faithful key-on priming experiment: `7` improved, `13` unchanged, `0` worsened.

This proved the renderer path was good and that the remaining accuracy problem was source-state faithfulness. The later real-SMP mailbox smoke keeps this audible boundary while replacing the custom CPU-input shortcut with ares' own mailbox path.

## No-Command Negative Control

The harness also supports `--disable-diagnostic-command-preseed`. `tools/run_audio_ares_no_command_experiment.py` runs the 20-track corpus with that flag and writes a local ignored frontier report.

Result:

- `20 / 20` no-command ares captures validate.
- `0 / 20` inject a host command.
- `0 / 20` reach a host-command first-read event.
- `0 / 20` reach DSP key-on.
- all `20` stop at final PC `$055A`.

This is the useful negative control for the next phase. The diagnostic command preseed is not merely improving timing; without the CPU/APU track-start command, the driver never reaches the audible key-on boundary at all.

## Command Timing Experiment

The harness also supports `--diagnostic-command-preseed-on-first-read`. `tools/run_audio_ares_command_timing_experiment.py --mode on_first_read` runs the 20-track corpus with the diagnostic APUIO0 command withheld until the driver first reads port 0.

Result:

- `20 / 20` on-first-read ares captures validate.
- `20 / 20` inject the host command at the first port-0 read.
- `20 / 20` reach DSP key-on after that command read.
- `20 / 20` last-key-on snapshots render as audible through libgme.
- compared with the earlier last-key-on render corpus: `0` improved, `20` unchanged, `0` worsened.
- compared with baseline final-state diagnostic snapshots: `20` improved, `0` unchanged, `0` worsened.

This makes the diagnostic shortcut narrower and cleaner. The audible boundary does not require seeding the command before the driver asks for it; it requires delivering the same one-byte CPU/APU track-start command at the real mailbox boundary.

## Mailbox Frontier

`tools/collect_audio_mailbox_frontier.py` and `tools/validate_audio_mailbox_frontier.py` turn the command IO window into a regression target for replacing the shortcut. The current 20-track on-first-read corpus shows a stable driver pattern:

- first APUIO0 command read at `$062A`;
- command byte equals the one-based track id sent by `CHANGE_MUSIC -> C0ABBD`;
- immediate APUIO0 write of `$00` at `$062A`;
- repeated APUIO0 reads of the same command shortly afterward;
- last-key-on boundary occurs after the command read.

This is still diagnostic because the CPU side is not running yet, but it narrows the faithful replacement target to a concrete mailbox transcript instead of a vague "make audio happen" milestone.

`tools/build_audio_cpu_mailbox_contract.py` promotes that transcript into a checked contract at `manifests/audio-cpu-mailbox-contract.json` and `notes/audio-cpu-mailbox-contract.md`. It ties together:

- ebsrc `CHANGE_MUSIC`, which sends the one-based track id through `UNKNOWN_C0ABBD`;
- local C0 source for `C0ABBD_SendApuPort0CommandByte`, which writes A low byte to `$2140/APUIO0`;
- local C0 source for `C0AC20_ReadApuPort0Byte`, which reads `$2140/APUIO0`;
- ares CPU `$2140-$2143` accessors, which call `smp.portWrite/portRead`;
- ares SMP `$F4-$F7` accessors, which expose the reciprocal CPU/APU mailbox fields.

The next faithful bridge should reproduce the same `$062A` command-read, `$00` acknowledgement, and key-on ordering through those ares mailbox paths instead of diagnostic APUIO0 injection.

## ares SMP Mailbox Smoke

`tools/ares_smp_mailbox_smoke` is a deliberately small bridge test between the custom shim and a full scheduled SFC run. It loads a generated APU RAM seed into ares' real `SuperFamicom::dsp.apuram`, uses the real `SuperFamicom::smp` object, and delivers the track command through `smp.portWrite(0, track)` when the SMP reaches the `$062A` command-read boundary.

Result:

- initial `smp.portWrite` before driver setup is too early: the driver clears the mailbox during initialization and does not reach key-on.
- timed `smp.portWrite` at `$062A` reaches the zero acknowledgement and key-on boundary.
- `tools/run_audio_ares_smp_mailbox_smoke.py` validates this across the 20-track representative corpus.
- `20 / 20` tracks reach `$062A`, zero acknowledgement, and key-on after timed ares `smp.portWrite`.
- `tools/build_audio_ares_smp_mailbox_spc_index.py` promotes the generated key-on snapshots into a snes_spc/libgme snapshot index.
- the indexed snapshots render `20 / 20` representative tracks as audible through libgme.
- compared with the custom last-key-on corpus: `0` improved, `20` unchanged, `0` worsened at the classification level.
- compared with baseline final-state diagnostic snapshots: `20` improved, `0` unchanged, `0` worsened.
- the same smoke harness now also supports `--inject-via-cpu-apu-write`, which calls `ares::SuperFamicom::cpu.writeAPU(0x2140, track)` at the same `$062A` command-read boundary.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery cpu_writeapu --out build/audio/ares-cpu-writeapu-mailbox-smoke-jobs` validates that CPU-facing bridge across the same 20-track corpus.
- CPU-side `writeAPU` snapshots also render `20 / 20` tracks as audible, with `0` classification regressions versus direct `smp.portWrite` and `20` improvements versus baseline final-state diagnostic snapshots.
- the smoke harness also supports `--inject-via-cpu-instruction`, which executes the modeled WDC65816 prefix of `C0:ABBD` (`sep #$20; sta.l $002140`) and routes that instruction's bus write through `cpu.writeAPU`.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_sta2140 --out build/audio/ares-wdc65816-sta2140-mailbox-smoke-jobs` validates that instruction bridge across the same 20-track corpus.
- modeled WDC65816 snapshots also render `20 / 20` tracks as audible, with `0` classification regressions versus CPU-side `writeAPU` and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_c0abbd --out build/audio/ares-wdc65816-c0abbd-mailbox-smoke-jobs` executes the full modeled `C0:ABBD` routine bytes (`sep #$20; sta.l $002140; rep #$30; rtl`) with a synthetic return address.
- full modeled `C0:ABBD` snapshots also render `20 / 20` tracks as audible, with `0` classification regressions versus the STA-prefix probe and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/build_audio_cpu_routine_fixtures.py` extracts the real `C0:ABBD` routine bytes from the user-provided ROM into ignored local fixtures.
- that fixture caught and corrected a source truth issue: the retail ROM uses `STA long $002140` (`E2 20 8F 40 21 00 C2 30 6B`), not absolute `STA $2140`.
- local C0 sources now use `sta.l $002140` for both the track-command sender and the stop-music sender.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_rom_c0abbd --out build/audio/ares-wdc65816-rom-c0abbd-mailbox-smoke-jobs` executes the ROM-derived `C0:ABBD` fixture bytes with the same synthetic return context.
- ROM-derived `C0:ABBD` snapshots render `20 / 20` tracks as audible, with `0` classification regressions versus the modeled full routine and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_rom_c0abbd_jsl --out build/audio/ares-wdc65816-rom-c0abbd-jsl-mailbox-smoke-jobs` executes a modeled `JSL $C0ABBD` caller with the ROM-derived routine bytes mapped at their real CPU address.
- the JSL-call probe executes five CPU instructions, writes exactly once to `$2140`, and returns through `RTL` to `$008004`; it removes the older pre-baked return-address shortcut while still using a timed harness trigger at the SMP `$062A` boundary.
- ROM-derived `C0:ABBD` JSL-call snapshots render `20 / 20` tracks as audible, with `0` classification regressions versus direct ROM-derived C0:ABBD and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_change_music_tail --out build/audio/ares-wdc65816-change-music-tail-mailbox-smoke-jobs` executes ROM-derived `C4:FD0E` bytes from the tail of `CHANGE_MUSIC`: `LDY $10; TYA; INC; JSL C0:ABBD; PLD; RTL`.
- the tail probe seeds direct-page `$10` with the zero-based track index, so the one-based APUIO0 command is computed by the real `CHANGE_MUSIC` tail instructions instead of being preloaded in A.
- CHANGE_MUSIC tail snapshots render `20 / 20` tracks as audible, with `0` classification regressions versus the ROM-derived C0:ABBD JSL-call corpus and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_full_change_music --out build/audio/ares-wdc65816-full-change-music-mailbox-smoke-jobs` executes ROM-derived `C4:FBBD..FD17` `CHANGE_MUSIC` bytes under a documented pre-satisfied pack state.
- the full `CHANGE_MUSIC` probe seeds A with the requested one-based track id, lets the real routine normalize table/direct-page state, serves `MusicDatasetTable` reads from a 573-byte ROM-derived fixture, pre-satisfies current pack variables to the selected real table row, maps ROM-derived `C0:ABBD`, and stubs side-effect helpers that are outside this isolated CPU probe.
- the full probe executes 71 WDC65816 instructions for ONETT, writes exactly once to `$2140`, returns to `$008004`, reaches `$062A`, zero acknowledgement, and key-on for `20 / 20` representative tracks.
- full `CHANGE_MUSIC` pre-satisfied-pack snapshots render `20 / 20` tracks as audible, with `0` classification regressions versus the CHANGE_MUSIC tail corpus and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_full_change_music_load_stub --out build/audio/ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs` executes the same ROM-derived `CHANGE_MUSIC` body with current pack variables intentionally unsatisfied, maps the ROM-derived `GET_AUDIO_BANK` helper bytes and `MusicPackPointerTable`, and records each `LOAD_SPC700_DATA` call before stubbing the transfer itself.
- the load-path-stub probe reaches command read, zero acknowledgement, and key-on for `20 / 20` representative tracks; `tools/collect_audio_change_music_load_stub_metrics.py` reports `0` loader-argument mismatches against the ROM tables, with call counts `{2: 2, 3: 18}`.
- full `CHANGE_MUSIC` load-path-stub snapshots render `20 / 20` tracks as audible, with `0` classification regressions versus the pre-satisfied full `CHANGE_MUSIC` corpus and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/collect_audio_load_stream_transfer_metrics.py` semantically replays the contract-selected cold-start `LOAD_SPC700_DATA` streams into APU RAM and compares them against the generated corpus.
- semantic transfer metrics currently validate `20 / 20` representative tracks with `0` RAM mismatches and `0` load-call mismatches; destination-role coverage is 156 high/sample payload blocks, 57 sequence/runtime-table blocks, 34 music-sequence/sample-directory blocks, and 21 driver/overlay blocks.
- `tools/build_audio_bootstrap_snapshot_corpus.py` builds bootstrap-only APU RAM seeds so the smoke harness can start from the initializer/common pack instead of fully prebuilt track RAM.
- `tools/run_audio_ares_smp_mailbox_smoke.py --delivery wdc65816_full_change_music_load_apply --out build/audio/ares-wdc65816-full-change-music-load-apply-mailbox-smoke-jobs` starts from those bootstrap seeds, lets full `CHANGE_MUSIC` choose track packs, and semantically applies the selected `LOAD_SPC700_DATA` streams from ROM bytes into ares APU RAM before sending the track command.
- load-apply metrics currently apply 58 streams, 188 payload blocks, and 531593 bytes across the 20-track corpus with `0` apply errors; the resulting snapshots render `20 / 20` tracks as audible, with `0` classification regressions versus load-stub snapshots and `20` improvements versus baseline final-state diagnostic snapshots.
- `tools/collect_audio_c0ab06_loader_contract.py` anchors that semantic stream application to a byte-checked ROM-derived `C0:AB06..ABA7` loader fixture; the fixture SHA-1 is `e0cfb01348233939a0c4d98c42a0d8350f0ce6d9`, and the selected stream totals match load-apply evidence for `20 / 20` jobs.
- `tools/ares_c0ab06_loader_handshake` executes the same ROM-derived loader fixture through ares' WDC65816 core against a modeled APUIO receiver.
- `tools/run_audio_c0ab06_loader_handshake_corpus.py` validates `58 / 58` selected stream occurrences across `33` unique pack streams, matching expected payload bytes, payload writes, block-start tokens, terminal tokens, return PC `$008004`, per-block final-region hashes, and full 64 KiB APU RAM reconstruction hashes.
- `tools/collect_audio_c0ab06_real_ipl_frontier.py` executes the ROM-derived loader fixture against the real ares SMP IPL receiver.
- the real-IPL frontier validates payload-region equality for `33 / 33` selected unique pack streams and proves pack `1` completes the terminal handoff back to the CPU loader at `$008004`.
- `tools/collect_audio_c0ab06_post_bootstrap_frontier.py` boots pack `1` through the real IPL, keeps the game driver alive, then reloads later packs through the running driver.
- the post-bootstrap frontier validates payload-region equality for `32 / 32` non-bootstrap selected unique pack streams.
- `tools/collect_audio_c0ab06_continuous_track_load_frontier.py` boots pack `1` once, then loads each representative track's full selected pack sequence through the running driver.
- the continuous track-load frontier validates stable payload-region equality for `20 / 20` representative tracks; live driver/overlay code is explicitly marked as mutable runtime state rather than static payload.
- `tools/collect_audio_change_music_continuous_sequence_contract.py` joins the real `CHANGE_MUSIC` load-stub call order, the byte-checked C0:AB06 loader-contract stream order, and the continuous real-driver C0:AB06 sequence order.
- the sequence contract validates `20 / 20` representative tracks, so the current continuous harness is now proven to run exactly the pack order requested by real `CHANGE_MUSIC`, even though the two control paths are not yet fused into one execution.
- `tools/collect_audio_c0ab06_change_music_fusion_frontier.py` fuses the paths: after real IPL bootstrap, full ROM-derived `CHANGE_MUSIC` invokes real `JSL C0:AB06` calls against the running driver, then sends the final C0:ABBD track command.
- the fusion frontier validates `20 / 20` representative runs, `20 / 20` stable payload-region matches, command read, zero acknowledgement, and key-on after acknowledgement.
- the same fusion frontier now emits `20 / 20` valid key-on SPC snapshots; `tools/build_audio_c0ab06_change_music_fusion_spc_index.py` indexes them, and the libgme backend renders `20 / 20` successful WAV jobs with `20 / 20` audible classifications.
- the all-track fusion corpus validates `191 / 191` load paths and `191 / 191` stable payload-region matches. It emits `190 / 191` key-on snapshots; track `4` (`NONE2`) is explicitly load-ok/no-key-on.
- `tools/build_audio_backend_jobs_from_spc_index.py` builds renderer jobs directly from the all-track snapshot index, and the libgme backend now renders `190 / 190` successful WAV jobs with `190 / 190` audible classifications.
- `tools/collect_audio_fusion_timing_metrics.py` confirms the final command write now uses `0` immediate SMP burst instructions. Across the all-track corpus, command-read/zero-ack appears after `4055..8240` observed SMP instructions, and the `190` key-on tracks reach key-on `22245..134926` observed SMP instructions after acknowledgement.

This is still not final fidelity because the harness uses bounded post-command SMP-main observation and captures at key-on. It is, however, now using ROM-verified WDC65816 control flow from the start of the real `CHANGE_MUSIC` body, real pack-decision branches, ROM-derived dataset and pack-pointer fixtures, direct CPU execution of the real C0:AB06 loader bytes inside the `CHANGE_MUSIC` call path, the real ares SMP IPL receiver for boot-loader payload transfer, the running game driver for post-bootstrap pack reloads, a real `JSL`/`RTL` stack round trip into `C0:ABBD`, ares' CPU-facing APUIO bridge, command-read/ack/key-on evidence, and the same audible SPC/render pipeline. Gate 1 is satisfied for the representative corpus, Gate 2 now advances the post-command boundary through `ares::SuperFamicom::smp.main()` with zero immediate SMP burst instructions after the command write, and Gate 3 broad-corpus playback/export is satisfied for every snapshot-backed track. The next implementation step is Gate 2 continued: move this boundary into fuller CPU/APU/DSP scheduling.

## Harness Direction

The ares SFC core exposes useful state:

- `ares::SuperFamicom::dsp.apuram[64_KiB]`
- `ares::SuperFamicom::dsp.registers[128]`
- `ares::SuperFamicom::smp.portRead/portWrite(...)`
- system serialization through `ares::SuperFamicom::system.serialize(...)`

Important caveat: several SMP/DSP timing and register fields needed for a faithful snapshot are intentionally private, so the first accurate backend should drive the real SNES/APU boot and command path rather than trying to synthesize private state from the outside.

## Next Implementation Step

Extend the native harness past the current fused `CHANGE_MUSIC -> real C0:AB06 -> live driver -> C0:ABBD command` frontier. The next real seam is driving the boot/load/track-command path through more natural ares CPU/APU scheduling so the same audible boundary comes from less harness-controlled timing plus full runtime state: SPC700 registers, DSP registers, timer/control state, APUIO mailbox state, and a stable capture/render boundary. Use the fused C0:AB06/CHANGE_MUSIC frontier as the positive target and the no-command `$055A`/zero-key-on corpus as the negative control.

The first track should remain `ares-track-046-onett`, with the 20-track representative corpus kept as the regression suite.
