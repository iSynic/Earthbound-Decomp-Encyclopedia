# EB-M2 Listing Integration Plan

The EB-M2 Listing v1 archive is a major reference input for the project. It
appears to be a large address-annotated US/JP source listing with established
labels, include paths, macros, and emitted bytes for banks `C0` through `EF`.

The repository should integrate this listing as a source-label and
module-boundary authority where applicable, while preserving its existing role
as:

> a validated integration, documentation, and tooling layer that cross-checks
> ROM bytes, EB-M2 source listings, EBSRC/CoilSnake resource semantics, and
> romhacker/porter-facing notes.

## Integration Principles

- Treat EB-M2 Listing as a major reference oracle, not as uncredited source to
  copy wholesale.
- Record the reported Unlicense/public-domain dedication in reference notes and
  third-party notices before importing listing-derived source structure.
- Keep `refs/EB-M2-Listing-v1/` ignored by default because the archive is large,
  even though listing-derived metadata may be committed.
- Prefer crosswalks, evidence links, and derived metadata over bulk imported
  listing text.
- Preserve our byte-equivalence validators as independent checks.
- Promote names only when the address match is exact and the semantic role is
  compatible with our surrounding notes.
- Mark conflicts explicitly instead of silently overwriting our older working
  names.
- Separate three grades of confidence:
  - `exact-listing-match`: same address/range and compatible code/data role.
  - `listing-name-adopted`: name promoted from EB-M2 Listing into our docs.
  - `needs-review`: listing and local scaffold disagree, or role is ambiguous.

## Phase 1: Reference Index

Goal: make the listing searchable and measurable without committing the listing
itself.

Tasks:

- Keep `refs/EB-M2-Listing-v1/` as the local ignored source.
- Maintain `notes/reference-eb-m2-listing-v1.md` with archive hashes, shape, and
  cautions.
- Extend `tools/lookup_eb_m2_listing.py` only as needed for targeted lookup.
- Build a generated manifest of listing modules:
  - region
  - bank
  - address
  - include/module path
  - symbol labels
  - byte-bearing line count
  - first/last address

Outputs:

- `manifests/eb-m2-listing-index.json`
- `notes/eb-m2-listing-index.md`

Good enough:

- every US `bank00` through `bank2F` file is indexed;
- at least top-level include boundaries and public labels are extractable by
  address;
- the index contains no ROM-derived binary payloads.

## Phase 2: Name Crosswalk

Goal: compare EB-M2 Listing labels against our current source scaffold labels.

Tasks:

- Extract our current labels from `src/**/bank_*_helpers_asar.asm`.
- Extract EB-M2 labels from US listing files.
- Join by canonical address.
- Classify:
  - exact same name
  - EB-M2 has stronger name
  - our name is more descriptive but should cite EB-M2
  - conflicting names
  - local-only label
  - listing-only label

Outputs:

- `manifests/eb-m2-name-crosswalk.json`
- `notes/eb-m2-name-crosswalk.md`
- `manifests/symbol-aliases.json`
- `manifests/eb-m2-needs-review-triage.json`
- `notes/eb-m2-needs-review-triage.md`

Good enough:

- `C0`, `C1`, `C2`, `C3`, `C4`, and `EF` reviewed first;
- no automatic source renames until the report is reviewed;
- public docs stop implying that all routine names are original discoveries.

## Phase 3: Module Boundary Crosswalk

Goal: use listing include paths to improve our source organization and explain
where our generated modules differ.

Tasks:

- Parse `>>> path.asm` boundaries from the listing.
- Map listing module spans to our source module spans.
- Identify modules that are:
  - aligned
  - split differently
  - merged in our scaffold
  - data/binary include in the listing
  - absent from our semantic notes

Outputs:

- `manifests/eb-m2-module-crosswalk.json`
- `notes/eb-m2-module-crosswalk.md`

Good enough:

- high-value source-heavy banks have module boundary reports;
- our README can accurately explain why the repo uses generated range modules
  while EB-M2 Listing uses more traditional source includes.

## Phase 4: Semantic Reconciliation

Goal: merge the best of both worlds: EB-M2's established labels and our local
runtime/asset/script/audio contracts.

Tasks:

- Update notes where EB-M2 names make our working names obsolete.
- Add "also known as" aliases where community terminology differs.
- Prefer EBSRC/CoilSnake terminology for resource/project formats.
- Prefer EB-M2 Listing terminology for source labels and module names.
- Prefer our validators/manifests for byte coverage and reproducibility claims.

Outputs:

- revised subsystem notes;
- updated `notes/project-status.md`;
- updated README status wording;
- optional `manifests/symbol-aliases.json`.

Good enough:

- public-facing docs clearly distinguish:
  - byte-equivalent scaffold coverage;
  - EB-M2 corroborated source naming;
  - EBSRC/CoilSnake resource semantics;
  - our own still-provisional research.

## Phase 5: Buildability Roadmap Reset

Goal: use EB-M2 Listing to make the rebuild milestone less speculative.

Tasks:

- Compare EB-M2 include layout against our Asar scaffolds.
- Decide whether future buildability should:
  - adapt our scaffold into a top-level assembler pipeline;
  - generate source from a user-provided ROM plus EB-M2-derived metadata;
  - or document a bridge to an existing EB-M2/EBSRC build flow.
- Identify licensing/provenance constraints before importing any source text.
- Keep ROM-derived game assets and generated outputs outside tracked source even
  when listing source text is license-compatible.

Outputs:

- `notes/rebuild-roadmap-after-eb-m2-listing.md`

Good enough:

- the project has an honest answer for "why use this repo if EB-M2 Listing
  exists?";
- the next build milestone has a concrete toolchain direction.

## Immediate Next Steps

1. Review the generated whole-repo reports:
   `notes/eb-m2-promote-ready.md`, `notes/eb-m2-keep-local.md`, and
   `notes/eb-m2-needs-review.md`. Use
   `notes/eb-m2-needs-review-triage.md` as the active conflict queue.
2. Use `notes/eb-m2-module-crosswalk.md` to decide future source file
   organization; do not reorganize files in the same batch as name promotion.
3. Keep README/project status wording aligned with the generated crosswalk
   reports after each promoted bank/subsystem batch.

## First Implemented Wave

- `tools/build_eb_m2_name_crosswalk.py` emits the v2 name schema with
  confidence, role compatibility, review status, recommended action, old/new
  symbols, and conflict reasons.
- `tools/build_eb_m2_module_crosswalk.py` emits the module-boundary crosswalk
  before any physical source reorganization.
- `tools/lookup_eb_m2_symbol.py` resolves addresses, EB-M2 symbols, old local
  symbols, and `UNKNOWN_*` aliases through the crosswalk.
- `tools/promote_eb_m2_source_symbols.py` performs reviewed source-symbol
  promotion while preserving old address-prefixed names as aliases/equates.
- `tools/build_eb_m2_needs_review_triage.py` groups the remaining conflicts
  into boundary, script, table, and true role-review buckets without changing
  source.
- `tools/inspect_eb_m2_boundary_review.py` emits previous/current local range
  evidence for boundary cases before any alias/start-label fix is applied.
- Every currently ready exact-address, non-`UNKNOWN_*`, role-compatible EB-M2
  name is promoted into source and each affected bank validates byte-equivalent
  with `0` mismatches.
- The first conflict-resolution batch handled `CA`/`CC`/`CE` terminal-boundary
  data labels, preserved old end labels as aliases, and validated each affected
  bank with `0` mismatches.

## What Remains Useful

- Independent ROM hash/header validation.
- Bank-wide byte-equivalence reports across `C0` through `EF`.
- Machine-readable asset/audio/script/text/data manifests.
- Audio playback/export backend work.
- EBSRC/CoilSnake crosswalk tooling.
- Encyclopedia-facing organization and public explanation.
- A place to combine source labels, resource semantics, runtime consumers, and
  validation evidence in one coherent project.
