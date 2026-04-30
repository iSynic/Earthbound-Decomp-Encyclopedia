# Audio Pack Format And Renderer Frontier

Status: audio pack contract implemented; fused runtime snapshot generation and local libgme WAV export now validate across the snapshot-backed music table.

EarthBound audio packs are modeled here as `LOAD_SPC700_DATA` streams that populate APU RAM. The current playback/export path boots the real APU loader path, executes ROM-derived CHANGE_MUSIC through real C0:AB06 loader calls, captures key-on SPC snapshots, and renders them locally through libgme.

## Summary

- audio packs represented: `169`
- music tracks represented: `192`
- pack pointer entries represented: `169`
- stream statuses: `{'ok': 169}`
- unused pack ids in track table: `0`
- generated audio outputs policy: `build/audio` is ignored/local only

## What This Proves

- Every known audio pack has a byte-exact ROM source range and SHA-1.
- Every known audio pack parses as a complete `LOAD_SPC700_DATA` stream.
- Every music track resolves to the same primary/secondary/sequence pack order used by `CHANGE_MUSIC`.
- The corpus tools can deterministically construct 64 KiB APU RAM images for selected tracks.
- The fused all-track runtime corpus validates `191 / 191` load paths and `191 / 191` stable payload-region matches.
- The playback/export corpus renders `190 / 190` snapshot-backed tracks as audible local WAVs; track `4` (`NONE2`) is explicitly load-ok/no-key-on.

## What Is Not Final Yet

- The remaining fidelity gap is a bounded post-command observation loop rather than a full continuously scheduled SNES runtime.
- Generated SPC/WAV outputs are ROM-derived local artifacts and must stay ignored/uncommitted.
- External emulator comparison is still needed before claiming final audio-cycle equivalence.

## Loader Contract

- Runtime entry: `C0:AB06 LoadSpc700DataStream`.
- Cold-start initializer: `C4:FB58 InitializeMusicSubsystem` loads row-0 sequence/common pack before track changes.
- Each stream block is `u16 payload_byte_count`, then `u16 apu_destination` and payload bytes when the count is nonzero.
- A zero count terminates the stream with the loader's `$0500` final handshake.
- `CHANGE_MUSIC` applies primary sample pack, secondary sample pack, then sequence pack, skipping unchanged or `$FF` packs.

## Renderer Backends

| Backend | Status | Role | License policy |
| --- | --- | --- | --- |
| `ares` | diagnostic_runtime_harness_implemented | accuracy-first runtime/capture harness and future differential oracle | ISC/permissive candidate; review third-party notices before vendoring. |
| `snes_spc` | libgme_snapshot_renderer_implemented | lightweight SPC snapshot renderer for local WAV export once snapshots are generated | LGPL-2.1; use as lightweight SPC snapshot renderer with compliance notes. |
| `external_reference` | planned | bsnes/higan, Mesen2, or Mednafen comparison/export checks | GPL/noncommercial tools stay optional and out-of-process. |

## Tooling

- Rebuild: `python tools/build_audio_pack_contracts.py`.
- Validate: `python tools/validate_audio_pack_contracts.py`.
- Build ignored APU RAM seed for a track: `python tools/build_audio_track_snapshot.py 46`.
- Build ignored 20-track APU RAM corpus: `python tools/build_audio_snapshot_corpus.py`.
- Validate ignored corpus outputs: `python tools/validate_audio_snapshot_corpus.py`.
- Collect semantic loader transfer metrics: `python tools/collect_audio_load_stream_transfer_metrics.py`.
- Validate semantic loader transfer metrics: `python tools/validate_audio_load_stream_transfer_metrics.py`.
- Collect C0:AB06 loader contract evidence: `python tools/collect_audio_c0ab06_loader_contract.py`.
- Validate C0:AB06 loader contract evidence: `python tools/validate_audio_c0ab06_loader_contract.py`.
- Run byte-level C0:AB06 loader handshake corpus: `python tools/run_audio_c0ab06_loader_handshake_corpus.py`.
- Validate byte-level C0:AB06 loader handshake corpus: `python tools/validate_audio_c0ab06_loader_handshake_corpus.py`.
- Collect real ares SMP IPL receiver frontier: `python tools/collect_audio_c0ab06_real_ipl_frontier.py`.
- Validate real ares SMP IPL receiver frontier: `python tools/validate_audio_c0ab06_real_ipl_frontier.py`.
- Collect post-bootstrap game-driver reload frontier: `python tools/collect_audio_c0ab06_post_bootstrap_frontier.py`.
- Validate post-bootstrap game-driver reload frontier: `python tools/validate_audio_c0ab06_post_bootstrap_frontier.py`.
- Collect continuous representative track load frontier: `python tools/collect_audio_c0ab06_continuous_track_load_frontier.py`.
- Validate continuous representative track load frontier: `python tools/validate_audio_c0ab06_continuous_track_load_frontier.py`.
- Collect CHANGE_MUSIC-to-continuous-load sequence contract: `python tools/collect_audio_change_music_continuous_sequence_contract.py`.
- Validate CHANGE_MUSIC-to-continuous-load sequence contract: `python tools/validate_audio_change_music_continuous_sequence_contract.py`.
- Collect full CHANGE_MUSIC/real-C0:AB06 fusion frontier: `python tools/collect_audio_c0ab06_change_music_fusion_frontier.py`.
- Validate full CHANGE_MUSIC/real-C0:AB06 fusion frontier: `python tools/validate_audio_c0ab06_change_music_fusion_frontier.py`.
- Build fused CHANGE_MUSIC/C0:AB06 SPC index: `python tools/build_audio_c0ab06_change_music_fusion_spc_index.py`.
- Render fused CHANGE_MUSIC/C0:AB06 SPC corpus through libgme using `tools/run_audio_backend_batch.py`.
- Build all-track renderer jobs directly from the SPC index: `python tools/build_audio_backend_jobs_from_spc_index.py`.
- Build the all-track playback/export handoff: `python tools/build_audio_playback_export_manifest.py`.
- Validate the all-track playback/export handoff: `python tools/validate_audio_playback_export_manifest.py`.
- Collect fused post-command timing metrics: `python tools/collect_audio_fusion_timing_metrics.py`.
- Validate fused post-command timing metrics: `python tools/validate_audio_fusion_timing_metrics.py`.
- Build ignored renderer fixtures: `python tools/build_audio_renderer_fixtures.py --tracks 46`.
- Validate renderer fixtures: `python tools/validate_audio_renderer_fixtures.py`.
- Build ignored backend job queue: `python tools/build_audio_backend_jobs.py --backend ares`.
- Validate backend job queue: `python tools/validate_audio_backend_jobs.py`.
- Dry-run one backend job: `python tools/run_audio_backend_job.py ares-track-046-onett`.
- Check external harness shape: `python tools/run_audio_backend_job.py ares-track-046-onett --mode external --external python tools/audio_backend_stub_harness.py --job "{job}" --result "{result}"`.
- Dry-run pending backend jobs in batch: `python tools/run_audio_backend_batch.py --limit 2`.
- Collect backend result statuses: `python tools/collect_audio_backend_results.py`.
- Validate backend result summary: `python tools/validate_audio_backend_result_summary.py`.
- Check local ares prerequisite: `python tools/check_ares_backend_prereq.py`.
- Build ares link smoke: `cmake -S tools/ares_link_smoke -B build/audio/ares-link-smoke-msvc -G "Visual Studio 17 2022" -DARES_ROOT=<local-ares-checkout>`.
- Build backend adapter contract: `python tools/build_audio_backend_contract.py`.
- Validate backend adapter contract: `python tools/validate_audio_backend_contract.py`.
- Build a dry-run backend result: `python tools/build_audio_backend_result_stub.py --job-id ares-track-046-onett`.
- Validate one backend result: `python tools/validate_audio_backend_result.py build/audio/backend-jobs/ares-track-046-onett/result.json --job build/audio/backend-jobs/ares-jobs.json`.
- Inspect track-to-pack mappings: `python tools/lookup_audio_track.py onett`.
- Build SPC state frontier: `python tools/build_audio_spc_state_frontier.py`.
- Validate SPC state frontier: `python tools/validate_audio_spc_state_frontier.py`.
- Build APU destination region map: `python tools/build_audio_apu_region_map.py`.
- Validate APU destination region map: `python tools/validate_audio_apu_region_map.py`.
- Renderer abstraction scaffold: `tools/audio_renderers.py`.

## Audio Pack Contracts

| Pack | Kind | ROM range | Bytes | Parse | Blocks | Pointer | Track uses |
| ---: | --- | --- | ---: | --- | ---: | --- | ---: |
| `0` | `standard_audio_pack` | `E2:77F0..E2:ED2C` | 30012 | `ok` | 4 | `E2:77F0` | 2 |
| `1` | `custom_inline_audio_pack` | `E6:0000..E6:45D8` | 17880 | `ok` | 5 | `E6:0000` | 2 |
| `2` | `standard_audio_pack` | `E9:E084..E9:F8C8` | 6212 | `ok` | 4 | `E9:E084` | 5 |
| `3` | `standard_audio_pack` | `E3:0000..E3:5F64` | 24420 | `ok` | 4 | `E3:0000` | 3 |
| `4` | `standard_audio_pack` | `DF:EC46..DF:FFEE` | 5032 | `ok` | 4 | `DF:EC46` | 3 |
| `5` | `standard_audio_pack` | `EB:520C..EB:78D6` | 9930 | `ok` | 4 | `EB:520C` | 183 |
| `6` | `standard_audio_pack` | `E0:FCE1..E0:FFB3` | 722 | `ok` | 2 | `E0:FCE1` | 1 |
| `7` | `standard_audio_pack` | `E8:FF1B..E8:FFED` | 210 | `ok` | 2 | `E8:FF1B` | 1 |
| `8` | `standard_audio_pack` | `E7:849C..E7:C5C8` | 16684 | `ok` | 4 | `E7:849C` | 21 |
| `9` | `standard_audio_pack` | `EE:894F..EE:8ACA` | 379 | `ok` | 2 | `EE:894F` | 1 |
| `10` | `standard_audio_pack` | `ED:BD60..ED:C36C` | 1548 | `ok` | 5 | `ED:BD60` | 4 |
| `11` | `standard_audio_pack` | `EE:42BB..EE:46CE` | 1043 | `ok` | 2 | `EE:42BB` | 1 |
| `12` | `standard_audio_pack` | `EE:67B7..EE:6A85` | 718 | `ok` | 2 | `EE:67B7` | 1 |
| `13` | `standard_audio_pack` | `EB:FE22..EB:FFFF` | 477 | `ok` | 2 | `EB:FE22` | 1 |
| `14` | `standard_audio_pack` | `ED:DAFD..ED:E0AE` | 1457 | `ok` | 4 | `ED:DAFD` | 3 |
| `15` | `standard_audio_pack` | `EC:EB51..EC:F578` | 2599 | `ok` | 2 | `EC:EB51` | 1 |
| `16` | `standard_audio_pack` | `EE:365D..EE:3A7D` | 1056 | `ok` | 2 | `EE:365D` | 1 |
| `17` | `standard_audio_pack` | `EE:798E..EE:7BDF` | 593 | `ok` | 2 | `EE:798E` | 1 |
| `18` | `standard_audio_pack` | `E2:FC88..E2:FFFD` | 885 | `ok` | 2 | `E2:FC88` | 1 |
| `19` | `standard_audio_pack` | `ED:CF55..ED:D539` | 1508 | `ok` | 3 | `ED:CF55` | 2 |
| `20` | `standard_audio_pack` | `EE:1EFE..EE:2401` | 1283 | `ok` | 2 | `EE:1EFE` | 1 |
| `21` | `standard_audio_pack` | `EB:29E8..EB:520C` | 10276 | `ok` | 4 | `EB:29E8` | 5 |
| `22` | `standard_audio_pack` | `EE:7737..EE:798E` | 599 | `ok` | 2 | `EE:7737` | 1 |
| `23` | `standard_audio_pack` | `EE:3E9C..EE:42BB` | 1055 | `ok` | 3 | `EE:3E9C` | 2 |
| `24` | `standard_audio_pack` | `E7:C5C8..E7:FF64` | 14748 | `ok` | 4 | `E7:C5C8` | 12 |
| `25` | `standard_audio_pack` | `EC:E101..EC:EB51` | 2640 | `ok` | 9 | `EC:E101` | 8 |
| `26` | `standard_audio_pack` | `ED:9824..ED:9E93` | 1647 | `ok` | 2 | `ED:9824` | 1 |
| `27` | `standard_audio_pack` | `E9:0000..E9:3A74` | 14964 | `ok` | 4 | `E9:0000` | 7 |
| `28` | `standard_audio_pack` | `ED:B753..ED:BD60` | 1549 | `ok` | 3 | `ED:B753` | 2 |
| `29` | `standard_audio_pack` | `ED:FC9C..ED:FFFE` | 866 | `ok` | 2 | `ED:FC9C` | 1 |
| `30` | `standard_audio_pack` | `ED:E65C..ED:EBF4` | 1432 | `ok` | 2 | `ED:E65C` | 1 |
| `31` | `standard_audio_pack` | `EE:7274..EE:74D7` | 611 | `ok` | 2 | `EE:7274` | 1 |
| `32` | `standard_audio_pack` | `E3:FDCC..E3:FFF2` | 550 | `ok` | 2 | `E3:FDCC` | 1 |
| `33` | `standard_audio_pack` | `EB:9F8E..EB:C4E8` | 9562 | `ok` | 4 | `EB:9F8E` | 2 |
| `34` | `standard_audio_pack` | `ED:27F7..ED:3195` | 2462 | `ok` | 2 | `ED:27F7` | 2 |
| `35` | `standard_audio_pack` | `EA:C590..EA:F124` | 11156 | `ok` | 4 | `EA:C590` | 2 |
| `36` | `standard_audio_pack` | `E2:ED2C..E2:FC88` | 3932 | `ok` | 2 | `E2:ED2C` | 1 |
| `37` | `standard_audio_pack` | `E3:B0FA..E3:FDCC` | 19666 | `ok` | 4 | `E3:B0FA` | 3 |
| `38` | `standard_audio_pack` | `ED:6409..ED:6C06` | 2045 | `ok` | 3 | `ED:6409` | 2 |
| `39` | `standard_audio_pack` | `ED:4BA7..ED:53DF` | 2104 | `ok` | 2 | `ED:4BA7` | 1 |
| `40` | `standard_audio_pack` | `EB:78D6..EB:9F8E` | 9912 | `ok` | 4 | `EB:78D6` | 1 |
| `41` | `standard_audio_pack` | `EE:90FF..EE:9201` | 258 | `ok` | 2 | `EE:90FF` | 1 |
| `42` | `standard_audio_pack` | `E4:514A..E4:A232` | 20712 | `ok` | 4 | `E4:514A` | 1 |
| `43` | `standard_audio_pack` | `ED:9E93..ED:A4D7` | 1604 | `ok` | 2 | `ED:9E93` | 1 |
| `44` | `standard_audio_pack` | `EB:0000..EB:29E8` | 10728 | `ok` | 4 | `EB:0000` | 9 |
| `45` | `standard_audio_pack` | `D9:FC18..D9:FFE1` | 969 | `ok` | 2 | `D9:FC18` | 1 |
| `46` | `standard_audio_pack` | `E8:F872..E8:FF1B` | 1705 | `ok` | 2 | `E8:F872` | 1 |
| `47` | `standard_audio_pack` | `E6:CF08..E6:FF18` | 12304 | `ok` | 4 | `E6:CF08` | 5 |
| `48` | `standard_audio_pack` | `ED:436B..ED:4BA7` | 2108 | `ok` | 2 | `ED:436B` | 1 |
| `49` | `standard_audio_pack` | `EE:87CB..EE:894F` | 388 | `ok` | 2 | `EE:87CB` | 1 |
| `50` | `standard_audio_pack` | `E5:0000..E5:4C4A` | 19530 | `ok` | 4 | `E5:0000` | 1 |
| `51` | `standard_audio_pack` | `EE:56DF..EE:5A99` | 954 | `ok` | 2 | `EE:56DF` | 1 |
| `52` | `standard_audio_pack` | `EA:337A..EA:6594` | 12826 | `ok` | 4 | `EA:337A` | 1 |
| `53` | `standard_audio_pack` | `EE:14D4..EE:19EE` | 1306 | `ok` | 2 | `EE:14D4` | 1 |
| `54` | `standard_audio_pack` | `EA:0000..EA:337A` | 13178 | `ok` | 4 | `EA:0000` | 2 |
| `55` | `standard_audio_pack` | `EC:CAA1..EC:D5D8` | 2871 | `ok` | 3 | `EC:CAA1` | 2 |
| `56` | `standard_audio_pack` | `E5:954E..E5:DD32` | 18404 | `ok` | 4 | `E5:954E` | 2 |
| `57` | `standard_audio_pack` | `ED:D539..ED:DAFD` | 1476 | `ok` | 2 | `ED:D539` | 1 |
| `58` | `standard_audio_pack` | `EC:A7D8..EC:B38A` | 2994 | `ok` | 4 | `EC:A7D8` | 1 |
| `59` | `standard_audio_pack` | `CB:FEE2..CB:FFE4` | 258 | `ok` | 2 | `CB:FEE2` | 1 |
| `60` | `standard_audio_pack` | `E8:4066..E8:7EA6` | 15936 | `ok` | 4 | `E8:4066` | 4 |
| `61` | `standard_audio_pack` | `D8:F6B7..D8:FFE9` | 2354 | `ok` | 2 | `D8:F6B7` | 1 |
| `62` | `standard_audio_pack` | `EC:9B76..EC:A7D8` | 3170 | `ok` | 2 | `EC:9B76` | 1 |
| `63` | `standard_audio_pack` | `EE:28FE..EE:2DCD` | 1231 | `ok` | 2 | `EE:28FE` | 1 |
| `64` | `standard_audio_pack` | `E4:0000..E4:514A` | 20810 | `ok` | 4 | `E4:0000` | 1 |
| `65` | `standard_audio_pack` | `DB:F2EB..DB:FF64` | 3193 | `ok` | 2 | `DB:F2EB` | 1 |
| `66` | `standard_audio_pack` | `CB:E02A..CB:FEE2` | 7864 | `ok` | 4 | `CB:E02A` | 1 |
| `67` | `standard_audio_pack` | `EE:19EE..EE:1EFE` | 1296 | `ok` | 2 | `EE:19EE` | 1 |
| `68` | `standard_audio_pack` | `ED:73E2..ED:7BB6` | 2004 | `ok` | 2 | `ED:73E2` | 1 |
| `69` | `standard_audio_pack` | `EE:8ACA..EE:8C1E` | 340 | `ok` | 2 | `EE:8ACA` | 1 |
| `70` | `standard_audio_pack` | `E3:5F64..E3:B0FA` | 20886 | `ok` | 4 | `E3:5F64` | 2 |
| `71` | `standard_audio_pack` | `CC:F617..CC:FFDB` | 2500 | `ok` | 2 | `CC:F617` | 1 |
| `72` | `standard_audio_pack` | `EA:6594..EA:96F6` | 12642 | `ok` | 4 | `EA:6594` | 1 |
| `73` | `standard_audio_pack` | `E6:FF18..E6:FFF5` | 221 | `ok` | 2 | `E6:FF18` | 1 |
| `74` | `standard_audio_pack` | `E6:45D8..E6:8B9A` | 17858 | `ok` | 4 | `E6:45D8` | 1 |
| `75` | `standard_audio_pack` | `DD:FECE..DD:FFF8` | 298 | `ok` | 2 | `DD:FECE` | 1 |
| `76` | `standard_audio_pack` | `E6:8B9A..E6:CF08` | 17262 | `ok` | 4 | `E6:8B9A` | 3 |
| `77` | `standard_audio_pack` | `ED:C96E..ED:CF55` | 1511 | `ok` | 3 | `ED:C96E` | 2 |
| `78` | `standard_audio_pack` | `E7:0000..E7:4314` | 17172 | `ok` | 4 | `E7:0000` | 3 |
| `79` | `standard_audio_pack` | `DC:F8BF..DC:FF92` | 1747 | `ok` | 4 | `DC:F8BF` | 3 |
| `80` | `standard_audio_pack` | `E9:3A74..E9:7356` | 14562 | `ok` | 4 | `E9:3A74` | 2 |
| `81` | `standard_audio_pack` | `EE:7E29..EE:804D` | 548 | `ok` | 3 | `EE:7E29` | 2 |
| `82` | `standard_audio_pack` | `E7:4314..E7:849C` | 16776 | `ok` | 4 | `E7:4314` | 3 |
| `83` | `standard_audio_pack` | `EE:6D36..EE:6FDD` | 679 | `ok` | 4 | `EE:6D36` | 3 |
| `84` | `standard_audio_pack` | `E8:0000..E8:4066` | 16486 | `ok` | 4 | `E8:0000` | 8 |
| `85` | `standard_audio_pack` | `ED:AB12..ED:B136` | 1572 | `ok` | 2 | `ED:AB12` | 1 |
| `86` | `standard_audio_pack` | `ED:8B21..ED:91AF` | 1678 | `ok` | 2 | `ED:8B21` | 1 |
| `87` | `standard_audio_pack` | `ED:0A07..ED:1406` | 2559 | `ok` | 3 | `ED:0A07` | 2 |
| `88` | `standard_audio_pack` | `EE:6FDD..EE:7274` | 663 | `ok` | 2 | `EE:6FDD` | 1 |
| `89` | `standard_audio_pack` | `EA:96F6..EA:C590` | 11930 | `ok` | 4 | `EA:96F6` | 2 |
| `90` | `standard_audio_pack` | `ED:8389..ED:8B21` | 1944 | `ok` | 2 | `ED:8389` | 1 |
| `91` | `standard_audio_pack` | `EE:7BDF..EE:7E29` | 586 | `ok` | 2 | `EE:7BDF` | 1 |
| `92` | `standard_audio_pack` | `E5:4C4A..E5:954E` | 18692 | `ok` | 4 | `E5:4C4A` | 1 |
| `93` | `standard_audio_pack` | `EE:5A99..EE:5DFA` | 865 | `ok` | 2 | `EE:5A99` | 1 |
| `94` | `standard_audio_pack` | `CF:F2B5..CF:FF38` | 3203 | `ok` | 5 | `CF:F2B5` | 4 |
| `95` | `standard_audio_pack` | `EE:5DFA..EE:614C` | 850 | `ok` | 4 | `EE:5DFA` | 1 |
| `96` | `standard_audio_pack` | `CF:FF38..CF:FFF9` | 193 | `ok` | 2 | `CF:FF38` | 1 |
| `97` | `standard_audio_pack` | `EC:BF28..EC:CAA1` | 2937 | `ok` | 3 | `EC:BF28` | 2 |
| `98` | `standard_audio_pack` | `EC:6700..EC:8864` | 8548 | `ok` | 4 | `EC:6700` | 1 |
| `99` | `standard_audio_pack` | `ED:B136..ED:B753` | 1565 | `ok` | 2 | `ED:B136` | 1 |
| `100` | `standard_audio_pack` | `ED:91AF..ED:9824` | 1653 | `ok` | 2 | `ED:91AF` | 1 |
| `101` | `standard_audio_pack` | `EE:4EEA..EE:52E6` | 1020 | `ok` | 2 | `EE:4EEA` | 1 |
| `102` | `standard_audio_pack` | `CE:F8C6..CE:FFAA` | 1764 | `ok` | 3 | `CE:F8C6` | 2 |
| `103` | `standard_audio_pack` | `EE:52E6..EE:56DF` | 1017 | `ok` | 4 | `EE:52E6` | 3 |
| `104` | `standard_audio_pack` | `ED:7BB6..ED:8389` | 2003 | `ok` | 2 | `ED:7BB6` | 1 |
| `105` | `standard_audio_pack` | `EB:C4E8..EB:E9E4` | 9468 | `ok` | 4 | `EB:C4E8` | 1 |
| `106` | `standard_audio_pack` | `EC:D5D8..EC:E101` | 2857 | `ok` | 2 | `EC:D5D8` | 1 |
| `107` | `standard_audio_pack` | `EC:4592..EC:6700` | 8558 | `ok` | 2 | `EC:4592` | 1 |
| `108` | `standard_audio_pack` | `E2:0000..E2:77F0` | 30704 | `ok` | 4 | `E2:0000` | 1 |
| `109` | `standard_audio_pack` | `EC:23EC..EC:4592` | 8614 | `ok` | 2 | `EC:23EC` | 1 |
| `110` | `standard_audio_pack` | `E0:ED03..E0:FCE1` | 4062 | `ok` | 4 | `E0:ED03` | 3 |
| `111` | `standard_audio_pack` | `DA:FB07..DA:FFEE` | 1255 | `ok` | 2 | `DA:FB07` | 1 |
| `112` | `standard_audio_pack` | `EE:0554..EE:0A8B` | 1335 | `ok` | 2 | `EE:0554` | 1 |
| `113` | `standard_audio_pack` | `ED:F183..ED:F710` | 1421 | `ok` | 2 | `ED:F183` | 1 |
| `114` | `standard_audio_pack` | `EC:0000..EC:23EC` | 9196 | `ok` | 4 | `EC:0000` | 3 |
| `115` | `standard_audio_pack` | `EE:0FB2..EE:14D4` | 1314 | `ok` | 2 | `EE:0FB2` | 2 |
| `116` | `standard_audio_pack` | `ED:1DFF..ED:27F7` | 2552 | `ok` | 4 | `ED:1DFF` | 1 |
| `117` | `standard_audio_pack` | `ED:C36C..ED:C96E` | 1538 | `ok` | 2 | `ED:C36C` | 1 |
| `118` | `standard_audio_pack` | `E9:7356..E9:AC26` | 14544 | `ok` | 4 | `E9:7356` | 2 |
| `119` | `standard_audio_pack` | `ED:3195..ED:3A9C` | 2311 | `ok` | 2 | `ED:3195` | 1 |
| `120` | `standard_audio_pack` | `ED:5C01..ED:6409` | 2056 | `ok` | 2 | `ED:5C01` | 1 |
| `121` | `standard_audio_pack` | `ED:0000..ED:0A07` | 2567 | `ok` | 2 | `ED:0000` | 1 |
| `122` | `standard_audio_pack` | `E5:DD32..E5:FF38` | 8710 | `ok` | 4 | `E5:DD32` | 1 |
| `123` | `standard_audio_pack` | `E1:F581..E1:FFF2` | 2673 | `ok` | 2 | `E1:F581` | 1 |
| `124` | `standard_audio_pack` | `E8:BC88..E8:F872` | 15338 | `ok` | 4 | `E8:BC88` | 1 |
| `125` | `standard_audio_pack` | `E4:EED0..E4:FD92` | 3778 | `ok` | 2 | `E4:EED0` | 1 |
| `126` | `standard_audio_pack` | `E4:A232..E4:EED0` | 19614 | `ok` | 4 | `E4:A232` | 2 |
| `127` | `standard_audio_pack` | `EE:3236..EE:365D` | 1063 | `ok` | 2 | `EE:3236` | 1 |
| `128` | `standard_audio_pack` | `EE:8466..EE:8638` | 466 | `ok` | 2 | `EE:8466` | 1 |
| `129` | `standard_audio_pack` | `EE:74D7..EE:7737` | 608 | `ok` | 2 | `EE:74D7` | 1 |
| `130` | `standard_audio_pack` | `EE:8D65..EE:8EA2` | 317 | `ok` | 2 | `EE:8D65` | 1 |
| `131` | `standard_audio_pack` | `E9:AC26..E9:E084` | 13406 | `ok` | 4 | `E9:AC26` | 13 |
| `132` | `standard_audio_pack` | `ED:1406..ED:1DFF` | 2553 | `ok` | 4 | `ED:1406` | 3 |
| `133` | `standard_audio_pack` | `EC:B38A..EC:BF28` | 2974 | `ok` | 5 | `EC:B38A` | 4 |
| `134` | `standard_audio_pack` | `ED:EBF4..ED:F183` | 1423 | `ok` | 2 | `ED:EBF4` | 1 |
| `135` | `standard_audio_pack` | `EE:6A85..EE:6D36` | 689 | `ok` | 2 | `EE:6A85` | 1 |
| `136` | `standard_audio_pack` | `EE:0000..EE:0554` | 1364 | `ok` | 3 | `EE:0000` | 2 |
| `137` | `standard_audio_pack` | `EE:8FD6..EE:90FF` | 297 | `ok` | 2 | `EE:8FD6` | 1 |
| `138` | `standard_audio_pack` | `EE:2DCD..EE:3236` | 1129 | `ok` | 2 | `EE:2DCD` | 1 |
| `139` | `standard_audio_pack` | `D0:DFB4..D0:FFA8` | 8180 | `ok` | 4 | `D0:DFB4` | 2 |
| `140` | `standard_audio_pack` | `EA:F124..EA:FE8B` | 3431 | `ok` | 2 | `EA:F124` | 1 |
| `141` | `standard_audio_pack` | `ED:3A9C..ED:436B` | 2255 | `ok` | 2 | `ED:3A9C` | 1 |
| `142` | `standard_audio_pack` | `EE:46CE..EE:4ADF` | 1041 | `ok` | 2 | `EE:46CE` | 1 |
| `143` | `standard_audio_pack` | `DE:FCDD..DE:FFD4` | 759 | `ok` | 2 | `DE:FCDD` | 1 |
| `144` | `standard_audio_pack` | `EE:2401..EE:28FE` | 1277 | `ok` | 2 | `EE:2401` | 1 |
| `145` | `standard_audio_pack` | `EA:FE8B..EA:FFE2` | 343 | `ok` | 2 | `EA:FE8B` | 2 |
| `146` | `standard_audio_pack` | `ED:F710..ED:FC9C` | 1420 | `ok` | 2 | `ED:F710` | 1 |
| `147` | `standard_audio_pack` | `EE:804D..EE:826C` | 543 | `ok` | 2 | `EE:804D` | 1 |
| `148` | `standard_audio_pack` | `EE:3A7D..EE:3E9C` | 1055 | `ok` | 2 | `EE:3A7D` | 1 |
| `149` | `standard_audio_pack` | `E9:F8C8..E9:FF65` | 1693 | `ok` | 4 | `E9:F8C8` | 3 |
| `150` | `standard_audio_pack` | `ED:53DF..ED:5C01` | 2082 | `ok` | 3 | `ED:53DF` | 2 |
| `151` | `standard_audio_pack` | `EE:648C..EE:67B7` | 811 | `ok` | 2 | `EE:648C` | 1 |
| `152` | `standard_audio_pack` | `EE:826C..EE:8466` | 506 | `ok` | 2 | `EE:826C` | 1 |
| `153` | `standard_audio_pack` | `E8:7EA6..E8:BC88` | 15842 | `ok` | 4 | `E8:7EA6` | 2 |
| `154` | `standard_audio_pack` | `EB:E9E4..EB:FE22` | 5182 | `ok` | 2 | `EB:E9E4` | 1 |
| `155` | `standard_audio_pack` | `E4:FD92..E4:FFF9` | 615 | `ok` | 2 | `E4:FD92` | 1 |
| `156` | `standard_audio_pack` | `DC:E037..DC:F8BF` | 6280 | `ok` | 4 | `DC:E037` | 10 |
| `157` | `standard_audio_pack` | `EC:F578..EC:FF94` | 2588 | `ok` | 10 | `EC:F578` | 10 |
| `158` | `standard_audio_pack` | `ED:E0AE..ED:E65C` | 1454 | `ok` | 2 | `ED:E0AE` | 1 |
| `159` | `standard_audio_pack` | `EE:8638..EE:87CB` | 403 | `ok` | 2 | `EE:8638` | 1 |
| `160` | `standard_audio_pack` | `EE:4ADF..EE:4EEA` | 1035 | `ok` | 2 | `EE:4ADF` | 1 |
| `161` | `standard_audio_pack` | `ED:6C06..ED:73E2` | 2012 | `ok` | 4 | `ED:6C06` | 2 |
| `162` | `standard_audio_pack` | `ED:A4D7..ED:AB12` | 1595 | `ok` | 3 | `ED:A4D7` | 2 |
| `163` | `standard_audio_pack` | `EE:0A8B..EE:0FB2` | 1319 | `ok` | 2 | `EE:0A8B` | 1 |
| `164` | `standard_audio_pack` | `EE:614C..EE:648C` | 832 | `ok` | 2 | `EE:614C` | 1 |
| `165` | `standard_audio_pack` | `EC:8864..EC:9B76` | 4882 | `ok` | 4 | `EC:8864` | 1 |
| `166` | `standard_audio_pack` | `E5:FF38..E5:FFDE` | 166 | `ok` | 2 | `E5:FF38` | 1 |
| `167` | `standard_audio_pack` | `EE:8C1E..EE:8D65` | 327 | `ok` | 2 | `EE:8C1E` | 1 |
| `168` | `standard_audio_pack` | `EE:8EA2..EE:8FD6` | 308 | `ok` | 2 | `EE:8EA2` | 1 |

## Next Implementation Step

Continue Gate 2 by replacing the remaining bounded post-command SMP observation loop with a fuller scheduled runtime, then use external emulator captures as accuracy oracles for selected tracks.
