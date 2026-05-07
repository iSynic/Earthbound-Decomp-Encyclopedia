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
