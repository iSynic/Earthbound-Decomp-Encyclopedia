# Public Release Checklist

Use this before making the repository public or cutting a first release.

## Required

- `git status --short` reviewed so only durable docs, source, manifests, and
  tools are candidates for commit.
- `.gitignore` still excludes ROMs, `baserom/`, `build/`, `asm/`, `dumps/`,
  `refs/`, caches, and `tmp_*.asm`.
- No ROMs, generated SPC/WAV/PCM files, extracted asset dumps, local references,
  or build products are tracked.
- README and `notes/project-status.md` describe the current state without
  claiming a finished decompilation or C port.
- `notes/public-release-known-limits.md` is linked from README.
- Audio dependency/license posture is current in
  `notes/audio-dependency-policy.md`.

## Validation Commands

```powershell
python tools/verify_rom.py
python tools/build_source_scaffold_status.py
python tools/build_readable_source_bank_closure.py
python tools/build_asset_data_contract_frontier.py
python tools/build_audio_backend_contract.py
python tools/validate_audio_backend_contract.py
python tools/build_audio_dependency_policy.py
python tools/validate_audio_dependency_policy.py
python tools/build_audio_export_plan.py
python tools/validate_audio_export_plan.py
python tools/validate_audio_oracle_verification_report.py manifests/audio-oracle-verification-report-all-tracks.json
```

## Manual Scans

```powershell
git ls-files
git status --ignored --short
```

Confirm that any local absolute paths in tracked notes are examples, sanitized
placeholders, or explicitly local-only context. Machine-readable public
manifests should prefer repo-relative paths or placeholder external checkout
roots.

## Release Language

Recommended public wording:

> EarthBound Decomp Scaffold is a ROM-wide, byte-equivalent reverse-engineering
> scaffold and documentation corpus for the US headerless ROM. It does not
> include a ROM or generated copyrighted assets. It is intended for romhacking,
> research, validation, and future porting work, but it is not yet a finished C
> port.
