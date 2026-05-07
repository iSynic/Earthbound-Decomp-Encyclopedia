# Phase 4 Asset/Data Closeout

Status: phase-good-enough, with bounded deferred edges.

This note records the current asset/data milestone boundary. The goal of this
phase was not to finish every future decoder or engine bundle, but to make sure
asset/data banks are byte-accounted, classified, contract-backed where the
runtime evidence is strong, and honest about the payload families that remain
format-boundary work.

## Current Snapshot

Primary dashboard: `notes/asset-data-contract-frontier.md`.

- manifests: `38`
- represented assets/tables/gaps: `2219`
- represented source bytes: `2490368`
- output recipes: `6175`
- coverage gap bytes still represented as raw gaps: `75549`
- manifest-inferred payload metadata units: `5`
- contract-covered inferred payload metadata units: `5`
- unresolved missing payload metadata units: `0`

The five inferred E0/E1 payload metadata units are no longer live unknowns for
this phase. They are preserved as manifest provenance because the original yml
metadata was incomplete, but their roles are now covered by checked-in
contracts:

- `asset.e0.compressed_sram`: `notes/sram-template-contracts.md`
- `asset.e1.unknown_e1ae7c`: `notes/title-screen-palette-animation-contracts.md`
- `asset.e1.unknown_e1d6e1`: `notes/landing-cast-visual-contracts.md`

## Phase-Good-Enough Families

| Family | Banks | Phase 4 status | Remaining work type |
| --- | --- | --- | --- |
| Battle visual assets | `CA..CE` | Contract-seeded | Optional alias polish, Evil Eye sprite-id-110 edge, optional swirl internals. |
| Overworld sprites | `D1..D5` | Contract-backed | Contributor-facing alias and unowned-payload explanations only. |
| Map tilesets/runtime tables | `D6..DF` | Contract-backed | Collision low-bit labels and DA palette metadata behavior are bounded runtime-semantics polish. |
| UI, fonts, and town-map assets | `E0..E1` | Contract-seeded | Palette-row names and town-map renderer flag names are bounded semantic polish. |
| EF debug/late-tail data | `EF` | Seed contract | Further split belongs to EF source/runtime semantics, not broad asset discovery. |

## Deliberately Deferred

- `CF`/`D0` mixed asset/table banks: byte-accounted and scaffolded, but their
  variable-list subrecords need caller/runtime context before row-level source
  definitions should pretend to be final.
- `E2..EE` audio packs: raw-pack manifests are enough for this phase. Splitting
  BRR/sample/sequence/pointer contracts should happen as a focused audio phase.
- Engine-ready bundle emission: manifests and contracts are now good inputs for
  a future installer/extractor, but this milestone does not choose the final
  native engine asset schema.

## Closeout Rule

Phase 4 is good enough when the dashboard reports:

- `0` unresolved missing payload metadata units
- no asset/data family with unexplained ownership for known source-heavy banks
- map, UI/font/town-map, battle visual, and overworld sprite families have
  checked-in runtime or structural contracts
- remaining gaps are explicitly raw padding, raw audio packs, table-subrecord
  semantics, or runtime semantic polish

By that rule, Phase 4 can stop being the main blocking lane. Future work should
pull from the deferred list only when it directly supports editing, validation,
port-bundle design, or runtime semantics.
