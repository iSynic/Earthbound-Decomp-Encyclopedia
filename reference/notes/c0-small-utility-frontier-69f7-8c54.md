# C0 Small Utility Frontier `C0:69F7-C0:8C54`

This note clears the next audit-frontier routines whose bodies are small wrappers, reset helpers, stream helpers, or display/input queue bridges.

Covered starts:

- `C0:69F7`
- `C0:6E1A`
- `C0:73C0`
- `C0:778A`
- `C0:7A31`
- `C0:83B8`
- `C0:83C1`
- `C0:8496`
- `C0:8529`
- `C0:8573`
- `C0:878B`
- `C0:87AB`
- `C0:888B`
- `C0:88A5`
- `C0:8C53`
- `C0:8C54`

## Decoder Tooling Note

This pass expanded `tools/decode_snippet.py` with common indexed direct-page opcodes and `EOR #imm`. That matters for the input and frame-wait area around `C0:8496-C0:88A5`, where the decoder previously drifted on opcodes such as `B5`, `95`, `D5`, `D6`, `74`, and `49`.

## Music/Transition Wrappers

`C0:69F7` is a current-position music-track wrapper around `C0:68F4`:

- loads current player position from `$9877/$987B`
- calls `C0:68F4`
- returns `$5DD6`, now strong as the current map music track

Direct caller:

- `C1:8428`

`C0:6A07` is the sibling wrapper already referenced in older movement notes.
It performs the same current-position `C0:68F4` call, then calls
`C4:FBBD ChangeMusic($5DD6)`.

Direct callers:

- `C0:3D21`
- `C2:6542`
- `EF:1016`

## Working Names

- `C0:69F7` -> `Get_CurrentPositionMusicTrack`
- `C0:6A07` -> `Apply_CurrentPositionMusicTrack`

The focused source follow-up lives in
`notes/c0-current-position-music-refresh-c068f4-c069af.md`.

## Staged Movement Reset Helper

`C0:6E1A` is the missing reset sibling near the staged movement callbacks:

- `$5DC4 = #$FFFF`
- clears `$9883`
- clears `$5D56`
- clears `$5DBA`

No direct call site was found, but there is a raw pointer hit. This should be treated as a callback-compatible staged-motion reset helper, adjacent to `C0:6E2C` and `C0:6E4A`.

## Working Names

- `C0:6E1A` -> `Reset_StagedMovementState`

## Boundary Trigger Watcher

`C0:73C0` is called from the normal movement path after accepted movement:

- `C0:4711`
- `C0:4728`

The caller chooses slot `0` when `$0002 & 1 == 0` and `$5E3C != 0`, or slot `1` when `$0002 & 1 != 0` and `$5E4A != 0`.

`C0:73C0` treats each selected entry as a small rectangular range record rooted at:

```text
$00  active/type word
+$02  min X
+$04  min Y
+$06  max X
+$08  max Y
+$0A  queued pointer low
+$0C  queued pointer bank/high companion
```

It tests the current player position `$9877/$987B` against that rectangle. When the active/inclusion test says the boundary condition has been crossed, it clears the active word, enqueues queue type `#$0009` through `C0:64E3`, and clears `$98BD[index]`.

## Working Names

- `C0:73C0` -> `Check_MovementBoundaryTrigger`

## Event-Driven Current-Slot Orbit/Offset Helper

`C0:778A` is called from `EVENT_786` via:

```asm
EVENT_EX_CALLROUTINE $1, UNKNOWN_C0778A
```

It updates the current slot `$1A42` relative to current player position:

- if `$10B6[$9889] & #$C000` is set, writes `#$FFFF` to `$10F2[current_slot]`
- otherwise calls `C4:1FFF` with `$9F6D` and `X=#$3000`
- uses returned `$06/$08` to offset `$0B8E[current_slot]` from `$9877`
- computes `$0BCA[current_slot]` from `$987B - 8 + C0:925B($06, #$0A)`
- advances `$9F6D += #$0300`
- clears `$10F2[current_slot]`

## Working Names

- `C0:778A` -> `Update_CurrentSlotOrbitOffsetFromLeader`

## Overlay/Display Flag Helper

`C0:7A31` is a tiny helper called from `C4:F417`.

If caller `X` has bit `#$0080`, it ORs `#$4000` into `$2E7A[slot]`, where the slot is passed in `A`. This matches the existing `$2E7A` model as a runtime overlay/display enable word.

## Working Names

- `C0:7A31` -> `Set_SlotOverlayFlag4000IfRequested`

## Input Stream And Recording Helpers

`C0:83B8` clears `$007B`, disabling the small input/script stream state. Direct caller:

- `EF:EA0F`

`C0:83C1` initializes the input recording stream:

- `$0E/$10 -> $0085/$0087` destination pointer
- `$0065 -> $008B` last-sample word
- `$0089 = 1` run length
- sets `$007B` bit `#$8000`

`C0:83E3` was already documented as the matching playback installer, using bit `#$4000` in `$007B`.

## Working Names

- `C0:83B8` -> `Clear_InputPlaybackOrRecordStream`
- `C0:83C1` -> `Start_InputRecordStream`
- `C0:83E3` -> `Install_InputPlaybackStream`
- `C0:841B` -> `Advance_InputPlaybackStream`
- `C0:8456` -> `Advance_InputRecordStream`

## Frame Input Poller

`C0:8496` is the input poller reached by the frame wait path at `C0:8756`.

It:

- waits until `$4212` indicates a safe polling moment
- advances the playback stream through `C0:841B`
- advances the recording stream through `C0:8456`
- debounces three word families rooted at `$65`, `$69`, and `$6D`
- uses `$71/$73/$75` as small repeat/hold timers
- merges alternate input words back into the primary families unless `$436C` is set
- increments `$0A34` when `$6D` is nonzero

## Working Names

- `C0:8496` -> `Poll_FrameInputAndStreams`

## Transfer Queue Helpers

`C0:8529` copies a caller-described block into RAM and ORs a flag into `$0030`.

Record shape from `[$0E]`:

```text
+$00  count/flags, low 9 bits used as byte/word count
+$01  flag bit source, shifted right and ORed into $0030
+$02  source pointer low
+$04  source pointer bank/high companion
+$06  destination address
```

No direct call was found, which suggests this is table or script-dispatch reached.

`C0:8573` iterates a descriptor list at `$0E/$10`; each record contributes `$91/$93/$95/$97` and is handed to `C0:865F`. `C0:865F` either appends an 8-byte DMA descriptor to the `$0400` queue or, when `$0D` is negative, performs an immediate DMA path through `$431x`, `$2115/$2116`, and `$420B`.

## Working Names

- `C0:8529` -> `Copy_RecordBlockAndSetTransferFlag`
- `C0:8573` -> `Submit_TransferDescriptorList`
- `C0:865F` -> `Submit_TransferDescriptorOrImmediateDma`

## Frame Wait And Display Timing Helpers

`C0:878B` takes a count in `A`, increments `$002C`, and calls `C0:8756` once per count. This is a counted frame-wait/front-end helper.

Direct callers:

- `C0:8805`
- `C0:8846`

`C0:87AB` writes `$0010` from the inverse high nibble of `$000D` combined with caller low bits. It is used by the small timing loops at `C0:87CE` and `C0:8814`.

Direct callers:

- `C0:87A7`
- `C0:8800`
- `C0:8841`

`C0:888B` loops while `$0028` is nonzero, running:

- `C0:88B1`
- `C0:8B26`
- `C0:8756`

Direct caller:

- `C4:C459`

`C0:88A5` swaps or sets the low-byte flag at `$000B`, returning the previous value.

Direct callers:

- `C2:F8FE`
- `C4:AF2C`
- `C4:D459`
- `C4:D54A`

## Working Names

- `C0:8756` -> `Wait_OneFrameAndPollInput`
- `C0:878B` -> `Wait_Frames_CountA`
- `C0:886C` -> `Set_DisplayWaitCounter`
- `C0:887A` -> `Set_NegatedDisplayWaitCounter`
- `C0:87AB` -> `Update_DisplayNibble10From0D`
- `C0:888B` -> `Run_DisplayWaitLoopUntilCounterClear`
- `C0:88A5` -> `Swap_DisplayFlag0B`

## Display Queue No-op / Wrapper Pair

`C0:8C53` is a bare `RTS`, used by four local producer paths:

- `C0:8B99`
- `C0:8BC9`
- `C0:8BF9`
- `C0:8C29`

`C0:8C54` is a far-call wrapper around the already-documented `C0:8C58` display-record enqueue helper.

## Working Names

- `C0:8C53` -> `DisplayQueue_NoOpHook`
- `C0:8C54` -> `Enqueue_DisplayRecord_FarWrapper`

## Open Edges

- `C0:8529` and `C0:8573` need caller-side proof before their record formats get final names.
- The exact gameplay identity of the `C0:778A` orbit/offset behavior is event-specific; `EVENT_786` is the local script anchor, but the visible object identity still needs script context.
- The display timing words `$000D/$0010/$0028/$002C` are locally coherent as timing/display globals, but final names should wait for a broader `8756-88B1` pass.
