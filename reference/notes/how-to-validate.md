# How To Validate

This guide explains the minimum validation loop for the repository. Use it after
pulling changes, regenerating a scaffold, or promoting a bank range.

## Requirements

Use the US headerless EarthBound ROM:

- Size: `3145728` bytes
- SHA-1: `D67A8EF36EF616BC39306AA1B486E1BD3047815A`
- Map mode: `0x31`

Place it at one of these paths:

```text
./EarthBound (USA).sfc
./baserom/EarthBound (USA).sfc
```

The ROM is local-only and must not be committed.

## Verify The ROM

```powershell
python tools/verify_rom.py
```

For automation-friendly output:

```powershell
python tools/verify_rom.py --json
```

With an explicit ROM path:

```powershell
python tools/verify_rom.py --rom "baserom/EarthBound (USA).sfc"
```

## Validate One Bank Scaffold

The generic validator is the normal byte-equivalence check:

```powershell
python tools/validate_source_bank_byte_equivalence.py --bank C2 --module all --combined --scaffold src/c2/bank_c2_helpers_asar.asm --strict
```

Expected result:

- assembler step succeeds
- protected byte ranges compare equal to the original ROM
- report status is `OK`
- strict mode exits `0`

The validator writes reports to `build/` and `notes/` by default. Generated
scratch output under `build/` is ignored; durable Markdown reports under
`notes/` can be committed when they record a meaningful result.

## Regenerate A Bank Scaffold

For a bank that already has a build-candidate range manifest:

```powershell
python tools/build_source_bank_scaffold.py --bank C2
```

Default output:

```text
src/c2/bank_c2_helpers_asar.asm
```

Use explicit paths when testing a custom manifest or temporary output:

```powershell
python tools/build_source_bank_scaffold.py --bank C2 --ranges build/c2-build-candidate-ranges.json --output src/c2/bank_c2_helpers_asar.asm
```

Then rerun the byte-equivalence validator.

## Regenerate Status Dashboards

Source residual map for a single bank:

```powershell
python tools/build_source_bank_residual_map.py --bank C2
```

Candidate range report for a single bank:

```powershell
python tools/build_source_bank_candidate_ranges_doc.py --bank C2
```

Whole-project scaffold dashboard:

```powershell
python tools/build_source_scaffold_status.py
```

Source readiness triage:

```powershell
python tools/build_source_readiness_triage.py
```

Asset/data contract frontier:

```powershell
python tools/build_ui_font_town_map_asset_contracts.py
python tools/build_asset_data_contract_frontier.py
```

Audio playback/export backend handoff:

```powershell
python tools/validate_audio_backend_result_summary.py build/audio/ares-wdc65816-full-change-music-load-apply-mailbox-render-jobs/snes_spc-result-summary.json
python tools/validate_audio_render_metrics.py build/audio/ares-wdc65816-full-change-music-load-apply-mailbox-render-jobs/libgme-render-metrics.json
python tools/build_audio_playback_export_manifest.py
python tools/validate_audio_playback_export_manifest.py
```

The playback/export manifest is local-only. It references ROM-derived SPC/WAV
payloads under ignored `build/audio`, so it is a handoff contract for local app
playback and user export, not a distributable artifact.

Public audio contract manifests and docs:

```powershell
python tools/build_audio_backend_contract.py
python tools/validate_audio_backend_contract.py
python tools/build_audio_dependency_policy.py
python tools/validate_audio_dependency_policy.py
python tools/build_audio_export_duration_policy.py
python tools/validate_audio_export_duration_policy.py
python tools/build_audio_export_plan.py
python tools/validate_audio_export_plan.py
python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json
```

Those files are safe to commit because they contain contracts, counts, hashes,
and policy decisions, not ROM-derived audio bytes. Generated SPC/WAV/PCM files
remain under ignored `build/audio`.

## Promote Common Bank Shapes

Text banks:

```powershell
python tools/promote_text_bank_to_source_scaffold.py C5
```

Asset banks:

```powershell
python tools/promote_asset_bank_to_source_scaffold.py CA
```

Table-split banks:

```powershell
python tools/promote_table_splits_to_source_scaffold.py CF
```

Mixed asset/table banks:

```powershell
python tools/promote_mixed_asset_table_bank_to_source_scaffold.py D5
```

After any promotion:

```powershell
python tools/build_source_bank_scaffold.py --bank <BANK>
python tools/validate_source_bank_byte_equivalence.py --bank <BANK> --module all --combined --scaffold src/<bank>/bank_<bank>_helpers_asar.asm --strict
python tools/build_source_bank_residual_map.py --bank <BANK>
```

Use uppercase bank names for command arguments and lowercase bank names in paths.

## Before Committing

Run:

```powershell
git status --short
```

Commit durable changes only:

- source scaffolds under `src/`
- notes under `notes/`
- reusable tools under `tools/`
- root metadata such as `README.md`, `.gitignore`, and `.gitattributes`

Do not commit ROMs, generated scratch, local refs, build products, caches, or
temporary dumps.
