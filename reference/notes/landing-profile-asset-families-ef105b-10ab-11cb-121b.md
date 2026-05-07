# Landing Profile Asset Families `EF:105B / 10AB / 11CB / 121B`

This note captures the current best layered model for the asset families selected in parallel by cached landing profile selector `$4372`.

See also [landing-profile-cache-436e-4474.md](notes/landing-profile-cache-436e-4474.md).
See also [landing-display-profile-overview.md](notes/landing-display-profile-overview.md).
See also [landing-profile-bundles-ef121b-43dc.md](notes/landing-profile-bundles-ef121b-43dc.md).
See also [transition-landing-mode-family-9f3f-9f41.md](notes/transition-landing-mode-family-9f3f-9f41.md).
See also [landing-display-assembly-cluster-c007b6-c4b26b.md](notes/landing-display-assembly-cluster-c007b6-c4b26b.md).
See also [landing-palette-interpolation-export-c4958e-c426ed.md](notes/landing-palette-interpolation-export-c4958e-c426ed.md).
See also [landing-hdma-dispatch-family-ef117b-c00d7e.md](notes/landing-hdma-dispatch-family-ef117b-c00d7e.md).

## Main result

The strongest current local read is that one landing profile does not choose just one asset blob.

Instead, the same profile id fans out into several parallel asset families:

- `EF:105B` = bulk compressed payload pointers
- `EF:10AB` = compressed word-oriented payload pointers
- `EF:117B` = raw overlay-map payload pointers
- `EF:11CB` = compressed graphics-page payload pointers
- `EF:121B` = animated VRAM upload script pointers over the `EF:11CB` graphics pages

So the cleanest current system-level wording is:

- `$4372` selects a landing display profile made of multiple coordinated asset layers

not just one decompressed blob or one timed upload script.

## Selector path

The shared selector path is local and strong:

- `C0:08CF` derives coarse landing-region class `$04`
- `C0:090E` indexes `EF:101B`
- the selected profile id is stored to `$4372`
- that same profile id is then used to resolve:
  - `EF:10AB`
  - `EF:105B`
  - later `EF:11CB`
  - later `EF:121B`

So these four tables really do belong to one profile family rather than being unrelated neighbors.

## `EF:105B` as bulk compressed VRAM source family

When the coarse landing-region class changes, `C0:097E+` resolves a pointer from `EF:105B` and decompresses it through `C41A9E` into `7F:0000`.

After that, the same path calls `C085B7`, which is a chunking VRAM-DMA helper.

Local call shape from `C0:09BE..09EA`:

- source = `7F:0000`
- VRAM destination = `0`
- transfer size = either `0x7000` or `0x4000`, depending on branch

The decompressor cross-check is unusually strong here too:

- profile-side `EF:105B` blobs commonly decompress to about `0x7000` bytes
- example sizes:
  - `DD:3294 -> 0x7001`
  - `DE:0000 -> 0x7001`
  - `DE:32C9 -> 0x7001`

So the safest current read is now a bit sharper:

- `EF:105B` = bulk landing-profile VRAM payload family
- best current asset-side fit: landing background CHR or other large static tile-graphics layer

I am still keeping the exact identity slightly open, but this clearly looks like the big static display/background tile-graphics side, not the small animated strip side.

## `EF:10AB` as compressed word-oriented payload family

Earlier in the same `C0:08CF` path, `C0:091A+` resolves a pointer from `EF:10AB` and decompresses it through `C41A9E` into `7F:8000`.

Immediately after that, `C0:0968` calls `C08ED2` with:

- source = `7F:8000`
- destination = `$0100`
- length = `0x0300`

`C08ED2` is a simple word-copy helper, not a graphics renderer.

The decompressed `EF:10AB` data also looks word-oriented rather than tile-graphic-oriented. Example first bytes:

- `D9:34E9`: `C4 0C C5 0C 33 0C 34 0C ...`
- `D9:68AB`: `A7 4C A6 0C 9E 0C 9F 0C ...`
- `DA:1342`: `D8 0D D8 0D D8 0D D8 0D ...`
- `DB:26C1`: `C0 0D C1 0D C0 0D C1 0D ...`

So the safest current read is now a bit sharper too:

- `EF:10AB` = landing-profile word-table / screen-template style payload family
- best current asset-side fit: compressed BG tilemap or closely related screen-entry map layer

I am still keeping the exact consumer-facing identity cautious, but the packed 16-bit entry shape now looks much healthier as tilemap-like data than as arbitrary word scratch.

## `EF:117B` as HDMA dispatch family

Claude's latest handoff materially improved this layer, and the core claim checks out locally.

A parallel loader at `C0:062A` resolves pointers from `EF:117B`, but unlike `EF:105B / 10AB / 11CB` it does not route through `C41A9E`. Instead, it performs a direct fixed-size copy into `7F:F800`.

The strongest current local read is now:

- `EF:117B` = landing-profile HDMA dispatch pointer family

Why this is healthier than the old overlay-map model:

- all 20 slots point into bank `D8`
- `C0:062A` copies exactly `0x03C0` words into `7F:F800`
- the only pinned local consumers of `7F:F800` are `C0:0D39` and `C0:0DB7` inside `C0:0D7E`
- `C0:0D7E` explicitly treats the fetched `7F:F800` word as an offset into bank `D8`, not as a direct display word

So the safest current interpretation is that `EF:117B` is part of a landing HDMA parameter-dispatch layer rather than a BG overlay tilemap layer.

See also [landing-hdma-dispatch-family-ef117b-c00d7e.md](notes/landing-hdma-dispatch-family-ef117b-c00d7e.md).

## `EF:11CB / EF:121B` as animated graphics-strip family

This layer is now the most tightly mapped one.

- `EF:11CB` holds compressed graphics-page payloads, decompressed into `7E:C000`
- `EF:121B` holds repeated 8-byte animated VRAM upload entries
- `C0:0172` ticks those entries and calls `C08616` in VRAM-DMA mode `A = 0`

The asset-side cross-check is strong:

- many `EF:11CB` blobs decompress to full `0x2000`-byte pages
- that is exactly one 256-tile 4bpp graphics page
- the `EF:121B` upload entries use tile-sized source offsets, transfer sizes, and VRAM destinations
- rendered blobs look like effect-oriented or environment-overlay strip graphics, not ordinary text or sprite sheets

So the safest current read is:

- `EF:11CB / EF:121B` = animated landing display / arrival-effect graphics-strip family

## Layered profile model

Putting the current evidence together, the best layered model is:

- `EF:105B`
  - large bulk landing-profile VRAM tile-graphics payload
- `EF:10AB`
  - word-oriented landing-profile screen or tilemap-style payload copied into WRAM work block
- `EF:117B`
  - landing HDMA dispatch payload copied into `7F:F800`
- `EF:11CB`
  - compressed landing-profile graphics pages
- `EF:121B`
  - animated VRAM upload scripts selecting timed strips from those graphics pages

That means the landing profile system now looks less like one special effect routine and more like a small coordinated arrival-display assembler.

## Confidence boundaries

### Locally proved

- the same profile id selected by `EF:101B` feeds `EF:105B`, `EF:10AB`, `EF:11CB`, and `EF:121B`
- `EF:105B` pointers are decompressed through `C41A9E` into `7F:0000`
- `C085B7` then performs chunked VRAM DMA from that `7F:0000` source
- `EF:10AB` pointers are decompressed through `C41A9E` into `7F:8000`
- `C08ED2` then performs a word copy from `7F:8000` into `$0100`
- `EF:11CB` pointers are decompressed through `C41A9E` into `7E:C000`
- `EF:121B` entries are expanded into runtime upload records and consumed by `C0:0172`
- `C0:0172` calls `C08616` in VRAM-DMA mode `A = 0`

### Locally strong but still interpretive

- `EF:105B` is best described as the bulk static display/background tile-graphics side of the landing profile
- `EF:10AB` is best described as a word-oriented screen/template layer, likely BG tilemap-like or closely related
- `EF:117B` is best described as a landing HDMA dispatch layer
- `EF:11CB / EF:121B` are best described as the animated arrival-effect graphics layer
- the whole family is best described as a coordinated landing display profile system

### Still open

- the exact in-game role of the large `EF:105B` VRAM payloads
- the exact semantic identity of the `EF:10AB -> $0100` word-oriented payloads
- the exact downstream HDMA consumer of the `EF:117B -> 7F:F800 -> D8 -> $E000` path
- how the separate WRAM-template sequencer at `C0:A1F2` interlocks with these asset layers
- the exact player-visible meaning of each profile id

## Best next target

The cleanest next move is to keep following the sharper display-side assembly path now that the main bridge is pinned:

- `0x0300` as the active 16-word row-selection cache
- the `C08C58` queue families fed by the `2EB6 / 2F6A / 301E / 30D2` timed control streams
- the later display-side readers of `B3F8 / B3FA`

That should tell us how the bulk VRAM layer, the word-oriented layer, the row-cache layer, the timed control-stream layer, and the animated strip layer combine into the final arrival display.
