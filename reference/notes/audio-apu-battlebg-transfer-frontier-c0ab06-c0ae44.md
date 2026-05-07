# Audio/APU and battle-background transfer frontier (`C0:AB06-C0:AE44`)

## Scope

`C0:AB06-C0:AE44` bridges three closely packed hardware-facing families:

- SPC700 data upload and APUIO command wrappers.
- The small stereo/mono configuration table at `C0:AC2C`.
- Battle-background DMA descriptor preparation, including the `EVENT_786`
  action script and the DMA enable/disable tables at `C0:AE16-C0:AE44`.

The ebsrc bank map confirms this sequence as `LOAD_SPC700_DATA`,
`UNKNOWN_C0ABBD`, `STOP_MUSIC`, `PLAY_SOUND`, `UNKNOWN_C0AC0C`,
`UNKNOWN_C0AC20`, `STEREO_MONO_DATA`, `UNKNOWN_C0AC3A`,
`UNKNOWN_C0AC43`, `UNKNOWN_C0AD56`, `EVENT_786`, `UNKNOWN_C0AD9F`,
`DO_BATTLEBG_DMA`, `DMA_FLAGS`, `UNKNOWN_C0AE34`, and `UNKNOWN_C0AE44`.

## SPC700/APUIO command layer

- `C0:AB06` is the SPC700 loader. It stores the source pointer in `$00C6`
  and `$00C8`, normalizes DB/DP to bank 0, waits for the SPC ready signature
  `$BBAA` on `APUPort0`, disables NMI through `$001E/$4200`, streams blocks
  through `APUPort0` and `APUPort2`, then restores NMI on exit. The local
  decoder now recognizes opcode `2A` as `ROL A`, which is the carry-to-byte
  step used before writing `APUPort1`.
- `C0:ABA8` is the local wait/reset subroutine for the loader. It clears
  `APUPort2` and `APUPort0`, then loops writing `$00FF` to `APUPort0` until
  `$BBAA` is echoed.
- `C0:ABBD` writes the low byte of A directly to `APUPort0`.
- `C0:ABC6` is `STOP_MUSIC`: it writes zero to `APUPort0`, polls
  `C0:AC20` until the port reads back zero, then stores `$FFFF` in
  `$B53B`/`CURRENT_MUSIC_TRACK`.
- `C0:ABE0` is `PLAY_SOUND`: nonzero A is queued into the eight-entry
  `$1AC2` sound-effect ring using `$00CA` and the `$1ACA` high-bit flipper.
  Zero branches to `C0:AC01`, which writes `$57` to `APUPort3`.
- `C0:AC0C` writes A OR `$1ACB` to `APUPort1`, then toggles `$1ACB` with
  `$80`. `CHANGE_MUSIC` uses this before stopping most non-Sound-Stone tracks.
- `C0:AC20` reads `APUPort0` and returns it masked to one byte.
- `C0:AC2C-C0:AC39` is `STEREO_MONO_DATA`, two compact records immediately
  before the `APUPort2` writer.
- `C0:AC3A` writes the low byte of A directly to `APUPort2`.

## Music caller corroboration

`refs/ebsrc-main/src/audio/change_music.asm` shows the higher-level contract:
it calls `PLAY_SOUND_UNKNOWN0`, optionally signals `UNKNOWN_C0AC0C` with
`#$0001`, stops music, loads changed primary/secondary/sequence packs through
`LOAD_SPC700_DATA`, updates `CURRENT_MUSIC_TRACK`, then calls
`UNKNOWN_C0ABBD` with the one-based track index. That makes `ABBD` the final
track-start command byte rather than a generic queue helper.

## Battle-background transfer selector

- `C0:AC43` is the long per-slot battle-background transfer selector. It
  seeds a C4 bank byte in `$04/$000B`, uses `$2BAA[slot]` low bits for mode
  selection and a `+0/+5` tile offset, then conditionally expands cached
  descriptor streams through `C0:AD56`.
- The routine uses four cached pointer/count pairs:
  `$301E/$305A` with destination base `$3096`, `$30D2/$310E` with `$314A`,
  `$2F6A/$2FA6` with `$2FE2`, and `$2EB6/$2EF2` with `$2F2E`.
- After a stream is active, it decrements that stream's countdown, combines
  the cached value with the mode offset, loads the source slot from `$0B16`
  and Y position from `$0B52`, and calls `C0:8C58` to emit the actual transfer
  descriptor.
- `$2E7A[slot]` gates the extra background passes. Negative values enable the
  `$2F6A/$2FE2` stream for slots `>= $002E`; bit `$4000` enables the
  `$2EB6/$2F2E` stream.

## Descriptor expansion and DMA control

- `C0:AD56` expands a compact descriptor stream referenced through `$02`.
  Record type `1` copies a word into the destination array at base + current
  slot; record type `3` redirects `$02` to a new stream; any other type ends
  the expansion and returns the next stream pointer in A plus the elapsed word
  count in Y.
- `C0:AD8A-C0:AD9E` is `EVENT_786`, not code. It installs position-change
  callback `C0:A039`, physics callback `C0:A26B`, pauses, sets animation 0,
  runs `EVENT_UNKNOWN_C0A443_ENTRY3`, then loops on `UNKNOWN_C0778A`.
- `C0:AD9F` writes `$003B/$003C` to `VMAIN/VMADDL` (`$2112`) as a tiny RTS
  helper.
- `C0:ADB2` is `DO_BATTLEBG_DMA`. It configures DMA channel registers under
  `$43x0`: bank `$7E`, source bank fields, DMAP `$42`, the B-bus register
  selected from `C0:AE1D`, a temporary source descriptor copied from
  `C0:AE26` or `C0:AE2D`, and then ORs `$001F` with `DMA_FLAGS` at
  `C0:AE16`.
- `C0:AE16-C0:AE1C` is the DMA channel bit table:
  `01, 02, 04, 08, 10, 20, 40`.
- `C0:AE1D-C0:AE25` is the B-bus register selection table used by
  `DO_BATTLEBG_DMA`.
- `C0:AE26-C0:AE33` are the two source descriptor templates copied into
  `$3C32` or `$3C3C`.
- `C0:AE34` clears one pending DMA bit in `$001F` by indexing the inverse mask
  table at `C0:AE44`.
- `C0:AE44-C0:AE4B` is the inverse DMA mask table:
  `FE, FD, FB, F7, EF, DF, BF, 7F`.

## Practical decomp notes

This cluster is a useful boundary for a future native engine: the music layer
is already reduced to high-level commands (`load pack`, `stop`, `play track`,
`queue sfx`), while the battle-background layer describes a descriptor ABI
that can be lifted as "prepare transfer list, then mark DMA channel active."
The exact visual meaning of the four cached battle-background streams still
needs caller-side naming, but their storage, countdown, and descriptor output
shape are now explicit.

## Working Names

- `C0:AB06` = `LoadSpc700DataStream`
- `C0:ABA8` = `WaitForSpcReadyAndResetApuPorts`
- `C0:ABBD` = `SendApuPort0CommandByte`
- `C0:ABC6` = `StopMusicAndLatchNoTrack`
- `C0:ABE0` = `QueueSoundEffectOrPlayApuPort3Cue`
- `C0:AC0C` = `ToggleAndSendApuPort1Command`
- `C0:AC20` = `ReadApuPort0Byte`
- `C0:AC3A` = `SendApuPort2Byte`
- `C0:AC43` = `SelectAndEmitBattleBgTransferDescriptors`
- `C0:AD56` = `ExpandBattleBgTransferDescriptorStream`
- `C0:AD8A` = `Event786_CurrentSlotOrbitScript`
- `C0:AD9F` = `WriteVramAddressFrom3B3C`
- `C0:ADB2` = `ConfigureBattleBgDmaChannel`
- `C0:AE16` = `DmaChannelFlagTable`
- `C0:AE1D` = `BattleBgDmaBbusRegisterTable`
- `C0:AE26` = `BattleBgDmaSourceDescriptorTemplates`
- `C0:AE34` = `ClearPendingDmaChannelBit`
- `C0:AE44` = `InverseDmaChannelMaskTable`
