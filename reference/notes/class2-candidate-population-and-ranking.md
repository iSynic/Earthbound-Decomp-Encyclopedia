# Class2 Candidate Population And Ranking

This note captures the current ROM-first model for how the class-`2` family populates the 32-entry candidate pool and later derives ranked outputs.

See also `notes/class2-candidate-table-9fac.md`.
See also `notes/class2-005e-record-domain.md`.

## Working Names

- `C2:4958` = `PopulateCandidatePoolFromSixSources`
- `C2:4A80` = `PopulateCandidatePoolFromVariableSources`

## The `49xx` / `4Axx` region looks like candidate-pool setup

The strongest current reading is that the routines around `C2:4922` and `C2:4A00` are dedicated setup passes for the candidate pool, not late consumers.

Why that fits:

- they write candidate-side metadata bytes such as `9FBA`, `9FBB`, `9FBC`, `9FBF`, `9FBD`, `9FC5`, and `9FC3`
- they run before the later selection logic that only reads those fields
- they iterate over small bounded source lists rather than the full 32-bit working set

## Population pass A: six-source setup around `C2:4958`

Current best reading:

- this pass iterates six source entries
- for each entry it reads a source byte from the `986F` family
- values below `4` go through one helper path
- values `4` and `5` go through a richer setup path
- on that richer path it resolves a linked slot through `C0:8FF7` with selector `#$005F`
- it writes candidate metadata fields including `9FBA`, `9FBB`, `9FBC`, and `9FBF`
- it also clears `9FC5` and `9FC3` for the candidate

The important point is that several of the candidate-domain fields are clearly seeded here, not produced by the later mask helpers.

## Population pass B: variable-count setup around `C2:4A80`

Current best reading:

- this pass iterates a bounded source list whose count is compared against `9F8A`
- it reads source values from the `986F` family again
- value `5` uses a special path rooted at `D5:8F23`
- it resolves candidate-linked slots through `C0:8FF7` with selector `#$005F`
- it writes candidate-side fields including `9FBC`, `9FBF`, `9FBD`, `9FC5`, `9FC3`, `9FBA`, and `9FBB`

This looks like a second-stage enrichment or alternative source path for the same runtime candidate pool.

Source follow-up (2026-05-06): the `C2:4A8A` variable-source path now names the
presentation and selection joins that sit around this enrichment pass. After the
six source rows are considered it refreshes selected-row presentation through
`C1:DD3B`, ticks one frame through `C1:2DD5`, keeps the battle-background frame
lane moving through `C2:DB3F`, and hands the current battle-group index to
`C1:E1A5` / `RunEnemySelectMode` when the enemy-select input branch is taken.
The final present/result setup then opens the battle text window through
`C1:DD47`.

## What this sharpens about the candidate fields

These setup passes make a few earlier field guesses much stronger:

- `9FBA` is not just an incidental status byte; it is explicitly seeded during setup and later re-tested during selection
- `9FBB` is also seeded during setup, which fits a candidate-local state or mode byte better than a derived counter
- `9FBC` is setup-time metadata that later partitions candidates into subfamilies during ranking
- `9FBF` is explicitly written during setup, supporting the interpretation that it marks candidates claimed, armed, or otherwise selected into the live pool

## The `F920+` region is a later ranking/output pass

The routines around `C2:F920`, `C2:F980`, and `C2:FA30` look different from setup.

Current best reading:

- they rescan the full 32-entry candidate pool
- they keep the familiar eligibility gates on `9FB8`, `9FC9`, `9FBA`, and `9FBC`
- they compare candidate-local ranking values such as `9FF0`
- they emit condensed results into working tables `AD7A`, `AD5A`, `AD62`, and the sibling `AD82`, `AD6A`, `AD72` family

That means the `ADxx` tables are not the candidate pool itself. They are ranked or condensed outputs derived from the pool.

## Current best reading of the ranking outputs

The safest current interpretation is:

- `AD7A` / `AD82` store selected candidate indices
- `AD5A` / `AD6A` store a coarse transformed ranking value derived by shifting the candidate-local score
- `AD62` / `AD72` store a complementary transformed value derived from a linked candidate-side byte near `9FAE`

The exact gameplay meaning of those output tables is still open, but they now look much more like ranked selections than raw world-state.

## C4 bridge into `battler.current_target`

`C4:A228` is the direct bridge from these ranked `ADxx` outputs back into a battler row.

Inputs:

- `A` = battler row base pointer
- `X` = battler/candidate index, normally computed as `(rowBase - 9FAC) / 0x4E`

The helper first scans `AD7A[0..AD56)`. If the incoming `X` matches an entry, it stores `entryIndex + 1` into `row + 0x0A`. If no match is found, it scans `AD82[0..AD58)` and stores `AD56 + entryIndex + 1` into `row + 0x0A` on a match. If neither ranked list contains the candidate index, it leaves the row untouched.

The two direct callers are:

- `C2:459D`, in a battler-row path that otherwise stores the unranked `(rowBase - 9FAC) / 0x4E + 1` directly into `row + 0x0A`
- `C2:58BB`, after `$A970` has been selected as the active battler row

The WRAM crosswalk identifies `9FAC + 0x0A` as `battler.current_target`, so the local name should stay mechanical: this routine maps a battler index through the ranked `AD7A/AD82` target lists and stores the resulting one-based target ordinal into the battler row.

## Current safest model

Putting the setup and ranking passes together:

- the candidate domain is a live WRAM pool of up to 32 linked entries
- `49xx` / `4Axx` setup passes seed candidate metadata into `9FBA..9FC5`
- the upstream `9F8C` ids feeding those setup passes map into a `D5:9589`-rooted record family with stride `0x005E`
- the mask helper family in `notes/class2-mask-helper-family.md` performs set algebra over that seeded pool
- the `F920+` ranking passes rescan the seeded pool and export condensed winners into `ADxx` working tables
- `C4:A228` maps those ranked `ADxx` outputs back into `battler.current_target`

## Working Names

- `C4:A228` = `StoreRankedBattlerTargetOrdinal`

This is enough to say the family has three distinct layers:

- candidate population
- mask-based filtering
- ranked export

## Source-family note

See `notes/class2-source-families-986f-9f8a.md`, `notes/class2-9f8c-upstream-verification.md`, and `notes/class2-005e-record-domain.md` for the upstream-source writeup and verification pass. The strongest current local claim is now that `C0:D323` builds `9F8A` / `9F8C`, bank `C2` consumes `9F8C` as an upstream structured source list, and the `#$005E` mapping lands in a `D5:9589`-rooted record family.

## Best next target

- Decode the high-value fields in the `D5:9589` record family reached after mapping `9F8C` entries through selector `#$005E`, so the population and ranking layers can be named from concrete gameplay data instead of just control flow.
