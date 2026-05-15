# PSI Magnet Drain Amount

`PSI_MAGNET_ALPHA` and `PSI_MAGNET_OMEGA` are action-table entries that route
to the C2 battle action handlers:

```asm
; src/data/battle/action_table.asm
; PSI_MAGNET_ALPHA
.DWORD BTLACT_MAGNET_A

; PSI_MAGNET_OMEGA
.DWORD BTLACT_MAGNET_O
```

The useful readable source is:

```asm
; refs/ebsrc-main/ebsrc-main/src/battle/actions/magnet_alpha.asm
BTLACT_MAGNET_A:
    ...
    LDA #4
    JSR RAND_LIMIT
    TAX
    STX @LOCAL02
    LDA #4
    JSR RAND_LIMIT
    STA @VIRTUAL02
    LDX @LOCAL02
    TXA
    CLC
    ADC @VIRTUAL02
    STA @VIRTUAL02
    INC @VIRTUAL02
    INC @VIRTUAL02
    ...
```

So the drain amount is not a single constant. It is:

```text
RAND_LIMIT(4) + RAND_LIMIT(4) + 2
```

Assuming `RAND_LIMIT(n)` returns `0..n-1`, vanilla PSI Magnet drains `2..8` PP,
with a triangular distribution, then caps the amount to the target's available
PP.

The local C2 scaffold maps this to `C2:9F5E`:

```asm
; src/c2/c2_9f57_run_asleep_status_wrapper_action.asm
BTLACT_MAGNET_A:
C29F5E_RunHpSuckerStylePpDrainAction = BTLACT_MAGNET_A
    ...
C29F7E_RunAsleepStatusWrapperAction_L9F7E:
    lda.w #$0004
    jsr C26A2D_RollRandomThreshold
    ...
    lda.w #$0004
    jsr C26A2D_RollRandomThreshold
    ...
    inc $02
    inc $02
```

ROM/SNES addresses to look at in the vanilla routine:

- first roll limit immediate: `C2:9F7E` instruction, operand starts at
  `C2:9F7F`, vanilla `$0004`
- second roll limit immediate: `C2:9F87` instruction, operand starts at
  `C2:9F88`, vanilla `$0004`
- base `+2`: two `INC $02` instructions around `C2:9F97` and `C2:9F99`

`BTLACT_MAGNET_O` is mostly a wrapper; it calls `BTLACT_MAGNET_A` for each valid
target, so alpha and omega share the same per-target drain amount.

## Phase 2 Trace-Oracles

PSI Magnet should be treated as a transfer contract, not just PP loss. The
per-target trace should capture the two `RAND_LIMIT(4)` rolls, the `+2` base,
the cap against target available PP, the target PP decrease, the user PP
recovery side, and the amount-bearing battle text.

This is the comparison point for the late PP-reduction action at `C2:8E42`.
That sibling is loss-only: it should trace amount selection, cap, and PP-loss
text, but should not inherit Magnet's recovery-side wording unless local source
evidence proves a transfer.

Current controlled runtime evidence now reaches the middle of that proof lane.
The `bash-row-psi-magnet-force-reducer` fixture plus the
`resource-magnet-transfer-pp32` runner profile seeds the selected row with `32`
PP and the active row with `0/32` PP. The reviewed manual capture observes
`C2:9F5E -> C2:721D -> C2:7191`: amount payload `5`, selected target PP
`32 -> 27`, and active row PP `0 -> 5`. This proves the local reducer/recovery
mechanics under controlled state, but it is still not a natural vanilla PSI
Magnet promotion because the target PP was seeded by the runner.

The generated comparison note is
`notes/c2-resource-amount-controlled-comparison.md`.

Natural vanilla evidence now covers the amount-bearing target-loss half of the
same contract. The Stonehenge Base Mook save-state capture
`stonehenge-mook-paula-psi-magnet-slot1/resource-neutral` observes Paula's
queued PSI Magnet with no input after load. The route hits
`C2:9F5E -> C2:721D -> C2:7191`, carries amount payload `6`, and reduces the
selected Mook PP target from `0x02BC` to `0x02B6`. The same run calls
`C2:7191` for Paula with requested PP target `0x00D9`, but Paula's PP is
already capped at `0x00D3`, so the visible caster-side delta is `0`. This is
enough to treat natural PSI Magnet as proven for nonzero target PP loss and
capped caster recovery routing; a non-full caster save remains useful only to
show a visible positive caster PP delta.

Natural PP-reduction evidence now covers the loss-only comparison. The Desert
Gold Mine Mad Duck save-state capture `mad-duck-pp-loss-slot1/resource-neutral`
observes the enemy PP-loss action with no input after load. The route hits
`C2:8E42 -> C2:721D -> C2:7191`, rolls amount `4`, and reduces the selected
party row PP target from `0x0043` to `0x003F`. The active enemy row remains
`0`, and there is no caster-side recovery call after the reducer, which proves
that row `95` should not inherit PSI Magnet's transfer wording.
