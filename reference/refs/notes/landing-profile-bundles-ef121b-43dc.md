# Landing Profile Bundles `EF:121B` and Runtime Block `$43DC..4474`

This note captures the current best local model for the small profile bundles selected by `$4372` and expanded into runtime block `$43DC..4474`.

See also [landing-profile-cache-436e-4474.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-profile-cache-436e-4474.md).
See also [transition-landing-mode-family-9f3f-9f41.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/transition-landing-mode-family-9f3f-9f41.md).
See also [landing-profile-asset-families-ef105b-10ab-11cb-121b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md).

## Main result

The strongest current local read is:

- `$4372` selects one record from pointer table `EF:121B`
- the same selector also chooses one companion payload blob from `EF:11CB`
- `C0:0085` first decompresses that `EF:11CB` blob into WRAM buffer `7E:C000` through `C41A9E`
- `C0:0085` then expands the selected `EF:121B` record into runtime entries at `$43DC..`
- `C0:0172` advances those runtime entries each tick
- each runtime step calls `C08616` in transfer mode `A = 0`
- in that mode, `C08616` is a VRAM-DMA helper

So the safest current wording is now stronger than before: these are landing-profile VRAM upload bundles over a decompressed WRAM payload, not generic transfer tables.

## Selector path

The local selector path is now fairly clear:

- `C0:08CF` rebuilds cached profile selector `$4372`
- `C0:0085` reads `$4372`
- `C0:0085` doubles it twice and indexes `EF:121B`
- the selected pointer becomes the active logic-bundle pointer in direct-page `$18/$1A`

So `EF:121B` is best read as the logic-bundle pointer table for the landing profile currently chosen by `$4372`.

## Companion payload table `EF:11CB`

`C0:0085` also resolves a second pointer from `EF:11CB` using the same selector.

That second pointer is passed to `C41A9E` with:

- source = selected `EF:11CB` long pointer
- destination = `7E:C000`

`C41A9E` is a generic compressed-data expander. Its local format handling includes:

- raw literal runs
- repeated-byte runs
- repeated-word runs
- incrementing runs
- backreference-style copy modes
- `#$FF` end marker

So the cleanest current layered model is:

- `EF:11CB` = compressed source-data blob pointers
- `EF:121B` = VRAM upload script pointers that operate over the decompressed blob in `7E:C000`

The first `EF:11CB` blobs also look asset-like rather than logic-like from raw bytes alone, which is consistent with that decompressor path.

### Asset-side tightening

The new decompressor pass makes the source side substantially clearer:

- the first `EF:11CB` blobs decompress to full `0x2000`-byte pages
- `0x2000` bytes is exactly one 256-tile 4bpp CHR page
- the `EF:121B` source offsets start on `0x20`-byte boundaries like `0x0020`, `0x01A0`, `0x0320`, `0x0520`, `0x08A0`
- the transfer sizes are also `0x20`-byte multiples like `0x0060`, `0x0080`, `0x00E0`, `0x0100`, `0x0140`, `0x0240`, `0x03E0`
- the VRAM destinations advance in matching tile-sized steps

So the strongest current asset-side read is no longer just "some decompressed payload." These look very much like decompressed 4bpp graphics pages, with the `EF:121B` bundle selecting tile-sized slices for timed VRAM upload.

### Visual inspection cross-check

The rendered pages strengthen the asset-side read further. Using the new local renderer on several decompressed blobs:

- profile `0` shows repeated slanted / swirling strip graphics
- profile `1` shows crescent-like and small sparkle-like shapes
- profile `5` shows a repeating zigzag strip family
- profile `6/7/8` show broader wave, cloud-like, or layered organic strip graphics

Even allowing for grayscale rendering and missing palette context, these do not read like ordinary menu glyphs, alphabet tiles, or generic actor sprite sheets. They read much more like effect-oriented or environment-overlay graphics assembled from animated strips.

So the safest current player-facing phrasing is now:

- landing display / arrival-effect graphics pages

rather than something narrow like text graphics or something broad like arbitrary VRAM assets.

### Destination-side clustering

The first destination-record crosswalk also supports the same broad read. Using the landing-destination records at `D5:7880` and the local `$438A/$438C -> D7:A800 -> EF:101B -> $4372` path:

- `Onett` derives profile `1`
- `Twoson` derives profile `2`
- `Threed` derives profile `3`
- `Saturn Valley` derives profile `6`
- `Fourside` derives profile `4`
- `Winters` derives profile `17`
- `Summers` derives profile `7`
- `Scaraba` derives profile `18`
- `Dalaam` derives profile `9`
- `Deep Darkness` and `Tenda Village` both derive profile `6`

That gives two useful constraints:

- the profile choice is clearly arrival-context dependent rather than town-name unique
- some named destinations share one animated graphics family, while at least one destination-linked profile (`9`) currently looks effectively empty or inert from the decompressed-asset side

So the best current read is that `$4372` selects a landing display family determined by the destination's coarse arrival region, not a one-profile-per-town table.

## Bundle format behind `EF:121B`

`C0:0085` gives a concrete local struct sketch.

The selected bundle starts with:

- byte `+0` = entry count

If this byte is zero, `C0:0085` aborts immediately.

After that, the bundle is interpreted as repeated 8-byte entries.

The first bundle at `EF:126B` decodes as:

- count `5`
- entry `0`: `04 0C 60 00 20 00 10 00`
- entry `1`: `04 0F 60 00 A0 01 40 00`
- entry `2`: `04 0F 80 00 20 03 70 00`
- entry `3`: `04 15 E0 00 20 05 B0 00`
- entry `4`: `04 15 00 01 A0 08 20 01`

The currently safest per-entry local struct is:

- byte `+0` = step-count limit
- byte `+1` = reload delay
- word `+2` = VRAM transfer size in bytes
- word `+4` = source-base offset inside decompressed WRAM payload `7E:C000`
- word `+6` = VRAM destination address

## Runtime expansion at `$43DC..`

`C0:0085` expands each 8-byte source entry into a 16-byte runtime record at `$43DC + 0x10 * index`.

The strongest current local mapping is:

- runtime `+0x00` = step-count limit
- runtime `+0x02` = reload delay
- runtime `+0x04` = VRAM transfer size
- runtime `+0x06` = source-base offset in `7E:C000`
- runtime `+0x08` = VRAM destination address
- runtime `+0x0A` = live countdown, seeded from runtime `+0x02`
- runtime `+0x0C` = live step counter, seeded to `0`
- runtime `+0x0E` = live current source offset, seeded from runtime `+0x06`

`$4472` receives the entry count, so the whole `$43DC..4474` block is one active upload-script instance.

## Runtime tick path `C0:0172`

`C0:0172` is the runtime consumer.

For each active runtime record it:

- decrements runtime `+0x0A`
- when that countdown hits zero, reloads it from runtime `+0x02`
- compares runtime `+0x0C` against runtime `+0x00`
- if equal, clears runtime `+0x0C` and restores runtime `+0x0E` from runtime `+0x06`
- calls `C08616` using:
  - `A = 0`
  - `X = runtime +0x04`
  - `Y = runtime +0x08`
  - source long pointer `7E:C000 + runtime +0x0E`
- increments runtime `+0x0C`
- advances runtime `+0x0E` by runtime `+0x00`

That is strong local evidence for a small looping VRAM upload program:

- count through a short set of source offsets
- wait a programmable delay between uploads
- reset to the base source offset after the step-count limit

## Profile-wide animation cross-check

The asset-side cross-check is now unusually strong.

For every nonempty profile checked so far, the decompressed blob's nonzero tile count matches the sum of:

- `(transfer size / 0x20)` tiles per upload strip
- multiplied by the entry step-count limit

Examples:

- profile `0`: `3*4 + 3*4 + 4*4 + 7*4 + 8*4 = 100` nonzero tiles
- profile `1`: `10*4 + 2*2 = 44` nonzero tiles
- profile `5`: `8*8 = 64` nonzero tiles
- profile `6`: `12*4 + 18*4 = 120` nonzero tiles
- profile `7`: `20*5 + 9*4 = 136` nonzero tiles
- profile `8`: `31*4 = 124` nonzero tiles

That is a very strong local fit for the following model:

- each `EF:121B` entry describes one animated graphics strip
- `word +2` is the strip size
- `byte +0` is the frame count for that strip
- the current source offset advances by one strip-sized slice per step
- after the frame count is exhausted, the source offset resets to the base slice

So the best current read is no longer just "timed VRAM upload script." It is a timed VRAM upload script for multi-strip animated graphics pages.

## Why `C08616` is now the key anchor

The strongest new clue is the exact `C08616` mode used here.

In the landing-profile path, `C0:0172` always calls `C08616` with `A = 0`.

For `A = 0`, `C08616` indexes the first entry of table `C0:8FB0`, which sets up:

- DMA control / B-bus target for VRAM data port `$2118`
- VRAM destination address through `$2116/$2117`
- transfer size through DMA count `$4315`
- source pointer through `$4312/$4314`

So in this path the parameters now read cleanly as:

- `X` = VRAM transfer size
- `Y` = VRAM destination address
- source long pointer = decompressed payload slice inside `7E:C000`

That means the runtime bundle is not just a timing table. It is a timed VRAM upload script over a decompressed landing-profile payload.

## Confidence boundaries

### Locally proved

- `$4372` selects `EF:121B`
- the same selector also selects `EF:11CB`
- `C0:0085` decompresses the selected `EF:11CB` blob into `7E:C000` through `C41A9E`
- `EF:121B` entries are pointers, not inline code leaves
- the selected bundle begins with a one-byte count
- the bundle then consists of repeated 8-byte entries
- `C0:0085` expands those entries into 16-byte runtime records at `$43DC..`
- `$4472` stores the runtime entry count
- `C0:0172` consumes those runtime records as a looping timed sequence
- `C0:0172` calls `C08616` with `A = 0`
- in mode `A = 0`, `C08616` performs VRAM DMA setup
- the source side of that call is `7E:C000 + runtime +0x0E`

### Locally strong but still slightly interpretive

- runtime `+0x00` is best read as a frame count or step-count limit for one animated strip
- the decompressed `EF:11CB` payloads are best described as graphics-oriented VRAM source assets rather than a broader scratch blob family
- they are very likely 4bpp tile pages or something very close to that
- the whole bundle family is best described as landing-profile animated VRAM upload scripts

### Still open

- the exact in-game identity of the uploaded graphics pages and which arrival/landing situations they correspond to
- whether any of the bundles also touch tilemap-like destinations, or stay purely in graphics space
- the exact human-facing meaning of each animated landing profile selected by `$4372`

## Best next target

The cleanest next move is to tighten the asset identity side:

- the decompressed contents at `7E:C000`
- the exact VRAM destination addresses used by each bundle entry
- the relationship between these uploads and the separate WRAM-template installer at `C0:A1F2`

That should decide whether the final name should explicitly mention a landing animation, a landing visual effect, or a broader landing display profile.
