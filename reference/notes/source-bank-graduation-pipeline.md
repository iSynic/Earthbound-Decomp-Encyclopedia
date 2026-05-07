# Source Bank Graduation Pipeline

This note defines the reusable path for moving a documented source-bearing bank
from first-pass notes to checked-in, byte-equivalent assembler scaffolds. C3 is
the first completed multi-module pilot for this workflow; C4 now has the first
non-C3 pilot and has already proven the same path across mixed source plus a
preserved source-adjacent data gap. C5-C9 prove the same byte-equivalence
scaffold can also protect text/data banks when the source unit is an asset
corridor rather than executable source. CA proves the same route for an
asset/table bank.

## Gate 1: First-Pass Map

The bank first needs a durable note that separates ordinary code, data tables,
script/text bytecode, graphics/audio payloads, padding, and unknown regions. The
first-pass note should identify candidate source regions by bank address and
call out any mixed source/data ranges that need special treatment.

Output:

- `notes/bank-<bank>-first-pass.md`
- local source/data split notes where the bank is mixed

## Gate 2: Source Contracts

Each candidate source slice needs stable labels, entry/exit expectations,
important WRAM/ROM contracts, and external dependencies. This is the point where
working names become intentional source-facing names rather than loose notes.

Output:

- source contract notes for the slice or subsystem
- updated data-contract manifests when a routine consumes structured tables
- assembler-facing comments in the prototype source

## Gate 3: Build-Candidate Ranges

Closed source slices graduate into a machine-readable range manifest. Each range
records source path, ROM start/end, byte size, hashes or byte previews, and any
source-adjacent data gaps that must be preserved verbatim.

Output:

- `build/<bank>-build-candidate-ranges.json`
- `notes/<bank>-build-candidate-ranges.md`
- range/signature validation reports

For text banks with a generated `build/text-bank-<bank>.json`, use the text-bank
promoter instead of adding every range by hand:

```powershell
python tools\promote_text_bank_to_source_scaffold.py C5
```

This creates data-corridor stubs for each locale text segment and explicit
coverage gap, then writes the standard `build/<bank>-build-candidate-ranges.json`
manifest.

For asset banks with a generated `build/asset-bank-<bank>.json`, use the
asset-bank promoter:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py CA
```

This creates data-corridor stubs for binary assets, table includes, and explicit
coverage gaps, then writes the standard source-bank range manifest.

## Gate 4: Assembler Contract

The source must be shaped enough for an assembler translator:

- same-file labels and constants resolve
- external control-flow targets have named aliases
- branch/local labels remain address-anchored
- intentional data gaps are represented in the range manifest

Output:

- assembler-contract validation report
- `pilot-ready` status for every closed module

## Gate 5: Durable Scaffold

Generate a checked-in Asar scaffold from the build-candidate manifest:

```powershell
python tools\build_source_bank_scaffold.py --bank C3
```

For C3 this writes:

- `src/c3/bank_c3_helpers_asar.asm`

For the C4 pilot this writes:

- `src/c4/bank_c4_helpers_asar.asm`

For the text-bank pilots this writes:

- `src/c5/bank_c5_helpers_asar.asm`
- `src/c6/bank_c6_helpers_asar.asm`
- `src/c7/bank_c7_helpers_asar.asm`
- `src/c8/bank_c8_helpers_asar.asm`
- `src/c9/bank_c9_helpers_asar.asm`

For the first asset-bank pilot this writes:

- `src/ca/bank_ca_helpers_asar.asm`

Future banks should use the same command once they have a matching
`build/<bank>-build-candidate-ranges.json` manifest. Use `--ranges` and
`--output` when a bank needs a custom manifest or scaffold path.

## Gate 6: Byte-Equivalence

Validate the scaffold by patching a clean ROM copy and comparing every protected
range against the original ROM:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C3 --module all --combined --scaffold src\c3\bank_c3_helpers_asar.asm --strict
```

The same durable-scaffold validation shape now works for C4:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C4 --module all --combined --scaffold src\c4\bank_c4_helpers_asar.asm --strict
```

And for text-bank scaffolds:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C5 --module all --combined --scaffold src\c5\bank_c5_helpers_asar.asm --strict
```

The C3-specific wrapper remains available for compatibility:

```powershell
python tools\validate_c3_byte_equivalence.py --module all --combined --scaffold src\c3\bank_c3_helpers_asar.asm --strict
```

Output:

- `build/<bank>-byte-equivalence-validation.json`
- `notes/<bank>-byte-equivalence-validation.md`

## Graduation Definition

A source bank slice is considered scaffold-graduated when:

- the source range is closed and represented in the manifest
- source-adjacent data gaps are explicitly preserved
- the durable scaffold is checked in under `src/<bank>/`
- the generic byte-equivalence validator reports `OK`
- remaining exclusions are documented as data, asset, script, or VM work rather
  than hidden source debt

This is still short of a full linked decompilation. It proves a stronger,
repeatable invariant: documented source, assembler-shaped source text, preserved
data gaps, and original ROM bytes all agree under a checked-in build artifact.

## Readable Closure Follow-Up

After scaffold graduation, run the readable-source closure audit:

```powershell
python tools\build_readable_source_bank_closure.py
```

That report separates decoded 65816 assembly from preserved corridors and known
data/text/asset payloads. A bank can be scaffold-graduated while still failing
readable source-bank closure if a large source-bearing region is only emitted as
`db` bytes.
