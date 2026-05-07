# Yoshifanatic1 C0-C4 Handoff Format

This proposes a contributor-friendly packet for sharing our C0-C4 findings with
Yoshifanatic1 or anyone else continuing work in an EarthBound disassembly repo.
The goal is not to hand over our entire notes directory. The useful shape is a
small, reviewable bundle with provenance, confidence, and machine-readable
imports.

## Recommended packet

### 1. Short README

File: `C0-C4-handoff-README.md`

Keep this to one or two pages:

- scope: banks `C0`-`C4`, US ROM address notation, local working-name status
- caveat: names are descriptive working labels, not canonical upstream symbols
- artifact list and intended use
- how to regenerate the files from our repo
- a short map of the highest-value systems: overworld runtime, text/windows,
  battle engine, battle visuals, inventory/equipment, landing/coffee/tea, and
  file-select/town-map displays

### 2. Review table

File: `working-names-c0-c4.tsv`

Use the generated file:

```text
build/labels/working-names-c0-c1-c2-c3-c4.tsv
```

This is probably the most useful first artifact for another maintainer because
it is diffable and can be filtered by address, bank, tag, confidence, or note
evidence.

Columns:

- `address`
- `bank`
- `name`
- `confidence`
- `tags`
- `evidence`

### 3. Importable labels

Files:

```text
build/labels/working-names-c0-c1-c2-c3-c4.ca65.inc
build/labels/working-names-c0-c1-c2-c3-c4.asar.inc
build/labels/working-names-c0-c1-c2-c3-c4.sym
```

These should be presented as optional helper artifacts, not as a request to
bulk-accept every symbol. They let someone load the labels into a debugger or
prototype source branch, then accept/rename/reject entries gradually.

Recommended review strategy:

1. Import the `.sym` into a debugger or analysis view.
2. Review the TSV by subsystem tag rather than by raw address order.
3. Promote only the names whose local evidence is compelling.
4. Rename stylistically as needed for the target repository.

### 4. Contract manifest

Files:

```text
build/data-contracts-c0-c4.json
notes/data-contracts-c0-c4.md
```

This is where our work is more useful than plain labels. It captures fixed
WRAM roots, overlays, and ROM tables in a way that can drive table inspectors,
source comments, or future decompilation structs.

Suggested fields to preserve:

- `id`
- `domain`
- `address`
- `stride`
- `count`
- `struct`
- `confidence`
- `evidence`
- `fields[].name`
- `fields[].offset`
- `fields[].size`
- `fields[].count`
- `fields[].note`

### 5. Subsystem index

File: `C0-C4-subsystem-index.md`

This should be a curated document, not a dump. Start from
`notes/c0-c4-integration-pass.md` and include:

- system name
- banks involved
- important entry points
- relevant fixed contracts
- best evidence note
- unresolved naming or semantic questions

Example row:

| System | Banks | Entry points | Contracts | Caveat |
| --- | --- | --- | --- | --- |
| Window-mask HDMA | `C4`, called from `C0` | `C4:7501`, `C4:76A5`, `C4:7705`, `C4:7930` | `WH_WINDOW_SPAN_RADIUS_RAMP_TABLE` | exact player-facing effect names still need callsite naming |

### 6. Evidence snippets

File: `C0-C4-evidence-snippets.md`

Only include the strongest proof cases. This avoids burying the maintainer in
hundreds of local notes.

Good snippets:

- direct caller summaries
- table byte layouts
- record stride/count proofs
- before/after name conflict resolutions
- exact caveats when a label is useful but not final

## Suggested directory layout

```text
c0-c4-handoff/
  README.md
  working-names-c0-c4.tsv
  working-names-c0-c4.ca65.inc
  working-names-c0-c4.asar.inc
  working-names-c0-c4.sym
  data-contracts-c0-c4.json
  data-contracts-c0-c4.md
  C0-C4-subsystem-index.md
  C0-C4-evidence-snippets.md
```

## What to avoid

- Do not ask them to accept `1399` names as one giant patch.
- Do not present `proposed` names as canonical.
- Do not flatten the evidence chain; keep note path and line provenance.
- Do not ship only Markdown. The TSV, JSON, and symbol files are what make the
  work easy to test in their local tools.

## Highest-value first batch

If we wanted to send only a first slice, use the more contract-heavy systems:

1. WRAM roots and battle structs: `GAME_STATE`, `PARTY_CHARACTERS`,
   `BATTLERS_TABLE`, `BATTLE_SELECTION_SNAPSHOT`
2. fixed D5 battle/item data: `ITEM_CONFIGURATION_TABLE`,
   `BATTLE_ACTION_TABLE`, `PSI_ABILITY_TABLE`, `ENEMY_CONFIGURATION_TABLE`
3. C3/C4 visual tables: battle visual tables, window-mask radius ramp,
   movement-octant pulse tables, Your Sanctuary coordinate table
4. one subsystem note each for text/window, battle, overworld movement, and C4
   visual helpers

That would give them the highest confidence material first, while still making
the larger C0-C4 working-name set available for optional exploration.

