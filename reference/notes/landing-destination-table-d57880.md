# Landing Destination Table `D5:7880`

This note captures the current best local model for the destination-table family rooted at `D5:7880`.

See also [transition-landing-mode-family-9f3f-9f41.md](notes/transition-landing-mode-family-9f3f-9f41.md).
See also [jeff-repair-item-name-bridge.md](notes/jeff-repair-item-name-bridge.md).
See also [landing-profile-cache-436e-4474.md](notes/landing-profile-cache-436e-4474.md).

## Main result

`D5:7880` is no longer just "the town-name table" in the abstract.

The strongest current local read is that it is a fixed-stride landing-destination table whose records contain at least:

- a padded destination name string
- two destination-specific coarse world-coordinate words

That matters because the table now has two independent local consumers with different roles:

- `0x1C 06 -> C1:46DE` prints the destination name field
- `C0:DD79` reads the same record family and installs destination-specific coordinate override words into `$438A / $438C`

So the safest current system-level wording is:

- `D5:7880` is a landing-destination record table
- likely the same broad table family used for teleport-style named destinations

## Record layout

The record stride is strongly supported as `0x1F` bytes.

Local evidence:

- `C1:46DE` reaches the table through `C08FF7` with selector `#$001F`
- `C0:DD79` reaches the same table through `C08FF7` with selector `#$001F`
- `C0:DD79` then reads words at record offsets `+0x1B` and `+0x1D`

The first records dump cleanly as:

- record `0`
  - all zeroes
- record `1`
  - name `Onett`
  - `word +0x1B = 0x00FD`
  - `word +0x1D = 0x00BA`
- record `2`
  - name `Twoson`
  - `word +0x1B = 0x00B0`
  - `word +0x1D = 0x0334`
- record `3`
  - name `Threed`
  - `word +0x1B = 0x02B4`
  - `word +0x1D = 0x0466`
- record `4`
  - name `Saturn Valley`
  - `word +0x1B = 0x0022`
  - `word +0x1D = 0x03CC`
- record `5`
  - name `Fourside`
  - `word +0x1B = 0x017C`
  - `word +0x1D = 0x01F9`
- record `6`
  - name `Winters`
  - `word +0x1B = 0x003E`
  - `word +0x1D = 0x0121`
- record `7`
  - name `Summers`
  - `word +0x1B = 0x022A`
  - `word +0x1D = 0x0161`
- record `8`
  - name `Scaraba`

So the current best partial struct sketch is:

- `+0x00 .. +0x18`
  - padded destination-name string (`0x19` bytes)
- `+0x19 .. +0x1A`
  - unresolved small per-destination fields
- `+0x1B .. +0x1C`
  - destination coarse coordinate A
- `+0x1D .. +0x1E`
  - destination coarse coordinate B

## Local name-printing consumer

The print-side consumer is already in decent shape.

`0x1C 06 -> C1:46DE`:

- resolves a record index through `C08FF7`
- lands on `D5:7880`
- prints the first `0x19` bytes of the selected record

That is why the current local text dump gives clean records like:

- `Onett`
- `Twoson`
- `Threed`
- `Saturn Valley`
- `Fourside`
- `Winters`
- `Summers`
- `Scaraba`

So the string half of the record is on strong local ground.

## Local landing-side consumer

The more important recent gain is the landing-side consumer.

`C0:DD79`:

- reads destination selector `$9F3F`
- resolves a `D5:7880` record through `C08FF7`
- loads record words `+0x1B` and `+0x1D`
- installs them into `$438A / $438C`
- invalidates cached world-side selectors `$436E / $4370` and `$5DD4`
- then passes the scaled destination coordinates into `C019B2`

Those words are then not just left as passive cache.

Other local readers treat `$438A / $438C` as optional destination-coordinate override words:

- `C0:3A94` uses them instead of live `$9877 / $987B` when they are nonzero
- `C0:08CF` also consumes them and routes through broader table-driven world-side logic
- if both are zero, those readers fall back to live current coordinates instead

So the safest current local wording is:

- record offsets `+0x1B / +0x1D` are destination-specific coordinate override words
- `C0:DD79` uses them on the success-side branch of the landing controller
- and those words are important enough that the routine forces a fresh world-side landing-region/profile rebuild from the selected destination

## Why these now look like coarse tile-space coordinates

The scaling behavior is now the most useful local clue.

### `C0:3A94`

When `$438A / $438C` are nonzero, `C0:3A94` does:

- `$438A << 3`
- `$438C << 3`

before handing the result into `C00AA1`.

That is a strong fit for tile-to-pixel conversion rather than raw pixel storage.

### `C0:08CF`

The broader world-side helper at `C0:08CF` does the opposite kind of normalization:

- `$438A >> 5`
- `$438C >> 4`

before combining the results into a coarse table index.

That is exactly the sort of sector lookup you would expect if the stored values are already tile-space or coarse world-space coordinates.

So the safest current wording is:

- `+0x1B / +0x1D` are probably coarse tile-space world coordinates
- later code scales or groups them depending on whether it needs pixel-space placement or sector-style indexing

I am still keeping that one step short of "fully proved raw tile coordinates," but the local evidence now strongly favors that interpretation over raw pixel words.

## Why "landing destination table" is safer than "teleport destination table"

The names in the table line up very neatly with teleport destinations, and the community docs do point that way.

But the local ROM evidence is slightly broader:

- the table is used by a text printer for destination names
- the same records also feed the landing-controller success side
- the broader staged family around `$9F3F / $9F41` is used by what looks like a general landing / arrival pipeline, not just a one-off text command

So the safest current wording is:

- likely teleport-destination family
- definitely landing-destination record table

That keeps the note honest while still acknowledging the strong reference alignment.

## Confidence boundaries

### Locally proved

- `D5:7880` is reached through `C08FF7` with stride `0x1F`
- the first `0x19` bytes of each live record are padded destination-name strings
- `C1:46DE` prints that string field
- `C0:DD79` reads record words `+0x1B` and `+0x1D`
- those words are installed into `$438A / $438C`
- `$438A / $438C` are later treated as optional destination-coordinate override words
- `C0:3A94` scales those words upward by `<< 3`
- `C0:08CF` groups them through a coarser `>> 5` / `>> 4` normalization path
- `C0:DD79` also invalidates `$436E / $4370 / $5DD4`, which is strong local evidence that the selected destination record feeds a fresh landing-region or landing-profile recomputation rather than only a display label lookup

### Reference-backed and locally consistent

- the stronger semantic name "teleport destination table"
- the higher-level interpretation that this table is shared by teleport-style menu naming and landing-side world placement

### Still open

- the exact meaning of record bytes `+0x19 / +0x1A`
- whether `+0x1B / +0x1D` should be promoted all the way from "coarse tile-space coordinates" to a stricter exact field name
- whether all landing modes around `$9F41` use this same table family or only the named-destination success branch

## Best next target

The cleanest next move is to stay on the success-side branch around `C0:DD79` and tighten how the selected destination record interacts with the larger success finalizer `C0:E897`.

That should decide whether the table is only used by the named-destination branch or whether it leaks farther into the general landing-success path.


