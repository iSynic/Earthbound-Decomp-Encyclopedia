# Landing HDMA Dispatch Family `EF:117B` / `C0:062A` / `C0:0D7E`

This note captures the current best local model for the `EF:117B` landing-profile asset layer and its consumer path through `$7F:F800`.

See also [landing-profile-asset-families-ef105b-10ab-11cb-121b.md](notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md), [landing-display-profile-overview.md](notes/landing-display-profile-overview.md), and [landing-display-assembly-cluster-c007b6-c4b26b.md](notes/landing-display-assembly-cluster-c007b6-c4b26b.md).

## Main result

The older `EF:117B = raw overlay-map layer` model is no longer the safest local read.

The strongest current local model is:

- `EF:117B` = landing-profile HDMA dispatch pointer table
- `C0:062A` = fixed-size raw loader into `$7F:F800`
- `$7F:F800` = landing HDMA dispatch buffer
- `C0:0D7E` and its inner loops = landing-side HDMA parameter assembler over bank `D8`

So the safest current wording is that this layer is part of a landing HDMA assembly path, not a BG overlay tilemap path.

## `EF:117B`

`EF:117B` is a 20-entry pointer table in the same 4-byte family shape as the other `EF:` profile tables.

Locally verified structure:

- record layout = `[lo16, bank, 0x00]`
- all 20 records point into bank `D8`
- example entries:
  - slot `0` -> `D8:8F50`
  - slot `1` -> `D8:95D0`
  - slot `19` -> `D8:EC2E`

That already fits the handoff's broad picture unusually well: one per-profile pointer table into a dedicated `D8` data family.

## `C0:062A`

`C0:062A` is a direct raw loader, not a decompressor.

Locally proved behavior:

- selects one `EF:117B` entry by `profile * 4`
- resolves the source pointer into DP `$0A/$0C`
- sets destination to `$7F:F800`
- copies exactly `0x03C0` words by direct long read/write loop

So the safest current role for `C0:062A` is:

- load one landing HDMA dispatch block into `$7F:F800`

## `$7F:F800` consumers

Only two direct local consumers of `$7F:F800` are currently pinned:

- `C0:0D39`
- `C0:0DB7`

Both are inside the broader helper rooted at `C0:0D7E`.

That is the strongest single reason the old overlay-map model fell apart: the buffer does not currently behave like a directly rendered row/tilemap layer anywhere locally. It behaves like an indexed dispatch table.

## `C0:0D7E`

`C0:0D7E` now has a locally strong HDMA-assembly shape.

What is locally proved:

- packed input `A` is split into several small selector fields
- one field chooses a base in the `$F000` region
- another chooses an output base in the `$E000` region
- the low two bits become a small sub-offset used when reading later records
- inner loops read keys from the selected `$F000` region
- those keys index `$7F:F800`
- the fetched `$7F:F800` value is then used as an offset into bank `D8`
- the code explicitly stages `bank = $00D8`
- the selected `D8` record contents are copied into the chosen `$E000` output region

The critical local proof is the middle bridge:

- `LDA $7F:F800,X`
- `STA $12`
- `LDA #$00D8`
- use `$12 + suboffset` as a `D8` long-pointer offset

That means the `$7F:F800` words are functioning as `D8` record offsets, not display entries.

## Best current interpretation

The safest current local interpretation is:

- `EF:117B` selects one per-profile dispatch table
- that table is copied to `$7F:F800`
- later landing-side code uses `$7F:F800` to map compact animation/state keys to record offsets in bank `D8`
- those `D8` records are then assembled into a WRAM output block in the `$E000` region

This is strongly consistent with an HDMA parameter-dispatch system.

## Confidence boundaries

### Locally proved

- `EF:117B` is a 20-entry pointer table
- every `EF:117B` slot points into bank `D8`
- `C0:062A` copies one selected source block directly into `$7F:F800`
- the copy length is fixed at `0x03C0` words
- the only pinned local consumers of `$7F:F800` are `C0:0D39` and `C0:0DB7`
- both consumers are inside `C0:0D7E`
- `C0:0D7E` uses `$7F:F800` entries as offsets into bank `D8`, not as direct display words

### Locally strong but still interpretive

- the `D8` record family is best read as landing HDMA parameter records
- the `$F000` region is best read as a landing animation or dispatch-key array family
- the `$E000` region is best read as an HDMA output buffer family

### Still open

- the exact SNES HDMA channel or PPU target eventually fed by the `$E000` output block
- the exact semantic meaning of the `$F000` key arrays
- the exact structure of the `D8` records beyond their role as offset-indexed parameter blocks
- the relation between this HDMA side and the neighboring queue-driven BG/screen-base renderer setup

## Best next target

The cleanest next move, if this landing seam gets revisited, is now downstream of `C0:0D7E`:

- trace the later consumer of the `$E000` output region
- or decode `C0:86DE` / the nearby post-assembly helpers strongly enough to identify the actual HDMA channel and PPU register target

## Working Names

- `C0:062A` = `Load_LandingHdmaDispatchBlock`
- `C0:0D7E` = `Assemble_LandingHdmaParameterBlock`
