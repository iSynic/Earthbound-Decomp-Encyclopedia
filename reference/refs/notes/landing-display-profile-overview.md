# Landing Display Profile Overview

This note is a top-level summary of the current best local model for the landing or arrival display subsystem.

See also [transition-landing-mode-family-9f3f-9f41.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/transition-landing-mode-family-9f3f-9f41.md).
See also [landing-destination-table-d57880.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-destination-table-d57880.md).
See also [landing-profile-cache-436e-4474.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-profile-cache-436e-4474.md).
See also [landing-profile-asset-families-ef105b-10ab-11cb-121b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md).
See also [landing-profile-bundles-ef121b-43dc.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-profile-bundles-ef121b-43dc.md).
See also [landing-display-assembly-cluster-c007b6-c4b26b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-display-assembly-cluster-c007b6-c4b26b.md).
See also [landing-palette-interpolation-export-c4958e-c426ed.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-palette-interpolation-export-c4958e-c426ed.md).
See also [landing-hdma-dispatch-family-ef117b-c00d7e.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-hdma-dispatch-family-ef117b-c00d7e.md).
See also [landing-display-control-words-2baa-2e7a.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-display-control-words-2baa-2e7a.md).

## Main result

The strongest current local read is that EarthBound's landing or arrival display is a coordinated profile system, not one small teleport effect helper.

The current safest layered picture is:

- a staged destination and mode family at `$9F3F / $9F41`
- a destination record table at `D5:7880`
- a cached landing-region or landing-profile selector block at `$436E / $4370 / $4372`
- multiple coordinated profile-selected asset families at `EF:105B / 10AB / 117B / 11CB / 121B`, including a separate HDMA-dispatch layer
- a WRAM template and row-cache assembly layer at `0x0240 / 0x0200 / 0x0300`, with the strongest pinned follow-up currently the secondary export path through `C4:9440`
- a separate pre-render DMA strip layer gated by `$2BAA` through `C0:A56E / C0:8643 / C0:8240`
- a record-driven stream-dispatch layer plus four renderer queue families, timed control streams, and BG or screen-base setup work
- a parallel palette interpolation and direct `CGRAM` upload path

So the cleanest current system-level wording is:

- this subsystem assembles and animates a profile-selected landing display, with destination-sensitive assets, template data, timed display-control streams, animated strip uploads, and palette transitions

## End-to-end flow

The current best end-to-end flow is:

1. `0x19 26 -> C2:30F3`
   - snapshots saved landing coordinates and companion byte `$98B8`
2. `C2:ABFB -> C0:DD53`
   - stages destination selector `$9F3F` and landing-mode selector `$9F41`
3. `C0:EA99`
   - runs the broader landing or arrival controller
4. `C0:DD79`
   - on the success-side branch, resolves a destination record from `D5:7880`
   - installs destination override words into `$438A / $438C`
   - invalidates cached landing selectors so the world-side profile logic rebuilds
5. `C0:08CF / 090E`
   - derive the coarse landing region and choose landing profile id `$4372`
6. `$4372` then selects coordinated asset families:
   - `EF:105B`
   - `EF:10AB`
   - `EF:117B`
   - `EF:11CB`
   - `EF:121B`
7. `C007B6 / C00480 / C00778`
   - build the active template, packed row table, and active row cache
8. `C4:B26B` plus `C4:B3D0 / C4:B4BE` plus `C0:AC43 / AC68+ / ACE6+ / AD26+`
   - initialize child-anchor state, dispatch among timed control streams, resolve per-record queue assignment word `$103E`, then feed one of four renderer queue families
9. `C08B8E+ / C08CD5`
   - drain those record-driven queues into PPU BG or screen-base setup, with resolved queue value `1` also participating in a separate `$280C` ordering-side path
10. `C4:958E / C4:26ED / C4:9740`
   - interpolate packed 15-bit colors
   - repack them into `7E:0200`
   - mirror them to `7F:0000`
   - then arm direct `CGRAM` upload selector `#$18`

## Destination side

The destination record family at `D5:7880` now has two strong local roles:

- text-side destination-name printing
- success-side landing override installation

The record layout is locally strong enough to say:

- `+0x00 .. +0x18` = padded destination name
- `+0x1B .. +0x1E` = coarse destination override coordinates

That makes the table safer to describe as a landing-destination table than only a town-name table.

## Profile-selected asset layers

The current best layered read is:

- `EF:105B`
  - bulk landing-profile VRAM tile-graphics payload family
- `EF:10AB`
  - compressed word-oriented screen or tilemap-style payload family copied into WRAM work area
- `EF:117B`
  - landing HDMA dispatch payload family copied into `7F:F800`
- `EF:11CB`
  - compressed graphics pages
- `EF:121B`
  - timed strip-upload scripts over those graphics pages

The subsystem therefore looks like a coordinated display profile, not a single blob plus one animation table.

## WRAM assembly and renderer-control side

The central display-side assembly cluster is now best read as:

- `0x0240`
  - active landing template block
- `0x0200`
  - packed row-table derived from that template
- `0x0300`
  - active 16-word row cache selected from the row-table
- `$2EB6 / 2F6A / 301E / 30D2` families
  - timed control-stream pointer families
- `$103E`
  - per-record render-queue assignment word feeding `$2400`, with indirect and one-shot behavior
- `C08C58`
  - queue builder for four renderer update families
- `C08CD5`
  - queue worker that performs BG or screen-base PPU setup

This is stronger than the older broad "display logic" wording because the row-cache layer, control-stream layer, and renderer queue layer now have distinct local roles.

## Palette side

The palette side is now one of the cleanest parts of the subsystem.

The strongest current local read is:

- `C4:958E`
  - builds six `7F:` component-work planes from packed 15-bit source colors
- `C4:26ED`
  - steps and saturates those planes and repacks them into `7E:0200`
- `C4:9740`
  - mirrors `7E:0200` to `7F:0000`
  - then arms `$0030 = #$18`
- `C0:81C8`
  - resolves selector `#$18` through `DATA_C08F98`
  - performs a direct `CGRAM` DMA of `0x0200` bytes from CPU address `$0200` to `CGRAM` address `0`

So the safest current wording is:

- this is a landing-profile palette interpolation, repack, and direct upload path

## What is well understood

The subsystem is now in good shape structurally.

Locally strong areas:

- staged destination and mode selection
- destination-table role and coordinate overrides
- profile selection through `$4372`
- coordinated profile asset layers
- WRAM template and row-cache assembly
- child-anchor updates, a record-driven stream-dispatch layer, timed control streams, four renderer queue families, and renderer-side PPU setup
- palette interpolation and direct `CGRAM` upload

## What is still open

The remaining gaps are mostly detail-level rather than structural:

- exact semantic identity of the `EF:10AB` word-oriented payloads
- exact semantic identity of the `EF:105B` bulk VRAM payloads
- exact downstream HDMA target and channel identity of the `EF:117B -> 7F:F800 -> D8 -> $E000` dispatch path
- exact queue-to-layer mapping on the renderer side
- exact meaning and later consumer of the special `$280C` ordering-side path used when resolved queue value `1` is singled out
- exact final consumer role of the live `0x0300` row cache beyond the current `C4:9440` export-side anchor
- exact semantic identity of the record/control bits that steer `C0:AC43`
- exact user-facing meaning of some row/template fields
- whether the `7F:0000` palette mirror has any meaningful later nonlocal consumer or is just a persistent backup copy

## Best next targets

If this subsystem gets revisited later, the cleanest follow-ups are:

- identify whether `7F:0000` has any meaningful later nonlocal landing-display consumer
- tighten the exact display-side identity of `EF:10AB`
- tighten the exact display-side identity of `EF:105B`
