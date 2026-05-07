# Source Prototype Policy

This policy defines the staged source artifacts used while moving from documentation to real source files.

## Prototype Levels

### `contract-sketch`

Purpose: capture the source module shape before byte-equivalent assembly exists.

Required:

- source file exists at the path named by the emission plan
- header declares `Prototype level: contract-sketch`
- every planned unit range is listed
- every planned callable label appears as a source label or explicit label marker
- external calls, WRAM fields, and table dependencies are listed
- bodies may be pseudocode or comments, but they must not pretend to be build-ready

Allowed:

- placeholder bodies such as `rtl`
- high-level pseudocode comments
- final local/struct field names still pending

### `annotated-asm`

Purpose: preserve original instruction flow in source form while retaining explanatory comments.

Required:

- all `contract-sketch` requirements
- original branch/entry labels represented
- file explicitly states that original instruction flow is preserved
- file no longer describes its bodies as pseudocode-only
- instruction flow matches the original routine structure closely enough to audit
- any intentional abstraction is called out near the affected block

Allowed:

- symbolic constants and labels
- comments that explain DP locals, width state, and external contracts

### `build-candidate`

Purpose: prepare for assembler integration and byte equivalence checks.

Required:

- all `annotated-asm` requirements
- assembler syntax chosen and documented
- dependencies/imports resolved or stubbed through a declared build harness
- byte-equivalence or relocation differences tracked by a dedicated checker

For C3, the chosen build-candidate conventions are documented in
[notes/c3-build-candidate-source-conventions.md](notes/c3-build-candidate-source-conventions.md).
`tools/validate_c3_source_signatures.py` checks source instruction alignment
against ROM decode, while `tools/validate_c3_build_candidate_ranges.py` checks
the recorded ROM byte range, size, SHA-1, label set, and signature-clean status.

## File Invariants

Every source prototype file must:

- link back to the emission plan or source contract notes
- state its prototype level
- list covered address ranges
- include every planned entry and internal callable label from the emission plan
- list external routines, WRAM fields, and ROM tables it depends on
- explicitly mark pseudocode-only bodies while the level is `contract-sketch`

## Current C3 Policy

For C3, [notes/c3-source-emission-plan.md](notes/c3-source-emission-plan.md) is the source of truth for planned modules and labels.

The first accepted level for a new C3 source file is `contract-sketch`. Promotion to `annotated-asm` should happen one module at a time after the validator can prove the file still matches the emission plan. Promotion to `build-candidate` additionally requires a clean source-signature report and a passing build-candidate range validation report.
