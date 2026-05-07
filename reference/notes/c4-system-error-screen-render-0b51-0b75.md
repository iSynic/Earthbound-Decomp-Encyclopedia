# C4 system error screen render helpers (`C4:0B51-C4:0B75`)

## Reference context

The next two C4 unknown includes after the early script-pointer table are:

- `unknown/C4/C40B51.asm`
- `unknown/C4/C40B75.asm`

They sit before `data/map/footstep_sound_table.asm`, `data/unknown/C40BE8.asm`, and the early event/data include run. Direct callers come from the bank C3 system-screen region:

- `C3:0100` calls `C4:0B51`, decompresses two payloads through `C4:1A9E`, then calls `C4:0B75`
- `C3:0142` has the same structure with a different pair of payload pointers

The bank C3 reference map places this region at `system/display_antipiracy_screen.asm` and `system/display_faulty_gamepak_screen.asm`, which fits the shape of both routines.

## Shared display setup

`C4:0B51` is the common setup helper for these system error screens:

- calls `C0:ABC6` (`StopMusicAndLatchNoTrack`)
- calls `C0:8D79` (`Update_BgModeRegisterFromQueue`) with `A = 1`
- calls `C0:8E1C` (`Update_Bg3ScreenBaseRegistersFromQueue`) with `A = 0`, `X = $4000`, `Y = 0`
- stores byte `$04` into `$001A`
- calls `C0:8726`, which forces display shadow `$000D = $80`, waits for the frame flag at `$002B`, disables HDMA through `$420C`, and returns in 16-bit mode

So `C4:0B51` is not a generic event helper. It blanks/stabilizes display state, stops music, and stages the background mode/screen-base state used by the terminal system-screen render.

## Caller-side payload split

After `C4:0B51`, each C3 system-screen routine decompresses two compressed payloads through `C4:1A9E`:

| Caller | First payload | First destination | Second payload | Second destination |
| --- | --- | --- | --- | --- |
| `C3:0100` | `D8:F20D` | `7F:0000` | `D8:F05E` | `7F:4000` |
| `C3:0142` | `D8:F5C4` | `7F:0000` | `D8:F3C6` | `7F:4000` |

Existing landing-display notes already identify `C4:1A9E` as the generic compressed-data expander used for asset payloads. Here it is reused for the anti-piracy and faulty-Game-Pak screens rather than for the landing profile display path.

## Render and halt

`C4:0B75` consumes those two decompressed WRAM blocks:

- queues a VRAM transfer from `7F:0000` to target `$0000`, size `$0A00`, through `C0:8616`
- queues a VRAM transfer from `7F:4000` to target `$4000`, size `$0800`, through `C0:8616`
- copies a short word block from `D8:F3BE` to `$0200` through `C0:8ED2`
- writes byte `$18` to `$0030` through `C0:856B`
- calls `C0:87CE` with `A = 1`, `X = 1`, `Y = 0`
- falls into the infinite halt loop at `C4:0BD2`

The helper does not return to the C3 caller in normal execution. That is the expected behavior for both a piracy warning and a faulty hardware warning: build the screen, settle display state, then halt permanently.

## Working Names

- `C3:0100` = `DisplayAntiPiracyScreen`
- `C3:0142` = `DisplayFaultyGamePakScreen`
- `C4:0B51` = `SetupSystemErrorScreenDisplay`
- `C4:0B75` = `RenderSystemErrorScreenAndHalt`
- `C4:0BD2` = `SystemErrorScreenHaltLoop`
- `C4:1A9E` = `DecompressAssetToLongDest`

## Remaining questions

- The shared palette/control block at `D8:F3BE -> $0200` is still only identified structurally. It should be compared against the two rendered system screens if we later build an asset extractor for these payloads.
- `C0:8726` is now clearly part of the blank/wait/HDMA-off entry sequence, but it still belongs to a C0 display-control naming pass rather than this C4 note.
