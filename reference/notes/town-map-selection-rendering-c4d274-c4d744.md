# Town Map Selection And Rendering `C4:D274..D7D9`

## Scope

This note documents the town-map helpers around the `ebsrc-main` bracket:

- `overworld/get_town_map_id.asm`
- `unknown/C4/C4D2A8.asm`
- `unknown/C4/C4D2F0.asm`
- `unknown/C4/C4D43F.asm`
- `overworld/load_town_map_data.asm`
- `overworld/display_town_map.asm`
- `unknown/C4/C4D744.asm`

The reference names are useful here because the local call graph lines up exactly with the text-command case for town maps: `C1:BFD0` calls `C4:D681` from `[1F 41 07]`, and `notes/text-command-1f41-special-event-dispatch-c1befc.md` already identifies case `07` as the town-map special event.

## Source status

This pocket is source-promoted and byte-equivalent in the C4 scaffold:

- `src/c4/town_map_selection_render_helpers.asm` covers `C4:D274..C4:D553`
- `src/c4/town_map_data_load_helpers.asm` covers `C4:D553..C4:D681`
- `src/c4/town_map_display_viewer_helpers.asm` covers `C4:D681..C4:D7D9`

`LoadTownMapData` needs explicit width-restoration hints at `C4:D618`,
`C4:D62F`, and `C4:D65B` when emitted linearly, matching the external VRAM/DMA
helpers' return-width contract.

## Map id helper

`C4:D274` is the local body corresponding to `overworld/get_town_map_id.asm`.

It derives a compact tile/region index from the live overworld coordinates:

- high byte of `$9877`
- `$987B` divided by `0x80` through `C0:915B`
- 3-column/0x60-byte stride math into `EF:A70F`

The helper returns `EF:A70F[index] & 00FF`. `C4:D681` masks that to the low nibble and treats zero as "no town map available here"; nonzero values become one-based town-map ids.

## Animation and overlay timers

`C4:D2A8` is a 12-frame town-map icon/palette animation tick. It uses `$B4B2` as the countdown. When the timer reaches zero, it:

- resets `$B4B2 = 0x000C`
- shifts a small `$0200` CGRAM/shadow span covering entries `0x81..0x86`
- mirrors `$0302` into `$030E`
- calls `C0:856B(0x10)`, matching the broader C0 display/palette commit family

`C4:D2F0` is the current-position overlay updater. It recomputes the current coarse map cell from `$9877/$987B`, reads `EF:A70F`, and uses bits `0x10`, `0x20`, `0x40`, and `0x30` to optionally draw adjacent connector/arrow icons. The icon ids come from `EF:C513`, `EF:C515`, `EF:C517`, and `EF:C519`, are mapped through `E1:F44C`, and are submitted through `C0:8C54`.

After connector overlays, `C4:D2F0` draws the current-position marker. `$B4B0` is a 20-frame blink timer:

- values below `0x000A` use icon id from `EF:C511`
- values `0x000A..0x0013` use icon id from `EF:C50F`
- the timer decrements every call and resets to `0x0014`

## Static icon renderer

`C4:D43F` renders the static icon list for a selected town map id.

Input:

- `A` = zero-based town-map id

It clears `$2400`, temporarily swaps display flag `$000B` through `C0:88A5`, indexes a pointer table at `E1:F491`, then walks five-byte records until an `FF` sentinel.

The `E1:F203..E1:F581` support span now has a generated structural split in
`notes/ui-font-town-map-asset-contracts.md`:

- `E1:F203..E1:F44C` = `117` five-byte icon graphics descriptor records
  across `22` unique descriptor lists
- `E1:F44C..E1:F47A` = `23` 16-bit local pointers mapping icon ids to those
  descriptor lists
- `E1:F47A..E1:F491` = `23` one-byte blink/suppress flags
- `E1:F491..E1:F4A9` = six 4-byte placement-list pointers
- `E1:F4A9..E1:F581` = six town-map icon placement lists with `42` total
  five-byte records

Icon graphics descriptor record shape:

- byte `+0` = signed Y offset added to the base Y submitted through `C0:8C54`; the generic renderer has a special control branch for `$80`, but that control value does not appear in the E1 town-map icon descriptor range
- word `+1` = tile/attribute word copied into the renderer staging record
- byte `+3` = signed X offset added to the base X submitted through `C0:8C54`
- byte `+4` = control flags; bit `7` marks the final record in a descriptor list, bit `0` feeds `C0:8CD5`'s packed renderer mask/attribute bit, and bits `1..6` are zero in the checked E1 town-map descriptors

Placement record shape:

- byte `+0` = X coordinate passed to `C0:8C54`
- byte `+1` = Y coordinate passed to `C0:8C54`
- byte `+2` = icon id, mapped through `E1:F44C`
- word `+3` = event flag id; high bit means the icon is drawn when the flag is set, clear high bit means it is drawn when the flag is clear

Before the event-flag test, the icon id is checked against `E1:F47A`. When that byte is nonzero and `$B4AE < 0x000A`, the icon is suppressed for that pass. `$B4AE` is therefore the 60-frame blink phase used for town-map animated/static icon alternation.

Each visible record is submitted through `C0:8C54`, then `C4:D43F` calls `C4:D2F0` for the current-position/connector overlay, decrements `$B4AE`, restores the display flag through `C0:88A5(previous)`, and calls `C4:D2A8`.

## Load and display bodies

`C4:D553` is the local body corresponding to `overworld/load_town_map_data.asm`.

Input:

- `A` = zero-based town-map id

It selects a pointer from the table at `E0:2190`, decompresses the selected town-map asset into bank `7F` through `C4:1A9E`, waits for the decompressor busy byte `$0028` to clear, clears/transfers staging buffers through `C0:8ED2`, `C0:8D9E`, `C0:8D92`, `C0:8616`, and `C0:85B7`, and resets display color/math state before returning. The byte-level transfer contract is display setup, while the reference include gives the player-facing identity: load town map data.

Source polish: the town-map source helpers now name the `EF:A70F` sector
lookup, E0 graphics pointer table, E1 icon pointer/suppress/placement tables,
`$B4AE/$B4B0/$B4B2` blink/palette timers, town-map input masks, decompressor
busy byte, display mode latches, and the main VRAM transfer destinations for
map graphics, labels, and icon tiles.

`C4:D681` is the local body corresponding to `overworld/display_town_map.asm`.

It initializes the town-map timers:

- `$B4AE = 0x003C`
- `$B4B0 = 0x0014`
- `$B4B2 = 0x000C`

Then it calls `C4:D274` with live `$9877/$987B`. If no map id is available, it returns zero. Otherwise it:

1. converts the one-based map id to a zero-based index
2. calls `C4:D553` to load the selected map data
3. runs a frame loop: `C0:8756`, `C0:88B1`, `C4:D43F`, `C0:8B26`
4. exits when input bits in `$006D` indicate cancel/confirm/directional exit
5. runs a 16-frame closeout loop that keeps drawing the map
6. applies the same world/display restore path seen elsewhere: `$5DD8`, `C0:18F3`, `$5DD4 = $5DD6`, `C4:800B`, `$001A = 0x17`, `C0:886C`

It returns the one-based town-map id in `A`, which is why text command `[1F 41 07]` preserves the return value.

## Browsable map viewer

`C4:D744` is a second town-map display entry point. Instead of deriving the town-map id from `$9877/$987B`, it starts at map index zero and lets input bits in `$006D` adjust the selected map:

- `0x0800` decrements the zero-based map index
- `0x0400` increments it
- the index wraps across `0..5`
- when the index changes, it reloads map data through `C4:D553`
- each frame draws through `C4:D43F`
- `0x0080` exits and restores display state

The only direct caller found locally is `C1:30BF`, in a C1 special/menu dispatch corridor. The safe local name is therefore a town-map browse/cycle viewer rather than the position-derived town-map command.

## Working Names

- `C4:D274` = `GetTownMapIdForCurrentPosition`
- `C4:D2A8` = `TickTownMapPaletteAnimation`
- `C4:D2F0` = `DrawTownMapCurrentPositionOverlay`
- `C4:D43F` = `DrawTownMapStaticIconsAndOverlay`
- `C4:D553` = `LoadTownMapData`
- `C4:D681` = `DisplayCurrentPositionTownMap`
- `C4:D744` = `RunTownMapBrowseViewer`

## Confidence boundaries

- The town-map identities for `C4:D274`, `C4:D553`, and `C4:D681` are corroborated by `ebsrc-main` include names and the local `[1F 41 07]` caller.
- The `C4:D2A8/D2F0/D43F` names are local mechanical names; they are not reference names.
- The exact user-facing source of `C1:30BF -> C4:D744` still needs a C1 dispatch pass, but the C4 body itself is clearly a map-index browsing viewer.
