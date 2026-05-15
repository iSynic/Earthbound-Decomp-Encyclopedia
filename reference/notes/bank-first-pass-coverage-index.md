# Bank First-Pass Coverage Index

## Main result

The configured bank first-pass sweep now has a wrapper note for every bank from
`C0` through `EF`: `48 / 48` first-pass notes.

This does not mean every byte is source-ready. It means every configured bank
now has a documented first-pass classification, artifact list, confidence
boundary, and recommended follow-up direction.

## Coverage set

- `C0..C4`: code-heavy engine/runtime banks with deep local audits, working-name
  manifests, and C0-C4 data-contract integration.
- `C5..C9`: text-heavy banks with first-pass text data maps.
- `CA..CF`: mixed asset/data banks with generated asset/data maps.
- `D0..D5`: transition from asset/table banks into overworld sprites and D5
  gameplay/battle table data.
- `D6..E1`: mixed data/asset/table banks with first-pass maps.
- `E2..EE`: primarily audio-pack banks, with EE ending in a large zero/unclaimed
  tail.
- `EF`: final configured mixed code/data/text/debug/save/map bank.

## Wrapper notes

- `notes/bank-c0-first-pass.md`
- `notes/bank-c1-first-pass.md`
- `notes/bank-c2-first-pass.md`
- `notes/bank-c3-first-pass.md`
- `notes/bank-c4-first-pass.md`
- `notes/bank-c5-first-pass.md` through `notes/bank-cf-first-pass.md`
- `notes/bank-d0-first-pass.md` through `notes/bank-df-first-pass.md`
- `notes/bank-e0-first-pass.md` through `notes/bank-ef-first-pass.md`

## Remaining work classes

The remaining work is no longer "which banks have no first pass?" It is now:

- promote stable working names into source labels.
- split table/text/script/data regions where first-pass notes intentionally keep
  broad spans.
- recover or derive missing generated source includes from the reference tree.
- turn data contracts into source-ready structs and table definitions.
- separate script/bytecode assets from ordinary 65816 routines before any port
  or engine-reimplementation work.

## Best next move

The highest-value next pass has moved beyond first-pass triage. Use this note as
the historical coverage index, then switch to the semantic package for live work:

- `notes/source-readiness-triage.md`: generated implementation queue.
- `notes/semantic-notes-package.md`: documentation ownership and naming policy.
- `notes/phase-2-semantic-status.md`: current subsystem semantic status.
