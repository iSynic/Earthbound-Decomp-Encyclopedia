# File Select Entity Scripts And Swirl Transition (`C4:D830..C4:D989`)

This note documents the caller-dense C4 cluster rooted at `C4:D830`, `C4:D8FA`, and `C4:D989`. The C1 callers sit in the file-select / setup-option corridor, and the C4-side byte contracts line up with three jobs:

1. run scripts on existing file-select entities selected by cached pose descriptor
2. spawn a small fixed set of file-select entities
3. run the battle-swirl-style transition loop used by the file-select flow

See also [file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md](notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md), [file-select-setup-option-menus-c1f497-c1f616.md](notes/file-select-setup-option-menus-c1f497-c1f616.md), and [battle-overlay-script-state-c4a67e-c4a7b0.md](notes/battle-overlay-script-state-c4a67e-c4a7b0.md).

## Source status

The file-select helper and init-intro dispatcher bodies are source-promoted
and byte-equivalent in the C4 scaffold:

- `src/c4/file_select_pose_entity_script_helpers.asm` covers `C4:D830..C4:D8FA`
- `src/c4/file_select_fixed_entity_spawn_helpers.asm` covers `C4:D8FA..C4:D989`
- `src/c4/file_select_swirl_transition_helpers.asm` covers `C4:D989..C4:DAD2`
- `src/c4/file_select_intro_state_dispatcher_helpers.asm` covers `C4:DAD2..C4:DCF6`
- `src/c4/file_select_tilemap_priority_helpers.asm` covers `C4:DCF6..C4:DD28`
- `src/c4/itoi_production_intro_asset_loader.asm` covers `C4:DD28..C4:DDD0`
- `src/c4/nintendo_presentation_intro_asset_loader.asm` covers `C4:DDD0..C4:DE78`

The immediately preceding ebsrc-named include
`intro/display_animated_naming_sprite.asm` is also promoted as
`src/c4/animated_naming_sprite_helpers.asm` (`C4:D7D9..C4:D830`).
`C4:DE78` is now the next open boundary, and it is data: the Your Sanctuary
location coordinate table before the next named overworld display helpers.

## `C4:D830` - table-driven file-select entity script runner

Direct caller:

- `C1:FA9D`

`C4:D830` waits until `$B4B4` is clear, indexes a four-byte pointer table at `C3:FD49` with the caller's `A`, and walks the selected list until a zero terminator.

Each list record is two words:

- word `+0`: cached pose descriptor id
- word `+2`: script-record index

For each record, the helper:

1. resolves an existing entity slot by pose descriptor through `C4:6028`
2. ignores records whose entity is not currently present
3. uses the second word as a three-byte script-record index into the table rooted at `C4:00D4`
4. passes the selected script pointer/argument pair to `C0:93F9` with `X` as the resolved entity slot

After the list is processed, it repeatedly ticks `C1:004E` until all 23 words in `$0A62..` AND together to `#$FFFF`, which makes this a synchronous "run these entity scripts and wait until the involved live entity state clears" helper.

Source polish: `src/c4/file_select_pose_entity_script_helpers.asm` now names
the `C3:FD49` pose-script pointer table, `C4:00D4` script-record table, missing
entity sentinel, live entity status table, 23-word wait scan, and all-inactive
word used by the synchronous completion loop.

## `C4:D8FA` - fixed file-select entity spawn batch

Direct caller:

- `C1:FCC0`

`C4:D8FA` walks five eight-byte records at `C3:FD65`. For each record it prepares the parameter block expected by `C0:1E49`, creates an entity with `Y = #$FFFF`, and then forces the new entity's `$2AF6` frame selector to `4`.

Source polish: `src/c4/file_select_fixed_entity_spawn_helpers.asm` now names
the `C3:FD65` fixed entity table, five-record count, `+6` Y argument offset,
no-parent sentinel, `$2AF6` frame selector table, and initial selector `4`.

The caller context at `C1:FCC0` is in the file-select/options tail after two small C4 text records are installed and before `$5E6E` is set to `#$00FF`, so the safest current read is that this routine spawns the fixed file-select/menu entity batch used by that screen.

## `C4:D989` - file-select swirl transition runner

Direct callers:

- `C4:DC4A`
- `C4:DC56`
- `C4:DC62`
- `C4:DC6E`
- `C4:DC7A`
- `C4:DC86`
- `C4:DC92`
- `C4:DC9E`

All direct callers are branch bodies in the larger `C4:DAD2` state dispatcher. They pass small mode values such as `0`, `2`, `3`, `4`, `5`, `6`, `7`, and `9`.

At a high level, `C4:D989`:

- calls `C0:927C` and `C0:1A86` to reset delayed-action/entity state
- runs the `C0:1C11 / C0:1A69` setup pair with `A = #$8000`
- seeds `$4A58 = 1`, clears `$4A5A`, and calls `C4:FD45(0)`
- seeds `$0A4C/$0A4E` to `#$0017/#$0018`
- calls `C0:9321(1, 0, 0)` and `C0:2D29`
- clears six bytes at `$986F..$9874`
- initializes the screen/player position through `C0:B65F(#$1D60, X = #$0B08)` and `C0:3A24`
- clears a CGRAM/palette work area through `C0:8EFC(#$0200, X = #$0200)`
- starts the battle-swirl overlay with `C2:EA15(0)`
- steps `C4:A7B0` and frame-wait helpers while watching `$9641` and input bits at `$006D`
- closes the overlay through `C2:EA74`, polls `C2:EACF`, then calls `C2:EAAA`
- returns a small result in `A` through local `$12`

The input mode selects a pointer from the table at `C3:FD8D`, and that pointer is handed to `C1:86B1` before the loop. So this is not just a generic battle-swirl helper; it is a file-select transition runner with a mode-selected C1 text/menu payload and a battle-swirl overlay open/close sequence.

Source polish: `src/c4/file_select_swirl_transition_helpers.asm` now names the
delayed-action/entity reset callees, auto-sector music latch, `$4A58/$4A5A`
presentation flags, `$0A4C/$0A4E` camera seeds, `$986F..$9874` scratch clear,
file-select swirl text pointer table at `C3:FD8D`, `$9641` overlay completion
latch, `$006D` abort masks, `$001A` display mode, `$0028` busy byte, and the
small abort/completed return values.

## `C4:DAD2` - init-intro file-select state dispatcher

Direct caller:

- `C0:B7EB`

ebsrc names this exact span `intro/init_intro.asm` / `INIT_INTRO`. The local
body is a state machine that initializes file-select/intro presentation state,
clears a set of display counters twice through `C0:8B26`, then loops over
state `$02`.

States `0` and `1` poll earlier menu/intro predicates at `C0:F009` and
`C0:F33C`, play the Sound Stone melody helper at `C4:FBBD`, and advance
through `C3:F3C5`. States `3..9` funnel into `C4:D989` with the corresponding
file-select swirl mode values. The common exit clears `$5DD8`, resets color
math registers `$2130/$2131`, and sets `$001A/$001B` to the same post-transition
display state used by the file-select visual corridor.

Source polish: `src/c4/file_select_intro_state_dispatcher_helpers.asm` now
names the init-intro state ids, result scratch, `$B4B6` file-select session
flag, `$5DD8` presentation flag, screen-origin reset words, forced-blank
display shadow check, color/display latches, Sound Stone melody ids,
`C3:F3C5` still-image arguments, and the swirl mode values passed into
`C4:D989`.

## `C4:DCF6` - decompressed tile word priority pass

Direct callers:

- `C4:DD50`
- `C4:DDF8`

`C4:DCF6` is a tight post-decompression pass over `$7F:0000`:

```text
for word in 0..0x3FF:
    [$7F:0000 + word * 2] |= 0x2000
```

Both local callers follow the same pattern:

1. decompress an `E1` asset into `$7F:0000` through `C4:1A9E`
2. call `C4:DCF6` to OR bit `0x2000` into 0x400 tilemap words
3. transfer the resulting 0x800-byte block to VRAM destination `$7C00` through `C0:8616`
4. decompress a second `E1` asset and transfer a 0x400-byte block to `$6000`
5. decompress a palette/block into `$0200` and queue selector `0x18` through `C0:856B`

The two callers are now source-promoted as the Itoi production and Nintendo
presentation intro asset loaders. Mechanically `C4:DCF6` is not a renderer by
itself; it is the tilemap attribute/prioritization pass used by those visual
asset loaders before upload.

Source polish: `src/c4/file_select_tilemap_priority_helpers.asm` now names the
`7F:0000` tilemap buffer, `#$2000` priority attribute bit, and 0x400-word pass
count.

## Working Names

- `C4:D830` = `RunFileSelectPoseEntityScriptList`
- `C4:D8FA` = `SpawnFileSelectFixedEntityBatch`
- `C4:D989` = `RunFileSelectSwirlTransitionMode`
- `C4:DAD2` = `InitIntroFileSelectStateDispatcher`
- `C4:DCF6` = `SetPriorityBitOnFileSelectTilemap7f0000`
- `C4:DD28` = `DecompressItoiProductionIntroAssets`
- `C4:DDD0` = `DecompressNintendoPresentationIntroAssets`

## Still open

- the exact record names for the `C3:FD49`, `C3:FD65`, and `C3:FD8D` file-select tables
- the exact return-value meaning of `C4:D989` beyond the clear local "input abort vs completed transition" shape
- the final user-facing names for the mode values passed into `C4:D989`
- the exact source-table names for the E1 asset pointers consumed by the two intro asset loaders
