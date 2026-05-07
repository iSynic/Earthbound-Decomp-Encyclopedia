# Cast Scene Loader, Credits, And Audio Tail Helpers `C4:E369..C4:FD4B`

## Scope

This note records the first clean source-promoted islands inside the ending
cast-scene cluster after the Your Sanctuary corridor.

The surrounding ebsrc include order begins at `C4:E369`:

- `ending/load_cast_scene.asm`
- `ending/set_cast_scroll_threshold.asm`
- `ending/check_cast_scroll_threshold.asm`
- `ending/handle_cast_scrolling.asm`
- `ending/render_cast_name_text.asm`
- cast-name text/tilemap helpers, print wrappers, scene controller, and an
- unused scratch renderer, VWF conversion helper, credits/photo playback
  controller, music table block, and audio helper tail through `C4:FD4B`

The loader span at `C4:E369..C4:E4DA` needs several accumulator-width boundary
hints after byte-sized transfer calls, but with those boundaries pinned it is a
closed byte-equivalent routine. The three scroll helpers after it are also
closed routines and validate byte-for-byte in the C4 scaffold.

## Source Status

The promoted helper islands are:

- `src/c4/cast_scene_loader.asm` covers `C4:E369..C4:E4DA`
- `src/c4/cast_scroll_threshold_helpers.asm` covers `C4:E4DA..C4:E4F9`
- `src/c4/cast_scroll_threshold_check_helpers.asm` covers `C4:E4F9..C4:E51E`
- `src/c4/cast_scrolling_helpers.asm` covers `C4:E51E..C4:E583`
- `src/c4/cast_name_text_renderer.asm` covers `C4:E583..C4:E7AE`
- `src/c4/cast_name_tilemap_prepare_helpers.asm` covers `C4:E7AE..C4:EA9C`
- `src/c4/cast_name_tilemap_copy_helpers.asm` covers `C4:EA9C..C4:EB04`
- `src/c4/cast_name_print_helpers.asm` covers `C4:EB04..C4:EBAD`
- `src/c4/cast_name_party_print_helpers.asm` covers `C4:EBAD..C4:EC05`
- `src/c4/cast_name_entity_var0_print_helpers.asm` covers `C4:EC05..C4:EC52`
- `src/c4/cast_name_current_threshold_print_helpers.asm` covers `C4:EC52..C4:EC6E`
- `src/c4/special_cast_palette_upload_helpers.asm` covers `C4:EC6E..C4:ECAD`
- `src/c4/cast_entity_spawn_position_helpers.asm` covers `C4:ECAD..C4:ECE7`
- `src/c4/cast_entity_onscreen_check_helpers.asm` covers `C4:ECE7..C4:ED0E`
- `src/c4/cast_scene_play_controller.asm` covers `C4:ED0E..C4:EDA3`
- `src/c4/unused_cast_name_scratch_renderer.asm` covers `C4:EDA3..C4:EE9D`
- `src/c4/unused_cast_name_scratch_wrapper.asm` covers `C4:EE9D..C4:EEE1`
- `src/c4/vwf_2bpp_to_three_color_helpers.asm` covers `C4:EEE1..C4:EFC4`
- `src/c4/credits_dma_enqueue_helpers.asm` covers `C4:EFC4..C4:F01D`
- `src/c4/credits_dma_queue_process_helpers.asm` covers `C4:F01D..C4:F07D`
- `src/c4/credits_scene_initializer.asm` covers `C4:F07D..C4:F264`
- `src/c4/credits_photograph_render_helpers.asm` covers `C4:F264..C4:F433`
- `src/c4/credits_photo_flag_counter.asm` covers `C4:F433..C4:F46F`
- `src/c4/credits_photograph_slide_helpers.asm` covers `C4:F46F..C4:F554`
- `src/c4/credits_scene_playback_controller.asm` covers `C4:F554..C4:F70A`
- `src/c4/music_dataset_and_pack_pointer_tables.asm` covers `C4:F70A..C4:FB42`
  as two preserved table spans: `C4:F70A..C4:F947` for
  `MusicDatasetTable` and `C4:F947..C4:FB42` for `MusicPackPointerTable`
- `src/c4/audio_bank_resolver.asm` covers `C4:FB42..C4:FB58`
- `src/c4/music_subsystem_initializer.asm` covers `C4:FB58..C4:FBBD`
- `src/c4/music_change_pack_loader.asm` covers `C4:FBBD..C4:FD18`
- `src/c4/audio_channel_mode_loader.asm` covers `C4:FD18..C4:FD45`
- `src/c4/auto_sector_music_change_latch.asm` covers `C4:FD45..C4:FD4B`

They are included in `src/c4/bank_c4_helpers_asar.asm` and the combined C4
byte-equivalence check currently validates all `142` C4 scaffold modules with
`0` mismatches.

## Main Result

`C4:E369` initializes the cast scene display state. It resets active entity
slots, marks active entity records, loads battle BG preset `0x0117`, clears the
BG3 scroll words at `$0031..$003B`, clears and uploads staging buffers, expands
several `E1`/`C3` asset payloads through `C4:1A9E`, prepares the cast-name
tilemap, refreshes the window-flavor palette, sets `$0030 = 0x18` and
`$001A = 0x14`, clears `$B4CF/$B4D1`, and opens the display transition bracket.

2026-05-06 cast loader presentation follow-up: the source now keeps these as
loader-local contracts, naming the `$9F2A` presentation latch reset, live
entity `$0A62` sentinel scan and `$116A/$8000` marker, cast-name glyph-width
mode byte `$B4CE`, BG3 `$7C00` clear/upload size, E1/C3 low-word asset staging
tuples, and final `$0030/$001A` display selector seeds. The C0/C4 callee names
remain caller references only.

`C4:E4DA` stores a BG3/cast-scroll threshold for the active cast slot. It is
called by event 801's `WaitForCastScrollThreshold` short subroutine after the
script writes a small spacing/delay value. The helper uses `$1A42` as the
current cast driver slot, scales the incoming value by eight pixels, adds the
current scroll position at `$003B`, and writes the absolute threshold to
`$0E5E + slot * 2`.

`C4:E4F9` checks whether the active slot has reached its stored threshold. It
compares `$0E5E + slot * 2` against `$003B` and returns `1` once the threshold
has been met or passed.

`C4:E51E` advances the cast scrolling state and queues a small BG3 VRAM row
transfer. Event 801 installs it as a tick callback before setting the driver
slot's Y velocity. The helper mirrors the active slot's live Y coordinate from
`$0BCA + slot * 2` into the BG3 scroll shadow at `$003B`, advances a per-slot
blank-row upload cursor at `$1002 + slot * 2` toward that scroll position in
8-pixel steps, derives a wrapped `$7C00` tilemap destination row, clears a word
at `$7FFE`, and calls `C0:8616`/`QueueVramTransfer_FromDpSource` for a `$40`
byte transfer.

`C4:E583` renders cast-name text into the `$3492` scratch rows. It formats a
source name through the C1 file-select text layout helper, resolves glyph
metadata from the `C3:F054` table family, calls `C4:4B3A` to merge glyph runs
into scratch rows, and then copies the staged rows toward the local tilemap
buffer. The short `C4:E796..C4:E7AE` byte table is kept inline with the source
module because the renderer and the following preparation routine both use it
as local cast-name tilemap data.

`C4:E7AE..C4:EBAD` prepares and copies the cast-name tilemap rows, then queues
the row upload used by the ending cast display. The helpers share the
`C4:E796` tilemap patch data, write through the `$7F:4000` staging buffer,
apply the cast-name base tile offset at `$B4D1`, and use the C0 local-buffer
copy/VRAM transfer contracts already seen in earlier text/window helpers.

2026-05-06 cast-name patch follow-up: the inline `C4:E796..E7AE` table is now
split into the three C4-local suffix patch rows consumed by
`PrepareCastNameTilemap`: possessive dad, possessive mom, and possessive
Master. The prep helper names the three patch source lows plus the C4 bank byte
where it stages the local copy arguments for the C0 tilemap-patch callee.

2026-05-06 cast-name tilemap prep follow-up: the preparation and print helpers
now name the local row/template counts, C3:FDB5 party source table, current-bank
template lows, E1:2EFA pointer-record offsets for dad/mom/Master, `$7F:4000`
staging bank, BG3 `$7C00` row wrap math, and C0 transfer selector byte. These
remain C4-local presentation-table contracts; C0 copy/VRAM queue internals and
C3/E1 payload decoding stay external.

2026-05-06 cast-name wrapper follow-up: the copy/wrapper helpers now carry the
same local `$7F:4000` row shape, `$B4D1` tile-base delta, E1:2EFA three-byte
pointer-record shape, C3:FDB5 party source lookup, and special source-selector
`7 -> 01C0` contract used by the polished preparation path.

`C4:EBAD..C4:EC6E` are small print wrappers that select the party/current-slot
or entity-var0 source before entering the cast-name print path.

`C4:EC6E..C4:ED0E` covers a special cast palette upload helper and two entity
position/onscreen helpers used by the cast controller. The spawn helper reads
staged cast X/Y fields from `$0E5E/$0E9A` and adds the live BG3 Y scroll at
`$003B`; the onscreen check compares `$003B - 8` against the current slot's
live Y at `$0BCA`.

2026-05-06 cast palette/spawn follow-up: the current-slot print wrapper now
keeps `$0E5E + slot*2` local to the cast-name selector role, the special palette
helper names its `$7F:7000 + index*$20 -> $0380` transfer and `$0030 = #$10`
selector, and the spawn/onscreen helpers name the `$0A38` rotating spawn
variant, `$FFFF` default parent argument, and word-indexed live-Y comparison.
The entity constructor and palette transfer callees remain external contracts.

`C4:ED0E..C4:EDA3` is the promoted `PlayCastScene` controller. It brackets cast
scene loading, transition state, event-801 driver allocation (`#$0321`),
per-frame updates until `$9641` is set, final driver cleanup, and restoration
of the normal delayed-action/presentation state.

2026-05-06 cast controller follow-up: the controller now names the event-801
driver id, `$9641` completion latch, live `$0A62` driver cleanup scan,
delayed-action restore anchors `$0A4C/$0A4E = 17/18`, return transition mode,
and final `$001A = #$17` display mode. The C0/C1/C2 frame/update/remove
callees remain caller references.

`C4:EDA3..C4:EE9D` is ebsrc's following unused cast-name scratch renderer. It
shares the same glyph-run renderer and VRAM queue contracts as the live
cast-name path, but is kept as a separate module because ebsrc gives it a hard
unused include boundary.

`C4:EE9D..C4:EEE1` is the next unused wrapper over the scratch renderer. It
iterates the four `$B4D5` cast-name sources and a final `$B4DD` source before
returning.

`C4:EEE1..C4:EFC4` converts the staged VWF scratch rows from 2bpp into the
three-color format used by the ending/credits display path. The branch joins
need explicit accumulator-width hints during source emission, but the resulting
module validates byte-for-byte.

`C4:EFC4..C4:F07D` is the credits DMA queue pair. `C4:EFC4` appends a
9-byte queue record under `$B4F5`; the record carries the C0 VRAM-transfer
selector byte, destination VRAM word, long source pointer, and byte count that
the C0 credits command-stream callback supplies. `C4:F01D` drains one record
per call from `$B4F3` and forwards it to `C0:8616`.

2026-05-06 credits DMA queue follow-up: the enqueue and drain helpers now share
named record constants for the 9-byte stride, selector byte, VRAM destination,
source low/bank words, byte count, and `$007F` ring-index mask. The source
comments keep this as a C4-owned queue-packing/unpacking contract while leaving
the C0 VRAM transfer helper semantics to C0.

`C4:F07D..C4:F70A` is the main credits scene block. It initializes the credits
display, seeds the command-stream WRAM fields at `$B4E3/$B4E5/$B4E7..$B4ED`,
checks which photograph flags are set, installs `C0:F41E` through the C0 frame
callback pointer, renders eligible photographs, slides them while draining the
credits DMA queue, resets the callback to the default stub, reinstalls the
delayed-action callback, and restores the display state after the credits
presentation.

2026-05-06 credits scene state follow-up: the initializer now names the local
`$7F:0000` work buffer, E1 command-stream start at `E1:413F`, initial BG3 row
threshold, `$7DFE` clear span, and display selector/mode bytes it seeds before
arming the C0 command-stream callback. The playback tail now names the fixed
post-scroll hold, return entity spawn coordinates, final `$7DFE` clear span,
and display mode restored before the delayed-action callback is reinstalled.

2026-05-06 credits photograph follow-up: the photograph render/count/slide
helpers now share C4-local names for the `E1:2F8A` record gate, map-cell
offsets, object and attached-visual coordinate/id fields, four-object and
six-visual loop bounds, `$98CB` optional visual rows, fixed photo palette block,
and slide angle/frame-count fields. The source comments identify only the C4
argument staging for map load, entity spawn, visual attach, BG3 scroll, and
DMA queue drains; the C0/C2 helper internals remain external.

The adjacent producer-side follow-up in
`src/c4/photo_and_new_entity_preparation_helpers.asm` now uses compatible
names for the same photographer record family when `C4:6D4B` places the current
slot from offsets `+$0A/+$0C`; see
`notes/current-slot-position-staging-c46b8d-c46d4b.md` for that movement-facing
contract.

`C4:F70A..C4:F947` is the ebsrc-named music dataset table. `ChangeMusic` treats
the requested music id as one-based, subtracts one for the row lookup, and reads
three byte fields per row: primary sample pack, secondary sample pack, and
sequence pack. A field value of `$FF` means that pack role does not request a
new load.

`C4:F947..C4:FB42` is the music pack pointer table selected by the audio
loader. Each 3-byte row carries the pack stream bank byte followed by a 16-bit
stream address. `GetAudioBank` resolves the bank byte unchanged in the US ROM
and resets `SequencePackMask` to `$FFFF` before the address word is consumed.

`C4:FB58..C4:FBBD` is the cold-start music initializer. It clears the current
sequence/primary pack latches, loads the row-0 sequence/common pack into the
bootstrap shared-pack latch, streams that pack through `C0:AB06`, and enables
auto sector music changes.

`C4:FBBD..C4:FD18` is the runtime music change loader. It skips unchanged or
`$FF` pack roles, applies primary sample pack, secondary sample pack, then
sequence pack loads through `C0:AB06`, skips the bootstrap shared pack in the
secondary role, preserves seamless playback for Sound Stone recording tracks
`$00A0..$00A7`, and finally sends the one-based track id through
`C0:ABBD`.

`C4:FD18..C4:FD4B` loads the stereo/mono SPC data stream selected by
`SetAudioChannels`, then stores the auto-sector music-change latch used by map
or sector refresh code.

## Working Names

- `C4:E369` = `LoadCastScene`
- `C4:E4DA` = `SetCastScrollThreshold`
- `C4:E4F9` = `CheckCastScrollThreshold`
- `C4:E51E` = `HandleCastScrolling`
- `C4:E583` = `RenderCastNameText`
- `C4:E796` = `CastNameTextTilemapPatchTable`
- `C4:E796` = `CastNameTextTilemapPatchPossessiveDad`
- `C4:E79D` = `CastNameTextTilemapPatchPossessiveMom`
- `C4:E7A4` = `CastNameTextTilemapPatchPossessiveMaster`
- `C4:E7AE` = `PrepareCastNameTilemap`
- `C4:EA9C` = `CopyCastNameTilemap`
- `C4:EB04` = `PrintCastName`
- `C4:EBAD` = `PrintCastNameParty`
- `C4:EC05` = `PrintCastNameEntityVar0`
- `C4:EC52` = `PrintCastNameCurrentThreshold`
- `C4:EC6E` = `UploadSpecialCastPalette`
- `C4:ECAD` = `CreateEntityAtV01PlusBg3Y`
- `C4:ECE7` = `IsEntityStillOnCastScreen`
- `C4:ED0E` = `PlayCastScene`
- `C4:EDA3` = `UnusedCastNameScratchRenderer`
- `C4:EE9D` = `RenderUnusedCastNameScratchSet`
- `C4:EEE1` = `ConvertVwf2bppToThreeColor`
- `C4:EFC4` = `EnqueueCreditsDma`
- `C4:F01D` = `ProcessCreditsDmaQueue`
- `C4:F07D` = `InitializeCreditsScene`
- `C4:F264` = `TryRenderingPhotograph`
- `C4:F433` = `CountPhotoFlags`
- `C4:F46F` = `SlideCreditsPhotograph`
- `C4:F554` = `PlayCredits`
- `C4:F70A` = `MusicDatasetTable`
- `C4:F947` = `MusicPackPointerTable`
- `C4:FB42` = `GetAudioBank`
- `C4:FB58` = `InitializeMusicSubsystem`
- `C4:FBBD` = `ChangeMusic`
- `C4:FD18` = `SetAudioChannels`
- `C4:FD45` = `SetAutoSectorMusicChanges`

## Still Open

- The named ebsrc tail is source/data-covered through `C4:FD4B`; bank-end
  padding remains outside the source scaffold.
- The cast-scroll side now has a cast-local contract for `$0BCA`, `$0E5E`, and
  `$1002`: `$0BCA[current]` is the driver slot's live Y, `$0E5E[current]` is a
  script-polled scroll threshold or staged cast spawn X depending on the helper
  family, and `$1002[current]` is the blank-row upload cursor used only by the
  scrolling tick callback. Keep these names local because the same per-slot
  tables have broader action-script meanings elsewhere.
- The credits side now identifies `$003B` as the high word consumed by the
  BG3 vertical-scroll/credits progress loop; the broader display-scroll naming
  still needs one cross-bank pass before making it a global symbol.
- The audio tail now has table-local contracts for the music dataset row
  fields, audio-pack pointer row shape, bootstrap shared-pack latch, Sound
  Stone transition exception, and `ChangeMusic -> C0:ABBD` one-based mailbox
  command. Keep the table roles local until the audio exporter/frontier notes
  settle a broader public API vocabulary for packs versus sequences.
