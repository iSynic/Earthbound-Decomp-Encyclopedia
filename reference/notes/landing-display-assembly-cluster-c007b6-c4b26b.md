# Landing Display Assembly Cluster `C007B6 / C00480 / C00778 / C4:B26B`

This note captures the current best local model for the display-side consumer cluster that sits immediately after landing-profile selection and bulk asset installation.

See also [landing-profile-asset-families-ef105b-10ab-11cb-121b.md](notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md).
See also [landing-profile-cache-436e-4474.md](notes/landing-profile-cache-436e-4474.md).
See also [landing-display-profile-overview.md](notes/landing-display-profile-overview.md).
See also [landing-palette-interpolation-export-c4958e-c426ed.md](notes/landing-palette-interpolation-export-c4958e-c426ed.md).
See also [landing-display-control-words-2baa-2e7a.md](notes/landing-display-control-words-2baa-2e7a.md).

## Main result

The strongest current local read is that these routines are the assembly-side bridge between the selected landing profile assets and the final arrival display state.

The current layered picture is:

- `C007B6`
  - installs the active landing-profile template block into WRAM work area `0x0240`, with flag-gated variant selection
- `C0391`
  - scans the `0x0240` template and derives three component sums plus per-component counts into `$43D0..43DA`
- `C00480`
  - turns the active `0x0240` template into a `0x0100`-entry packed row table at `0x0200`
- `C00778`
  - uses the template-controlled selector words at `0x0240 + 0x40` to cache one 16-word row from `0x0200` into `0x0300`
- `C4:9440 / C4:958E` family
  - mirrors and repacks the `0x0240 / 0x0300 / 4476` display-side tables into larger `7F:` work blocks for a secondary consumer path
- `C4:B26B`
  - initializes `0x1E` slots of timed control-stream state for the same display system
- `C0:AC68+ / ACE6+ / AD26+`
  - tick those control streams and emit per-slot values through `C08C58` into active renderer update queues
- `C08B8E+`
  - drains those queues through common worker `C08CD5`, which performs renderer-side PPU BG and screen-base setup
- the adjacent `$0030 -> C0:81C8 -> DATA_C08F98` path
  - separately handles landing-local `CGRAM` DMA selectors such as `#$18`, which uploads `0x0200` bytes from CPU address `$0200` to `CGRAM` address `0`
  - the nearby `C4:9740` helper also mirrors that same `7E:0200` block to `7F:0000`, but no landing-local reader of that mirror is currently pinned
- `C0:023F / 030F`
  - build and advance a separate landing-profile sequencer over `$445C/$445E/$4460/$4474`

So the safest current wording is that this cluster assembles and drives the runtime landing-display work tables after the profile's bulk assets and animated graphics layers are already in place, then feeds a renderer-side queue system that programs PPU display state.

## `C007B6` as template-block installer

`C007B6` begins by selecting a pointer from table `EF:10FB` using the caller's profile argument.

Normal path:

- resolves a `0x00C0`-word block through `C08FF7`
- copies that block into WRAM work area `0x0240` via `C08ED2`
- inspects the first word of the loaded block
- uses `C21628` to test its low `15` bits as a flag id
- compares the flag result against the sign/high-bit state of that first word
- if the condition matches, switches to an alternate pointer at record offset `+0x20`
- then reloads the same `0x00C0`-word block into `0x0240`

Alternate `B4EF` path:

- decompresses a blob rooted at `E1:374A`
- selects a `0x00C0`-word slice through `B4F1` and table `E1:2F8A`
- copies that slice into `0x0240`

So the safest current read is:

- `C007B6` installs the active landing-profile template block into WRAM work area `0x0240`
- that block can be switched by flag-gated or mode-gated variant logic

## `C0391` as template-sum helper

`C0391` is a small but important setup-side helper over the active `0x0240` template.

It scans `0x60` words from the template, treats each nonzero word as three packed component fields, and accumulates:

- low 5-bit component sum into `$43D0`
- middle 5-bit component sum into `$43D2`
- high 5-bit component sum into `$43D4`
- nonzero-entry count into `$43D6/$43D8/$43DA`

Those sums and counts are then consumed immediately by `C00480`.

So the safest current read is:

- `C0391` derives template component totals and counts for the later row-table builder

## `C00480` as packed row-table builder over `0x0240`

`C00480` starts by calling `C0391` on `0x0240`, then combines the three profile base pairs:

- `$43D0 / $43D6`
- `$43D2 / $43D8`
- `$43D4 / $43DA`

through repeated `C0915B` calls.

It then loops over `0x0100` output entries and writes words into WRAM table `0x0200`.

Inside that loop it:

- reads a packed template-derived word
- splits it into three 5-bit component fields
- conditionally remaps those fields through `C09032`
- adjusts one component through helper `C0434`, which behaves like a wrap or nearest-neighbor adjuster over a 6-step ring
- repacks the result into a single word
- stores that packed word to `0x0200`

The packed output word is therefore best read as a three-component row-entry descriptor, not just an arbitrary scratch value.

So the strongest safe read is:

- `C00480` builds a `0x0100`-entry packed row table at `0x0200` from the selected `0x0240` template and landing-profile base values

I am still keeping the exact player-facing meaning of the three packed components open.

## `C00778` as row-selector cache builder

`C00778` uses the same `0x0240` template family but a narrow selector subsection:

- reads `16` words from `0x0240 + 0x40`
- for each nonzero selector, shifts it by `5` and adds `0x0200`
- copies `16` words from that selected source block into `0x0300`

That means each selector chooses one 16-word row block from `0x0200`.

So the safest current read is:

- `0x0200` is arranged as row-sized blocks of `16` packed entries
- `C00778` builds `0x0300` as a 16-word active row-selection cache from those `0x0200` blocks

This is stronger than the older generic ?companion lookup table? wording.

## `C4:9440 / C4:958E` as secondary export and repack path

A second caller family now gives the `0x0240 / 0x0300` side a cleaner boundary than before.

`C4:9440`:

- copies a caller-selected `0x00C0`-word block into `0x0240`
- copies a fixed `00:C300` `0x0100`-word block into `0x0300`
- reruns `C00480` and `C00778`
- arms selector `#$18` through `C0856B` and waits on `$0030` before returning

That means the row-table and row-cache builders are reusable outside the immediate `C0:09FA..0A12` landing path, but the strongest currently pinned structured follow-up is still this secondary export or repack path rather than a late direct landing-local reader of the live `0x0300` cache.

The follow-up helpers `C4:96E7 / 96F0 / 96F9 / 9740 / 978E` then route through `C4:958E`, which uses source families rooted at `0x0200` or `4476` and writes several `7F:` work blocks including:

- `7F:0200`
- `7F:0400`
- `7F:0600`
- `7F:0800`
- `7F:0A00`
- `7F:0C00`

Even with some decoder rough edges now resolved by the local assembly cross-check, the safest current read is:

- `C4:9440 / 958E` are a secondary export or repack path for the display-side row and sequence tables
- within that family, `C4:958E / C4:26ED` now have a stronger local identity as a six-plane color interpolation and export layer over packed 15-bit words
- landing-local callers like `C4:F20E` then arm `$0030 = #$18`, and the NMI-side handler resolves that through `DATA_C08F98` into a direct `CGRAM` upload descriptor (`size 0x0200 / source $0200 / CGRAM address 0`)
- they are locally adjacent to the same landing-display work data, but are not the same thing as the timed queue or PPU-setup path

See also [landing-palette-interpolation-export-c4958e-c426ed.md](notes/landing-palette-interpolation-export-c4958e-c426ed.md).

## `C0:023F / 030F` as separate sequencer builder

The direct landing-only caller at `C0:0A12` is now better bounded too.

`C0:023F` does not read `0x0300`. Instead it:

- selects a record through `DF:E4E1` using `$02A0`
- decompresses a profile-selected payload into `7E:B800`
- clears and fills `$4460`
- seeds `$445C`, `$445E`, and `$4474`

Then `C0:030F` advances that sequencer and calls `C0:A1F2` with the current step id.

So the safest current read is:

- the `$445C/$445E/$4460/$4474` layer is a separate landing-profile sequencer
- it is adjacent to the row-cache layer, but not a direct consumer of `0x0300`

## `C4:B26B` as timed control-stream initializer

`C4:B26B` is called immediately before the landing-profile animated-strip setup at `C0:0A0B`.

Its strongest current local roles are:

- reads small descriptor records rooted at `C4:0E32`
- delegates tile/graphics transfer work to `C4:B1B8`
- updates running placement/bounds words at `B3F8/B3FA`
- initializes `0x1E` slots of four parallel control-stream pointer families:
  - `$2EB6`
  - `$2F6A`
  - `$301E`
  - `$30D2`
- seeds those families from fixed script roots:
  - `C4:0EE4`
  - `C4:0EB0`
  - `C4:0EF0`
  - `C4:0F04`
- uses the same geometry-family tables already seen elsewhere (`C42A1F / C42A41`) when adjusting `B3F8/B3FA`

So the safest current read is:

- `C4:B26B` initializes the timed control-stream side and the live placement anchor side of the landing display

### `C4:B1B8` landing-display asset transfer helper

`C4:B1B8` is the small transfer worker used by `C4:B26B` while walking the `C4:0E32` descriptor records.

Inputs:

- `A` = current destination offset, initialized by `C4:B26B` to `0x5600`
- `X` = asset/profile index read from the descriptor record
- `Y` = subpiece selector byte read from descriptor record offsets `+2` or `+3`

If `Y == 0x00FF`, the helper returns the incoming destination offset unchanged. Otherwise it:

1. selects a four-byte pointer from the table at `EF:133F` using `X`
2. reads a size-like byte at selected record offset `+1` and doubles it
3. reads a bank/source selector byte at offset `+8`
4. uses `Y` to choose a source pointer from the selected record's subpiece list at `+9 + Y * 2`
5. transfers two adjacent chunks through `C0:8616`: one to destination `A`, one to destination `A + 0x0100`
6. returns the advanced destination offset used by the caller for the next subpiece

The two direct callers are the paired calls inside `C4:B26B`: first with descriptor byte `+2`, then with byte `+3`. This makes `C4:B1B8` the landing-display graphics/subpiece transfer helper that packs variable selected assets into the VRAM destination sequence before the control-stream and child-anchor setup continues.

Source polish: `src/c4/landing_display_asset_stream_helpers.asm` now names
the `EF:133F` subpiece pointer table, `C4:0E32` stream descriptor table,
no-subpiece sentinel, subpiece length/source-bank/list offsets, `0x5600`
VRAM cursor, paired `+0x100` plane transfer, and stream pointer families
`$2EB6/$2F6A/$301E/$30D2`.

The placement side is tighter than before now that the nearby child-entity subsystem is better mapped. Local readers and writers around `C4:B37D..B48F` show that `$B3F8/$B3FA` are not just abstract bounds words. They are the live anchor coordinates later fed into `C4:B3D0`, which in turn calls `C01E49` through the already-mapped child-entity spawn family. In this landing path, `C4:B3D0` seeds `$B3F8/$B3FA` from the active record's `0B8E/0BCA` pair, applies placement-adjusted signed offsets from the compact `C4:0DE8` child-definition table, and then spawns the child object.

The byte-clean source scaffold now promotes this corridor through `C4:B587`.
`C4:B329` adjusts the live child anchor using the entity footprint geometry
tables at `C4:2A1F/2A41`, `C4:B3D0` spawns the attached child and mirrors the
parent `$103E/$2BAA` control words into the child slot, and `C4:B4BE` scans the
`0x1E` active slots for matching parent-tagged `$103E` words before clearing the
matching child slot through `C02140`. The wrapper band at `C4:B4FE..B587`
resolves parent slots by registry type, visual type, or pose descriptor before
calling the common spawn/clear helpers.

So the current safest refinement is:

- `$B3F8/$B3FA` are the live landing-display child-anchor coordinates
- `C4:B26B` and the nearby `C4:B37D..B48F` helpers update that anchor
- `C4:B3D0 / C4:B4BE` are the spawn and clear side of attached landing-display child objects, not a separate unrelated visual system

## `C0:AC43 / AC68+ / ACE6+ / AD26+` as producer-side stream dispatcher and tickers

The later bank-`00` consumers make the `C4:B26B` arrays much clearer.

`C0:AC43` is the important front end. It is not just a thin wrapper around the stream tickers. It reads control bits from the active record family's `$2BAA`, examines additional live state such as `$2A7E` and `$2E7A`, and then decides which timed stream family to run before enqueuing a renderer record through `C08C58`.

They pair each pointer family with a countdown mirror and a current-value mirror:

- `$2EB6 -> $2EF2 -> $2F2E`
- `$2F6A -> $2FA6 -> $2FE2`
- `$301E -> $305A -> $3096`
- `$30D2 -> $310E -> $314A`

The front-end selection logic is also useful now. The current safest local read is:

- `$2BAA bit 0` chooses a small `+0` versus `+5` bias added to emitted stream values before they are enqueued
- `$2BAA bits 2-3` choose whether the first active stream group is skipped, or whether `C0:AC43` enters the `301E/3096` versus `30D2/314A` side directly
- when `$2A7E == #$0040`, `C0:AC68` prefers the `301E/3096` family
- otherwise it prefers the `30D2/314A` family
- later in the same pass, sign and bit-`14` tests on `$2E7A` decide whether the `2F6A/2FE2` and `2EB6/2F2E` families are also emitted

The earlier `$2BAA`-gated setup side is now cleaner too. In `C0:A508..A56D` and `C0:A7C8..A82E`, those same bits do not choose queue families directly. They gate one or two extra passes through `C0:A56E`, and `C0:A56E` now looks like a DMA strip or descriptor generator over the local `$0094/$0092/$0097` geometry words. Its worker `C0:8643` either appends 8-byte DMA descriptor records into the live `$0400` queue family or, when `$0D` is negative, performs an immediate DMA-style path through `$431x` and `$2115/$2116`. The nonnegative `$0400` path is now locally pinned too: `C0:8240` consumes those records as standard DMA descriptors, so this setup-side layer is distinct from the later `C08C58` renderer-update queues. The source split is also healthier now: the extra setup-side passes seed a fixed bank-`C4` source at `$0BE8`, while the later main pass uses `$341A & #$FFFE` plus record bank byte `$2A42`. So the setup-side meaning is stronger than before: `$2BAA` is not just a later dispatch hint, it also controls how much extra pre-render DMA strip generation occurs before the main object path continues, with those extra passes looking more like auxiliary or common strip uploads wrapped around the record's main DMA path.

That is a better fit for a small render-phase or record-driven stream dispatcher than for a one-to-one hardwired BG number switch. The four queue families may still end up mapping cleanly onto BG-layer buckets, but the local producer-side evidence now says the record/control-word layer is richer than a simple `BG1/BG2/BG3/BG4` selector.

The helper `C0:AD56` interprets the pointer streams as tiny control scripts:

- command `1`
  - copy the next word into the current-value mirror and continue parsing
- command `3`
  - jump to another script pointer and continue parsing
- any other word
  - treat that word as a delay count and return the advanced script pointer plus that count

The callers then:

- cache the returned advanced pointer back into the relevant pointer family
- store the returned delay count into the countdown mirror
- decrement the countdown once per tick
- read the current value from the current-value mirror
- hand that value to `C08C58`

So the safest current read is:

- `$2EB6/$2F6A/$301E/$30D2` are not plain pointer arrays
- they are four timed per-slot control-stream families driving display update values over time

## `C08C58` as renderer update enqueuer

`C08C58` dispatches on `$2400` and appends the emitted values into four parallel renderer update-queue families. Each family has four field arrays plus a running write head:

- family `0`
  - fields at `$2404/$2444/$2484/$24C4`
  - write head at `$2504`
- family `1`
  - fields at `$2506/$2546/$2586/$25C6`
  - write head at `$2606`
- family `2`
  - fields at `$2608/$2648/$2688/$26C8`
  - write head at `$2708`
- family `3`
  - fields at `$270A/$274A/$278A/$27CA`
  - write head at `$280A`

Each append writes four columns of values:

- emitted value from the control stream
- caller-supplied base or offset value
- caller-supplied index-like value
- current bank or context byte from `$000B`

The producer side is tighter now too. Local callers like `C0:A10C` and `C0:A409/C0:A41D` write `$2400` from per-record field `$103E`, then immediately route through `C08C58`. That means the queue family is not chosen ad hoc at the call site; it is part of the display-record or control-record payload.

`$103E` is also more structured than a plain queue id. In the `C0:A406..A42C` producer path, the current record's `$103E` word is first copied into `$2400`. If bit `15` is set, the low six bits are then used as an index into another record's `$103E`, and that second value replaces `$2400`. If bit `14` is clear in the original word, the current record's `$103E` is cleared after use. So the safest current local read is:

- the low queue bits of `$103E` carry a renderer queue-family assignment
- bit `15` enables indirection through another record's `$103E`
- bit `14` acts like a persist-versus-one-shot control bit

So the safest current read is:

- `C08C58` is an active landing-display renderer enqueuer, not a generic math helper
- `$2400` is a renderer queue-family selector derived from the active display records
- `$103E` is best described as a per-record render-queue assignment or selector word feeding `$2400`

I am still keeping the exact per-queue BG-layer identity cautious, but these queues now look renderer-facing rather than abstract. The safest current interpretation is that the four families are render-submission groups or render phases, not yet a locally proved one-to-one `BG1/BG2/BG3/BG4` mapping.

## `C08B8E+ / C08CD5` as queue drainer and renderer-side worker

The direct queue consumers are much tighter than before.

`C08B8E+` walks the four queue families in order using their running lengths:

- `$2404..24C4` with length at `$2504`
- `$2506..25C6` with length at `$2606`
- `$2608..26C8` with length at `$2708`
- `$270A..27CA` with length at `$280A`

Each queued record is unpacked the same way:

- value column
- base or offset column
- index-like column
- bank/context byte

and then passed into common worker `C08CD5`.

One useful producer-side refinement from the newer queue pass is that resolved queue value `1` is singled out by the scan loops at `C0:DA55` and `C0:DB59`. Those paths bypass the ordinary `A0CA` dispatch and instead write per-entity values into `$280C`, which now looks like a separate landing-display ordering or priority-side scratch table. That is a strong reason to keep the queue-family model richer than a simple hardware-plane label.

`C08CD5` is now clearly renderer-side rather than generic script logic. Even with some decoder rough edges, the locally visible calls show it and its immediate helpers writing to PPU registers including:

- `$2105`
- `$2101`
- `$2107..210A`
- `$210B/$210C`

Those leaves are now tight enough to name by register family:

- `C08D79` = `BGMODE` updater through `$2105`
- `C08D92` = `OBSEL` updater through `$2101`
- `C08D9E` = `BG1SC` plus BG1-side `BG12NBA` updater through `$2107/$210B`
- `C08DDE` = `BG2SC` plus BG2-side `BG12NBA` updater through `$2108/$210B`
- `C08E1C` = `BG3SC` plus BG3-side `BG34NBA` updater through `$2109/$210C`
- `C08E5C` = `BG4SC` plus BG4-side `BG34NBA` updater through `$210A/$210C`

That makes the safest current read much stronger:

- the queue system is feeding landing-display BG or screen-layer configuration work
- `C08D79 / 8D92 / 8D9E / 8DDE / 8E1C / 8E5C` are locally strong register-family helpers for `BGMODE`, `OBSEL`, `BG1SC..BG4SC`, and `BG12NBA/BG34NBA`
- not just arbitrary timed values
- `C08CD5` is a reusable BG or screen-base setup worker that the landing subsystem is driving through queued record streams

I am still keeping the exact mapping from the four queue families to specific BG layers or sublayers open. The queue-family selector `$2400` is clearly record-driven, but the final one-to-one queue-to-layer alignment is still one step short of direct proof, and the special handling of resolved value `1` suggests some extra ordering or priority semantics on top of the plain family split.

## Combined display-side flow

The current best display-side flow is:

1. profile id `$4372` selects multiple asset families
2. bulk VRAM layer is installed from `EF:105B`
3. word-oriented profile layer is installed from `EF:10AB`
4. `C007B6` installs a profile/template block into `0x0240`
5. `C0391` derives component sums and counts from that template
6. `C00480` builds packed row table `0x0200`
7. `C00778` caches one active 16-word row set into `0x0300`
8. `C4:9440 / C4:958E` provide a secondary export or repack path for the row and sequence tables
9. `C4:B26B` initializes child-anchor state at `$B3F8/$B3FA` plus four timed control-stream families
10. `C4:B3D0 / C4:B4BE` reuse that anchor through the child-entity spawn / clear family for attached landing-display objects
11. `C0:AC68+ / ACE6+ / AD26+` tick those streams and enqueue live renderer updates through `C08C58`
12. `C08B8E+ / C08CD5` drain those queues into renderer-side PPU BG and screen-base setup work
13. `C0:0085` installs the animated graphics-strip layer
14. `C0:023F / 030F` build and advance the separate landing-profile sequencer layer

That ordering is still slightly interpretive in spots, but it is a much better local assembly model than treating the animated strip layer in isolation.

## Confidence boundaries

### Locally proved

- `C007B6`, `C00480`, `C00778`, and `C4:B26B` all sit on the active landing-profile path around `C0:09FA..0A12`
- `C007B6` installs a `0x00C0`-word block into `0x0240`
- `C007B6` supports alternate variant selection based on flag evaluation and first-word sign/high-bit state
- `C0391` scans `0x60` template words and accumulates component sums and counts into `$43D0..43DA`
- `C00480` writes a `0x0200` table across `0x0100` entries
- `C00778` reads selectors from `0x0240 + 0x40` and copies `16` selected words into `0x0300`
- `C4:9440` seeds `0x0240` and `0x0300`, reruns `C00480 / C00778`, then waits on selector `#$18` in a second local path
- no stronger late landing-local direct reader of the live `0x0300` cache is currently pinned than that secondary export path
- `C0:023F` builds `$445C/$445E/$4460/$4474` from separate profile records and `7E:B800`, not from `0x0300`
- `C4:B26B` populates `$2EB6/$2F6A/$301E/$30D2` and updates the child-anchor pair `$B3F8/$B3FA`
- landing-local readers around `C4:B37D..B48F` feed `$B3F8/$B3FA` into `C4:B3D0`, which reaches the already-mapped child-entity spawn path at `C01E49`
- `C4:B4BE` clears attached landing-display children by matching the parent-tagged `$103E` word and calling `C02140`
- `C4:B4FE..B587` are thin resolver wrappers that route registry-type, visual-type, and pose-descriptor inputs into the common spawn/clear helpers
- local producer paths derive `$2400` from record selector field `$103E` before routing through `C08C58`
- in `C0:A406..A42C`, `$103E` can act as an indirect or one-shot selector word, not just a raw queue id
- the four queue families have fixed field-array bases plus running heads at `$2504/$2606/$2708/$280A`
- resolved queue value `1` is singled out in `C0:DA55 / DB59` and diverted through `$280C`, which looks like a separate ordering or priority-side landing-display scratch table
- `C08D79 / 8D92 / 8D9E / 8DDE / 8E1C / 8E5C` target `BGMODE`, `OBSEL`, `BG1SC..BG4SC`, and `BG12NBA/BG34NBA` register families
- `C0:A56E` repeatedly mutates `$0094/$0092/$0097` and feeds worker `C0:8643`, which appends 8-byte records into `$0400` when `$0D` is nonnegative and takes an immediate DMA-style path through `$431x/$2115/$2116` when `$0D` is negative
- the earlier `$2BAA`-gated setup callers at `C0:A508..A56D` and `C0:A7C8..A82E` use those `C0:A56E` passes as extra setup-side DMA strip or descriptor generation before the main object path continues
- `C0:AC43` is a producer-side dispatcher over the timed stream families, steered by record control bits in `$2BAA` plus live state such as `$2A7E` and `$2E7A`
- `C0:AD56` implements a tiny stream interpreter with locally proved command words `1` and `3`
- `C0:AC68+ / ACE6+ / AD26+` pair the pointer arrays with current-value and countdown mirrors and feed `C08C58`
- `C08C58` appends four-column records into one of several queue families selected by `$2400`
- `C08B8E+` drains those queue families through common worker `C08CD5`
- `C08CD5` and its immediate helpers write to PPU register families including `$2105`, `$2107..210A`, and `$210B/$210C`

### Locally strong but still interpretive

- `0x0240` is best read as the active landing-profile template block
- `0x0200` is best read as a packed row table of three-component descriptors
- `0x0300` is best read as a 16-word active row-selection cache
- `C4:B26B` is best read as a timed control-stream and child-anchor initializer for the same display system
- the landing path appears to reuse the broader child-entity spawn family for attached display objects positioned from `$B3F8/$B3FA`
- `C08C58` is best read as an active display-update enqueuer for the landing renderer
- `$103E` is best read as a per-record render-queue assignment or indirection word feeding `$2400`
- the four queue families are best read as render-submission groups or render phases, not yet a fully proved one-to-one BG-layer map
- `C0:AC43` is best read as a record-driven stream-dispatch layer rather than a plain hardwired BG selector
- `C08B8E+ / C08CD5` are best read as the queue-drain and renderer-side BG/screen-layer setup stage

### Still open

- the exact player-facing meaning of the three packed components written to `0x0200`
- the exact final consumer of the cached row block at `0x0300`, beyond the currently pinned secondary export path through `C4:9440`
- the exact display meaning of the four control-stream families
- the exact per-queue mapping from the four queue families to specific BG layers or sublayers
- the exact meaning and later consumer of the special `$280C` side table built when resolved queue value `1` is singled out
- the exact visual meaning of the extra DMA strip or descriptor records generated by the `$2BAA`-gated `C0:A56E` passes
- the exact semantic meaning of the controlling bits in `$2BAA` and `$2E7A` beyond the currently proved dispatch behavior

See also [landing-display-control-words-2baa-2e7a.md](notes/landing-display-control-words-2baa-2e7a.md).

## Best next target

The cleanest next move is to pin the direct consumers of:

- `0x0300`
- the queue families written by `C08C58`
- the later display-side readers of `B3F8/B3FA`

That should decide whether the remaining open layer is best described as tile-row assembly, scripted landing-window motion, or a richer mixed display-control stage.

## Working Names

- `C0:0085` = `Install_LandingAnimatedGraphicsStrip`
- `C0:023F` = `Build_LandingProfileStepSequencer`
- `C0:030F` = `Advance_LandingProfileStepSequencer`
- `C0:0391` = `Sum_LandingTemplateComponents`
- `C0:0480` = `Build_LandingPackedRowTable0200`
- `C0:0778` = `Build_LandingActiveRowCache0300`
- `C0:07B6` = `Install_LandingProfileTemplateBlock0240`
- `C0:8B8E` = `Drain_DisplayRendererUpdateQueues`
- `C0:8C58` = `Enqueue_DisplayRendererUpdateRecord`
- `C0:8CD5` = `Apply_DisplayRendererQueueRecord`
- `C0:8D79` = `Update_BgModeRegisterFromQueue`
- `C0:8D92` = `Update_ObselRegisterFromQueue`
- `C0:8D9E` = `Update_Bg1ScreenBaseRegistersFromQueue`
- `C0:8DDE` = `Update_Bg2ScreenBaseRegistersFromQueue`
- `C0:8E1C` = `Update_Bg3ScreenBaseRegistersFromQueue`
- `C0:8E5C` = `Update_Bg4ScreenBaseRegistersFromQueue`
- `C0:A56E` = `Generate_RenderDmaStripDescriptors`
- `C0:AC68` = `Tick_LandingDisplayStreamGroup301EOr30D2`
- `C0:ACE6` = `Tick_LandingDisplayStreamGroup2F6A`
- `C0:AD26` = `Tick_LandingDisplayStreamGroup2EB6`
- `C4:B1B8` = `TransferLandingDisplayAssetSubpiecePair`
- `C4:B26B` = `InitializeLandingDisplayStreamsAndChildAnchors`
- `C4:B329` = `AdjustChildEntityAnchorForParentGeometry`
- `C4:B3D0` = `SpawnAttachedChildEntityFromParentSlot`
- `C4:B4BE` = `ClearAttachedChildEntitiesByParentSlot`
- `C4:B4FE` = `SpawnAttachedChildForRegistryTypeCode`
- `C4:B519` = `ClearAttachedChildForRegistryTypeCode`
- `C4:B524` = `SpawnAttachedChildForVisualTypeId`
- `C4:B53F` = `ClearAttachedChildForVisualTypeId`
- `C4:B54A` = `SpawnAttachedChildForPoseDescriptorId`
- `C4:B565` = `ClearAttachedChildForPoseDescriptorId`
- `C4:B570` = `SpawnDefaultAttachedChildForBaseSlot18`
- `C4:B57D` = `ClearDefaultAttachedChildForBaseSlot18`

## Source Polish Follow-Up

2026-05-06 source polish names the early C0 landing helper-call surface across
`C0:030F`, `C0:0480`, `C0:08CF`, and `C0:097B`. The source now calls the
profile sequencer payload installer, component-sum helper, packed-component
ring adjuster, HDMA dispatch loader, profile action dispatcher, template reload
and component snapshot helper, template/row-cache builders, C4 stream/child
anchor initializer, animated graphics-strip installer, sequencer builder,
debug-menu graphics refresh edge, and C4 palette mirror through named local
contracts while preserving byte equivalence.
