# C3 window and battle visual unknown tail E7E3-F981

## Reference context

This pass covers the C3 `unknown/C3/...` starts that the corrected progress audit still found without hand-written note coverage:

- `C3:E7E3` `unknown/C3/C3E7E3.asm`
- `C3:F5F9` `unknown/C3/C3F5F9.asm`
- `C3:F67D` `unknown/C3/C3F67D.asm`
- `C3:F705` `unknown/C3/C3F705.asm`
- `C3:F7FB` `unknown/C3/C3F7FB.asm`
- `C3:F981` `unknown/C3/C3F981.asm`

They are not one subsystem. `C3:E7E3` belongs to window record cleanup near the text/window helpers; `C3:F5F9-F7FB` belongs to VRAM/tile transfer helpers near the title/battle visual tail; `C3:F981` is an internal battle visual/effect token dispatcher used by the neighboring `C3:FAC9` wrapper.

## `C3:E7E3` - clear a window registration chain

Direct xrefs:

- `C1:1388` calls `C3:E7E3` with the active/focused window id from `$8958`.
- `C3:E521` calls `C3:E7E3` inside the larger C3 window record manipulation path.

The routine exits immediately for input `#$FFFF`. Otherwise it maps the input window id through `$88E4`, resolves the window-stat record at `$8650 + C0:8FF7(selector #$0052)`, and checks record offset `$2B`. If that offset is not `#$FFFF`, it traverses a linked allocation/copy chain rooted in `$89D4 + C0:8FF7(selector #$002D)`, clearing each node's first word until the next pointer is `#$FFFF`.

After clearing the chain, it resets the window record's offsets `$2B/$2D/$2F` to `#$FFFF` and writes `1` to offsets `$31/$33`.

This lines up with the nearby C2 title/name buffer helper notes: `$8650` is the window statistics table, `$88E4` maps window ids, and `$89D4` is the table used for registered tile-copy slots.

## `C3:F705` transfer family

The core public helper is `C3:F705`. It receives:

- source pointer in the caller's direct-page `$28/$2A`
- an input low-word in `A`
- an input column/offset in `X`

It stores transfer state in `$9F7A-$9F88`, reads a two-byte header from the source stream, and then delegates to local row upload helpers. Every actual row upload in the family reaches `C0:8616` with `A = 0`, which the C0 manifest names `QueueVramTransfer_FromDpSource`.

`C4:8B08` calls `C3:F705` after setting source `$7F:0000`, `X = #$024C`, and `A = #$0328`. That corroborates this as a VRAM-facing tile/block transfer helper, not a pure decoder.

`C3:F5F9` is the linear row queue helper. It uses `$9F7A/$9F7C/$9F80/$9F82/$9F84/$9F86/$9F88` as transfer state, computes VRAM destination rows from `$9F84 + row*0x20 + column`, and queues each row via `C0:8616`.

`C3:F67D` is the wrapped row queue helper. It performs the same `C0:8616` queueing but advances the source pointer and toggles the `$0400` destination bit when the column crosses row/page boundaries.

`C3:F7FB` is a fixed-source wrapper:

```text
C3:F803  lda #$EB3D
C3:F806  sta $0E
C3:F808  lda #$00EF
C3:F80B  sta $10
C3:F80D  ldx #$001F
C3:F810  lda #$039E
C3:F813  jsl $C3F705
```

The hard-coded source is `EF:EB3D`; the helper then returns. No direct control-flow caller has been found yet, so this remains a fixed transfer preset awaiting a caller-side identity.

## `C3:F981` - battle visual/effect token dispatcher

`tools/find_xrefs.py C3F981` finds the direct local callers inside `C3:FAC9`.

`C3:F981` dispatches an input token in ranges:

- tokens `< #$0023`: call `C2:E116(token)`
- tokens `#$0023..#$002D`: use the 3-byte record table at `C3:F951`, call `C2:DE0F`, pass table fields through `C0:B01A` and `C0:B039`, then call `C4:A67E(5, 7)`
- tokens `#$002E..#$0030`: write fixed values into `$AD92` or `$AD94`, or no-op
- tokens `#$0031..#$0035`: use the 3-byte record table at `C3:F972`, then take the same C2/C0/C4 visual-effect path

Existing C2 battle background notes already flagged `C3:F9A2` and `C3:FA4A` as important in the battle background/effect corridor. This pass ties those branch bodies back to the wrapper entry at `C3:F981`. The later source-contract pass closes the extraction caveat: keep the `C3:F951` and `C3:F972` 3-byte colour-token tables as explicit data next to the dispatcher rather than folding them into per-token branches.

`C3:FAC9` chooses which token to dispatch from battle actor/record state at `$A972 + $0E/$0F`, special-casing byte `$0F == #$D5`, then returns `0` or `1` to indicate which path it took.

`C3:FB09` is a final tiny actor visual-flag helper. It reads the alternate
current battle actor record pointer at `$A970`, returns `1` when actor byte
`+$0E` is nonzero, and returns `0` otherwise. The legacy reference marks
`C3:FB1F` as `DATA_C3FB1F`, immediately after this helper's `RTL`, so
`C3:FB09..C3:FB1F` is the closed source slice and the following bytes return
to data/frontier material.

## Working Names

- `C3:E7E3` = `ClearWindowRegisteredCopyChain`
- `C3:F5F9` = `QueueVisualTileRowsLinear`
- `C3:F67D` = `QueueVisualTileRowsWrapped`
- `C3:F705` = `QueueVisualTileBlockFromStream`
- `C3:F7FB` = `QueueFixedEfEb3dVisualTileBlock`
- `C3:F981` = `DispatchBattleVisualEffectToken`
- `C3:FAC9` = `DispatchBattleActorVisualEffectToken`
- `C3:FB09` = `CheckCurrentBattleActorVisualFlag`
- `C3:FB1F` = `DATA_C3FB1F`

## Remaining questions

- `C3:F7FB` still needs its actual caller or dispatch-table entry. Its payload is clear, but not the gameplay-facing event that needs it.
- The exact gameplay-facing meaning of each `C3:F981` token still belongs to the battle action/effect caller pass, but the source-level dispatcher and table layout are now pinned.
- `C3:F67D` decodes awkwardly if linear disassembly does not recover the accumulator-width transition after `C0:8616`; the control-flow shape is still pinned by the surrounding `C3:F705` caller and the row/page wrap branches.
