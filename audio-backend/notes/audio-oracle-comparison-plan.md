# Audio Oracle Comparison Plan

Status: oracle comparison contract ready; reference capture runner pending.

- scope: `representative_tracks`
- jobs: `20`
- source playback manifest: `build/audio/c0ab06-change-music-fusion-render-jobs-all/playback-export-manifest.json`
- generated output root: `build/audio/oracle-comparison`

## Reference Oracles

| Oracle | Status | Role | Integration policy |
| --- | --- | --- | --- |
| `ares` | `runner_pending` | permissive accuracy-first in-process/out-of-tree reference capture runner | preferred first implementation target because the project already has local ares harnesses |
| `mesen2_or_bsnes_higan_or_mednafen` | `optional_runner_pending` | external emulator validation oracle | use to corroborate ares/libgme output, not as a required app dependency |

## Comparison Policy

- SPC exactness: compare signatures, header registers, selected APU RAM region hashes, and DSP register snapshots where the reference exposes them
- PCM exactness: do not require byte-perfect PCM across independent renderers before alignment/timing has been characterized
- first gate: all representative jobs produce reference captures and classify as pass, audio_equivalent_state_delta, explained_timing_offset, or investigated_mismatch
- promotion gate: expand the same comparison contract from representative_tracks to all_tracks after the runner is stable
- PCM thresholds: `{'sample_rate': 32000, 'channels': 2, 'bits_per_sample': 16, 'minimum_seconds': 30.0, 'minimum_normalized_correlation_after_alignment': 0.98, 'maximum_leading_silence_delta_samples': 4096}`

## Workflow

1. Build or refresh this plan with `python tools/build_audio_oracle_comparison_plan.py`.
2. Capture a planned track with the reference emulator as SPC plus 32 kHz stereo WAV.
3. Import that capture with `python tools/import_audio_oracle_reference_capture.py --track-id <id> --spc <capture.spc> --wav <capture.wav> --oracle-id <emulator>`.
4. Collect comparison records with `python tools/collect_audio_oracle_comparison_results.py`.
5. Validate the gate with `python tools/validate_audio_oracle_comparison_summary.py`; add `--require-compared` only when the reference capture set should be complete.
6. After the representative gate is stable, regenerate with `--all-tracks` and use the same import/collect/validate flow.

Current ares-managed near-oracle result: full CHANGE_MUSIC/load-apply captures for the representative set classify `20 / 20` as `audio_equivalent_state_delta`: PCM output is byte-identical/zero-offset equivalent while full APU RAM differs in non-audio-affecting regions, with matching header registers and DSP registers.

## Release Gates

- Reference captures must be generated locally from a user-provided ROM.
- Reference SPC/WAV/PCM outputs must stay under ignored build/audio paths.
- Each mismatch must be classified as timing offset, renderer difference, snapshot-state difference, or unknown.
- Representative-track oracle comparison must pass before claiming release-quality audio playback/export.
- All-track oracle comparison should pass before claiming fully validated audio reconstruction.

## Jobs

| Track | Name | Source SPC | Comparison result path |
| ---: | --- | --- | --- |
| `001` | `GAS_STATION` | `fusion-track-001-gas_station-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-001-gas_station/oracle-comparison-result.json` |
| `002` | `NAMING_SCREEN` | `fusion-track-002-naming_screen-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-002-naming_screen/oracle-comparison-result.json` |
| `046` | `ONETT` | `fusion-track-046-onett-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-046-onett/oracle-comparison-result.json` |
| `056` | `SUMMERS` | `fusion-track-056-summers-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-056-summers/oracle-comparison-result.json` |
| `072` | `GIYGAS_AWAKENS` | `fusion-track-072-giygas_awakens-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-072-giygas_awakens/oracle-comparison-result.json` |
| `076` | `RUNAWAY5_CONCERT_1` | `fusion-track-076-runaway5_concert_1-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-076-runaway5_concert_1/oracle-comparison-result.json` |
| `082` | `BICYCLE` | `fusion-track-082-bicycle-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-082-bicycle/oracle-comparison-result.json` |
| `083` | `SKY_RUNNER` | `fusion-track-083-sky_runner-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-083-sky_runner/oracle-comparison-result.json` |
| `092` | `COFFEE_BREAK` | `fusion-track-092-coffee_break-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-092-coffee_break/oracle-comparison-result.json` |
| `095` | `SMILES_AND_TEARS` | `fusion-track-095-smiles_and_tears-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-095-smiles_and_tears/oracle-comparison-result.json` |
| `096` | `VS_CRANKY_LADY` | `fusion-track-096-vs_cranky_lady-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-096-vs_cranky_lady/oracle-comparison-result.json` |
| `100` | `VS_NEW_AGE_RETRO_HIPPIE` | `fusion-track-100-vs_new_age_retro_hippie-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-100-vs_new_age_retro_hippie/oracle-comparison-result.json` |
| `105` | `POKEY_MEANS_BUSINESS` | `fusion-track-105-pokey_means_business-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-105-pokey_means_business/oracle-comparison-result.json` |
| `109` | `EXPLOSION` | `fusion-track-109-explosion-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-109-explosion/oracle-comparison-result.json` |
| `121` | `ONETT_INTRO` | `fusion-track-121-onett_intro-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-121-onett_intro/oracle-comparison-result.json` |
| `133` | `HIDDEN_SONG` | `fusion-track-133-hidden_song-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-133-hidden_song/oracle-comparison-result.json` |
| `157` | `ATTRACT_MODE` | `fusion-track-157-attract_mode-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-157-attract_mode/oracle-comparison-result.json` |
| `175` | `TITLE_SCREEN` | `fusion-track-175-title_screen-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-175-title_screen/oracle-comparison-result.json` |
| `185` | `GIYGAS_PHASE3` | `fusion-track-185-giygas_phase3-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-185-giygas_phase3/oracle-comparison-result.json` |
| `190` | `GIYGAS_DEATH` | `fusion-track-190-giygas_death-change-music-fusion-last-keyon.spc` | `build/audio/oracle-comparison/track-190-giygas_death/oracle-comparison-result.json` |
