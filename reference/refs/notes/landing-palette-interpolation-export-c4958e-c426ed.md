# Landing Palette Interpolation And Export `C4:958E / C4:26ED`

This note captures the current best local model for the color-work layer that sits beside the landing row-cache and timed control-stream families.

See also [landing-display-assembly-cluster-c007b6-c4b26b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-display-assembly-cluster-c007b6-c4b26b.md).
See also [landing-profile-asset-families-ef105b-10ab-11cb-121b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md).
See also [landing-display-profile-overview.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-display-profile-overview.md).

## Main result

The strongest current local read is that `C4:958E` and `C4:26ED` form a palette-style interpolation and export path over packed 15-bit color words.

The current safest layered model is:

- `C4:958E`
  - reads packed color words from source families rooted at `0x0200` or `4476`
  - splits them into the three 5-bit color components
  - builds six `7F:` work planes:
    - `7F:0200 / 0400 / 0600` = per-step component deltas
    - `7F:0800 / 0A00 / 0C00` = current component values
- `C4:26ED`
  - adds the deltas into the current values
  - saturates each component to the `0..31` range
  - repacks the three 5-bit channels into one 15-bit color word at `7E:0200`
- `C4:9740`
  - first mirrors that `7E:0200` export block out to `7F:0000` through `C08EED`
  - no convincing landing-local readers of that `7F:0000` mirror are currently pinned in banks `C0` or `C4`
- landing-local callers such as `C4:F20E`
  - arm `$0030 = #$18`, which the NMI-side handler at `C0:81C8` resolves through `DATA_C08F98` into a direct `CGRAM` DMA descriptor
  - for selector `#$18`, that descriptor uploads `size = 0x0200` from CPU address `$0200` to `CGRAM` address `0`

So the safest current wording is now stronger: this is a landing-display color interpolation and direct palette-upload preparation layer, not just a generic `7F:` scratch family.

## `C4:958E` as six-plane color-work builder

The legacy assembly cross-check resolves the noisy decode cleanly.

`C4:958E`:

- takes source-family base in `Y`
- initializes long work pointers rooted at:
  - `7F:0200`
  - `7F:0400`
  - `7F:0600`
  - later `7F:0800`
  - `7F:0A00`
  - `7F:0C00`
- iterates the source in `0x10`-word bands
- for each packed source word pair:
  - extracts low 5 bits
  - extracts middle 5 bits (`0x03E0 >> 5`)
  - extracts high 5 bits (`0x7C00` normalized through `C0915B`)
- uses `C4:91EE` to compute a per-step signed delta between paired component values
- stores those deltas to:
  - `7F:0200`
  - `7F:0400`
  - `7F:0600`
- also stores the base packed components from the current source row to:
  - `7F:0800`
  - `7F:0A00`
  - `7F:0C00`

The strongest current component alignment is therefore:

- `7F:0200 / 0800` = low-channel delta / current
- `7F:0400 / 0A00` = middle-channel delta / current
- `7F:0600 / 0C00` = high-channel delta / current

I am still keeping the human-facing channel names slightly cautious, but the packed `BBBBBGGGGGRRRRR` style layout makes `low / middle / high` line up naturally with red / green / blue order.

## `C4:91EE` as per-step component delta helper

`C4:91EE` is now locally bounded enough to describe safely.

It:

- takes two component values in `A` and `X`
- computes `target - source`
- shifts that difference into the fixed-point form expected by `C090E6`
- calls `C090E6` with `Y` as the step-count or divisor-like input

So the safest current read is:

- `C4:91EE` computes a signed fixed-point per-step component increment

That fits the later behavior in `C4:26ED` unusually well.

## `C0915B` as shared fixed-point divide helper

`C0915B` is already widely reused elsewhere, but here its local role is especially clear.

It is used by `C4:958E` before the high-channel delta calculation, and it is also used by `C0:0391 / C0:0480` when the landing template sums are normalized.

So the safest current read is:

- `C0915B` is a shared fixed-point divide or normalize helper used by this landing color-work layer

I am still keeping the exact internal arithmetic wording cautious, because the local role is clearer than the exact implementation detail.

## `C4:26ED` as saturating component stepper and repacker

`C4:26ED` reads the six `7F:` planes in three pairs:

- `7F:0200 + 7F:0800`
- `7F:0400 + 7F:0A00`
- `7F:0600 + 7F:0C00`

For each pair it:

- adds delta into current value
- writes the updated current value back into the `current` plane
- saturates negative values to `0`
- saturates positive overflow to `0x1F00`
- clears the delta plane when the channel reaches a bound

It then repacks the three saturated channels into a single color word and stores that word into `7E:0200 + X`.

That makes the strongest current read:

- `C4:26ED` steps one frame of color interpolation and exports the repacked 15-bit result block

The final `SEP #$20 ; LDA #$18 ; STA $0030` now has a concrete local meaning too. The NMI-side handler at `C0:81C8` reads `$0030`, resolves it through `DATA_C08F98`, and uses that descriptor to program `DMA[$00].SourceLo`, `REGISTER_CGRAMAddress`, and `DMA[$00].SizeLo`. For selector `#$18`, the descriptor is `size 0x0200 / source $0200 / CGRAM address 0`, so this export pass is directly scheduling a full `CGRAM` upload from the WRAM-low mirror of the freshly repacked `7E:0200` block.

## Parallel `7F:7900..7E00` family

The adjacent `C4:92D2` family strongly supports the same interpretation.

It builds and later advances another six-plane set at:

- `7F:7900`
- `7F:7A00`
- `7F:7B00`
- `7F:7C00`
- `7F:7D00`
- `7F:7E00`

`C4:9303..9387` then adds those component planes back into `7F:7C00/7D00/7E00`, repacks them into color words, and writes the results into the `0x0240` work family.

So the safest current cross-check is:

- the landing subsystem contains at least two closely related color interpolation families
- the `7F:0200..0C00` family is not an isolated oddity; it matches a broader palette-style work pattern

## Confidence boundaries

### Locally proved

- `C4:958E` writes six `7F:` work planes rooted at `7F:0200..0C00`
- `C4:26ED` reads those six planes in three pairs, updates them, and repacks results into `7E:0200`
- `C4:9740` copies the resulting `7E:0200` block out through `C08EED`
- `C4:91EE` computes a per-step signed delta from paired component values and calls `C090E6`
- `C0915B` is part of the same normalization path used on the high component here and on the landing template sums in `C0:0391 / 0480`

### Locally strong but still interpretive

- `7F:0200 / 0400 / 0600` are best read as low/mid/high component delta planes
- `7F:0800 / 0A00 / 0C00` are best read as low/mid/high current component planes
- the packed output words at `7E:0200` are best read as 15-bit color words
- the whole family is best described as a landing palette interpolation, repack, and upload-preparation layer

### Still open

- whether the intermediate `7F:0000` mirror is only a persistent backup copy or feeds a later nonlocal consumer outside the currently pinned landing-local path
- the exact relationship between this color-work layer and the larger `EF:105B / EF:10AB` asset layers
- the exact human-facing color or palette role of the parallel `7F:7900..7E00` family

## Best next target

The cleanest next move from here is narrower now:

- identify whether the `7F:0000` mirror has any later nonlocal consumer that matters for landing display
- or accept it as a persistent backup copy while keeping the direct `7E:0200 -> CGRAM` upload path as the only locally proved visible consumer
