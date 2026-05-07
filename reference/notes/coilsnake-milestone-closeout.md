# CoilSnake Milestone Closeout

This closes the current CoilSnake oracle milestone as a contract-building pass.
The tracked outputs remain payload-free; ROMs, rebuilt ROMs, copied CoilSnake
projects, script dumps, PNGs, and experiment reports stay under ignored
`build/coilsnake/`.

## Completed

- Baseline CoilSnake decompile and rebuild were established from the verified
  US headerless ROM.
- Field-to-runtime joins promoted the initial fixed-byte YAML probes and Phase
  2A/2B table probes where local ranges or routines supported them.
- Scriptdump and CCScript probes were captured as authoring/lowering evidence,
  not native runtime truth.
- Phase 2C format probes classified WindowGraphics, battle backgrounds, fonts,
  town-map metadata, battle sprites, and tilesets by observed rebuild behavior.
- The Phase 2C promotion assessment reduced broad "candidate" status to two
  contract promotions: `bg-data-distortion1-probe` and
  `windowgraphics-windows1-copy-probe`.

## What We Learned

- CoilSnake is strongest at proving editor-field lowering, fixed-size resource
  handling, and compiler/repack constraints.
- Original-ROM runtime knowledge still has to come from this repo's bank
  scaffolds, caller notes, source labels, and range manifests.
- Some CoilSnake rebuild bytes are real oracle evidence but not direct retail
  address evidence. The font-width and town-map icon probes are the clearest
  examples: their rebuilt bytes landed in original ranges owned by other local
  contracts, so they need a rebuilt-to-original layout map before promotion.
- Broad image/tile replacements are useful for tool constraints, but they are
  poor candidates for field naming because compression and repacking touch many
  unrelated spans.

## Remaining Work

- Promote only the CoilSnake facts that already have original-ROM/runtime
  support into local contracts.
- Build rebuilt-to-original layout maps for deferred families before treating
  their CoilSnake rebuild addresses as retail table fields.
- Continue bank-by-bank semantic polish, using CoilSnake vocabulary as a hint
  only after local bytes and callers support the name.
- Add new CoilSnake experiments only when they answer a specific runtime or
  tool-contract question that the current reports do not already answer.
