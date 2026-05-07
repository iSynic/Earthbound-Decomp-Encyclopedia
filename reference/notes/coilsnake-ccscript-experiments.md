# CoilSnake CCScript Experiments

This note summarizes payload-free CCScript edit experiments.
Generated CCScript projects and rebuilt ROMs remain under ignored `build/coilsnake/`.

## Summary

- Experiments: `2`
- Experiment root: `build/coilsnake/edit-experiments`

| Experiment | Source | Comparison base | Changed bytes | Changed span | Evidence |
| --- | --- | --- | ---: | --- | --- |
| `ccscript-body-command-byte-probe` | `ccscript/data_07.ccs` | `build/coilsnake/scriptdump-rebuild.sfc` | `1` | `0x3896F6` (`F8:96F6`)..`0x3896F7` (`F8:96F7`) | `diff-confirmed` |
| `ccscript-rom-goto-label-probe` | `ccscript/main.ccs` | `build/coilsnake/scriptdump-rebuild.sfc` | `2` | `0x050001` (`C5:0001`)..`0x050003` (`C5:0003`) | `diff-confirmed` |

## Interpretation

- CCScript edit probes should compare against an unedited scriptdump rebuild when the scriptdump roundtrip itself is compiler-normalized.
- These probes can prove CCScript lowering behavior, but runtime text VM naming still needs local parser or handler evidence.
