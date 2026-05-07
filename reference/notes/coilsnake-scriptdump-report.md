# CoilSnake Scriptdump Report

This note records a payload-free summary of CoilSnake `scriptdump` output.
Generated CCScript files, text payloads, and rebuilt ROMs stay under ignored `build/coilsnake/`.

## Run

- Scriptdump project: `build/coilsnake/scriptdump-project`
- CCScript directory: `build/coilsnake/scriptdump-project/ccscript`
- Result: scriptdump succeeded and populated ccscript files in an ignored project copy.
- Compile roundtrip: scriptdump project compiled successfully against the expanded base ROM.

## Output Shape

| Source | Files | `.ccs` files | Data modules | Bytes | Text lines |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline `ccscript/` | 1 | 0 | 0 | 0 | 0 |
| Scriptdump `ccscript/` | 65 | 64 | 63 | 1601998 | 39287 |

Delta from the baseline project:

- added files: `64`
- removed files: `0`
- common files with changed size: `1`
- `main.ccs` present: `true`
- `summary.txt` present: `true`

## Roundtrip Diff

- Compared against: `build/coilsnake/baseline-rebuild.sfc`
- Rebuilt ROM: `build/coilsnake/scriptdump-rebuild.sfc`
- Status: `different`
- Changed bytes: `511398`
- Changed runs: `30055`
- First changed offset: `0x03FD8D` (`C3:FD8D`)
- Last changed offset exclusive: `0x38A10C` (`F8:A10C`)

Interpretation:

- `scriptdump` is usable as an authoring oracle because its generated project compiles.
- The compiled scriptdump project should be treated as compiler-normalized output unless the diff is byte-identical to `baseline-rebuild.sfc`.
- Any command-lowering claim still needs a tiny edited CCScript experiment; compare that edited rebuild against the unedited scriptdump rebuild to isolate the edit when this broad roundtrip is normalized.
