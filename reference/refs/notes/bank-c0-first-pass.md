# Bank C0 First-Pass Disassembly

This is a recursive first-pass disassembly rooted at the reset and interrupt vector trampolines that live in the canonical `C0` ROM mirror.

## Seed Entry Points

- `ResetVector_008141` at `C0:8141` with assumed state `E1 M8 X8 C?`
- `NativeNMI_008147` at `C0:8147` with assumed state `E0 M8 X8 C?`
- `NativeIRQ_00814B` at `C0:814B` with assumed state `E0 M8 X8 C?`

## Analysis Roots

- `Probe_InteractableAlongFacing` at `C0:41E3` with assumed state `E0 M16 X16 C?`
- `Resolve_InteractableAlongFacingTarget` at `C0:4279` with assumed state `E0 M16 X16 C?`
- `Prepare_Class1ActorInteraction` at `C0:42C2` with assumed state `E0 M16 X16 C?`
- `Probe_FrontInteractionFacing` at `C0:42EF` with assumed state `E0 M16 X16 C?`
- `Resolve_InteractionFacingRotation` at `C0:43BC` with assumed state `E0 M16 X16 C?`
- `Resolve_FrontInteractionTarget` at `C0:4452` with assumed state `E0 M16 X16 C?`
- `Reset_StagedMovementQueue` at `C0:64D4` with assumed state `E0 M16 X16 C?`
- `Enqueue_StagedMovementQueueEntry` at `C0:64E3` with assumed state `E0 M16 X16 C?`
- `Peek_StagedMovementQueueType` at `C0:6537` with assumed state `E0 M16 X16 C?`
- `Peek_StagedMovementQueuePayload` at `C0:654E` with assumed state `E0 M16 X16 C?`
- `Push_PendingPair5E36` at `C0:6578` with assumed state `E0 M16 X16 C?`
- `Flush_PendingPair5E36` at `C0:65A3` with assumed state `E0 M16 X16 C?`
- `Probe_FrontType6DoorCandidate` at `C0:65C2` with assumed state `E0 M16 X16 C?`
- `MovementTriggerType0_QueueDoorDestination` at `C0:6A1B` with assumed state `E0 M16 X16 C?`
- `MovementTriggerType5Or7_NoOp` at `C0:6A8B` with assumed state `E0 M16 X16 C?`
- `MovementTriggerType6_NoOp` at `C0:6A8E` with assumed state `E0 M16 X16 C?`
- `MovementTriggerType1_SetState07Or08` at `C0:6A91` with assumed state `E0 M16 X16 C?`
- `MovementTriggerType2_QueueDoorTransition` at `C0:6ACA` with assumed state `E0 M16 X16 C?`
- `TimerCallback_CommitStagedPosition_State0C` at `C0:6E2C` with assumed state `E0 M16 X16 C?`
- `TimerCallback_CommitStagedPosition_ClearMotion` at `C0:6E4A` with assumed state `E0 M16 X16 C?`
- `MovementTriggerType3_QueueOffsetStep` at `C0:6E6E` with assumed state `E0 M16 X16 C?`
- `TimerCallback_WaitForStagedY_State0D` at `C0:6F82` with assumed state `E0 M16 X16 C?`
- `TimerCallback_WaitForStagedY_ClearMotion` at `C0:6FED` with assumed state `E0 M16 X16 C?`
- `Select_StagedMovementFacing` at `C0:705F` with assumed state `E0 M16 X16 C?`
- `Queue_StagedMovementFromGridCoords` at `C0:70CB` with assumed state `E0 M16 X16 C?`
- `Lookup_MovementTriggerType` at `C0:7477` with assumed state `E0 M16 X16 C?`
- `Dispatch_MovementHelperFromLookup` at `C0:7526` with assumed state `E0 M16 X16 C?`
- `Process_StagedMovementQueueEntry` at `C0:75DD` with assumed state `E0 M16 X16 C?`
- `NMI_ServiceAudioQueue` at `C0:8501` with assumed state `E0 M8 X8 C?`
- `Frame_CallbackDispatcher` at `C0:8518` with assumed state `E0 M16 X16 C?`
- `Frame_CallbackReturn` at `C0:851B` with assumed state `E0 M16 X16 C?`
- `Set_FrameCallbackPtr` at `C0:851C` with assumed state `E0 M16 X16 C?`
- `Reset_FrameCallbackToDefault` at `C0:8522` with assumed state `E0 M16 X16 C?`
- `Dispatch_DelayedActionTarget` at `C0:9279` with assumed state `E0 M16 X16 C?`
- `Init_DelayedActionPools` at `C0:927C` with assumed state `E0 M16 X16 C?`
- `Init_DelayedActionState` at `C0:9321` with assumed state `E0 M16 X16 C?`
- `Process_ActiveTaskSlots` at `C0:94AA` with assumed state `E0 M16 X16 C?`
- `Process_TaskSlotRecordChain` at `C0:94D0` with assumed state `E0 M16 X16 C?`
- `Alloc_TaskSlotOrFail` at `C0:9C02` with assumed state `E0 M16 X16 C?`
- `Release_TaskSlotByIndex` at `C0:9C35` with assumed state `E0 M16 X16 C?`
- `Release_TaskSlot_Core` at `C0:9C3B` with assumed state `E0 M16 X16 C?`
- `Link_TaskSlotIntoActiveList` at `C0:9C57` with assumed state `E0 M16 X16 C?`
- `Detach_TaskSlotLink` at `C0:9C73` with assumed state `E0 M16 X16 C?`
- `Push_TaskSlotToFreeList` at `C0:9C8F` with assumed state `E0 M16 X16 C?`
- `Restore_TaskRecordChain` at `C0:9C99` with assumed state `E0 M16 X16 C?`
- `Find_TaskSlotPredecessor` at `C0:9CB5` with assumed state `E0 M16 X16 C?`
- `Pop_TaskRecordFromFreeList` at `C0:9D03` with assumed state `E0 M16 X16 C?`
- `Push_TaskRecordToFreeList` at `C0:9D12` with assumed state `E0 M16 X16 C?`
- `Unlink_TaskRecordFromSlotChain` at `C0:9D1F` with assumed state `E0 M16 X16 C?`
- `Find_TaskRecordPredecessor` at `C0:9D3E` with assumed state `E0 M16 X16 C?`
- `Init_TaskRecordDefaults` at `C0:9DA1` with assumed state `E0 M16 X16 C?`
- `Dispatch_ActiveTaskSlots` at `C0:DB0F` with assumed state `E0 M16 X16 C?`
- `Queue_DelayedActionTimer` at `C0:DBE6` with assumed state `E0 M16 X16 C?`
- `Clear_DelayedActionTimerSlot` at `C0:DC38` with assumed state `E0 M16 X16 C?`
- `FrameCallback_ProcessDelayedActions` at `C0:DC4E` with assumed state `E0 M16 X16 C?`
- `FrameCallback_ProcessCommandStream` at `C0:F41E` with assumed state `E0 M16 X16 C?`

## Listing

```asm
Probe_InteractableAlongFacing:
C0:41E3  C2 31        rep #$31                ; E0 M16 X16 C?
C0:41E5  0B           phd                     ; E0 M16 X16 C?
C0:41E6  7B           tdc                     ; E0 M16 X16 C?
C0:41E7  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:41EA  5B           tcd                     ; E0 M16 X16 C?
C0:41EB  AD 7F 98     lda $987F               ; E0 M16 X16 C?
C0:41EE  29 FE FF     and #$FFFE              ; E0 M16 X16 C?
C0:41F1  A8           tay                     ; E0 M16 X16 C?
C0:41F2  84 10        sty $10                 ; E0 M16 X16 C?
C0:41F4  BB           tyx                     ; E0 M16 X16 C?
C0:41F5  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:41F7  8A           txa                     ; E0 M16 X16 C?
C0:41F8  20 16 41     jsr $4116               ; E0 M16 X16 C?
C0:41FB  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:41FE  F0 0A        beq $420A               ; E0 M16 X16 C?
C0:4200  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:4203  F0 05        beq $420A               ; E0 M16 X16 C?
C0:4205  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4207  8A           txa                     ; E0 M16 X16 C?
C0:4208  80 6D        bra $4277               ; E0 M16 X16 C?
Code_C0420A:
C0:420A  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:420C  8A           txa                     ; E0 M16 X16 C?
C0:420D  1A           inc a                   ; E0 M16 X16 C?
C0:420E  1A           inc a                   ; E0 M16 X16 C?
C0:420F  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:4212  AA           tax                     ; E0 M16 X16 C?
C0:4213  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:4215  8E 7F 98     stx $987F               ; E0 M16 X16 C?
C0:4218  8A           txa                     ; E0 M16 X16 C?
C0:4219  20 16 41     jsr $4116               ; E0 M16 X16 C?
C0:421C  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:421F  F0 0A        beq $422B               ; E0 M16 X16 C?
C0:4221  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:4224  F0 05        beq $422B               ; E0 M16 X16 C?
C0:4226  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4228  8A           txa                     ; E0 M16 X16 C?
C0:4229  80 4C        bra $4277               ; E0 M16 X16 C?
Code_C0422B:
C0:422B  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:422D  8A           txa                     ; E0 M16 X16 C?
C0:422E  1A           inc a                   ; E0 M16 X16 C?
C0:422F  1A           inc a                   ; E0 M16 X16 C?
C0:4230  1A           inc a                   ; E0 M16 X16 C?
C0:4231  1A           inc a                   ; E0 M16 X16 C?
C0:4232  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:4235  AA           tax                     ; E0 M16 X16 C?
C0:4236  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:4238  8E 7F 98     stx $987F               ; E0 M16 X16 C?
C0:423B  8A           txa                     ; E0 M16 X16 C?
C0:423C  20 16 41     jsr $4116               ; E0 M16 X16 C?
C0:423F  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:4242  F0 0A        beq $424E               ; E0 M16 X16 C?
C0:4244  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:4247  F0 05        beq $424E               ; E0 M16 X16 C?
C0:4249  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:424B  8A           txa                     ; E0 M16 X16 C?
C0:424C  80 29        bra $4277               ; E0 M16 X16 C?
Code_C0424E:
C0:424E  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4250  8A           txa                     ; E0 M16 X16 C?
C0:4251  3A           dec a                   ; E0 M16 X16 C?
C0:4252  3A           dec a                   ; E0 M16 X16 C?
C0:4253  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:4256  AA           tax                     ; E0 M16 X16 C?
C0:4257  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:4259  8E 7F 98     stx $987F               ; E0 M16 X16 C?
C0:425C  8A           txa                     ; E0 M16 X16 C?
C0:425D  20 16 41     jsr $4116               ; E0 M16 X16 C?
C0:4260  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:4263  F0 0A        beq $426F               ; E0 M16 X16 C?
C0:4265  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:4268  F0 05        beq $426F               ; E0 M16 X16 C?
C0:426A  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:426C  8A           txa                     ; E0 M16 X16 C?
C0:426D  80 08        bra $4277               ; E0 M16 X16 C?
Code_C0426F:
C0:426F  A4 10        ldy $10                 ; E0 M16 X16 C?
C0:4271  8C 7F 98     sty $987F               ; E0 M16 X16 C?
C0:4274  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
Code_C04277:
C0:4277  2B           pld                     ; E0 M16 X16 C?
C0:4278  60           rts                     ; E0 M16 X16 C?
Resolve_InteractableAlongFacingTarget:
C0:4279  C2 31        rep #$31                ; E0 M16 X16 C?
C0:427B  0B           phd                     ; E0 M16 X16 C?
C0:427C  7B           tdc                     ; E0 M16 X16 C?
C0:427D  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:4280  5B           tcd                     ; E0 M16 X16 C?
C0:4281  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:4284  8D 62 5D     sta $5D62               ; E0 M16 X16 C?
C0:4287  8D 64 5D     sta $5D64               ; E0 M16 X16 C?
C0:428A  20 E3 41     jsr $41E3               ; E0 M16 X16 C?
C0:428D  85 10        sta $10                 ; E0 M16 X16 C?
C0:428F  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:4292  F0 29        beq $42BD               ; E0 M16 X16 C?
C0:4294  A2 89 98     ldx #$9889              ; E0 M16 X16 C?
C0:4297  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:4299  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:429C  0A           asl a                   ; E0 M16 X16 C?
C0:429D  AA           tax                     ; E0 M16 X16 C?
C0:429E  A5 10        lda $10                 ; E0 M16 X16 C?
C0:42A0  DD           db $DD                 ; E0 M16 X16 C?
Code_C042BD:
C0:42BD  AD 62 5D     lda $5D62               ; E0 M16 X16 C?
C0:42C0  2B           pld                     ; E0 M16 X16 C?
C0:42C1  6B           rtl                     ; E0 M16 X16 C?
Prepare_Class1ActorInteraction:
C0:42C2  C2 31        rep #$31                ; E0 M16 X16 C?
C0:42C4  0B           phd                     ; E0 M16 X16 C?
C0:42C5  48           pha                     ; E0 M16 X16 C?
C0:42C6  7B           tdc                     ; E0 M16 X16 C?
C0:42C7  69 F0 FF     adc #$FFF0              ; E0 M16 X16 C?
C0:42CA  5B           tcd                     ; E0 M16 X16 C?
C0:42CB  68           pla                     ; E0 M16 X16 C?
C0:42CC  AA           tax                     ; E0 M16 X16 C?
C0:42CD  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:42CF  8A           txa                     ; E0 M16 X16 C?
C0:42D0  0A           asl a                   ; E0 M16 X16 C?
C0:42D1  48           pha                     ; E0 M16 X16 C?
C0:42D2  AD 7F 98     lda $987F               ; E0 M16 X16 C?
C0:42D5  0A           asl a                   ; E0 M16 X16 C?
C0:42D6  AA           tax                     ; E0 M16 X16 C?
C0:42D7  BF 68 E1 C3  lda $C3E168,x           ; E0 M16 X16 C?
C0:42DB  FA           plx                     ; E0 M16 X16 C?
C0:42DC  9D F6 2A     sta $2AF6,x             ; E0 M16 X16 C?
C0:42DF  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:42E1  8A           txa                     ; E0 M16 X16 C?
C0:42E2  22 07 99 C0  jsl $C09907             ; E0 M16 X16 C?
C0:42E6  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:42E8  8A           txa                     ; E0 M16 X16 C?
C0:42E9  22 8F A4 C0  jsl $C0A48F             ; E0 M16 X16 C?
C0:42ED  2B           pld                     ; E0 M16 X16 C?
C0:42EE  6B           rtl                     ; E0 M16 X16 C?
Probe_FrontInteractionFacing:
C0:42EF  C2 31        rep #$31                ; E0 M16 X16 C?
C0:42F1  0B           phd                     ; E0 M16 X16 C?
C0:42F2  48           pha                     ; E0 M16 X16 C?
C0:42F3  7B           tdc                     ; E0 M16 X16 C?
C0:42F4  69 E4 FF     adc #$FFE4              ; E0 M16 X16 C?
C0:42F7  5B           tcd                     ; E0 M16 X16 C?
C0:42F8  68           pla                     ; E0 M16 X16 C?
C0:42F9  85 1A        sta $1A                 ; E0 M16 X16 C?
C0:42FB  0A           asl a                   ; E0 M16 X16 C?
C0:42FC  AA           tax                     ; E0 M16 X16 C?
C0:42FD  BF 48 E1 C3  lda $C3E148,x           ; E0 M16 X16 C?
C0:4301  85 18        sta $18                 ; E0 M16 X16 C?
C0:4303  BF 58 E1 C3  lda $C3E158,x           ; E0 M16 X16 C?
C0:4307  85 16        sta $16                 ; E0 M16 X16 C?
C0:4309  AD 77 98     lda $9877               ; E0 M16 X16 C?
C0:430C  18           clc                     ; E0 M16 X16 C?
C0:430D  65 18        adc $18                 ; E0 M16 X16 C0
C0:430F  85 14        sta $14                 ; E0 M16 X16 C?
C0:4311  AD 7B 98     lda $987B               ; E0 M16 X16 C?
C0:4314  18           clc                     ; E0 M16 X16 C?
C0:4315  65 16        adc $16                 ; E0 M16 X16 C0
C0:4317  85 04        sta $04                 ; E0 M16 X16 C?
C0:4319  AD 58 5D     lda $5D58               ; E0 M16 X16 C?
C0:431C  85 12        sta $12                 ; E0 M16 X16 C?
C0:431E  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:4321  8D 58 5D     sta $5D58               ; E0 M16 X16 C?
Code_C04324:
C0:4324  A9 89 98     lda #$9889              ; E0 M16 X16 C?
C0:4327  85 02        sta $02                 ; E0 M16 X16 C?
C0:4329  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:432B  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:432E  A8           tay                     ; E0 M16 X16 C?
C0:432F  A6 04        ldx $04                 ; E0 M16 X16 C?
C0:4331  A5 14        lda $14                 ; E0 M16 X16 C?
C0:4333  22 F6 5F C0  jsl $C05FF6             ; E0 M16 X16 C?
C0:4337  85 10        sta $10                 ; E0 M16 X16 C?
C0:4339  C9 00 80     cmp #$8000              ; E0 M16 X16 C?
C0:433C  B0 0F        bcs $434D               ; E0 M16 X16 C?
C0:433E  0A           asl a                   ; E0 M16 X16 C?
C0:433F  AA           tax                     ; E0 M16 X16 C?
C0:4340  BD 9A 2C     lda $2C9A,x             ; E0 M16 X16 C?
C0:4343  8D 62 5D     sta $5D62               ; E0 M16 X16 C?
C0:4346  A5 10        lda $10                 ; E0 M16 X16 C?
C0:4348  8D 64 5D     sta $5D64               ; E0 M16 X16 C?
C0:434B  80 52        bra $439F               ; E0 M16 X16 C?
Code_C0434D:
C0:434D  A5 1A        lda $1A                 ; E0 M16 X16 C?
C0:434F  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:4351  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:4353  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:4356  A8           tay                     ; E0 M16 X16 C?
C0:4357  A6 04        ldx $04                 ; E0 M16 X16 C?
C0:4359  A5 14        lda $14                 ; E0 M16 X16 C?
C0:435B  22 D7 5C C0  jsl $C05CD7             ; E0 M16 X16 C?
C0:435F  29 82 00     and #$0082              ; E0 M16 X16 C?
C0:4362  C9 82 00     cmp #$0082              ; E0 M16 X16 C?
C0:4365  D0 38        bne $439F               ; E0 M16 X16 C?
C0:4367  A5 18        lda $18                 ; E0 M16 X16 C?
C0:4369  F0 15        beq $4380               ; E0 M16 X16 C?
C0:436B  A5 18        lda $18                 ; E0 M16 X16 C?
C0:436D  29 00 80     and #$8000              ; E0 M16 X16 C?
C0:4370  F0 05        beq $4377               ; E0 M16 X16 C?
C0:4372  A2 F8 FF     ldx #$FFF8              ; E0 M16 X16 C?
C0:4375  80 03        bra $437A               ; E0 M16 X16 C?
Code_C04377:
C0:4377  A2 08 00     ldx #$0008              ; E0 M16 X16 C?
Code_C0437A:
C0:437A  8A           txa                     ; E0 M16 X16 C?
C0:437B  18           clc                     ; E0 M16 X16 C?
C0:437C  65 14        adc $14                 ; E0 M16 X16 C0
C0:437E  85 14        sta $14                 ; E0 M16 X16 C?
Code_C04380:
C0:4380  A5 16        lda $16                 ; E0 M16 X16 C?
C0:4382  F0 A0        beq $4324               ; E0 M16 X16 C?
C0:4384  A5 16        lda $16                 ; E0 M16 X16 C?
C0:4386  29 00 80     and #$8000              ; E0 M16 X16 C?
C0:4389  F0 05        beq $4390               ; E0 M16 X16 C?
C0:438B  A2 F8 FF     ldx #$FFF8              ; E0 M16 X16 C?
C0:438E  80 03        bra $4393               ; E0 M16 X16 C?
Code_C04390:
C0:4390  A2 08 00     ldx #$0008              ; E0 M16 X16 C?
Code_C04393:
C0:4393  86 02        stx $02                 ; E0 M16 X16 C?
C0:4395  A5 04        lda $04                 ; E0 M16 X16 C?
C0:4397  18           clc                     ; E0 M16 X16 C?
C0:4398  65 02        adc $02                 ; E0 M16 X16 C0
C0:439A  85 04        sta $04                 ; E0 M16 X16 C?
C0:439C  4C 24 43     jmp $4324               ; E0 M16 X16 C?
Code_C0439F:
C0:439F  A5 12        lda $12                 ; E0 M16 X16 C?
C0:43A1  8D 58 5D     sta $5D58               ; E0 M16 X16 C?
C0:43A4  AD 62 5D     lda $5D62               ; E0 M16 X16 C?
C0:43A7  F0 08        beq $43B1               ; E0 M16 X16 C?
C0:43A9  AD 62 5D     lda $5D62               ; E0 M16 X16 C?
C0:43AC  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:43AF  D0 06        bne $43B7               ; E0 M16 X16 C?
Code_C043B1:
C0:43B1  A5 1A        lda $1A                 ; E0 M16 X16 C?
C0:43B3  22 C2 65 C0  jsl $C065C2             ; E0 M16 X16 C?
Code_C043B7:
C0:43B7  AD 62 5D     lda $5D62               ; E0 M16 X16 C?
C0:43BA  2B           pld                     ; E0 M16 X16 C?
C0:43BB  60           rts                     ; E0 M16 X16 C?
Resolve_InteractionFacingRotation:
C0:43BC  C2 31        rep #$31                ; E0 M16 X16 C?
C0:43BE  0B           phd                     ; E0 M16 X16 C?
C0:43BF  7B           tdc                     ; E0 M16 X16 C?
C0:43C0  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:43C3  5B           tcd                     ; E0 M16 X16 C?
C0:43C4  AD 7F 98     lda $987F               ; E0 M16 X16 C?
C0:43C7  29 FE FF     and #$FFFE              ; E0 M16 X16 C?
C0:43CA  A8           tay                     ; E0 M16 X16 C?
C0:43CB  84 10        sty $10                 ; E0 M16 X16 C?
C0:43CD  BB           tyx                     ; E0 M16 X16 C?
C0:43CE  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:43D0  8A           txa                     ; E0 M16 X16 C?
C0:43D1  20 EF 42     jsr $42EF               ; E0 M16 X16 C?
C0:43D4  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:43D7  F0 0A        beq $43E3               ; E0 M16 X16 C?
C0:43D9  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:43DC  F0 05        beq $43E3               ; E0 M16 X16 C?
C0:43DE  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:43E0  8A           txa                     ; E0 M16 X16 C?
C0:43E1  80 6D        bra $4450               ; E0 M16 X16 C?
Code_C043E3:
C0:43E3  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:43E5  8A           txa                     ; E0 M16 X16 C?
C0:43E6  1A           inc a                   ; E0 M16 X16 C?
C0:43E7  1A           inc a                   ; E0 M16 X16 C?
C0:43E8  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:43EB  AA           tax                     ; E0 M16 X16 C?
C0:43EC  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:43EE  8E 7F 98     stx $987F               ; E0 M16 X16 C?
C0:43F1  8A           txa                     ; E0 M16 X16 C?
C0:43F2  20 EF 42     jsr $42EF               ; E0 M16 X16 C?
C0:43F5  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:43F8  F0 0A        beq $4404               ; E0 M16 X16 C?
C0:43FA  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:43FD  F0 05        beq $4404               ; E0 M16 X16 C?
C0:43FF  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4401  8A           txa                     ; E0 M16 X16 C?
C0:4402  80 4C        bra $4450               ; E0 M16 X16 C?
Code_C04404:
C0:4404  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4406  8A           txa                     ; E0 M16 X16 C?
C0:4407  1A           inc a                   ; E0 M16 X16 C?
C0:4408  1A           inc a                   ; E0 M16 X16 C?
C0:4409  1A           inc a                   ; E0 M16 X16 C?
C0:440A  1A           inc a                   ; E0 M16 X16 C?
C0:440B  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:440E  AA           tax                     ; E0 M16 X16 C?
C0:440F  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:4411  8E 7F 98     stx $987F               ; E0 M16 X16 C?
C0:4414  8A           txa                     ; E0 M16 X16 C?
C0:4415  20 EF 42     jsr $42EF               ; E0 M16 X16 C?
C0:4418  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:441B  F0 0A        beq $4427               ; E0 M16 X16 C?
C0:441D  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:4420  F0 05        beq $4427               ; E0 M16 X16 C?
C0:4422  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4424  8A           txa                     ; E0 M16 X16 C?
C0:4425  80 29        bra $4450               ; E0 M16 X16 C?
Code_C04427:
C0:4427  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4429  8A           txa                     ; E0 M16 X16 C?
C0:442A  3A           dec a                   ; E0 M16 X16 C?
C0:442B  3A           dec a                   ; E0 M16 X16 C?
C0:442C  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:442F  AA           tax                     ; E0 M16 X16 C?
C0:4430  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:4432  8E 7F 98     stx $987F               ; E0 M16 X16 C?
C0:4435  8A           txa                     ; E0 M16 X16 C?
C0:4436  20 EF 42     jsr $42EF               ; E0 M16 X16 C?
C0:4439  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:443C  F0 0A        beq $4448               ; E0 M16 X16 C?
C0:443E  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:4441  F0 05        beq $4448               ; E0 M16 X16 C?
C0:4443  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:4445  8A           txa                     ; E0 M16 X16 C?
C0:4446  80 08        bra $4450               ; E0 M16 X16 C?
Code_C04448:
C0:4448  A4 10        ldy $10                 ; E0 M16 X16 C?
C0:444A  8C 7F 98     sty $987F               ; E0 M16 X16 C?
C0:444D  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
Code_C04450:
C0:4450  2B           pld                     ; E0 M16 X16 C?
C0:4451  60           rts                     ; E0 M16 X16 C?
Resolve_FrontInteractionTarget:
C0:4452  C2 31        rep #$31                ; E0 M16 X16 C?
C0:4454  0B           phd                     ; E0 M16 X16 C?
C0:4455  7B           tdc                     ; E0 M16 X16 C?
C0:4456  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:4459  5B           tcd                     ; E0 M16 X16 C?
C0:445A  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:445D  8D 62 5D     sta $5D62               ; E0 M16 X16 C?
C0:4460  8D 64 5D     sta $5D64               ; E0 M16 X16 C?
C0:4463  20 BC 43     jsr $43BC               ; E0 M16 X16 C?
C0:4466  85 10        sta $10                 ; E0 M16 X16 C?
C0:4468  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:446B  F0 29        beq $4496               ; E0 M16 X16 C?
C0:446D  A2 89 98     ldx #$9889              ; E0 M16 X16 C?
C0:4470  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:4472  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:4475  0A           asl a                   ; E0 M16 X16 C?
C0:4476  AA           tax                     ; E0 M16 X16 C?
C0:4477  A5 10        lda $10                 ; E0 M16 X16 C?
C0:4479  DD           db $DD                 ; E0 M16 X16 C?
Code_C04496:
C0:4496  AD 62 5D     lda $5D62               ; E0 M16 X16 C?
C0:4499  2B           pld                     ; E0 M16 X16 C?
C0:449A  6B           rtl                     ; E0 M16 X16 C?
Reset_StagedMovementQueue:
C0:64D4  C2 31        rep #$31                ; E0 M16 X16 C?
C0:64D6  9C 04 5E     stz $5E04               ; E0 M16 X16 C?
C0:64D9  9C 02 5E     stz $5E02               ; E0 M16 X16 C?
C0:64DC  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:64DF  8D C0 5D     sta $5DC0               ; E0 M16 X16 C?
C0:64E2  6B           rtl                     ; E0 M16 X16 C?
Enqueue_StagedMovementQueueEntry:
C0:64E3  C2 31        rep #$31                ; E0 M16 X16 C?
C0:64E5  0B           phd                     ; E0 M16 X16 C?
C0:64E6  48           pha                     ; E0 M16 X16 C?
C0:64E7  7B           tdc                     ; E0 M16 X16 C?
C0:64E8  69 F0 FF     adc #$FFF0              ; E0 M16 X16 C?
C0:64EB  5B           tcd                     ; E0 M16 X16 C?
C0:64EC  68           pla                     ; E0 M16 X16 C?
C0:64ED  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:64EF  A5 1E        lda $1E                 ; E0 M16 X16 C?
C0:64F1  85 06        sta $06                 ; E0 M16 X16 C?
C0:64F3  A5 20        lda $20                 ; E0 M16 X16 C?
C0:64F5  85 08        sta $08                 ; E0 M16 X16 C?
C0:64F7  A5 0E        lda $0E                 ; E0 M16 X16 C?
C0:64F9  CD C0 5D     cmp $5DC0               ; E0 M16 X16 C?
C0:64FC  F0 37        beq $6535               ; E0 M16 X16 C?
C0:64FE  AD 04 5E     lda $5E04               ; E0 M16 X16 C?
C0:6501  85 04        sta $04                 ; E0 M16 X16 C?
C0:6503  0A           asl a                   ; E0 M16 X16 C?
C0:6504  65 04        adc $04                 ; E0 M16 X16 C?
C0:6506  0A           asl a                   ; E0 M16 X16 C?
C0:6507  AA           tax                     ; E0 M16 X16 C?
C0:6508  A5 0E        lda $0E                 ; E0 M16 X16 C?
C0:650A  9D EA 5D     sta $5DEA,x             ; E0 M16 X16 C?
C0:650D  AD 04 5E     lda $5E04               ; E0 M16 X16 C?
C0:6510  85 04        sta $04                 ; E0 M16 X16 C?
C0:6512  0A           asl a                   ; E0 M16 X16 C?
C0:6513  65 04        adc $04                 ; E0 M16 X16 C?
C0:6515  0A           asl a                   ; E0 M16 X16 C?
C0:6516  18           clc                     ; E0 M16 X16 C?
C0:6517  69 EC 5D     adc #$5DEC              ; E0 M16 X16 C0
C0:651A  A8           tay                     ; E0 M16 X16 C?
C0:651B  A5 06        lda $06                 ; E0 M16 X16 C?
C0:651D  99 00 00     sta $0000,y             ; E0 M16 X16 C?
C0:6520  A5 08        lda $08                 ; E0 M16 X16 C?
C0:6522  99 02 00     sta $0002,y             ; E0 M16 X16 C?
C0:6525  AD 04 5E     lda $5E04               ; E0 M16 X16 C?
C0:6528  1A           inc a                   ; E0 M16 X16 C?
C0:6529  29 03 00     and #$0003              ; E0 M16 X16 C?
C0:652C  8D 04 5E     sta $5E04               ; E0 M16 X16 C?
C0:652F  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6532  8D 9A 5D     sta $5D9A               ; E0 M16 X16 C?
Code_C06535:
C0:6535  2B           pld                     ; E0 M16 X16 C?
C0:6536  6B           rtl                     ; E0 M16 X16 C?
Peek_StagedMovementQueueType:
C0:6537  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6539  0B           phd                     ; E0 M16 X16 C?
C0:653A  7B           tdc                     ; E0 M16 X16 C?
C0:653B  69 F2 FF     adc #$FFF2              ; E0 M16 X16 C?
C0:653E  5B           tcd                     ; E0 M16 X16 C?
C0:653F  AD 02 5E     lda $5E02               ; E0 M16 X16 C?
C0:6542  85 04        sta $04                 ; E0 M16 X16 C?
C0:6544  0A           asl a                   ; E0 M16 X16 C?
C0:6545  65 04        adc $04                 ; E0 M16 X16 C?
C0:6547  0A           asl a                   ; E0 M16 X16 C?
C0:6548  AA           tax                     ; E0 M16 X16 C?
C0:6549  BD EA 5D     lda $5DEA,x             ; E0 M16 X16 C?
C0:654C  2B           pld                     ; E0 M16 X16 C?
C0:654D  6B           rtl                     ; E0 M16 X16 C?
Peek_StagedMovementQueuePayload:
C0:654E  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6550  0B           phd                     ; E0 M16 X16 C?
C0:6551  7B           tdc                     ; E0 M16 X16 C?
C0:6552  69 F2 FF     adc #$FFF2              ; E0 M16 X16 C?
C0:6555  5B           tcd                     ; E0 M16 X16 C?
C0:6556  AD 02 5E     lda $5E02               ; E0 M16 X16 C?
C0:6559  85 04        sta $04                 ; E0 M16 X16 C?
C0:655B  0A           asl a                   ; E0 M16 X16 C?
C0:655C  65 04        adc $04                 ; E0 M16 X16 C?
C0:655E  0A           asl a                   ; E0 M16 X16 C?
C0:655F  18           clc                     ; E0 M16 X16 C?
C0:6560  69 EC 5D     adc #$5DEC              ; E0 M16 X16 C0
C0:6563  A8           tay                     ; E0 M16 X16 C?
C0:6564  B9 00 00     lda $0000,y             ; E0 M16 X16 C?
C0:6567  85 06        sta $06                 ; E0 M16 X16 C?
C0:6569  B9 02 00     lda $0002,y             ; E0 M16 X16 C?
C0:656C  85 08        sta $08                 ; E0 M16 X16 C?
C0:656E  A5 06        lda $06                 ; E0 M16 X16 C?
C0:6570  85 14        sta $14                 ; E0 M16 X16 C?
C0:6572  A5 08        lda $08                 ; E0 M16 X16 C?
C0:6574  85 16        sta $16                 ; E0 M16 X16 C?
C0:6576  2B           pld                     ; E0 M16 X16 C?
C0:6577  6B           rtl                     ; E0 M16 X16 C?
Push_PendingPair5E36:
C0:6578  C2 31        rep #$31                ; E0 M16 X16 C?
C0:657A  0B           phd                     ; E0 M16 X16 C?
C0:657B  48           pha                     ; E0 M16 X16 C?
C0:657C  7B           tdc                     ; E0 M16 X16 C?
C0:657D  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:6580  5B           tcd                     ; E0 M16 X16 C?
C0:6581  68           pla                     ; E0 M16 X16 C?
C0:6582  86 10        stx $10                 ; E0 M16 X16 C?
C0:6584  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6586  AD 36 5E     lda $5E36               ; E0 M16 X16 C?
C0:6589  0A           asl a                   ; E0 M16 X16 C?
C0:658A  0A           asl a                   ; E0 M16 X16 C?
C0:658B  AA           tax                     ; E0 M16 X16 C?
C0:658C  A5 0E        lda $0E                 ; E0 M16 X16 C?
C0:658E  9D 06 5E     sta $5E06,x             ; E0 M16 X16 C?
C0:6591  A6 10        ldx $10                 ; E0 M16 X16 C?
C0:6593  DA           phx                     ; E0 M16 X16 C?
C0:6594  AD 36 5E     lda $5E36               ; E0 M16 X16 C?
C0:6597  0A           asl a                   ; E0 M16 X16 C?
C0:6598  0A           asl a                   ; E0 M16 X16 C?
C0:6599  AA           tax                     ; E0 M16 X16 C?
C0:659A  68           pla                     ; E0 M16 X16 C?
C0:659B  9D 08 5E     sta $5E08,x             ; E0 M16 X16 C?
C0:659E  EE 36 5E     inc $5E36               ; E0 M16 X16 C?
C0:65A1  2B           pld                     ; E0 M16 X16 C?
C0:65A2  6B           rtl                     ; E0 M16 X16 C?
Flush_PendingPair5E36:
C0:65A3  C2 31        rep #$31                ; E0 M16 X16 C?
C0:65A5  80 15        bra $65BC               ; E0 M16 X16 C?
Code_C065A7:
C0:65A7  AD 36 5E     lda $5E36               ; E0 M16 X16 C?
C0:65AA  3A           dec a                   ; E0 M16 X16 C?
C0:65AB  8D 36 5E     sta $5E36               ; E0 M16 X16 C?
C0:65AE  0A           asl a                   ; E0 M16 X16 C?
C0:65AF  0A           asl a                   ; E0 M16 X16 C?
C0:65B0  A8           tay                     ; E0 M16 X16 C?
C0:65B1  B9 08 5E     lda $5E08,y             ; E0 M16 X16 C?
C0:65B4  AA           tax                     ; E0 M16 X16 C?
C0:65B5  B9 06 5E     lda $5E06,y             ; E0 M16 X16 C?
C0:65B8  22 07 65 C4  jsl $C46507             ; E0 M16 X16 C?
Code_C065BC:
C0:65BC  AD 36 5E     lda $5E36               ; E0 M16 X16 C?
C0:65BF  D0 E6        bne $65A7               ; E0 M16 X16 C?
C0:65C1  6B           rtl                     ; E0 M16 X16 C?
Probe_FrontType6DoorCandidate:
C0:65C2  C2 31        rep #$31                ; E0 M16 X16 C?
C0:65C4  0B           phd                     ; E0 M16 X16 C?
C0:65C5  48           pha                     ; E0 M16 X16 C?
C0:65C6  7B           tdc                     ; E0 M16 X16 C?
C0:65C7  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:65CA  5B           tcd                     ; E0 M16 X16 C?
C0:65CB  68           pla                     ; E0 M16 X16 C?
C0:65CC  85 10        sta $10                 ; E0 M16 X16 C?
C0:65CE  0A           asl a                   ; E0 M16 X16 C?
C0:65CF  AA           tax                     ; E0 M16 X16 C?
C0:65D0  AD 77 98     lda $9877               ; E0 M16 X16 C?
C0:65D3  4A           lsr a                   ; E0 M16 X16 C?
C0:65D4  4A           lsr a                   ; E0 M16 X16 C?
C0:65D5  4A           lsr a                   ; E0 M16 X16 C?
C0:65D6  18           clc                     ; E0 M16 X16 C?
C0:65D7  7F 30 E2 C3  adc $C3E230,x           ; E0 M16 X16 C0
C0:65DB  A8           tay                     ; E0 M16 X16 C?
C0:65DC  84 0E        sty $0E                 ; E0 M16 X16 C?
C0:65DE  AD 7B 98     lda $987B               ; E0 M16 X16 C?
C0:65E1  4A           lsr a                   ; E0 M16 X16 C?
C0:65E2  4A           lsr a                   ; E0 M16 X16 C?
C0:65E3  4A           lsr a                   ; E0 M16 X16 C?
C0:65E4  18           clc                     ; E0 M16 X16 C?
C0:65E5  7F 40 E2 C3  adc $C3E240,x           ; E0 M16 X16 C0
C0:65E9  85 02        sta $02                 ; E0 M16 X16 C?
C0:65EB  A5 10        lda $10                 ; E0 M16 X16 C?
C0:65ED  C9 06 00     cmp #$0006              ; E0 M16 X16 C?
C0:65F0  D0 03        bne $65F5               ; E0 M16 X16 C?
C0:65F2  88           dey                     ; E0 M16 X16 C?
C0:65F3  84 0E        sty $0E                 ; E0 M16 X16 C?
Code_C065F5:
C0:65F5  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:65F7  98           tya                     ; E0 M16 X16 C?
C0:65F8  22 77 74 C0  jsl $C07477             ; E0 M16 X16 C?
C0:65FC  C2 20        rep #$20                ; E0 M16 X16 C?
C0:65FE  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:6601  AA           tax                     ; E0 M16 X16 C?
C0:6602  E0 FF 00     cpx #$00FF              ; E0 M16 X16 C?
C0:6605  D0 10        bne $6617               ; E0 M16 X16 C?
C0:6607  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:6609  A4 0E        ldy $0E                 ; E0 M16 X16 C?
C0:660B  98           tya                     ; E0 M16 X16 C?
C0:660C  1A           inc a                   ; E0 M16 X16 C?
C0:660D  22 77 74 C0  jsl $C07477             ; E0 M16 X16 C?
C0:6611  C2 20        rep #$20                ; E0 M16 X16 C?
C0:6613  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:6616  AA           tax                     ; E0 M16 X16 C?
Code_C06617:
C0:6617  E0 FF 00     cpx #$00FF              ; E0 M16 X16 C?
C0:661A  F0 44        beq $6660               ; E0 M16 X16 C?
C0:661C  E0 06 00     cpx #$0006              ; E0 M16 X16 C?
C0:661F  D0 3F        bne $6660               ; E0 M16 X16 C?
C0:6621  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6624  85 06        sta $06                 ; E0 M16 X16 C?
C0:6626  A9 CF 00     lda #$00CF              ; E0 M16 X16 C?
C0:6629  85 08        sta $08                 ; E0 M16 X16 C?
C0:662B  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:662E  29 FF 7F     and #$7FFF              ; E0 M16 X16 C?
C0:6631  18           clc                     ; E0 M16 X16 C?
C0:6632  65 06        adc $06                 ; E0 M16 X16 C0
C0:6634  85 06        sta $06                 ; E0 M16 X16 C?
C0:6636  AD BE 5D     lda $5DBE               ; E0 M16 X16 C?
C0:6639  8D DC 5D     sta $5DDC               ; E0 M16 X16 C?
C0:663C  A5 06        lda $06                 ; E0 M16 X16 C?
C0:663E  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:6640  A5 08        lda $08                 ; E0 M16 X16 C?
C0:6642  85 0C        sta $0C                 ; E0 M16 X16 C?
C0:6644  A0 02 00     ldy #$0002              ; E0 M16 X16 C?
C0:6647  B7 0A        lda [$0A],y             ; E0 M16 X16 C?
C0:6649  A8           tay                     ; E0 M16 X16 C?
C0:664A  A7 0A        lda [$0A]               ; E0 M16 X16 C?
C0:664C  85 06        sta $06                 ; E0 M16 X16 C?
C0:664E  84 08        sty $08                 ; E0 M16 X16 C?
C0:6650  A5 06        lda $06                 ; E0 M16 X16 C?
C0:6652  8D DE 5D     sta $5DDE               ; E0 M16 X16 C?
C0:6655  A5 08        lda $08                 ; E0 M16 X16 C?
C0:6657  8D E0 5D     sta $5DE0               ; E0 M16 X16 C?
C0:665A  A9 FE FF     lda #$FFFE              ; E0 M16 X16 C?
C0:665D  8D 62 5D     sta $5D62               ; E0 M16 X16 C?
Code_C06660:
C0:6660  2B           pld                     ; E0 M16 X16 C?
C0:6661  6B           rtl                     ; E0 M16 X16 C?
MovementTriggerType0_QueueDoorDestination:
C0:6A1B  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6A1D  0B           phd                     ; E0 M16 X16 C?
C0:6A1E  48           pha                     ; E0 M16 X16 C?
C0:6A1F  7B           tdc                     ; E0 M16 X16 C?
C0:6A20  69 EA FF     adc #$FFEA              ; E0 M16 X16 C?
C0:6A23  5B           tcd                     ; E0 M16 X16 C?
C0:6A24  68           pla                     ; E0 M16 X16 C?
C0:6A25  29 FF 7F     and #$7FFF              ; E0 M16 X16 C?
C0:6A28  85 14        sta $14                 ; E0 M16 X16 C?
C0:6A2A  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6A2D  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:6A2F  A9 CF 00     lda #$00CF              ; E0 M16 X16 C?
C0:6A32  85 0C        sta $0C                 ; E0 M16 X16 C?
C0:6A34  A5 14        lda $14                 ; E0 M16 X16 C?
C0:6A36  18           clc                     ; E0 M16 X16 C?
C0:6A37  65 0A        adc $0A                 ; E0 M16 X16 C0
C0:6A39  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:6A3B  85 06        sta $06                 ; E0 M16 X16 C?
C0:6A3D  A5 0C        lda $0C                 ; E0 M16 X16 C?
C0:6A3F  85 08        sta $08                 ; E0 M16 X16 C?
C0:6A41  A7 06        lda [$06]               ; E0 M16 X16 C?
C0:6A43  29 FF 7F     and #$7FFF              ; E0 M16 X16 C?
C0:6A46  22 28 16 C2  jsl $C21628             ; E0 M16 X16 C?
C0:6A4A  AA           tax                     ; E0 M16 X16 C?
C0:6A4B  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6A4E  85 12        sta $12                 ; E0 M16 X16 C?
C0:6A50  A7 06        lda [$06]               ; E0 M16 X16 C?
C0:6A52  C9 00 80     cmp #$8000              ; E0 M16 X16 C?
C0:6A55  90 07        bcc $6A5E               ; E0 M16 X16 C?
C0:6A57  F0 05        beq $6A5E               ; E0 M16 X16 C?
C0:6A59  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6A5C  85 12        sta $12                 ; E0 M16 X16 C?
Code_C06A5E:
C0:6A5E  A5 12        lda $12                 ; E0 M16 X16 C?
C0:6A60  85 02        sta $02                 ; E0 M16 X16 C?
C0:6A62  8A           txa                     ; E0 M16 X16 C?
C0:6A63  C5 02        cmp $02                 ; E0 M16 X16 C?
C0:6A65  D0 22        bne $6A89               ; E0 M16 X16 C?
C0:6A67  A0 02 00     ldy #$0002              ; E0 M16 X16 C?
C0:6A6A  B7 0A        lda [$0A],y             ; E0 M16 X16 C?
C0:6A6C  48           pha                     ; E0 M16 X16 C?
C0:6A6D  C8           iny                     ; E0 M16 X16 C?
C0:6A6E  C8           iny                     ; E0 M16 X16 C?
C0:6A6F  B7 0A        lda [$0A],y             ; E0 M16 X16 C?
C0:6A71  85 08        sta $08                 ; E0 M16 X16 C?
C0:6A73  68           pla                     ; E0 M16 X16 C?
C0:6A74  85 06        sta $06                 ; E0 M16 X16 C?
C0:6A76  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6A78  A5 08        lda $08                 ; E0 M16 X16 C?
C0:6A7A  85 10        sta $10                 ; E0 M16 X16 C?
C0:6A7C  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6A7F  22 E3 64 C0  jsl $C064E3             ; E0 M16 X16 C?
C0:6A83  9C AA 5D     stz $5DAA               ; E0 M16 X16 C?
C0:6A86  9C A8 5D     stz $5DA8               ; E0 M16 X16 C?
Code_C06A89:
C0:6A89  2B           pld                     ; E0 M16 X16 C?
C0:6A8A  60           rts                     ; E0 M16 X16 C?
MovementTriggerType5Or7_NoOp:
C0:6A8B  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6A8D  60           rts                     ; E0 M16 X16 C?
MovementTriggerType6_NoOp:
C0:6A8E  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6A90  60           rts                     ; E0 M16 X16 C?
MovementTriggerType1_SetState07Or08:
C0:6A91  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6A93  A8           tay                     ; E0 M16 X16 C?
C0:6A94  A2 83 98     ldx #$9883              ; E0 M16 X16 C?
C0:6A97  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:6A9A  C9 07 00     cmp #$0007              ; E0 M16 X16 C?
C0:6A9D  F0 2A        beq $6AC9               ; E0 M16 X16 C?
C0:6A9F  C9 08 00     cmp #$0008              ; E0 M16 X16 C?
C0:6AA2  F0 25        beq $6AC9               ; E0 M16 X16 C?
C0:6AA4  C0 00 00     cpy #$0000              ; E0 M16 X16 C?
C0:6AA7  D0 08        bne $6AB1               ; E0 M16 X16 C?
C0:6AA9  A9 07 00     lda #$0007              ; E0 M16 X16 C?
C0:6AAC  9D 00 00     sta $0000,x             ; E0 M16 X16 C?
C0:6AAF  80 06        bra $6AB7               ; E0 M16 X16 C?
Code_C06AB1:
C0:6AB1  A9 08 00     lda #$0008              ; E0 M16 X16 C?
C0:6AB4  9D 00 00     sta $0000,x             ; E0 M16 X16 C?
Code_C06AB7:
C0:6AB7  A2 7F 98     ldx #$987F              ; E0 M16 X16 C?
C0:6ABA  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:6ABD  29 FE FF     and #$FFFE              ; E0 M16 X16 C?
C0:6AC0  9D 00 00     sta $0000,x             ; E0 M16 X16 C?
C0:6AC3  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:6AC6  8D C4 5D     sta $5DC4               ; E0 M16 X16 C?
Code_C06AC9:
C0:6AC9  60           rts                     ; E0 M16 X16 C?
MovementTriggerType2_QueueDoorTransition:
C0:6ACA  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6ACC  0B           phd                     ; E0 M16 X16 C?
C0:6ACD  48           pha                     ; E0 M16 X16 C?
C0:6ACE  7B           tdc                     ; E0 M16 X16 C?
C0:6ACF  69 EC FF     adc #$FFEC              ; E0 M16 X16 C?
C0:6AD2  5B           tcd                     ; E0 M16 X16 C?
C0:6AD3  68           pla                     ; E0 M16 X16 C?
C0:6AD4  85 12        sta $12                 ; E0 M16 X16 C?
C0:6AD6  AD 34 0A     lda $0A34               ; E0 M16 X16 C?
C0:6AD9  F0 44        beq $6B1F               ; E0 M16 X16 C?
C0:6ADB  AD A5 98     lda $98A5               ; E0 M16 X16 C?
C0:6ADE  C9 02 00     cmp #$0002              ; E0 M16 X16 C?
C0:6AE1  F0 3C        beq $6B1F               ; E0 M16 X16 C?
C0:6AE3  AD 9A 5D     lda $5D9A               ; E0 M16 X16 C?
C0:6AE6  D0 37        bne $6B1F               ; E0 M16 X16 C?
C0:6AE8  AD BA 4D     lda $4DBA               ; E0 M16 X16 C?
C0:6AEB  0D 60 5D     ora $5D60               ; E0 M16 X16 C?
C0:6AEE  D0 2F        bne $6B1F               ; E0 M16 X16 C?
C0:6AF0  A5 12        lda $12                 ; E0 M16 X16 C?
C0:6AF2  29 FF 7F     and #$7FFF              ; E0 M16 X16 C?
C0:6AF5  85 12        sta $12                 ; E0 M16 X16 C?
C0:6AF7  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6AFA  8D C2 5D     sta $5DC2               ; E0 M16 X16 C?
C0:6AFD  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6B00  85 06        sta $06                 ; E0 M16 X16 C?
C0:6B02  A9 CF 00     lda #$00CF              ; E0 M16 X16 C?
C0:6B05  85 08        sta $08                 ; E0 M16 X16 C?
C0:6B07  A5 12        lda $12                 ; E0 M16 X16 C?
C0:6B09  18           clc                     ; E0 M16 X16 C?
C0:6B0A  65 06        adc $06                 ; E0 M16 X16 C0
C0:6B0C  85 06        sta $06                 ; E0 M16 X16 C?
C0:6B0E  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6B10  A5 08        lda $08                 ; E0 M16 X16 C?
C0:6B12  85 10        sta $10                 ; E0 M16 X16 C?
C0:6B14  A9 02 00     lda #$0002              ; E0 M16 X16 C?
C0:6B17  22 E3 64 C0  jsl $C064E3             ; E0 M16 X16 C?
C0:6B1B  22 5B 7C C0  jsl $C07C5B             ; E0 M16 X16 C?
Code_C06B1F:
C0:6B1F  2B           pld                     ; E0 M16 X16 C?
C0:6B20  60           rts                     ; E0 M16 X16 C?
TimerCallback_CommitStagedPosition_State0C:
C0:6E2C  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6E2E  A9 0C 00     lda #$000C              ; E0 M16 X16 C?
C0:6E31  8D 83 98     sta $9883               ; E0 M16 X16 C?
C0:6E34  9C 56 5D     stz $5D56               ; E0 M16 X16 C?
C0:6E37  AD D0 5D     lda $5DD0               ; E0 M16 X16 C?
C0:6E3A  8D 77 98     sta $9877               ; E0 M16 X16 C?
C0:6E3D  AD D2 5D     lda $5DD2               ; E0 M16 X16 C?
C0:6E40  8D 7B 98     sta $987B               ; E0 M16 X16 C?
C0:6E43  9C 79 98     stz $9879               ; E0 M16 X16 C?
C0:6E46  9C 75 98     stz $9875               ; E0 M16 X16 C?
C0:6E49  6B           rtl                     ; E0 M16 X16 C?
TimerCallback_CommitStagedPosition_ClearMotion:
C0:6E4A  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6E4C  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:6E4F  8D C4 5D     sta $5DC4               ; E0 M16 X16 C?
C0:6E52  9C 83 98     stz $9883               ; E0 M16 X16 C?
C0:6E55  9C 56 5D     stz $5D56               ; E0 M16 X16 C?
C0:6E58  9C BA 5D     stz $5DBA               ; E0 M16 X16 C?
C0:6E5B  AD D0 5D     lda $5DD0               ; E0 M16 X16 C?
C0:6E5E  8D 77 98     sta $9877               ; E0 M16 X16 C?
C0:6E61  AD D2 5D     lda $5DD2               ; E0 M16 X16 C?
C0:6E64  8D 7B 98     sta $987B               ; E0 M16 X16 C?
C0:6E67  9C 79 98     stz $9879               ; E0 M16 X16 C?
C0:6E6A  9C 75 98     stz $9875               ; E0 M16 X16 C?
C0:6E6D  6B           rtl                     ; E0 M16 X16 C?
MovementTriggerType3_QueueOffsetStep:
C0:6E6E  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6E70  0B           phd                     ; E0 M16 X16 C?
C0:6E71  48           pha                     ; E0 M16 X16 C?
C0:6E72  7B           tdc                     ; E0 M16 X16 C?
C0:6E73  69 E4 FF     adc #$FFE4              ; E0 M16 X16 C?
C0:6E76  5B           tcd                     ; E0 M16 X16 C?
C0:6E77  68           pla                     ; E0 M16 X16 C?
C0:6E78  84 1A        sty $1A                 ; E0 M16 X16 C?
C0:6E7A  86 18        stx $18                 ; E0 M16 X16 C?
C0:6E7C  85 16        sta $16                 ; E0 M16 X16 C?
C0:6E7E  AD 81 00     lda $0081               ; E0 M16 X16 C?
C0:6E81  F0 03        beq $6E86               ; E0 M16 X16 C?
C0:6E83  4C 80 6F     jmp $6F80               ; E0 M16 X16 C?
Code_C06E86:
C0:6E86  22 69 8C C4  jsl $C48C69             ; E0 M16 X16 C?
C0:6E8A  A6 18        ldx $18                 ; E0 M16 X16 C?
C0:6E8C  8A           txa                     ; E0 M16 X16 C?
C0:6E8D  0A           asl a                   ; E0 M16 X16 C?
C0:6E8E  0A           asl a                   ; E0 M16 X16 C?
C0:6E8F  0A           asl a                   ; E0 M16 X16 C?
C0:6E90  AA           tax                     ; E0 M16 X16 C?
C0:6E91  86 14        stx $14                 ; E0 M16 X16 C?
C0:6E93  A4 1A        ldy $1A                 ; E0 M16 X16 C?
C0:6E95  98           tya                     ; E0 M16 X16 C?
C0:6E96  0A           asl a                   ; E0 M16 X16 C?
C0:6E97  0A           asl a                   ; E0 M16 X16 C?
C0:6E98  0A           asl a                   ; E0 M16 X16 C?
C0:6E99  85 12        sta $12                 ; E0 M16 X16 C?
C0:6E9B  A5 16        lda $16                 ; E0 M16 X16 C?
C0:6E9D  29 00 80     and #$8000              ; E0 M16 X16 C?
C0:6EA0  F0 73        beq $6F15               ; E0 M16 X16 C?
C0:6EA2  A0 83 98     ldy #$9883              ; E0 M16 X16 C?
C0:6EA5  B9 00 00     lda $0000,y             ; E0 M16 X16 C?
C0:6EA8  C9 0C 00     cmp #$000C              ; E0 M16 X16 C?
C0:6EAB  F0 03        beq $6EB0               ; E0 M16 X16 C?
C0:6EAD  4C 80 6F     jmp $6F80               ; E0 M16 X16 C?
Code_C06EB0:
C0:6EB0  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6EB3  99 00 00     sta $0000,y             ; E0 M16 X16 C?
C0:6EB6  A9 03 00     lda #$0003              ; E0 M16 X16 C?
C0:6EB9  8D 56 5D     sta $5D56               ; E0 M16 X16 C?
C0:6EBC  AD C6 5D     lda $5DC6               ; E0 M16 X16 C?
C0:6EBF  EB           xba                     ; E0 M16 X16 C?
C0:6EC0  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:6EC3  0A           asl a                   ; E0 M16 X16 C?
C0:6EC4  85 02        sta $02                 ; E0 M16 X16 C?
C0:6EC6  8A           txa                     ; E0 M16 X16 C?
C0:6EC7  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:6EC9  18           clc                     ; E0 M16 X16 C?
C0:6ECA  7F 0A 6E C0  adc $C06E0A,x           ; E0 M16 X16 C0
C0:6ECE  85 04        sta $04                 ; E0 M16 X16 C?
C0:6ED0  A5 12        lda $12                 ; E0 M16 X16 C?
C0:6ED2  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6ED4  A4 04        ldy $04                 ; E0 M16 X16 C?
C0:6ED6  AE 7B 98     ldx $987B               ; E0 M16 X16 C?
C0:6ED9  AD 77 98     lda $9877               ; E0 M16 X16 C?
C0:6EDC  22 58 8D C4  jsl $C48D58             ; E0 M16 X16 C?
C0:6EE0  A8           tay                     ; E0 M16 X16 C?
C0:6EE1  84 1A        sty $1A                 ; E0 M16 X16 C?
C0:6EE3  A2 10 00     ldx #$0010              ; E0 M16 X16 C?
C0:6EE6  86 18        stx $18                 ; E0 M16 X16 C?
C0:6EE8  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:6EEA  BF 12 6E C0  lda $C06E12,x           ; E0 M16 X16 C?
C0:6EEE  A6 18        ldx $18                 ; E0 M16 X16 C?
C0:6EF0  22 6B 8E C4  jsl $C48E6B             ; E0 M16 X16 C?
C0:6EF4  A9 4A 6E     lda #$6E4A              ; E0 M16 X16 C?
C0:6EF7  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6EF9  A9 C0 00     lda #$00C0              ; E0 M16 X16 C?
C0:6EFC  85 10        sta $10                 ; E0 M16 X16 C?
C0:6EFE  A4 1A        ldy $1A                 ; E0 M16 X16 C?
C0:6F00  98           tya                     ; E0 M16 X16 C?
C0:6F01  1A           inc a                   ; E0 M16 X16 C?
C0:6F02  22 E6 DB C0  jsl $C0DBE6             ; E0 M16 X16 C?
C0:6F06  22 95 8E C4  jsl $C48E95             ; E0 M16 X16 C?
C0:6F0A  9C C6 5D     stz $5DC6               ; E0 M16 X16 C?
C0:6F0D  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6F10  8D BA 5D     sta $5DBA               ; E0 M16 X16 C?
C0:6F13  80 5B        bra $6F70               ; E0 M16 X16 C?
Code_C06F15:
C0:6F15  AD 83 98     lda $9883               ; E0 M16 X16 C?
C0:6F18  C9 0C 00     cmp #$000C              ; E0 M16 X16 C?
C0:6F1B  F0 63        beq $6F80               ; E0 M16 X16 C?
C0:6F1D  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6F20  8D BA 5D     sta $5DBA               ; E0 M16 X16 C?
C0:6F23  A5 16        lda $16                 ; E0 M16 X16 C?
C0:6F25  8D C6 5D     sta $5DC6               ; E0 M16 X16 C?
C0:6F28  EB           xba                     ; E0 M16 X16 C?
C0:6F29  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:6F2C  0A           asl a                   ; E0 M16 X16 C?
C0:6F2D  85 16        sta $16                 ; E0 M16 X16 C?
C0:6F2F  AA           tax                     ; E0 M16 X16 C?
C0:6F30  BF 12 6E C0  lda $C06E12,x           ; E0 M16 X16 C?
C0:6F34  8D 7F 98     sta $987F               ; E0 M16 X16 C?
C0:6F37  A9 03 00     lda #$0003              ; E0 M16 X16 C?
C0:6F3A  8D 56 5D     sta $5D56               ; E0 M16 X16 C?
C0:6F3D  A5 16        lda $16                 ; E0 M16 X16 C?
C0:6F3F  48           pha                     ; E0 M16 X16 C?
C0:6F40  A6 14        ldx $14                 ; E0 M16 X16 C?
C0:6F42  8A           txa                     ; E0 M16 X16 C?
C0:6F43  FA           plx                     ; E0 M16 X16 C?
C0:6F44  18           clc                     ; E0 M16 X16 C?
C0:6F45  7F 02 6E C0  adc $C06E02,x           ; E0 M16 X16 C0
C0:6F49  85 04        sta $04                 ; E0 M16 X16 C?
C0:6F4B  A5 12        lda $12                 ; E0 M16 X16 C?
C0:6F4D  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6F4F  A4 04        ldy $04                 ; E0 M16 X16 C?
C0:6F51  AE 7B 98     ldx $987B               ; E0 M16 X16 C?
C0:6F54  AD 77 98     lda $9877               ; E0 M16 X16 C?
C0:6F57  22 58 8D C4  jsl $C48D58             ; E0 M16 X16 C?
C0:6F5B  AA           tax                     ; E0 M16 X16 C?
C0:6F5C  A9 2C 6E     lda #$6E2C              ; E0 M16 X16 C?
C0:6F5F  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6F61  A9 C0 00     lda #$00C0              ; E0 M16 X16 C?
C0:6F64  85 10        sta $10                 ; E0 M16 X16 C?
C0:6F66  8A           txa                     ; E0 M16 X16 C?
C0:6F67  1A           inc a                   ; E0 M16 X16 C?
C0:6F68  22 E6 DB C0  jsl $C0DBE6             ; E0 M16 X16 C?
C0:6F6C  22 95 8E C4  jsl $C48E95             ; E0 M16 X16 C?
Code_C06F70:
C0:6F70  A5 04        lda $04                 ; E0 M16 X16 C?
C0:6F72  8D D0 5D     sta $5DD0               ; E0 M16 X16 C?
C0:6F75  A5 12        lda $12                 ; E0 M16 X16 C?
C0:6F77  8D D2 5D     sta $5DD2               ; E0 M16 X16 C?
C0:6F7A  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:6F7D  8D C4 5D     sta $5DC4               ; E0 M16 X16 C?
Code_C06F80:
C0:6F80  2B           pld                     ; E0 M16 X16 C?
C0:6F81  60           rts                     ; E0 M16 X16 C?
TimerCallback_WaitForStagedY_State0D:
C0:6F82  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6F84  0B           phd                     ; E0 M16 X16 C?
C0:6F85  7B           tdc                     ; E0 M16 X16 C?
C0:6F86  69 EC FF     adc #$FFEC              ; E0 M16 X16 C?
C0:6F89  5B           tcd                     ; E0 M16 X16 C?
C0:6F8A  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6F8D  85 12        sta $12                 ; E0 M16 X16 C?
C0:6F8F  AD C4 5D     lda $5DC4               ; E0 M16 X16 C?
C0:6F92  F0 08        beq $6F9C               ; E0 M16 X16 C?
C0:6F94  AD C4 5D     lda $5DC4               ; E0 M16 X16 C?
C0:6F97  C9 00 01     cmp #$0100              ; E0 M16 X16 C?
C0:6F9A  D0 12        bne $6FAE               ; E0 M16 X16 C?
Code_C06F9C:
C0:6F9C  AD CE 5D     lda $5DCE               ; E0 M16 X16 C?
C0:6F9F  3A           dec a                   ; E0 M16 X16 C?
C0:6FA0  CD 7B 98     cmp $987B               ; E0 M16 X16 C?
C0:6FA3  90 17        bcc $6FBC               ; E0 M16 X16 C?
C0:6FA5  F0 15        beq $6FBC               ; E0 M16 X16 C?
C0:6FA7  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6FAA  85 12        sta $12                 ; E0 M16 X16 C?
C0:6FAC  80 0E        bra $6FBC               ; E0 M16 X16 C?
Code_C06FAE:
C0:6FAE  AD CE 5D     lda $5DCE               ; E0 M16 X16 C?
C0:6FB1  1A           inc a                   ; E0 M16 X16 C?
C0:6FB2  CD 7B 98     cmp $987B               ; E0 M16 X16 C?
C0:6FB5  B0 05        bcs $6FBC               ; E0 M16 X16 C?
C0:6FB7  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6FBA  85 12        sta $12                 ; E0 M16 X16 C?
Code_C06FBC:
C0:6FBC  A5 12        lda $12                 ; E0 M16 X16 C?
C0:6FBE  F0 1A        beq $6FDA               ; E0 M16 X16 C?
C0:6FC0  A9 0D 00     lda #$000D              ; E0 M16 X16 C?
C0:6FC3  8D 83 98     sta $9883               ; E0 M16 X16 C?
C0:6FC6  AD CC 5D     lda $5DCC               ; E0 M16 X16 C?
C0:6FC9  8D 77 98     sta $9877               ; E0 M16 X16 C?
C0:6FCC  AD CE 5D     lda $5DCE               ; E0 M16 X16 C?
C0:6FCF  8D 7B 98     sta $987B               ; E0 M16 X16 C?
C0:6FD2  9C 79 98     stz $9879               ; E0 M16 X16 C?
C0:6FD5  9C 75 98     stz $9875               ; E0 M16 X16 C?
C0:6FD8  80 11        bra $6FEB               ; E0 M16 X16 C?
Code_C06FDA:
C0:6FDA  A9 82 6F     lda #$6F82              ; E0 M16 X16 C?
C0:6FDD  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:6FDF  A9 C0 00     lda #$00C0              ; E0 M16 X16 C?
C0:6FE2  85 10        sta $10                 ; E0 M16 X16 C?
C0:6FE4  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:6FE7  22 E6 DB C0  jsl $C0DBE6             ; E0 M16 X16 C?
Code_C06FEB:
C0:6FEB  2B           pld                     ; E0 M16 X16 C?
C0:6FEC  6B           rtl                     ; E0 M16 X16 C?
TimerCallback_WaitForStagedY_ClearMotion:
C0:6FED  C2 31        rep #$31                ; E0 M16 X16 C?
C0:6FEF  0B           phd                     ; E0 M16 X16 C?
C0:6FF0  7B           tdc                     ; E0 M16 X16 C?
C0:6FF1  69 EC FF     adc #$FFEC              ; E0 M16 X16 C?
C0:6FF4  5B           tcd                     ; E0 M16 X16 C?
C0:6FF5  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:6FF8  85 12        sta $12                 ; E0 M16 X16 C?
C0:6FFA  AD C4 5D     lda $5DC4               ; E0 M16 X16 C?
C0:6FFD  F0 08        beq $7007               ; E0 M16 X16 C?
C0:6FFF  AD C4 5D     lda $5DC4               ; E0 M16 X16 C?
C0:7002  C9 00 01     cmp #$0100              ; E0 M16 X16 C?
C0:7005  D0 0F        bne $7016               ; E0 M16 X16 C?
Code_C07007:
C0:7007  AD 7B 98     lda $987B               ; E0 M16 X16 C?
C0:700A  CD CE 5D     cmp $5DCE               ; E0 M16 X16 C?
C0:700D  B0 16        bcs $7025               ; E0 M16 X16 C?
C0:700F  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:7012  85 12        sta $12                 ; E0 M16 X16 C?
C0:7014  80 0F        bra $7025               ; E0 M16 X16 C?
Code_C07016:
C0:7016  AD 7B 98     lda $987B               ; E0 M16 X16 C?
C0:7019  CD CE 5D     cmp $5DCE               ; E0 M16 X16 C?
C0:701C  90 07        bcc $7025               ; E0 M16 X16 C?
C0:701E  F0 05        beq $7025               ; E0 M16 X16 C?
C0:7020  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:7023  85 12        sta $12                 ; E0 M16 X16 C?
Code_C07025:
C0:7025  A5 12        lda $12                 ; E0 M16 X16 C?
C0:7027  F0 23        beq $704C               ; E0 M16 X16 C?
C0:7029  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:702C  8D C4 5D     sta $5DC4               ; E0 M16 X16 C?
C0:702F  9C 83 98     stz $9883               ; E0 M16 X16 C?
C0:7032  9C 56 5D     stz $5D56               ; E0 M16 X16 C?
C0:7035  AD CC 5D     lda $5DCC               ; E0 M16 X16 C?
C0:7038  8D 77 98     sta $9877               ; E0 M16 X16 C?
C0:703B  AD CE 5D     lda $5DCE               ; E0 M16 X16 C?
C0:703E  8D 7B 98     sta $987B               ; E0 M16 X16 C?
C0:7041  9C 79 98     stz $9879               ; E0 M16 X16 C?
C0:7044  9C 75 98     stz $9875               ; E0 M16 X16 C?
C0:7047  9C BA 5D     stz $5DBA               ; E0 M16 X16 C?
C0:704A  80 11        bra $705D               ; E0 M16 X16 C?
Code_C0704C:
C0:704C  A9 ED 6F     lda #$6FED              ; E0 M16 X16 C?
C0:704F  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:7051  A9 C0 00     lda #$00C0              ; E0 M16 X16 C?
C0:7054  85 10        sta $10                 ; E0 M16 X16 C?
C0:7056  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:7059  22 E6 DB C0  jsl $C0DBE6             ; E0 M16 X16 C?
Code_C0705D:
C0:705D  2B           pld                     ; E0 M16 X16 C?
C0:705E  6B           rtl                     ; E0 M16 X16 C?
Select_StagedMovementFacing:
C0:705F  C2 31        rep #$31                ; E0 M16 X16 C?
C0:7061  A0 01 00     ldy #$0001              ; E0 M16 X16 C?
C0:7064  AE 7F 98     ldx $987F               ; E0 M16 X16 C?
C0:7067  C9 00 01     cmp #$0100              ; E0 M16 X16 C?
C0:706A  F0 11        beq $707D               ; E0 M16 X16 C?
C0:706C  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:706F  F0 22        beq $7093               ; E0 M16 X16 C?
C0:7071  C9 00 03     cmp #$0300              ; E0 M16 X16 C?
C0:7074  F0 33        beq $70A9               ; E0 M16 X16 C?
C0:7076  C9 00 02     cmp #$0200              ; E0 M16 X16 C?
C0:7079  F0 3F        beq $70BA               ; E0 M16 X16 C?
C0:707B  80 4C        bra $70C9               ; E0 M16 X16 C?
Code_C0707D:
C0:707D  E0 00 00     cpx #$0000              ; E0 M16 X16 C?
C0:7080  F0 06        beq $7088               ; E0 M16 X16 C?
C0:7082  8A           txa                     ; E0 M16 X16 C?
C0:7083  29 03 00     and #$0003              ; E0 M16 X16 C?
C0:7086  F0 03        beq $708B               ; E0 M16 X16 C?
Code_C07088:
C0:7088  A0 00 00     ldy #$0000              ; E0 M16 X16 C?
Code_C0708B:
C0:708B  A9 02 00     lda #$0002              ; E0 M16 X16 C?
C0:708E  8D CA 5D     sta $5DCA               ; E0 M16 X16 C?
C0:7091  80 36        bra $70C9               ; E0 M16 X16 C?
Code_C07093:
C0:7093  E0 00 00     cpx #$0000              ; E0 M16 X16 C?
C0:7096  F0 06        beq $709E               ; E0 M16 X16 C?
C0:7098  8A           txa                     ; E0 M16 X16 C?
C0:7099  29 03 00     and #$0003              ; E0 M16 X16 C?
C0:709C  F0 03        beq $70A1               ; E0 M16 X16 C?
Code_C0709E:
C0:709E  A0 00 00     ldy #$0000              ; E0 M16 X16 C?
Code_C070A1:
C0:70A1  A9 06 00     lda #$0006              ; E0 M16 X16 C?
C0:70A4  8D CA 5D     sta $5DCA               ; E0 M16 X16 C?
C0:70A7  80 20        bra $70C9               ; E0 M16 X16 C?
Code_C070A9:
C0:70A9  8A           txa                     ; E0 M16 X16 C?
C0:70AA  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:70AD  F0 03        beq $70B2               ; E0 M16 X16 C?
C0:70AF  A0 00 00     ldy #$0000              ; E0 M16 X16 C?
Code_C070B2:
C0:70B2  A9 02 00     lda #$0002              ; E0 M16 X16 C?
C0:70B5  8D CA 5D     sta $5DCA               ; E0 M16 X16 C?
C0:70B8  80 0F        bra $70C9               ; E0 M16 X16 C?
Code_C070BA:
C0:70BA  8A           txa                     ; E0 M16 X16 C?
C0:70BB  29 07 00     and #$0007              ; E0 M16 X16 C?
C0:70BE  F0 03        beq $70C3               ; E0 M16 X16 C?
C0:70C0  A0 00 00     ldy #$0000              ; E0 M16 X16 C?
Code_C070C3:
C0:70C3  A9 06 00     lda #$0006              ; E0 M16 X16 C?
C0:70C6  8D CA 5D     sta $5DCA               ; E0 M16 X16 C?
Code_C070C9:
C0:70C9  98           tya                     ; E0 M16 X16 C?
C0:70CA  60           rts                     ; E0 M16 X16 C?
Queue_StagedMovementFromGridCoords:
C0:70CB  C2 31        rep #$31                ; E0 M16 X16 C?
C0:70CD  0B           phd                     ; E0 M16 X16 C?
C0:70CE  48           pha                     ; E0 M16 X16 C?
C0:70CF  7B           tdc                     ; E0 M16 X16 C?
C0:70D0  69 E6 FF     adc #$FFE6              ; E0 M16 X16 C?
C0:70D3  5B           tcd                     ; E0 M16 X16 C?
C0:70D4  68           pla                     ; E0 M16 X16 C?
C0:70D5  84 02        sty $02                 ; E0 M16 X16 C?
C0:70D7  9B           txy                     ; E0 M16 X16 C?
C0:70D8  84 18        sty $18                 ; E0 M16 X16 C?
C0:70DA  85 16        sta $16                 ; E0 M16 X16 C?
C0:70DC  AD 81 00     lda $0081               ; E0 M16 X16 C?
C0:70DF  F0 03        beq $70E4               ; E0 M16 X16 C?
C0:70E1  4C E3 71     jmp $71E3               ; E0 M16 X16 C?
Code_C070E4:
C0:70E4  22 69 8C C4  jsl $C48C69             ; E0 M16 X16 C?
C0:70E8  A5 16        lda $16                 ; E0 M16 X16 C?
C0:70EA  AA           tax                     ; E0 M16 X16 C?
C0:70EB  EB           xba                     ; E0 M16 X16 C?
C0:70EC  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:70EF  85 04        sta $04                 ; E0 M16 X16 C?
C0:70F1  A4 18        ldy $18                 ; E0 M16 X16 C?
C0:70F3  98           tya                     ; E0 M16 X16 C?
C0:70F4  0A           asl a                   ; E0 M16 X16 C?
C0:70F5  0A           asl a                   ; E0 M16 X16 C?
C0:70F6  0A           asl a                   ; E0 M16 X16 C?
C0:70F7  A8           tay                     ; E0 M16 X16 C?
C0:70F8  84 18        sty $18                 ; E0 M16 X16 C?
C0:70FA  A5 02        lda $02                 ; E0 M16 X16 C?
C0:70FC  0A           asl a                   ; E0 M16 X16 C?
C0:70FD  0A           asl a                   ; E0 M16 X16 C?
C0:70FE  0A           asl a                   ; E0 M16 X16 C?
C0:70FF  85 02        sta $02                 ; E0 M16 X16 C?
C0:7101  AD 83 98     lda $9883               ; E0 M16 X16 C?
C0:7104  F0 03        beq $7109               ; E0 M16 X16 C?
C0:7106  4C 86 71     jmp $7186               ; E0 M16 X16 C?
Code_C07109:
C0:7109  8A           txa                     ; E0 M16 X16 C?
C0:710A  20 5F 70     jsr $705F               ; E0 M16 X16 C?
C0:710D  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:7110  F0 03        beq $7115               ; E0 M16 X16 C?
C0:7112  4C E3 71     jmp $71E3               ; E0 M16 X16 C?
Code_C07115:
C0:7115  AD CA 5D     lda $5DCA               ; E0 M16 X16 C?
C0:7118  8D 7F 98     sta $987F               ; E0 M16 X16 C?
C0:711B  9C B8 5D     stz $5DB8               ; E0 M16 X16 C?
C0:711E  A9 03 00     lda #$0003              ; E0 M16 X16 C?
C0:7121  8D 56 5D     sta $5D56               ; E0 M16 X16 C?
C0:7124  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:7127  8D BA 5D     sta $5DBA               ; E0 M16 X16 C?
C0:712A  A5 04        lda $04                 ; E0 M16 X16 C?
C0:712C  EB           xba                     ; E0 M16 X16 C?
C0:712D  29 00 FF     and #$FF00              ; E0 M16 X16 C?
C0:7130  8D C4 5D     sta $5DC4               ; E0 M16 X16 C?
C0:7133  A5 04        lda $04                 ; E0 M16 X16 C?
C0:7135  0A           asl a                   ; E0 M16 X16 C?
C0:7136  AA           tax                     ; E0 M16 X16 C?
C0:7137  A4 18        ldy $18                 ; E0 M16 X16 C?
C0:7139  98           tya                     ; E0 M16 X16 C?
C0:713A  18           clc                     ; E0 M16 X16 C?
C0:713B  7F 10 E2 C3  adc $C3E210,x           ; E0 M16 X16 C0
C0:713F  85 16        sta $16                 ; E0 M16 X16 C?
C0:7141  A5 02        lda $02                 ; E0 M16 X16 C?
C0:7143  18           clc                     ; E0 M16 X16 C?
C0:7144  7F 18 E2 C3  adc $C3E218,x           ; E0 M16 X16 C0
C0:7148  85 02        sta $02                 ; E0 M16 X16 C?
C0:714A  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:714C  A4 16        ldy $16                 ; E0 M16 X16 C?
C0:714E  AE 7B 98     ldx $987B               ; E0 M16 X16 C?
C0:7151  AD 77 98     lda $9877               ; E0 M16 X16 C?
C0:7154  22 58 8D C4  jsl $C48D58             ; E0 M16 X16 C?
C0:7158  A8           tay                     ; E0 M16 X16 C?
C0:7159  84 14        sty $14                 ; E0 M16 X16 C?
C0:715B  D0 03        bne $7160               ; E0 M16 X16 C?
C0:715D  C8           iny                     ; E0 M16 X16 C?
C0:715E  84 14        sty $14                 ; E0 M16 X16 C?
Code_C07160:
C0:7160  A2 06 00     ldx #$0006              ; E0 M16 X16 C?
C0:7163  86 12        stx $12                 ; E0 M16 X16 C?
C0:7165  A5 04        lda $04                 ; E0 M16 X16 C?
C0:7167  0A           asl a                   ; E0 M16 X16 C?
C0:7168  AA           tax                     ; E0 M16 X16 C?
C0:7169  BF 00 E2 C3  lda $C3E200,x           ; E0 M16 X16 C?
C0:716D  A6 12        ldx $12                 ; E0 M16 X16 C?
C0:716F  22 6B 8E C4  jsl $C48E6B             ; E0 M16 X16 C?
C0:7173  A9 82 6F     lda #$6F82              ; E0 M16 X16 C?
C0:7176  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:7178  A9 C0 00     lda #$00C0              ; E0 M16 X16 C?
C0:717B  85 10        sta $10                 ; E0 M16 X16 C?
C0:717D  A4 14        ldy $14                 ; E0 M16 X16 C?
C0:717F  98           tya                     ; E0 M16 X16 C?
C0:7180  22 E6 DB C0  jsl $C0DBE6             ; E0 M16 X16 C?
C0:7184  80 4F        bra $71D5               ; E0 M16 X16 C?
Code_C07186:
C0:7186  A5 04        lda $04                 ; E0 M16 X16 C?
C0:7188  0A           asl a                   ; E0 M16 X16 C?
C0:7189  AA           tax                     ; E0 M16 X16 C?
C0:718A  98           tya                     ; E0 M16 X16 C?
C0:718B  18           clc                     ; E0 M16 X16 C?
C0:718C  7F 20 E2 C3  adc $C3E220,x           ; E0 M16 X16 C0
C0:7190  85 16        sta $16                 ; E0 M16 X16 C?
C0:7192  A5 02        lda $02                 ; E0 M16 X16 C?
C0:7194  18           clc                     ; E0 M16 X16 C?
C0:7195  7F 28 E2 C3  adc $C3E228,x           ; E0 M16 X16 C0
C0:7199  85 02        sta $02                 ; E0 M16 X16 C?
C0:719B  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:719D  A4 16        ldy $16                 ; E0 M16 X16 C?
C0:719F  AE 7B 98     ldx $987B               ; E0 M16 X16 C?
C0:71A2  AD 77 98     lda $9877               ; E0 M16 X16 C?
C0:71A5  22 58 8D C4  jsl $C48D58             ; E0 M16 X16 C?
C0:71A9  A8           tay                     ; E0 M16 X16 C?
C0:71AA  84 14        sty $14                 ; E0 M16 X16 C?
C0:71AC  D0 03        bne $71B1               ; E0 M16 X16 C?
C0:71AE  C8           iny                     ; E0 M16 X16 C?
C0:71AF  84 14        sty $14                 ; E0 M16 X16 C?
Code_C071B1:
C0:71B1  A2 0C 00     ldx #$000C              ; E0 M16 X16 C?
C0:71B4  86 18        stx $18                 ; E0 M16 X16 C?
C0:71B6  A5 04        lda $04                 ; E0 M16 X16 C?
C0:71B8  0A           asl a                   ; E0 M16 X16 C?
C0:71B9  AA           tax                     ; E0 M16 X16 C?
C0:71BA  BF 08 E2 C3  lda $C3E208,x           ; E0 M16 X16 C?
C0:71BE  A6 18        ldx $18                 ; E0 M16 X16 C?
C0:71C0  22 6B 8E C4  jsl $C48E6B             ; E0 M16 X16 C?
C0:71C4  A9 ED 6F     lda #$6FED              ; E0 M16 X16 C?
C0:71C7  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:71C9  A9 C0 00     lda #$00C0              ; E0 M16 X16 C?
C0:71CC  85 10        sta $10                 ; E0 M16 X16 C?
C0:71CE  A4 14        ldy $14                 ; E0 M16 X16 C?
C0:71D0  98           tya                     ; E0 M16 X16 C?
C0:71D1  22 E6 DB C0  jsl $C0DBE6             ; E0 M16 X16 C?
Code_C071D5:
C0:71D5  A5 16        lda $16                 ; E0 M16 X16 C?
C0:71D7  8D CC 5D     sta $5DCC               ; E0 M16 X16 C?
C0:71DA  A5 02        lda $02                 ; E0 M16 X16 C?
C0:71DC  8D CE 5D     sta $5DCE               ; E0 M16 X16 C?
C0:71DF  22 95 8E C4  jsl $C48E95             ; E0 M16 X16 C?
Code_C071E3:
C0:71E3  2B           pld                     ; E0 M16 X16 C?
C0:71E4  60           rts                     ; E0 M16 X16 C?
Lookup_MovementTriggerType:
C0:7477  C2 31        rep #$31                ; E0 M16 X16 C?
C0:7479  0B           phd                     ; E0 M16 X16 C?
C0:747A  48           pha                     ; E0 M16 X16 C?
C0:747B  7B           tdc                     ; E0 M16 X16 C?
C0:747C  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:747F  5B           tcd                     ; E0 M16 X16 C?
C0:7480  68           pla                     ; E0 M16 X16 C?
C0:7481  9B           txy                     ; E0 M16 X16 C?
C0:7482  84 10        sty $10                 ; E0 M16 X16 C?
C0:7484  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:7486  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:7489  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:748B  A9 D0 00     lda #$00D0              ; E0 M16 X16 C?
C0:748E  85 0C        sta $0C                 ; E0 M16 X16 C?
C0:7490  A5 0E        lda $0E                 ; E0 M16 X16 C?
C0:7492  4A           lsr a                   ; E0 M16 X16 C?
C0:7493  4A           lsr a                   ; E0 M16 X16 C?
C0:7494  4A           lsr a                   ; E0 M16 X16 C?
C0:7495  4A           lsr a                   ; E0 M16 X16 C?
C0:7496  4A           lsr a                   ; E0 M16 X16 C?
C0:7497  85 02        sta $02                 ; E0 M16 X16 C?
C0:7499  98           tya                     ; E0 M16 X16 C?
C0:749A  29 E0 FF     and #$FFE0              ; E0 M16 X16 C?
C0:749D  18           clc                     ; E0 M16 X16 C?
C0:749E  65 02        adc $02                 ; E0 M16 X16 C0
C0:74A0  0A           asl a                   ; E0 M16 X16 C?
C0:74A1  0A           asl a                   ; E0 M16 X16 C?
C0:74A2  18           clc                     ; E0 M16 X16 C?
C0:74A3  65 0A        adc $0A                 ; E0 M16 X16 C0
C0:74A5  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:74A7  A0 02 00     ldy #$0002              ; E0 M16 X16 C?
C0:74AA  B7 0A        lda [$0A],y             ; E0 M16 X16 C?
C0:74AC  A8           tay                     ; E0 M16 X16 C?
C0:74AD  A7 0A        lda [$0A]               ; E0 M16 X16 C?
C0:74AF  85 06        sta $06                 ; E0 M16 X16 C?
C0:74B1  84 08        sty $08                 ; E0 M16 X16 C?
C0:74B3  A7 06        lda [$06]               ; E0 M16 X16 C?
C0:74B5  AA           tax                     ; E0 M16 X16 C?
C0:74B6  D0 06        bne $74BE               ; E0 M16 X16 C?
C0:74B8  E2 20        sep #$20                ; E0 M16 X16 C?
C0:74BA  A9 FF        lda #$FF                ; E0 M8 X16 C?
C0:74BC  80 66        bra $7524               ; E0 M8 X16 C?
Code_C074BE:
C0:74BE  E6 06        inc $06                 ; E0 M16 X16 C?
C0:74C0  E6 06        inc $06                 ; E0 M16 X16 C?
C0:74C2  A5 0E        lda $0E                 ; E0 M16 X16 C?
C0:74C4  29 1F 00     and #$001F              ; E0 M16 X16 C?
C0:74C7  85 02        sta $02                 ; E0 M16 X16 C?
C0:74C9  A4 10        ldy $10                 ; E0 M16 X16 C?
C0:74CB  98           tya                     ; E0 M16 X16 C?
C0:74CC  29 1F 00     and #$001F              ; E0 M16 X16 C?
C0:74CF  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:74D1  80 48        bra $751B               ; E0 M16 X16 C?
Code_C074D3:
C0:74D3  E2 20        sep #$20                ; E0 M16 X16 C?
C0:74D5  A0 01 00     ldy #$0001              ; E0 M8 X16 C?
C0:74D8  B7 06        lda [$06],y             ; E0 M8 X16 C?
C0:74DA  C2 20        rep #$20                ; E0 M8 X16 C?
C0:74DC  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:74DF  C5 02        cmp $02                 ; E0 M16 X16 C?
C0:74E1  D0 2F        bne $7512               ; E0 M16 X16 C?
C0:74E3  A5 0E        lda $0E                 ; E0 M16 X16 C?
C0:74E5  85 04        sta $04                 ; E0 M16 X16 C?
C0:74E7  A5 06        lda $06                 ; E0 M16 X16 C?
C0:74E9  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:74EB  A5 08        lda $08                 ; E0 M16 X16 C?
C0:74ED  85 0C        sta $0C                 ; E0 M16 X16 C?
C0:74EF  A7 0A        lda [$0A]               ; E0 M16 X16 C?
C0:74F1  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:74F4  C5 04        cmp $04                 ; E0 M16 X16 C?
C0:74F6  D0 1A        bne $7512               ; E0 M16 X16 C?
C0:74F8  A0 03 00     ldy #$0003              ; E0 M16 X16 C?
C0:74FB  B7 06        lda [$06],y             ; E0 M16 X16 C?
C0:74FD  8D BC 5D     sta $5DBC               ; E0 M16 X16 C?
C0:7500  E6 06        inc $06                 ; E0 M16 X16 C?
C0:7502  E6 06        inc $06                 ; E0 M16 X16 C?
C0:7504  A7 06        lda [$06]               ; E0 M16 X16 C?
C0:7506  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:7509  8D BE 5D     sta $5DBE               ; E0 M16 X16 C?
C0:750C  E2 20        sep #$20                ; E0 M16 X16 C?
C0:750E  A7 06        lda [$06]               ; E0 M8 X16 C?
C0:7510  80 12        bra $7524               ; E0 M8 X16 C?
Code_C07512:
C0:7512  A9 05 00     lda #$0005              ; E0 M16 X16 C?
C0:7515  18           clc                     ; E0 M16 X16 C?
C0:7516  65 06        adc $06                 ; E0 M16 X16 C0
C0:7518  85 06        sta $06                 ; E0 M16 X16 C?
C0:751A  CA           dex                     ; E0 M16 X16 C?
Code_C0751B:
C0:751B  E0 00 00     cpx #$0000              ; E0 M16 X16 C?
C0:751E  D0 B3        bne $74D3               ; E0 M16 X16 C?
C0:7520  E2 20        sep #$20                ; E0 M16 X16 C?
C0:7522  A9 FF        lda #$FF                ; E0 M8 X16 C?
Code_C07524:
C0:7524  2B           pld                     ; E0 M8 X16 C?
C0:7525  6B           rtl                     ; E0 M8 X16 C?
Dispatch_MovementHelperFromLookup:
C0:7526  C2 31        rep #$31                ; E0 M16 X16 C?
C0:7528  0B           phd                     ; E0 M16 X16 C?
C0:7529  48           pha                     ; E0 M16 X16 C?
C0:752A  7B           tdc                     ; E0 M16 X16 C?
C0:752B  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:752E  5B           tcd                     ; E0 M16 X16 C?
C0:752F  68           pla                     ; E0 M16 X16 C?
C0:7530  9B           txy                     ; E0 M16 X16 C?
C0:7531  84 10        sty $10                 ; E0 M16 X16 C?
C0:7533  85 02        sta $02                 ; E0 M16 X16 C?
C0:7535  BB           tyx                     ; E0 M16 X16 C?
C0:7536  A5 02        lda $02                 ; E0 M16 X16 C?
C0:7538  22 77 74 C0  jsl $C07477             ; E0 M16 X16 C?
C0:753C  C2 20        rep #$20                ; E0 M16 X16 C?
C0:753E  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:7541  F0 25        beq $7568               ; E0 M16 X16 C?
C0:7543  C9 01 00     cmp #$0001              ; E0 M16 X16 C?
C0:7546  F0 2F        beq $7577               ; E0 M16 X16 C?
C0:7548  C9 02 00     cmp #$0002              ; E0 M16 X16 C?
C0:754B  F0 39        beq $7586               ; E0 M16 X16 C?
C0:754D  C9 03 00     cmp #$0003              ; E0 M16 X16 C?
C0:7550  F0 43        beq $7595               ; E0 M16 X16 C?
C0:7552  C9 04 00     cmp #$0004              ; E0 M16 X16 C?
C0:7555  F0 51        beq $75A8               ; E0 M16 X16 C?
C0:7557  C9 05 00     cmp #$0005              ; E0 M16 X16 C?
C0:755A  F0 5F        beq $75BB               ; E0 M16 X16 C?
C0:755C  C9 07 00     cmp #$0007              ; E0 M16 X16 C?
C0:755F  F0 5A        beq $75BB               ; E0 M16 X16 C?
C0:7561  C9 06 00     cmp #$0006              ; E0 M16 X16 C?
C0:7564  F0 64        beq $75CA               ; E0 M16 X16 C?
C0:7566  80 6F        bra $75D7               ; E0 M16 X16 C?
Code_C07568:
C0:7568  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:756B  20 1B 6A     jsr $6A1B               ; E0 M16 X16 C?
C0:756E  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:7571  85 04        sta $04                 ; E0 M16 X16 C?
C0:7573  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:7575  80 60        bra $75D7               ; E0 M16 X16 C?
Code_C07577:
C0:7577  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:757A  20 91 6A     jsr $6A91               ; E0 M16 X16 C?
C0:757D  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:7580  85 04        sta $04                 ; E0 M16 X16 C?
C0:7582  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:7584  80 51        bra $75D7               ; E0 M16 X16 C?
Code_C07586:
C0:7586  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:7589  20 CA 6A     jsr $6ACA               ; E0 M16 X16 C?
C0:758C  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:758F  85 04        sta $04                 ; E0 M16 X16 C?
C0:7591  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:7593  80 42        bra $75D7               ; E0 M16 X16 C?
Code_C07595:
C0:7595  A4 10        ldy $10                 ; E0 M16 X16 C?
C0:7597  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:7599  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:759C  20 6E 6E     jsr $6E6E               ; E0 M16 X16 C?
C0:759F  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:75A2  85 04        sta $04                 ; E0 M16 X16 C?
C0:75A4  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:75A6  80 2F        bra $75D7               ; E0 M16 X16 C?
Code_C075A8:
C0:75A8  A4 10        ldy $10                 ; E0 M16 X16 C?
C0:75AA  A6 02        ldx $02                 ; E0 M16 X16 C?
C0:75AC  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:75AF  20 CB 70     jsr $70CB               ; E0 M16 X16 C?
C0:75B2  A9 01 00     lda #$0001              ; E0 M16 X16 C?
C0:75B5  85 04        sta $04                 ; E0 M16 X16 C?
C0:75B7  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:75B9  80 1C        bra $75D7               ; E0 M16 X16 C?
Code_C075BB:
C0:75BB  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:75BE  20 8B 6A     jsr $6A8B               ; E0 M16 X16 C?
C0:75C1  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:75C4  85 04        sta $04                 ; E0 M16 X16 C?
C0:75C6  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:75C8  80 0D        bra $75D7               ; E0 M16 X16 C?
Code_C075CA:
C0:75CA  AD BC 5D     lda $5DBC               ; E0 M16 X16 C?
C0:75CD  20 8E 6A     jsr $6A8E               ; E0 M16 X16 C?
C0:75D0  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:75D3  85 04        sta $04                 ; E0 M16 X16 C?
C0:75D5  85 0E        sta $0E                 ; E0 M16 X16 C?
Code_C075D7:
C0:75D7  A5 0E        lda $0E                 ; E0 M16 X16 C?
C0:75D9  85 04        sta $04                 ; E0 M16 X16 C?
C0:75DB  2B           pld                     ; E0 M16 X16 C?
C0:75DC  6B           rtl                     ; E0 M16 X16 C?
Process_StagedMovementQueueEntry:
C0:75DD  C2 31        rep #$31                ; E0 M16 X16 C?
C0:75DF  0B           phd                     ; E0 M16 X16 C?
C0:75E0  7B           tdc                     ; E0 M16 X16 C?
C0:75E1  69 EC FF     adc #$FFEC              ; E0 M16 X16 C?
C0:75E4  5B           tcd                     ; E0 M16 X16 C?
C0:75E5  AD 02 5E     lda $5E02               ; E0 M16 X16 C?
C0:75E8  85 04        sta $04                 ; E0 M16 X16 C?
C0:75EA  0A           asl a                   ; E0 M16 X16 C?
C0:75EB  65 04        adc $04                 ; E0 M16 X16 C?
C0:75ED  0A           asl a                   ; E0 M16 X16 C?
C0:75EE  AA           tax                     ; E0 M16 X16 C?
C0:75EF  BD EA 5D     lda $5DEA,x             ; E0 M16 X16 C?
C0:75F2  85 12        sta $12                 ; E0 M16 X16 C?
C0:75F4  8A           txa                     ; E0 M16 X16 C?
C0:75F5  18           clc                     ; E0 M16 X16 C?
C0:75F6  69 EC 5D     adc #$5DEC              ; E0 M16 X16 C0
C0:75F9  A8           tay                     ; E0 M16 X16 C?
C0:75FA  B9 00 00     lda $0000,y             ; E0 M16 X16 C?
C0:75FD  85 06        sta $06                 ; E0 M16 X16 C?
C0:75FF  B9 02 00     lda $0002,y             ; E0 M16 X16 C?
C0:7602  85 08        sta $08                 ; E0 M16 X16 C?
C0:7604  A5 12        lda $12                 ; E0 M16 X16 C?
C0:7606  8D C0 5D     sta $5DC0               ; E0 M16 X16 C?
C0:7609  AD 02 5E     lda $5E02               ; E0 M16 X16 C?
C0:760C  1A           inc a                   ; E0 M16 X16 C?
C0:760D  29 03 00     and #$0003              ; E0 M16 X16 C?
C0:7610  8D 02 5E     sta $5E02               ; E0 M16 X16 C?
C0:7613  AD 58 5D     lda $5D58               ; E0 M16 X16 C?
C0:7616  29 FE FF     and #$FFFE              ; E0 M16 X16 C?
C0:7619  8D 58 5D     sta $5D58               ; E0 M16 X16 C?
C0:761C  22 5B 7C C0  jsl $C07C5B             ; E0 M16 X16 C?
C0:7620  A5 12        lda $12                 ; E0 M16 X16 C?
C0:7622  C9 02 00     cmp #$0002              ; E0 M16 X16 C?
C0:7625  F0 16        beq $763D               ; E0 M16 X16 C?
C0:7627  C9 0A 00     cmp #$000A              ; E0 M16 X16 C?
C0:762A  F0 1E        beq $764A               ; E0 M16 X16 C?
C0:762C  C9 00 00     cmp #$0000              ; E0 M16 X16 C?
C0:762F  F0 46        beq $7677               ; E0 M16 X16 C?
C0:7631  C9 08 00     cmp #$0008              ; E0 M16 X16 C?
C0:7634  F0 41        beq $7677               ; E0 M16 X16 C?
C0:7636  C9 09 00     cmp #$0009              ; E0 M16 X16 C?
C0:7639  F0 3C        beq $7677               ; E0 M16 X16 C?
C0:763B  80 46        bra $7683               ; E0 M16 X16 C?
Code_C0763D:
C0:763D  A5 06        lda $06                 ; E0 M16 X16 C?
C0:763F  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:7641  A5 08        lda $08                 ; E0 M16 X16 C?
C0:7643  85 10        sta $10                 ; E0 M16 X16 C?
C0:7645  20 FF 6B     jsr $6BFF               ; E0 M16 X16 C?
C0:7648  80 39        bra $7683               ; E0 M16 X16 C?
Code_C0764A:
C0:764A  A5 06        lda $06                 ; E0 M16 X16 C?
C0:764C  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:764E  A5 08        lda $08                 ; E0 M16 X16 C?
C0:7650  85 10        sta $10                 ; E0 M16 X16 C?
C0:7652  22 04 00 C1  jsl $C10004             ; E0 M16 X16 C?
C0:7656  A9 3E D3     lda #$D33E              ; E0 M16 X16 C?
C0:7659  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:765B  A9 C7 00     lda #$00C7              ; E0 M16 X16 C?
C0:765E  85 0C        sta $0C                 ; E0 M16 X16 C?
C0:7660  A5 08        lda $08                 ; E0 M16 X16 C?
C0:7662  C5 0C        cmp $0C                 ; E0 M16 X16 C?
C0:7664  D0 04        bne $766A               ; E0 M16 X16 C?
C0:7666  A5 06        lda $06                 ; E0 M16 X16 C?
C0:7668  C5 0A        cmp $0A                 ; E0 M16 X16 C?
Code_C0766A:
C0:766A  D0 17        bne $7683               ; E0 M16 X16 C?
C0:766C  A9 97 06     lda #$0697              ; E0 M16 X16 C?
C0:766F  8D 54 9E     sta $9E54               ; E0 M16 X16 C?
C0:7672  9C 56 9E     stz $9E56               ; E0 M16 X16 C?
C0:7675  80 0C        bra $7683               ; E0 M16 X16 C?
Code_C07677:
C0:7677  A5 06        lda $06                 ; E0 M16 X16 C?
C0:7679  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:767B  A5 08        lda $08                 ; E0 M16 X16 C?
C0:767D  85 10        sta $10                 ; E0 M16 X16 C?
C0:767F  22 04 00 C1  jsl $C10004             ; E0 M16 X16 C?
Code_C07683:
C0:7683  A2 00 00     ldx #$0000              ; E0 M16 X16 C?
C0:7686  AD 02 5E     lda $5E02               ; E0 M16 X16 C?
C0:7689  CD 04 5E     cmp $5E04               ; E0 M16 X16 C?
C0:768C  F0 03        beq $7691               ; E0 M16 X16 C?
C0:768E  A2 01 00     ldx #$0001              ; E0 M16 X16 C?
Code_C07691:
C0:7691  8E 9A 5D     stx $5D9A               ; E0 M16 X16 C?
C0:7694  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:7697  8D C0 5D     sta $5DC0               ; E0 M16 X16 C?
C0:769A  2B           pld                     ; E0 M16 X16 C?
C0:769B  6B           rtl                     ; E0 M16 X16 C?
Boot_InitHardware:
C0:8000  9C 00 42     stz $4200               ; E0 M8 X8 C1
C0:8003  64 00        stz $00                 ; E0 M8 X8 C1
C0:8005  A2 00        ldx #$00                ; E0 M8 X8 C1
C0:8007  A0 01        ldy #$01                ; E0 M8 X8 C1
C0:8009  C2 30        rep #$30                ; E0 M8 X8 C1
C0:800B  A9 FE 1F     lda #$1FFE              ; E0 M16 X16 C1
C0:800E  54 00 00     mvn $00, $00            ; E0 M16 X16 C1
C0:8011  9A           txs                     ; E0 M16 X16 C1
C0:8012  A9 00 1F     lda #$1F00              ; E0 M16 X16 C1
C0:8015  5B           tcd                     ; E0 M16 X16 C1
C0:8016  E2 20        sep #$20                ; E0 M16 X16 C1
C0:8018  A9 80        lda #$80                ; E0 M8 X16 C1
C0:801A  8D 00 21     sta $2100               ; E0 M8 X16 C1
C0:801D  8D 0D 00     sta $000D               ; E0 M8 X16 C1
C0:8020  9C 01 21     stz $2101               ; E0 M8 X16 C1
C0:8023  9C 02 21     stz $2102               ; E0 M8 X16 C1
C0:8026  9C 03 21     stz $2103               ; E0 M8 X16 C1
C0:8029  9C 05 21     stz $2105               ; E0 M8 X16 C1
C0:802C  9C 06 21     stz $2106               ; E0 M8 X16 C1
C0:802F  9C 07 21     stz $2107               ; E0 M8 X16 C1
C0:8032  9C 08 21     stz $2108               ; E0 M8 X16 C1
C0:8035  9C 09 21     stz $2109               ; E0 M8 X16 C1
C0:8038  9C 0A 21     stz $210A               ; E0 M8 X16 C1
C0:803B  9C 0B 21     stz $210B               ; E0 M8 X16 C1
C0:803E  9C 0C 21     stz $210C               ; E0 M8 X16 C1
C0:8041  9C 0D 21     stz $210D               ; E0 M8 X16 C1
C0:8044  9C 0D 21     stz $210D               ; E0 M8 X16 C1
C0:8047  9C 0E 21     stz $210E               ; E0 M8 X16 C1
C0:804A  9C 0E 21     stz $210E               ; E0 M8 X16 C1
C0:804D  9C 0F 21     stz $210F               ; E0 M8 X16 C1
C0:8050  9C 0F 21     stz $210F               ; E0 M8 X16 C1
C0:8053  9C 10 21     stz $2110               ; E0 M8 X16 C1
C0:8056  9C 10 21     stz $2110               ; E0 M8 X16 C1
C0:8059  9C 11 21     stz $2111               ; E0 M8 X16 C1
C0:805C  9C 11 21     stz $2111               ; E0 M8 X16 C1
C0:805F  9C 12 21     stz $2112               ; E0 M8 X16 C1
C0:8062  9C 12 21     stz $2112               ; E0 M8 X16 C1
C0:8065  9C 13 21     stz $2113               ; E0 M8 X16 C1
C0:8068  9C 13 21     stz $2113               ; E0 M8 X16 C1
C0:806B  9C 14 21     stz $2114               ; E0 M8 X16 C1
C0:806E  9C 14 21     stz $2114               ; E0 M8 X16 C1
C0:8071  A9 80        lda #$80                ; E0 M8 X16 C1
C0:8073  8D 15 21     sta $2115               ; E0 M8 X16 C1
C0:8076  9C 16 21     stz $2116               ; E0 M8 X16 C1
C0:8079  9C 17 21     stz $2117               ; E0 M8 X16 C1
C0:807C  9C 1A 21     stz $211A               ; E0 M8 X16 C1
C0:807F  9C 1B 21     stz $211B               ; E0 M8 X16 C1
C0:8082  A9 01        lda #$01                ; E0 M8 X16 C1
C0:8084  8D 1B 21     sta $211B               ; E0 M8 X16 C1
C0:8087  9C 1C 21     stz $211C               ; E0 M8 X16 C1
C0:808A  9C 1C 21     stz $211C               ; E0 M8 X16 C1
C0:808D  9C 1D 21     stz $211D               ; E0 M8 X16 C1
C0:8090  9C 1D 21     stz $211D               ; E0 M8 X16 C1
C0:8093  9C 1E 21     stz $211E               ; E0 M8 X16 C1
C0:8096  8D 1E 21     sta $211E               ; E0 M8 X16 C1
C0:8099  9C 1F 21     stz $211F               ; E0 M8 X16 C1
C0:809C  9C 1F 21     stz $211F               ; E0 M8 X16 C1
C0:809F  9C 20 21     stz $2120               ; E0 M8 X16 C1
C0:80A2  9C 20 21     stz $2120               ; E0 M8 X16 C1
C0:80A5  9C 21 21     stz $2121               ; E0 M8 X16 C1
C0:80A8  9C 23 21     stz $2123               ; E0 M8 X16 C1
C0:80AB  9C 24 21     stz $2124               ; E0 M8 X16 C1
C0:80AE  9C 25 21     stz $2125               ; E0 M8 X16 C1
C0:80B1  9C 26 21     stz $2126               ; E0 M8 X16 C1
C0:80B4  9C 27 21     stz $2127               ; E0 M8 X16 C1
C0:80B7  9C 28 21     stz $2128               ; E0 M8 X16 C1
C0:80BA  9C 29 21     stz $2129               ; E0 M8 X16 C1
C0:80BD  9C 2A 21     stz $212A               ; E0 M8 X16 C1
C0:80C0  9C 2B 21     stz $212B               ; E0 M8 X16 C1
C0:80C3  A9 1F        lda #$1F                ; E0 M8 X16 C1
C0:80C5  8D 2C 21     sta $212C               ; E0 M8 X16 C1
C0:80C8  9C 2D 21     stz $212D               ; E0 M8 X16 C1
C0:80CB  9C 2E 21     stz $212E               ; E0 M8 X16 C1
C0:80CE  9C 2F 21     stz $212F               ; E0 M8 X16 C1
C0:80D1  9C 30 21     stz $2130               ; E0 M8 X16 C1
C0:80D4  9C 31 21     stz $2131               ; E0 M8 X16 C1
C0:80D7  A9 E0        lda #$E0                ; E0 M8 X16 C1
C0:80D9  8D 32 21     sta $2132               ; E0 M8 X16 C1
C0:80DC  9C 33 21     stz $2133               ; E0 M8 X16 C1
C0:80DF  A9 FF        lda #$FF                ; E0 M8 X16 C1
C0:80E1  8D 02 42     sta $4202               ; E0 M8 X16 C1
C0:80E4  9C 02 42     stz $4202               ; E0 M8 X16 C1
C0:80E7  9C 03 42     stz $4203               ; E0 M8 X16 C1
C0:80EA  9C 04 42     stz $4204               ; E0 M8 X16 C1
C0:80ED  9C 05 42     stz $4205               ; E0 M8 X16 C1
C0:80F0  9C 06 42     stz $4206               ; E0 M8 X16 C1
C0:80F3  9C 07 42     stz $4207               ; E0 M8 X16 C1
C0:80F6  9C 08 42     stz $4208               ; E0 M8 X16 C1
C0:80F9  9C 09 42     stz $4209               ; E0 M8 X16 C1
C0:80FC  9C 0A 42     stz $420A               ; E0 M8 X16 C1
C0:80FF  9C 0B 42     stz $420B               ; E0 M8 X16 C1
C0:8102  9C 0C 42     stz $420C               ; E0 M8 X16 C1
C0:8105  A9 01        lda #$01                ; E0 M8 X16 C1
C0:8107  8D 0D 42     sta $420D               ; E0 M8 X16 C1
C0:810A  C2 30        rep #$30                ; E0 M8 X16 C1
C0:810C  A9 FF DF     lda #$DFFF              ; E0 M16 X16 C1
C0:810F  54 7E 7E     mvn $7E, $7E            ; E0 M16 X16 C1
C0:8112  A9 00 20     lda #$2000              ; E0 M16 X16 C1
C0:8115  8D A1 00     sta $00A1               ; E0 M16 X16 C1
C0:8118  8D A3 00     sta $00A3               ; E0 M16 X16 C1
C0:811B  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C1
C0:811E  8D 02 24     sta $2402               ; E0 M16 X16 C1
C0:8121  A9 34 12     lda #$1234              ; E0 M16 X16 C1
C0:8124  8D 24 00     sta $0024               ; E0 M16 X16 C1
C0:8127  A9 78 56     lda #$5678              ; E0 M16 X16 C1
C0:812A  8D 26 00     sta $0026               ; E0 M16 X16 C1
C0:812D  A9 01 00     lda #$0001              ; E0 M16 X16 C1
C0:8130  8D 2E 00     sta $002E               ; E0 M16 X16 C1
C0:8133  A9 1B 85     lda #$851B              ; E0 M16 X16 C1
C0:8136  8D 20 00     sta $0020               ; E0 M16 X16 C1
C0:8139  22 19 8B C0  jsl $C08B19             ; E0 M16 X16 C1
C0:813D  5C 9A B9 C0  jml $C0B99A             ; E0 M16 X16 C1
ResetVector_008141:
C0:8141  18           clc                     ; E1 M8 X8 C?
C0:8142  FB           xce                     ; E1 M8 X8 C0
C0:8143  5C 00 80 C0  jml $C08000             ; E0 M8 X8 C1
NativeNMI_008147:
C0:8147  5C 70 81 C0  jml $C08170             ; E0 M8 X8 C?
NativeIRQ_00814B:
C0:814B  5C 4F 81 C0  jml $C0814F             ; E0 M8 X8 C?
IRQ_Prologue:
C0:814F  08           php                     ; E0 M8 X8 C?
C0:8150  C2 30        rep #$30                ; E0 M8 X8 C?
C0:8152  48           pha                     ; E0 M16 X16 C?
C0:8153  DA           phx                     ; E0 M16 X16 C?
C0:8154  5A           phy                     ; E0 M16 X16 C?
C0:8155  0B           phd                     ; E0 M16 X16 C?
C0:8156  F4 00 00     pea $0000               ; E0 M16 X16 C?
C0:8159  2B           pld                     ; E0 M16 X16 C?
C0:815A  8B           phb                     ; E0 M16 X16 C?
C0:815B  F4 00 00     pea $0000               ; E0 M16 X16 C?
C0:815E  AB           plb                     ; E0 M16 X16 C?
C0:815F  AB           plb                     ; E0 M16 X16 C?
C0:8160  E2 20        sep #$20                ; E0 M16 X16 C?
C0:8162  AD 11 42     lda $4211               ; E0 M8 X16 C?
C0:8165  30 1C        bmi $8183               ; E0 M8 X16 C?
C0:8167  C2 30        rep #$30                ; E0 M8 X16 C?
C0:8169  AB           plb                     ; E0 M16 X16 C?
C0:816A  2B           pld                     ; E0 M16 X16 C?
C0:816B  7A           ply                     ; E0 M16 X16 C?
C0:816C  FA           plx                     ; E0 M16 X16 C?
C0:816D  68           pla                     ; E0 M16 X16 C?
C0:816E  28           plp                     ; E0 M16 X16 C?
C0:816F  40           rti                     ; E0 M16 X16 C?
NMI_Prologue:
C0:8170  08           php                     ; E0 M8 X8 C?
C0:8171  C2 30        rep #$30                ; E0 M8 X8 C?
C0:8173  48           pha                     ; E0 M16 X16 C?
C0:8174  DA           phx                     ; E0 M16 X16 C?
C0:8175  5A           phy                     ; E0 M16 X16 C?
C0:8176  0B           phd                     ; E0 M16 X16 C?
C0:8177  F4 00 00     pea $0000               ; E0 M16 X16 C?
C0:817A  2B           pld                     ; E0 M16 X16 C?
C0:817B  8B           phb                     ; E0 M16 X16 C?
C0:817C  F4 00 00     pea $0000               ; E0 M16 X16 C?
C0:817F  AB           plb                     ; E0 M16 X16 C?
C0:8180  AB           plb                     ; E0 M16 X16 C?
C0:8181  E2 20        sep #$20                ; E0 M16 X16 C?
NMI_FrameUpdate:
C0:8183  AD 10 42     lda $4210               ; E0 M8 X16 C?
C0:8186  9C 0C 42     stz $420C               ; E0 M8 X16 C?
C0:8189  A9 80        lda #$80                ; E0 M8 X16 C?
C0:818B  8D 00 21     sta $2100               ; E0 M8 X16 C?
C0:818E  E6 2B        inc $2B                 ; E0 M8 X16 C?
C0:8190  E6 02        inc $02                 ; E0 M8 X16 C?
C0:8192  C2 20        rep #$20                ; E0 M8 X16 C?
C0:8194  E2 10        sep #$10                ; E0 M16 X16 C?
C0:8196  A6 2C        ldx $2C                 ; E0 M16 X8 C?
C0:8198  F0 2E        beq $81C8               ; E0 M16 X8 C?
C0:819A  A0 00        ldy #$00                ; E0 M16 X8 C?
C0:819C  9C 02 21     stz $2102               ; E0 M16 X8 C?
C0:819F  8C 00 43     sty $4300               ; E0 M16 X8 C?
C0:81A2  8C 04 43     sty $4304               ; E0 M16 X8 C?
C0:81A5  A0 04        ldy #$04                ; E0 M16 X8 C?
C0:81A7  8C 01 43     sty $4301               ; E0 M16 X8 C?
C0:81AA  A9 00 05     lda #$0500              ; E0 M16 X8 C?
C0:81AD  A6 2C        ldx $2C                 ; E0 M16 X8 C?
C0:81AF  CA           dex                     ; E0 M16 X8 C?
C0:81B0  F0 03        beq $81B5               ; E0 M16 X8 C?
C0:81B2  A9 00 08     lda #$0800              ; E0 M16 X8 C?
Code_C081B5:
C0:81B5  8D 02 43     sta $4302               ; E0 M16 X8 C?
C0:81B8  A9 20 02     lda #$0220              ; E0 M16 X8 C?
C0:81BB  8D 05 43     sta $4305               ; E0 M16 X8 C?
C0:81BE  A0 01        ldy #$01                ; E0 M16 X8 C?
C0:81C0  8C 0B 42     sty $420B               ; E0 M16 X8 C?
C0:81C3  18           clc                     ; E0 M16 X8 C?
C0:81C4  65 99        adc $99                 ; E0 M16 X8 C0
C0:81C6  85 99        sta $99                 ; E0 M16 X8 C?
Code_C081C8:
C0:81C8  AE 30 00     ldx $0030               ; E0 M16 X8 C?
C0:81CB  F0 2A        beq $81F7               ; E0 M16 X8 C?
C0:81CD  BD 94 8F     lda $8F94,x             ; E0 M16 X8 C?
C0:81D0  8D 02 43     sta $4302               ; E0 M16 X8 C?
C0:81D3  BC 96 8F     ldy $8F96,x             ; E0 M16 X8 C?
C0:81D6  8C 21 21     sty $2121               ; E0 M16 X8 C?
C0:81D9  A9 00 22     lda #$2200              ; E0 M16 X8 C?
C0:81DC  8D 00 43     sta $4300               ; E0 M16 X8 C?
C0:81DF  A0 00        ldy #$00                ; E0 M16 X8 C?
C0:81E1  8C 04 43     sty $4304               ; E0 M16 X8 C?
C0:81E4  8C 30 00     sty $0030               ; E0 M16 X8 C?
C0:81E7  BD 92 8F     lda $8F92,x             ; E0 M16 X8 C?
C0:81EA  8D 05 43     sta $4305               ; E0 M16 X8 C?
C0:81ED  A0 01        ldy #$01                ; E0 M16 X8 C?
C0:81EF  8C 0B 42     sty $420B               ; E0 M16 X8 C?
C0:81F2  18           clc                     ; E0 M16 X8 C?
C0:81F3  65 99        adc $99                 ; E0 M16 X8 C0
C0:81F5  85 99        sta $99                 ; E0 M16 X8 C?
Code_C081F7:
C0:81F7  E2 20        sep #$20                ; E0 M16 X8 C?
C0:81F9  A5 28        lda $28                 ; E0 M8 X8 C?
C0:81FB  F0 22        beq $821F               ; E0 M8 X8 C?
C0:81FD  C6 2A        dec $2A                 ; E0 M8 X8 C?
C0:81FF  10 1E        bpl $821F               ; E0 M8 X8 C?
C0:8201  A5 29        lda $29                 ; E0 M8 X8 C?
C0:8203  85 2A        sta $2A                 ; E0 M8 X8 C?
C0:8205  A5 0D        lda $0D                 ; E0 M8 X8 C?
C0:8207  29 0F        and #$0F                ; E0 M8 X8 C?
C0:8209  18           clc                     ; E0 M8 X8 C?
C0:820A  65 28        adc $28                 ; E0 M8 X8 C0
C0:820C  10 07        bpl $8215               ; E0 M8 X8 C?
C0:820E  9C 1F 00     stz $001F               ; E0 M8 X8 C?
C0:8211  A9 80        lda #$80                ; E0 M8 X8 C?
C0:8213  80 06        bra $821B               ; E0 M8 X8 C?
Code_C08215:
C0:8215  C9 10        cmp #$10                ; E0 M8 X8 C?
C0:8217  90 04        bcc $821D               ; E0 M8 X8 C?
C0:8219  A9 0F        lda #$0F                ; E0 M8 X8 C?
Code_C0821B:
C0:821B  64 28        stz $28                 ; E0 M8 X8 C?
Code_C0821D:
C0:821D  85 0D        sta $0D                 ; E0 M8 X8 C?
Code_C0821F:
C0:821F  C2 10        rep #$10                ; E0 M8 X8 C?
C0:8221  A5 0D        lda $0D                 ; E0 M8 X16 C?
C0:8223  8D 00 21     sta $2100               ; E0 M8 X16 C?
C0:8226  A5 10        lda $10                 ; E0 M8 X16 C?
C0:8228  8D 06 21     sta $2106               ; E0 M8 X16 C?
C0:822B  A4 15        ldy $15                 ; E0 M8 X16 C?
C0:822D  8C 0B 21     sty $210B               ; E0 M8 X16 C?
C0:8230  A4 17        ldy $17                 ; E0 M8 X16 C?
C0:8232  A0 FF 00     ldy #$00FF              ; E0 M8 X16 C?
C0:8235  8C 28 21     sty $2128               ; E0 M8 X16 C?
C0:8238  C2 20        rep #$20                ; E0 M8 X16 C?
C0:823A  E2 10        sep #$10                ; E0 M16 X16 C?
C0:823C  A6 01        ldx $01                 ; E0 M16 X8 C?
C0:823E  80 32        bra $8272               ; E0 M16 X8 C?
NMI_ProcessTransferQueue:
C0:8240  BC 00 04     ldy $0400,x             ; E0 M16 X8 C?
C0:8243  B9 B0 8F     lda $8FB0,y             ; E0 M16 X8 C?
C0:8246  8D 00 43     sta $4300               ; E0 M16 X8 C?
C0:8249  B9 B2 8F     lda $8FB2,y             ; E0 M16 X8 C?
C0:824C  8D 15 21     sta $2115               ; E0 M16 X8 C?
C0:824F  BD 01 04     lda $0401,x             ; E0 M16 X8 C?
C0:8252  8D 05 43     sta $4305               ; E0 M16 X8 C?
C0:8255  BD 03 04     lda $0403,x             ; E0 M16 X8 C?
C0:8258  8D 02 43     sta $4302               ; E0 M16 X8 C?
C0:825B  BC 05 04     ldy $0405,x             ; E0 M16 X8 C?
C0:825E  8C 04 43     sty $4304               ; E0 M16 X8 C?
C0:8261  BD 06 04     lda $0406,x             ; E0 M16 X8 C?
C0:8264  8D 16 21     sta $2116               ; E0 M16 X8 C?
C0:8267  8A           txa                     ; E0 M16 X8 C?
C0:8268  18           clc                     ; E0 M16 X8 C?
C0:8269  69 08 00     adc #$0008              ; E0 M16 X8 C0
C0:826C  AA           tax                     ; E0 M16 X8 C?
C0:826D  A0 01        ldy #$01                ; E0 M16 X8 C?
C0:826F  8C 0B 42     sty $420B               ; E0 M16 X8 C?
Code_C08272:
C0:8272  E4 00        cpx $00                 ; E0 M16 X8 C?
C0:8274  D0 CA        bne $8240               ; E0 M16 X8 C?
C0:8276  86 01        stx $01                 ; E0 M16 X8 C?
C0:8278  E2 20        sep #$20                ; E0 M16 X8 C?
C0:827A  A5 2C        lda $2C                 ; E0 M8 X8 C?
C0:827C  D0 03        bne $8281               ; E0 M8 X8 C?
C0:827E  4C 34 83     jmp $8334               ; E0 M8 X8 C?
NMI_ApplyScrollSetA:
C0:8281  3A           dec a                   ; E0 M8 X8 C?
C0:8282  D0 52        bne $82D6               ; E0 M8 X8 C?
C0:8284  A5 41        lda $41                 ; E0 M8 X8 C?
C0:8286  8D 0D 21     sta $210D               ; E0 M8 X8 C?
C0:8289  A5 42        lda $42                 ; E0 M8 X8 C?
C0:828B  8D 0D 21     sta $210D               ; E0 M8 X8 C?
C0:828E  A5 45        lda $45                 ; E0 M8 X8 C?
C0:8290  8D 0E 21     sta $210E               ; E0 M8 X8 C?
C0:8293  A5 46        lda $46                 ; E0 M8 X8 C?
C0:8295  8D 0E 21     sta $210E               ; E0 M8 X8 C?
C0:8298  A5 49        lda $49                 ; E0 M8 X8 C?
C0:829A  8D 0F 21     sta $210F               ; E0 M8 X8 C?
C0:829D  A5 4A        lda $4A                 ; E0 M8 X8 C?
C0:829F  8D 0F 21     sta $210F               ; E0 M8 X8 C?
C0:82A2  A5 4D        lda $4D                 ; E0 M8 X8 C?
C0:82A4  8D 10 21     sta $2110               ; E0 M8 X8 C?
C0:82A7  A5 4E        lda $4E                 ; E0 M8 X8 C?
C0:82A9  8D 10 21     sta $2110               ; E0 M8 X8 C?
C0:82AC  A5 51        lda $51                 ; E0 M8 X8 C?
C0:82AE  8D 11 21     sta $2111               ; E0 M8 X8 C?
C0:82B1  A5 52        lda $52                 ; E0 M8 X8 C?
C0:82B3  8D 11 21     sta $2111               ; E0 M8 X8 C?
C0:82B6  A5 55        lda $55                 ; E0 M8 X8 C?
C0:82B8  8D 12 21     sta $2112               ; E0 M8 X8 C?
C0:82BB  A5 56        lda $56                 ; E0 M8 X8 C?
C0:82BD  8D 12 21     sta $2112               ; E0 M8 X8 C?
C0:82C0  A5 59        lda $59                 ; E0 M8 X8 C?
C0:82C2  8D 13 21     sta $2113               ; E0 M8 X8 C?
C0:82C5  A5 5A        lda $5A                 ; E0 M8 X8 C?
C0:82C7  8D 13 21     sta $2113               ; E0 M8 X8 C?
C0:82CA  A5 5D        lda $5D                 ; E0 M8 X8 C?
C0:82CC  8D 14 21     sta $2114               ; E0 M8 X8 C?
C0:82CF  A5 5E        lda $5E                 ; E0 M8 X8 C?
C0:82D1  8D 14 21     sta $2114               ; E0 M8 X8 C?
C0:82D4  80 5E        bra $8334               ; E0 M8 X8 C?
NMI_ApplyScrollSetB:
C0:82D6  A5 43        lda $43                 ; E0 M8 X8 C?
C0:82D8  8D 0D 21     sta $210D               ; E0 M8 X8 C?
C0:82DB  A5 44        lda $44                 ; E0 M8 X8 C?
C0:82DD  8D 0D 21     sta $210D               ; E0 M8 X8 C?
C0:82E0  A5 47        lda $47                 ; E0 M8 X8 C?
C0:82E2  8D 0E 21     sta $210E               ; E0 M8 X8 C?
C0:82E5  A5 48        lda $48                 ; E0 M8 X8 C?
C0:82E7  8D 0E 21     sta $210E               ; E0 M8 X8 C?
C0:82EA  A5 4B        lda $4B                 ; E0 M8 X8 C?
C0:82EC  8D 0F 21     sta $210F               ; E0 M8 X8 C?
C0:82EF  A5 4C        lda $4C                 ; E0 M8 X8 C?
C0:82F1  8D 0F 21     sta $210F               ; E0 M8 X8 C?
C0:82F4  A5 4F        lda $4F                 ; E0 M8 X8 C?
C0:82F6  8D 10 21     sta $2110               ; E0 M8 X8 C?
C0:82F9  A5 50        lda $50                 ; E0 M8 X8 C?
C0:82FB  8D 10 21     sta $2110               ; E0 M8 X8 C?
C0:82FE  A5 53        lda $53                 ; E0 M8 X8 C?
C0:8300  8D 11 21     sta $2111               ; E0 M8 X8 C?
C0:8303  A5 54        lda $54                 ; E0 M8 X8 C?
C0:8305  8D 11 21     sta $2111               ; E0 M8 X8 C?
C0:8308  A5 57        lda $57                 ; E0 M8 X8 C?
C0:830A  8D 12 21     sta $2112               ; E0 M8 X8 C?
C0:830D  A5 58        lda $58                 ; E0 M8 X8 C?
C0:830F  8D 12 21     sta $2112               ; E0 M8 X8 C?
C0:8312  A5 5B        lda $5B                 ; E0 M8 X8 C?
C0:8314  8D 13 21     sta $2113               ; E0 M8 X8 C?
C0:8317  A5 5C        lda $5C                 ; E0 M8 X8 C?
C0:8319  8D 13 21     sta $2113               ; E0 M8 X8 C?
C0:831C  A5 5F        lda $5F                 ; E0 M8 X8 C?
C0:831E  8D 14 21     sta $2114               ; E0 M8 X8 C?
C0:8321  A5 60        lda $60                 ; E0 M8 X8 C?
C0:8323  8D 14 21     sta $2114               ; E0 M8 X8 C?
C0:8326  C2 20        rep #$20                ; E0 M8 X8 C?
C0:8328  AD 31 00     lda $0031               ; E0 M16 X8 C?
C0:832B  8D 61 00     sta $0061               ; E0 M16 X8 C?
C0:832E  AD 33 00     lda $0033               ; E0 M16 X8 C?
C0:8331  8D 63 00     sta $0063               ; E0 M16 X8 C?
NMI_FinalizeFrame:
C0:8334  A0 00        ldy #$00                ; E0 M8 X8 C?
C0:8336  84 2C        sty $2C                 ; E0 M8 X8 C?
C0:8338  A6 0D        ldx $0D                 ; E0 M8 X8 C?
C0:833A  30 0F        bmi $834B               ; E0 M8 X8 C?
C0:833C  A6 1A        ldx $1A                 ; E0 M8 X8 C?
C0:833E  8E 2C 21     stx $212C               ; E0 M8 X8 C?
C0:8341  A6 1B        ldx $1B                 ; E0 M8 X8 C?
C0:8343  8E 2D 21     stx $212D               ; E0 M8 X8 C?
C0:8346  A6 1F        ldx $1F                 ; E0 M8 X8 C?
C0:8348  8E 0C 42     stx $420C               ; E0 M8 X8 C?
Code_C0834B:
C0:834B  20 01 85     jsr $8501               ; E0 M8 X8 C?
C0:834E  C2 30        rep #$30                ; E0 M8 X8 C?
C0:8350  64 99        stz $99                 ; E0 M16 X16 C?
C0:8352  AD 22 00     lda $0022               ; E0 M16 X16 C?
C0:8355  D0 16        bne $836D               ; E0 M16 X16 C?
C0:8357  EE 22 00     inc $0022               ; E0 M16 X16 C?
C0:835A  8B           phb                     ; E0 M16 X16 C?
C0:835B  F4 7E 7E     pea $7E7E               ; E0 M16 X16 C?
C0:835E  AB           plb                     ; E0 M16 X16 C?
C0:835F  AB           plb                     ; E0 M16 X16 C?
C0:8360  0B           phd                     ; E0 M16 X16 C?
C0:8361  F4 00 02     pea $0200               ; E0 M16 X16 C?
C0:8364  2B           pld                     ; E0 M16 X16 C?
C0:8365  20 18 85     jsr $8518               ; E0 M16 X16 C?
C0:8368  2B           pld                     ; E0 M16 X16 C?
C0:8369  AB           plb                     ; E0 M16 X16 C?
C0:836A  9C 22 00     stz $0022               ; E0 M16 X16 C?
Code_C0836D:
C0:836D  A9 00 20     lda #$2000              ; E0 M16 X16 C?
C0:8370  C5 A3        cmp $A3                 ; E0 M16 X16 C?
C0:8372  D0 03        bne $8377               ; E0 M16 X16 C?
C0:8374  A9 00 22     lda #$2200              ; E0 M16 X16 C?
Code_C08377:
C0:8377  85 A3        sta $A3                 ; E0 M16 X16 C?
C0:8379  85 A1        sta $A1                 ; E0 M16 X16 C?
C0:837B  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:837E  8F 2B 9E 7E  sta $7E9E2B             ; E0 M16 X16 C?
C0:8382  64 AB        stz $AB                 ; E0 M16 X16 C?
C0:8384  E6 A7        inc $A7                 ; E0 M16 X16 C?
C0:8386  D0 02        bne $838A               ; E0 M16 X16 C?
C0:8388  E6 A9        inc $A9                 ; E0 M16 X16 C?
Code_C0838A:
C0:838A  AB           plb                     ; E0 M16 X16 C?
C0:838B  2B           pld                     ; E0 M16 X16 C?
C0:838C  7A           ply                     ; E0 M16 X16 C?
C0:838D  FA           plx                     ; E0 M16 X16 C?
C0:838E  68           pla                     ; E0 M16 X16 C?
C0:838F  28           plp                     ; E0 M16 X16 C?
C0:8390  40           rti                     ; E0 M16 X16 C?
NMI_ServiceAudioQueue:
C0:8501  E2 30        sep #$30                ; E0 M8 X8 C?
C0:8503  A6 CB        ldx $CB                 ; E0 M8 X8 C?
C0:8505  E4 CA        cpx $CA                 ; E0 M8 X8 C?
C0:8507  F0 0C        beq $8515               ; E0 M8 X8 C?
C0:8509  BD C2 1A     lda $1AC2,x             ; E0 M8 X8 C?
C0:850C  8D 43 21     sta $2143               ; E0 M8 X8 C?
C0:850F  8A           txa                     ; E0 M8 X8 C?
C0:8510  1A           inc a                   ; E0 M8 X8 C?
C0:8511  29 07        and #$07                ; E0 M8 X8 C?
C0:8513  85 CB        sta $CB                 ; E0 M8 X8 C?
Code_C08515:
C0:8515  C2 30        rep #$30                ; E0 M8 X8 C?
C0:8517  60           rts                     ; E0 M16 X16 C?
Frame_CallbackDispatcher:
C0:8518  6C 20 00     jmp ($0020)             ; E0 M16 X16 C?
Frame_CallbackReturn:
C0:851B  60           rts                     ; E0 M16 X16 C?
Set_FrameCallbackPtr:
C0:851C  C2 30        rep #$30                ; E0 M16 X16 C?
C0:851E  8D 20 00     sta $0020               ; E0 M16 X16 C?
C0:8521  6B           rtl                     ; E0 M16 X16 C?
Reset_FrameCallbackToDefault:
C0:8522  A9 1B 85     lda #$851B              ; E0 M16 X16 C?
C0:8525  8D 20 00     sta $0020               ; E0 M16 X16 C?
C0:8528  6B           rtl                     ; E0 M16 X16 C?
Dispatch_DelayedActionTarget:
C0:9279  DC BC 00     jml [$00BC]             ; E0 M16 X16 C?
Init_DelayedActionPools:
C0:927C  A9 0F DB     lda #$DB0F              ; E0 M16 X16 C?
C0:927F  8D 5E 0A     sta $0A5E               ; E0 M16 X16 C?
C0:9282  A2 FF FF     ldx #$FFFF              ; E0 M16 X16 C?
C0:9285  8E 50 0A     stx $0A50               ; E0 M16 X16 C?
C0:9288  8E D8 0A     stx $0AD8               ; E0 M16 X16 C?
C0:928B  8E E4 12     stx $12E4               ; E0 M16 X16 C?
C0:928E  E8           inx                     ; E0 M16 X16 C?
C0:928F  8E 52 0A     stx $0A52               ; E0 M16 X16 C?
C0:9292  8E 54 0A     stx $0A54               ; E0 M16 X16 C?
C0:9295  18           clc                     ; E0 M16 X16 C?
C0:9296  A2 38 00     ldx #$0038              ; E0 M16 X16 C0
Code_C09299:
C0:9299  8A           txa                     ; E0 M16 X16 C0
C0:929A  69 02 00     adc #$0002              ; E0 M16 X16 C0
C0:929D  9D 9E 0A     sta $0A9E,x             ; E0 M16 X16 C?
C0:92A0  CA           dex                     ; E0 M16 X16 C?
C0:92A1  CA           dex                     ; E0 M16 X16 C?
C0:92A2  10 F5        bpl $9299               ; E0 M16 X16 C?
C0:92A4  A2 88 00     ldx #$0088              ; E0 M16 X16 C?
Code_C092A7:
C0:92A7  8A           txa                     ; E0 M16 X16 C?
C0:92A8  69 02 00     adc #$0002              ; E0 M16 X16 C?
C0:92AB  9D 5A 12     sta $125A,x             ; E0 M16 X16 C?
C0:92AE  CA           dex                     ; E0 M16 X16 C?
C0:92AF  CA           dex                     ; E0 M16 X16 C?
C0:92B0  10 F5        bpl $92A7               ; E0 M16 X16 C?
C0:92B2  A2 3A 00     ldx #$003A              ; E0 M16 X16 C?
C0:92B5  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
Code_C092B8:
C0:92B8  9D 62 0A     sta $0A62,x             ; E0 M16 X16 C?
C0:92BB  CA           dex                     ; E0 M16 X16 C?
C0:92BC  CA           dex                     ; E0 M16 X16 C?
C0:92BD  10 F9        bpl $92B8               ; E0 M16 X16 C?
C0:92BF  A2 3A 00     ldx #$003A              ; E0 M16 X16 C?
Code_C092C2:
C0:92C2  9E 6A 11     stz $116A,x             ; E0 M16 X16 C?
C0:92C5  9E B6 10     stz $10B6,x             ; E0 M16 X16 C?
C0:92C8  CA           dex                     ; E0 M16 X16 C?
C0:92C9  CA           dex                     ; E0 M16 X16 C?
C0:92CA  10 F6        bpl $92C2               ; E0 M16 X16 C?
C0:92CC  A2 06 00     ldx #$0006              ; E0 M16 X16 C?
Code_C092CF:
C0:92CF  9E 12 1A     stz $1A12,x             ; E0 M16 X16 C?
C0:92D2  9E 1A 1A     stz $1A1A,x             ; E0 M16 X16 C?
C0:92D5  9E 22 1A     stz $1A22,x             ; E0 M16 X16 C?
C0:92D8  9E 32 1A     stz $1A32,x             ; E0 M16 X16 C?
C0:92DB  9E 2A 1A     stz $1A2A,x             ; E0 M16 X16 C?
C0:92DE  9E 3A 1A     stz $1A3A,x             ; E0 M16 X16 C?
C0:92E1  9E 02 1A     stz $1A02,x             ; E0 M16 X16 C?
C0:92E4  9E 0A 1A     stz $1A0A,x             ; E0 M16 X16 C?
C0:92E7  9E 3E 10     stz $103E,x             ; E0 M16 X16 C?
C0:92EA  CA           dex                     ; E0 M16 X16 C?
C0:92EB  CA           dex                     ; E0 M16 X16 C?
C0:92EC  10 E1        bpl $92CF               ; E0 M16 X16 C?
C0:92EE  20 00 00     jsr $0000               ; E0 M16 X16 C?
C0:92F1  9C 60 0A     stz $0A60               ; E0 M16 X16 C?
C0:92F4  6B           rtl                     ; E0 M16 X16 C?
Init_DelayedActionState:
C0:9321  48           pha                     ; E0 M16 X16 C?
C0:9322  5A           phy                     ; E0 M16 X16 C?
C0:9323  DA           phx                     ; E0 M16 X16 C?
C0:9324  AD 4C 0A     lda $0A4C               ; E0 M16 X16 C?
C0:9327  0A           asl a                   ; E0 M16 X16 C?
C0:9328  8D 4C 0A     sta $0A4C               ; E0 M16 X16 C?
C0:932B  AD 4E 0A     lda $0A4E               ; E0 M16 X16 C?
C0:932E  0A           asl a                   ; E0 M16 X16 C?
C0:932F  8D 4E 0A     sta $0A4E               ; E0 M16 X16 C?
C0:9332  20 02 9C     jsr $9C02               ; E0 M16 X16 C?
C0:9335  90 07        bcc $933E               ; E0 M16 X16 C?
C0:9337  68           pla                     ; E0 M16 X16 C?
C0:9338  68           pla                     ; E0 M16 X16 C?
C0:9339  68           pla                     ; E0 M16 X16 C?
C0:933A  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:933D  6B           rtl                     ; E0 M16 X16 C?
Code_C0933E:
C0:933E  20 03 9D     jsr $9D03               ; E0 M16 X16 C?
C0:9341  98           tya                     ; E0 M16 X16 C?
C0:9342  9D DA 0A     sta $0ADA,x             ; E0 M16 X16 C?
C0:9345  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:9348  99 5A 12     sta $125A,y             ; E0 M16 X16 C?
C0:934B  A9 C8 9F     lda #$9FC8              ; E0 M16 X16 C?
C0:934E  9D 1E 12     sta $121E,x             ; E0 M16 X16 C?
C0:9351  A9 23 A0     lda #$A023              ; E0 M16 X16 C?
C0:9354  9D A6 11     sta $11A6,x             ; E0 M16 X16 C?
C0:9357  A9 A4 A3     lda #$A3A4              ; E0 M16 X16 C?
C0:935A  9D E2 11     sta $11E2,x             ; E0 M16 X16 C?
C0:935D  AD 38 0A     lda $0A38               ; E0 M16 X16 C?
C0:9360  9D 5E 0E     sta $0E5E,x             ; E0 M16 X16 C?
C0:9363  AD 3A 0A     lda $0A3A               ; E0 M16 X16 C?
C0:9366  9D 9A 0E     sta $0E9A,x             ; E0 M16 X16 C?
C0:9369  AD 3C 0A     lda $0A3C               ; E0 M16 X16 C?
C0:936C  9D D6 0E     sta $0ED6,x             ; E0 M16 X16 C?
C0:936F  AD 3E 0A     lda $0A3E               ; E0 M16 X16 C?
C0:9372  9D 12 0F     sta $0F12,x             ; E0 M16 X16 C?
C0:9375  AD 40 0A     lda $0A40               ; E0 M16 X16 C?
C0:9378  9D 4E 0F     sta $0F4E,x             ; E0 M16 X16 C?
C0:937B  AD 42 0A     lda $0A42               ; E0 M16 X16 C?
C0:937E  9D 8A 0F     sta $0F8A,x             ; E0 M16 X16 C?
C0:9381  AD 44 0A     lda $0A44               ; E0 M16 X16 C?
C0:9384  9D C6 0F     sta $0FC6,x             ; E0 M16 X16 C?
C0:9387  AD 46 0A     lda $0A46               ; E0 M16 X16 C?
C0:938A  9D 02 10     sta $1002,x             ; E0 M16 X16 C?
C0:938D  AD 4A 0A     lda $0A4A               ; E0 M16 X16 C?
C0:9390  9D 3E 10     sta $103E,x             ; E0 M16 X16 C?
C0:9393  A9 00 80     lda #$8000              ; E0 M16 X16 C?
C0:9396  9D 42 0C     sta $0C42,x             ; E0 M16 X16 C?
C0:9399  9D 7E 0C     sta $0C7E,x             ; E0 M16 X16 C?
C0:939C  9D BA 0C     sta $0CBA,x             ; E0 M16 X16 C?
C0:939F  68           pla                     ; E0 M16 X16 C?
C0:93A0  9D 8E 0B     sta $0B8E,x             ; E0 M16 X16 C?
C0:93A3  9D 16 0B     sta $0B16,x             ; E0 M16 X16 C?
C0:93A6  68           pla                     ; E0 M16 X16 C?
C0:93A7  9D CA 0B     sta $0BCA,x             ; E0 M16 X16 C?
C0:93AA  9D 52 0B     sta $0B52,x             ; E0 M16 X16 C?
C0:93AD  AD 48 0A     lda $0A48               ; E0 M16 X16 C?
C0:93B0  9D 06 0C     sta $0C06,x             ; E0 M16 X16 C?
C0:93B3  20 57 9C     jsr $9C57               ; E0 M16 X16 C?
C0:93B6  68           pla                     ; E0 M16 X16 C?
C0:93B7  80 12        bra $93CB               ; E0 M16 X16 C?
Code_C093CB:
C0:93CB  9D 62 0A     sta $0A62,x             ; E0 M16 X16 C?
C0:93CE  DA           phx                     ; E0 M16 X16 C?
C0:93CF  0A           asl a                   ; E0 M16 X16 C?
C0:93D0  7D 62 0A     adc $0A62,x             ; E0 M16 X16 C?
C0:93D3  9B           txy                     ; E0 M16 X16 C?
C0:93D4  AA           tax                     ; E0 M16 X16 C?
C0:93D5  BF D6 00 C4  lda $C400D6,x           ; E0 M16 X16 C?
C0:93D9  A8           tay                     ; E0 M16 X16 C?
C0:93DA  BF D4 00 C4  lda $C400D4,x           ; E0 M16 X16 C?
C0:93DE  FA           plx                     ; E0 M16 X16 C?
C0:93DF  9E F2 10     stz $10F2,x             ; E0 M16 X16 C?
C0:93E2  DE F2 10     dec $10F2,x             ; E0 M16 X16 C?
C0:93E5  9E AA 0D     stz $0DAA,x             ; E0 M16 X16 C?
C0:93E8  9E F6 0C     stz $0CF6,x             ; E0 M16 X16 C?
C0:93EB  9E E6 0D     stz $0DE6,x             ; E0 M16 X16 C?
C0:93EE  9E 32 0D     stz $0D32,x             ; E0 M16 X16 C?
C0:93F1  9E 22 0E     stz $0E22,x             ; E0 M16 X16 C?
C0:93F4  9E 6E 0D     stz $0D6E,x             ; E0 M16 X16 C?
C0:93F7  80 25        bra $941E               ; E0 M16 X16 C?
Code_C0941E:
C0:941E  5A           phy                     ; E0 M16 X16 C?
C0:941F  48           pha                     ; E0 M16 X16 C?
C0:9420  20 A1 9D     jsr $9DA1               ; E0 M16 X16 C?
C0:9423  9B           txy                     ; E0 M16 X16 C?
C0:9424  BE DA 0A     ldx $0ADA,y             ; E0 M16 X16 C?
C0:9427  68           pla                     ; E0 M16 X16 C?
C0:9428  9D FE 13     sta $13FE,x             ; E0 M16 X16 C?
C0:942B  68           pla                     ; E0 M16 X16 C?
C0:942C  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:942F  9D 8A 14     sta $148A,x             ; E0 M16 X16 C?
C0:9432  9E 72 13     stz $1372,x             ; E0 M16 X16 C?
C0:9435  9E E6 12     stz $12E6,x             ; E0 M16 X16 C?
C0:9438  98           tya                     ; E0 M16 X16 C?
C0:9439  4A           lsr a                   ; E0 M16 X16 C?
C0:943A  18           clc                     ; E0 M16 X16 C?
C0:943B  6B           rtl                     ; E0 M16 X16 C0
Process_ActiveTaskSlots:
C0:94AA  8E 42 1A     stx $1A42               ; E0 M16 X16 C?
C0:94AD  4E 42 1A     lsr $1A42               ; E0 M16 X16 C?
C0:94B0  86 88        stx $88                 ; E0 M16 X16 C?
C0:94B2  3C B6 10     bit $10B6,x             ; E0 M16 X16 C?
C0:94B5  70 03        bvs $94BA               ; E0 M16 X16 C?
C0:94B7  FC 1E 12     jsr ($121E,x)           ; E0 M16 X16 C?
Code_C094BA:
C0:94BA  FC A6 11     jsr ($11A6,x)           ; E0 M16 X16 C?
C0:94BD  A6 88        ldx $88                 ; E0 M16 X16 C?
C0:94BF  BD 9E 0A     lda $0A9E,x             ; E0 M16 X16 C?
C0:94C2  AA           tax                     ; E0 M16 X16 C?
C0:94C3  10 E5        bpl $94AA               ; E0 M16 X16 C?
C0:94C5  A2 00 00     ldx #$0000              ; E0 M16 X16 C?
C0:94C8  FC 5E 0A     jsr ($0A5E,x)           ; E0 M16 X16 C?
C0:94CB  2B           pld                     ; E0 M16 X16 C?
C0:94CC  9C 60 0A     stz $0A60               ; E0 M16 X16 C?
C0:94CF  6B           rtl                     ; E0 M16 X16 C?
Process_TaskSlotRecordChain:
C0:94D0  3C B6 10     bit $10B6,x             ; E0 M16 X16 C?
C0:94D3  70 1E        bvs $94F3               ; E0 M16 X16 C?
C0:94D5  BC DA 0A     ldy $0ADA,x             ; E0 M16 X16 C?
Code_C094D8:
C0:94D8  84 8A        sty $8A                 ; E0 M16 X16 C?
C0:94DA  8C 48 1A     sty $1A48               ; E0 M16 X16 C?
C0:94DD  8C 46 1A     sty $1A46               ; E0 M16 X16 C?
C0:94E0  4E 46 1A     lsr $1A46               ; E0 M16 X16 C?
C0:94E3  B9 5A 12     lda $125A,y             ; E0 M16 X16 C?
C0:94E6  8D 58 0A     sta $0A58               ; E0 M16 X16 C?
C0:94E9  20 06 95     jsr $9506               ; E0 M16 X16 C?
C0:94EC  AC 58 0A     ldy $0A58               ; E0 M16 X16 C?
C0:94EF  10 E7        bpl $94D8               ; E0 M16 X16 C?
C0:94F1  A6 88        ldx $88                 ; E0 M16 X16 C?
Code_C094F3:
C0:94F3  BD B6 10     lda $10B6,x             ; E0 M16 X16 C?
C0:94F6  30 0D        bmi $9505               ; E0 M16 X16 C?
C0:94F8  8D 5C 0A     sta $0A5C               ; E0 M16 X16 C?
C0:94FB  BD 7A 10     lda $107A,x             ; E0 M16 X16 C?
C0:94FE  8D 5A 0A     sta $0A5A               ; E0 M16 X16 C?
C0:9501  22 9E 9D C0  jsl $C09D9E             ; E0 M16 X16 C?
Code_C09505:
C0:9505  60           rts                     ; E0 M16 X16 C?
Alloc_TaskSlotOrFail:
C0:9C02  AD 54 0A     lda $0A54               ; E0 M16 X16 C?
C0:9C05  30 19        bmi $9C20               ; E0 M16 X16 C?
C0:9C07  A0 FF FF     ldy #$FFFF              ; E0 M16 X16 C?
C0:9C0A  AD 52 0A     lda $0A52               ; E0 M16 X16 C?
C0:9C0D  30 11        bmi $9C20               ; E0 M16 X16 C?
Code_C09C0F:
C0:9C0F  AA           tax                     ; E0 M16 X16 C?
C0:9C10  EC 4C 0A     cpx $0A4C               ; E0 M16 X16 C?
C0:9C13  90 05        bcc $9C1A               ; E0 M16 X16 C?
C0:9C15  EC 4E 0A     cpx $0A4E               ; E0 M16 X16 C?
C0:9C18  90 08        bcc $9C22               ; E0 M16 X16 C?
Code_C09C1A:
C0:9C1A  9B           txy                     ; E0 M16 X16 C?
C0:9C1B  BD 9E 0A     lda $0A9E,x             ; E0 M16 X16 C?
C0:9C1E  10 EF        bpl $9C0F               ; E0 M16 X16 C?
Code_C09C20:
C0:9C20  38           sec                     ; E0 M16 X16 C?
C0:9C21  60           rts                     ; E0 M16 X16 C1
Code_C09C22:
C0:9C22  98           tya                     ; E0 M16 X16 C?
C0:9C23  10 08        bpl $9C2D               ; E0 M16 X16 C?
C0:9C25  BD 9E 0A     lda $0A9E,x             ; E0 M16 X16 C?
C0:9C28  8D 52 0A     sta $0A52               ; E0 M16 X16 C?
C0:9C2B  18           clc                     ; E0 M16 X16 C?
C0:9C2C  60           rts                     ; E0 M16 X16 C0
Code_C09C2D:
C0:9C2D  BD 9E 0A     lda $0A9E,x             ; E0 M16 X16 C?
C0:9C30  99 9E 0A     sta $0A9E,y             ; E0 M16 X16 C?
C0:9C33  18           clc                     ; E0 M16 X16 C?
C0:9C34  60           rts                     ; E0 M16 X16 C0
Release_TaskSlotByIndex:
C0:9C35  0A           asl a                   ; E0 M16 X16 C?
C0:9C36  AA           tax                     ; E0 M16 X16 C?
C0:9C37  20 3B 9C     jsr $9C3B               ; E0 M16 X16 C?
C0:9C3A  6B           rtl                     ; E0 M16 X16 C?
Release_TaskSlot_Core:
C0:9C3B  48           pha                     ; E0 M16 X16 C?
C0:9C3C  BD 62 0A     lda $0A62,x             ; E0 M16 X16 C?
C0:9C3F  30 14        bmi $9C55               ; E0 M16 X16 C?
C0:9C41  5A           phy                     ; E0 M16 X16 C?
C0:9C42  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:9C45  9D 62 0A     sta $0A62,x             ; E0 M16 X16 C?
C0:9C48  20 A1 9D     jsr $9DA1               ; E0 M16 X16 C?
C0:9C4B  20 99 9C     jsr $9C99               ; E0 M16 X16 C?
C0:9C4E  20 73 9C     jsr $9C73               ; E0 M16 X16 C?
C0:9C51  20 8F 9C     jsr $9C8F               ; E0 M16 X16 C?
C0:9C54  7A           ply                     ; E0 M16 X16 C?
Code_C09C55:
C0:9C55  68           pla                     ; E0 M16 X16 C?
C0:9C56  60           rts                     ; E0 M16 X16 C?
Link_TaskSlotIntoActiveList:
C0:9C57  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:9C5A  9D 9E 0A     sta $0A9E,x             ; E0 M16 X16 C?
C0:9C5D  8A           txa                     ; E0 M16 X16 C?
C0:9C5E  AE 50 0A     ldx $0A50               ; E0 M16 X16 C?
C0:9C61  10 05        bpl $9C68               ; E0 M16 X16 C?
C0:9C63  8D 50 0A     sta $0A50               ; E0 M16 X16 C?
C0:9C66  80 09        bra $9C71               ; E0 M16 X16 C?
Code_C09C68:
C0:9C68  9B           txy                     ; E0 M16 X16 C?
C0:9C69  BE 9E 0A     ldx $0A9E,y             ; E0 M16 X16 C?
C0:9C6C  10 FA        bpl $9C68               ; E0 M16 X16 C?
C0:9C6E  99 9E 0A     sta $0A9E,y             ; E0 M16 X16 C?
Code_C09C71:
C0:9C71  AA           tax                     ; E0 M16 X16 C?
C0:9C72  60           rts                     ; E0 M16 X16 C?
Detach_TaskSlotLink:
C0:9C73  20 B5 9C     jsr $9CB5               ; E0 M16 X16 C?
C0:9C76  BD 9E 0A     lda $0A9E,x             ; E0 M16 X16 C?
C0:9C79  C0 FF FF     cpy #$FFFF              ; E0 M16 X16 C?
C0:9C7C  F0 05        beq $9C83               ; E0 M16 X16 C?
C0:9C7E  99 9E 0A     sta $0A9E,y             ; E0 M16 X16 C?
C0:9C81  80 03        bra $9C86               ; E0 M16 X16 C?
Code_C09C83:
C0:9C83  8D 50 0A     sta $0A50               ; E0 M16 X16 C?
Code_C09C86:
C0:9C86  EC 56 0A     cpx $0A56               ; E0 M16 X16 C?
C0:9C89  D0 03        bne $9C8E               ; E0 M16 X16 C?
C0:9C8B  8D 56 0A     sta $0A56               ; E0 M16 X16 C?
Code_C09C8E:
C0:9C8E  60           rts                     ; E0 M16 X16 C?
Push_TaskSlotToFreeList:
C0:9C8F  AD 52 0A     lda $0A52               ; E0 M16 X16 C?
C0:9C92  9D 9E 0A     sta $0A9E,x             ; E0 M16 X16 C?
C0:9C95  8E 52 0A     stx $0A52               ; E0 M16 X16 C?
C0:9C98  60           rts                     ; E0 M16 X16 C?
Restore_TaskRecordChain:
C0:9C99  BD DA 0A     lda $0ADA,x             ; E0 M16 X16 C?
C0:9C9C  30 16        bmi $9CB4               ; E0 M16 X16 C?
C0:9C9E  DA           phx                     ; E0 M16 X16 C?
C0:9C9F  AD 54 0A     lda $0A54               ; E0 M16 X16 C?
C0:9CA2  48           pha                     ; E0 M16 X16 C?
C0:9CA3  BD DA 0A     lda $0ADA,x             ; E0 M16 X16 C?
C0:9CA6  8D 54 0A     sta $0A54               ; E0 M16 X16 C?
Code_C09CA9:
C0:9CA9  AA           tax                     ; E0 M16 X16 C?
C0:9CAA  BD 5A 12     lda $125A,x             ; E0 M16 X16 C?
C0:9CAD  10 FA        bpl $9CA9               ; E0 M16 X16 C?
C0:9CAF  68           pla                     ; E0 M16 X16 C?
C0:9CB0  9D 5A 12     sta $125A,x             ; E0 M16 X16 C?
C0:9CB3  FA           plx                     ; E0 M16 X16 C?
Code_C09CB4:
C0:9CB4  60           rts                     ; E0 M16 X16 C?
Find_TaskSlotPredecessor:
C0:9CB5  C2 20        rep #$20                ; E0 M16 X16 C?
C0:9CB7  0B           phd                     ; E0 M16 X16 C?
C0:9CB8  48           pha                     ; E0 M16 X16 C?
C0:9CB9  7B           tdc                     ; E0 M16 X16 C?
C0:9CBA  38           sec                     ; E0 M16 X16 C?
C0:9CBB  E9 02 00     sbc #$0002              ; E0 M16 X16 C1
C0:9CBE  5B           tcd                     ; E0 M16 X16 C?
C0:9CBF  68           pla                     ; E0 M16 X16 C?
C0:9CC0  86 00        stx $00                 ; E0 M16 X16 C?
C0:9CC2  A0 FF FF     ldy #$FFFF              ; E0 M16 X16 C?
C0:9CC5  AE 50 0A     ldx $0A50               ; E0 M16 X16 C?
Code_C09CC8:
C0:9CC8  E4 00        cpx $00                 ; E0 M16 X16 C?
C0:9CCA  F0 07        beq $9CD3               ; E0 M16 X16 C?
C0:9CCC  9B           txy                     ; E0 M16 X16 C?
C0:9CCD  BD 9E 0A     lda $0A9E,x             ; E0 M16 X16 C?
C0:9CD0  AA           tax                     ; E0 M16 X16 C?
C0:9CD1  80 F5        bra $9CC8               ; E0 M16 X16 C?
Code_C09CD3:
C0:9CD3  A6 00        ldx $00                 ; E0 M16 X16 C?
C0:9CD5  2B           pld                     ; E0 M16 X16 C?
C0:9CD6  60           rts                     ; E0 M16 X16 C?
Pop_TaskRecordFromFreeList:
C0:9D03  AC 54 0A     ldy $0A54               ; E0 M16 X16 C?
C0:9D06  10 02        bpl $9D0A               ; E0 M16 X16 C?
C0:9D08  38           sec                     ; E0 M16 X16 C?
C0:9D09  60           rts                     ; E0 M16 X16 C1
Code_C09D0A:
C0:9D0A  B9 5A 12     lda $125A,y             ; E0 M16 X16 C?
C0:9D0D  8D 54 0A     sta $0A54               ; E0 M16 X16 C?
C0:9D10  18           clc                     ; E0 M16 X16 C?
C0:9D11  60           rts                     ; E0 M16 X16 C0
Push_TaskRecordToFreeList:
C0:9D12  20 1F 9D     jsr $9D1F               ; E0 M16 X16 C?
C0:9D15  AD 54 0A     lda $0A54               ; E0 M16 X16 C?
C0:9D18  99 5A 12     sta $125A,y             ; E0 M16 X16 C?
C0:9D1B  8C 54 0A     sty $0A54               ; E0 M16 X16 C?
C0:9D1E  60           rts                     ; E0 M16 X16 C?
Unlink_TaskRecordFromSlotChain:
C0:9D1F  DA           phx                     ; E0 M16 X16 C?
C0:9D20  20 3E 9D     jsr $9D3E               ; E0 M16 X16 C?
C0:9D23  B9 5A 12     lda $125A,y             ; E0 M16 X16 C?
C0:9D26  E0 FF FF     cpx #$FFFF              ; E0 M16 X16 C?
C0:9D29  F0 06        beq $9D31               ; E0 M16 X16 C?
C0:9D2B  9D 5A 12     sta $125A,x             ; E0 M16 X16 C?
C0:9D2E  FA           plx                     ; E0 M16 X16 C?
C0:9D2F  80 04        bra $9D35               ; E0 M16 X16 C?
Code_C09D31:
C0:9D31  FA           plx                     ; E0 M16 X16 C?
C0:9D32  9D DA 0A     sta $0ADA,x             ; E0 M16 X16 C?
Code_C09D35:
C0:9D35  CC 58 0A     cpy $0A58               ; E0 M16 X16 C?
C0:9D38  D0 03        bne $9D3D               ; E0 M16 X16 C?
C0:9D3A  8D 58 0A     sta $0A58               ; E0 M16 X16 C?
Code_C09D3D:
C0:9D3D  60           rts                     ; E0 M16 X16 C?
Find_TaskRecordPredecessor:
C0:9D3E  C2 20        rep #$20                ; E0 M16 X16 C?
C0:9D40  0B           phd                     ; E0 M16 X16 C?
C0:9D41  48           pha                     ; E0 M16 X16 C?
C0:9D42  7B           tdc                     ; E0 M16 X16 C?
C0:9D43  38           sec                     ; E0 M16 X16 C?
C0:9D44  E9 02 00     sbc #$0002              ; E0 M16 X16 C1
C0:9D47  5B           tcd                     ; E0 M16 X16 C?
C0:9D48  68           pla                     ; E0 M16 X16 C?
C0:9D49  84 00        sty $00                 ; E0 M16 X16 C?
C0:9D4B  BC DA 0A     ldy $0ADA,x             ; E0 M16 X16 C?
C0:9D4E  A2 FF FF     ldx #$FFFF              ; E0 M16 X16 C?
Code_C09D51:
C0:9D51  C4 00        cpy $00                 ; E0 M16 X16 C?
C0:9D53  F0 07        beq $9D5C               ; E0 M16 X16 C?
C0:9D55  BB           tyx                     ; E0 M16 X16 C?
C0:9D56  B9 5A 12     lda $125A,y             ; E0 M16 X16 C?
C0:9D59  A8           tay                     ; E0 M16 X16 C?
C0:9D5A  80 F5        bra $9D51               ; E0 M16 X16 C?
Code_C09D5C:
C0:9D5C  A4 00        ldy $00                 ; E0 M16 X16 C?
C0:9D5E  2B           pld                     ; E0 M16 X16 C?
C0:9D5F  60           rts                     ; E0 M16 X16 C?
Init_TaskRecordDefaults:
C0:9DA1  A9 3B 94     lda #$943B              ; E0 M16 X16 C?
C0:9DA4  9D 7A 10     sta $107A,x             ; E0 M16 X16 C?
C0:9DA7  A9 C0 00     lda #$00C0              ; E0 M16 X16 C?
C0:9DAA  9D B6 10     sta $10B6,x             ; E0 M16 X16 C?
C0:9DAD  60           rts                     ; E0 M16 X16 C?
Boot_EnterMainFlow:
C0:B99A  C2 31        rep #$31                ; E0 M16 X16 C1
C0:B99C  22 9E 0B EF  jsl $EF0B9E             ; E0 M16 X16 C1
C0:B9A0  22 58 FB C4  jsl $C4FB58             ; E0 M16 X16 C1
C0:B9A4  22 15 87 C0  jsl $C08715             ; E0 M16 X16 C1
C0:B9A8  22 1C A1 C0  jsl $C0A11C             ; E0 M16 X16 C1
C0:B9AC  22 56 87 C0  jsl $C08756             ; E0 M16 X16 C1
C0:B9B0  22 56 87 C0  jsl $C08756             ; E0 M16 X16 C1
C0:B9B4  9C 6C 43     stz $436C               ; E0 M16 X16 C1
C0:B9B7  22 D8 B7 C0  jsl $C0B7D8             ; E0 M16 X16 C1
C0:B9BB  60           rts                     ; E0 M16 X16 C1
Dispatch_ActiveTaskSlots:
C0:DB0F  C2 31        rep #$31                ; E0 M16 X16 C?
C0:DB11  0B           phd                     ; E0 M16 X16 C?
C0:DB12  7B           tdc                     ; E0 M16 X16 C?
C0:DB13  69 E8 FF     adc #$FFE8              ; E0 M16 X16 C?
C0:DB16  5B           tcd                     ; E0 M16 X16 C?
C0:DB17  AD 67 00     lda $0067               ; E0 M16 X16 C?
C0:DB1A  29 00 20     and #$2000              ; E0 M16 X16 C?
C0:DB1D  F0 06        beq $DB25               ; E0 M16 X16 C?
C0:DB1F  20 31 DA     jsr $DA31               ; E0 M16 X16 C?
C0:DB22  4C E4 DB     jmp $DBE4               ; E0 M16 X16 C?
Code_C0DB25:
C0:DB25  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:DB28  85 16        sta $16                 ; E0 M16 X16 C?
C0:DB2A  AC 50 0A     ldy $0A50               ; E0 M16 X16 C?
C0:DB2D  84 14        sty $14                 ; E0 M16 X16 C?
C0:DB2F  80 4B        bra $DB7C               ; E0 M16 X16 C?
Code_C0DB31:
C0:DB31  98           tya                     ; E0 M16 X16 C?
C0:DB32  4A           lsr a                   ; E0 M16 X16 C?
C0:DB33  0A           asl a                   ; E0 M16 X16 C?
C0:DB34  AA           tax                     ; E0 M16 X16 C?
C0:DB35  BD 52 0B     lda $0B52,x             ; E0 M16 X16 C?
C0:DB38  C9 00 01     cmp #$0100              ; E0 M16 X16 C?
C0:DB3B  90 05        bcc $DB42               ; E0 M16 X16 C?
C0:DB3D  C9 C0 FF     cmp #$FFC0              ; E0 M16 X16 C?
C0:DB40  90 2F        bcc $DB71               ; E0 M16 X16 C?
Code_C0DB42:
C0:DB42  98           tya                     ; E0 M16 X16 C?
C0:DB43  4A           lsr a                   ; E0 M16 X16 C?
C0:DB44  0A           asl a                   ; E0 M16 X16 C?
C0:DB45  AA           tax                     ; E0 M16 X16 C?
C0:DB46  BD 16 0B     lda $0B16,x             ; E0 M16 X16 C?
C0:DB49  C9 40 01     cmp #$0140              ; E0 M16 X16 C?
C0:DB4C  90 05        bcc $DB53               ; E0 M16 X16 C?
C0:DB4E  C9 C0 FF     cmp #$FFC0              ; E0 M16 X16 C?
C0:DB51  90 1E        bcc $DB71               ; E0 M16 X16 C?
Code_C0DB53:
C0:DB53  98           tya                     ; E0 M16 X16 C?
C0:DB54  4A           lsr a                   ; E0 M16 X16 C?
C0:DB55  85 12        sta $12                 ; E0 M16 X16 C?
C0:DB57  0A           asl a                   ; E0 M16 X16 C?
C0:DB58  AA           tax                     ; E0 M16 X16 C?
C0:DB59  BD 3E 10     lda $103E,x             ; E0 M16 X16 C?
C0:DB5C  C9 01 00     cmp #$0001              ; E0 M16 X16 C?
C0:DB5F  D0 0B        bne $DB6C               ; E0 M16 X16 C?
C0:DB61  A5 16        lda $16                 ; E0 M16 X16 C?
C0:DB63  9D 0C 28     sta $280C,x             ; E0 M16 X16 C?
C0:DB66  A5 12        lda $12                 ; E0 M16 X16 C?
C0:DB68  85 16        sta $16                 ; E0 M16 X16 C?
C0:DB6A  80 05        bra $DB71               ; E0 M16 X16 C?
Code_C0DB6C:
C0:DB6C  A5 12        lda $12                 ; E0 M16 X16 C?
C0:DB6E  20 CA A0     jsr $A0CA               ; E0 M16 X16 C?
Code_C0DB71:
C0:DB71  A4 14        ldy $14                 ; E0 M16 X16 C?
C0:DB73  98           tya                     ; E0 M16 X16 C?
C0:DB74  4A           lsr a                   ; E0 M16 X16 C?
C0:DB75  0A           asl a                   ; E0 M16 X16 C?
C0:DB76  AA           tax                     ; E0 M16 X16 C?
C0:DB77  BC 9E 0A     ldy $0A9E,x             ; E0 M16 X16 C?
C0:DB7A  84 14        sty $14                 ; E0 M16 X16 C?
Code_C0DB7C:
C0:DB7C  98           tya                     ; E0 M16 X16 C?
C0:DB7D  1A           inc a                   ; E0 M16 X16 C?
C0:DB7E  D0 B1        bne $DB31               ; E0 M16 X16 C?
C0:DB80  80 5D        bra $DBDF               ; E0 M16 X16 C?
Code_C0DB82:
C0:DB82  A5 16        lda $16                 ; E0 M16 X16 C?
C0:DB84  85 10        sta $10                 ; E0 M16 X16 C?
C0:DB86  A5 16        lda $16                 ; E0 M16 X16 C?
C0:DB88  0A           asl a                   ; E0 M16 X16 C?
C0:DB89  AA           tax                     ; E0 M16 X16 C?
C0:DB8A  BD CA 0B     lda $0BCA,x             ; E0 M16 X16 C?
C0:DB8D  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:DB8F  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:DB92  85 04        sta $04                 ; E0 M16 X16 C?
C0:DB94  A5 16        lda $16                 ; E0 M16 X16 C?
C0:DB96  85 02        sta $02                 ; E0 M16 X16 C?
C0:DB98  BC 0C 28     ldy $280C,x             ; E0 M16 X16 C?
C0:DB9B  80 1A        bra $DBB7               ; E0 M16 X16 C?
Code_C0DB9D:
C0:DB9D  98           tya                     ; E0 M16 X16 C?
C0:DB9E  0A           asl a                   ; E0 M16 X16 C?
C0:DB9F  AA           tax                     ; E0 M16 X16 C?
C0:DBA0  BD CA 0B     lda $0BCA,x             ; E0 M16 X16 C?
C0:DBA3  C5 0E        cmp $0E                 ; E0 M16 X16 C?
C0:DBA5  90 08        bcc $DBAF               ; E0 M16 X16 C?
C0:DBA7  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:DBA9  84 10        sty $10                 ; E0 M16 X16 C?
C0:DBAB  A5 02        lda $02                 ; E0 M16 X16 C?
C0:DBAD  85 04        sta $04                 ; E0 M16 X16 C?
Code_C0DBAF:
C0:DBAF  84 02        sty $02                 ; E0 M16 X16 C?
C0:DBB1  98           tya                     ; E0 M16 X16 C?
C0:DBB2  0A           asl a                   ; E0 M16 X16 C?
C0:DBB3  AA           tax                     ; E0 M16 X16 C?
C0:DBB4  BC 0C 28     ldy $280C,x             ; E0 M16 X16 C?
Code_C0DBB7:
C0:DBB7  98           tya                     ; E0 M16 X16 C?
C0:DBB8  1A           inc a                   ; E0 M16 X16 C?
C0:DBB9  D0 E2        bne $DB9D               ; E0 M16 X16 C?
C0:DBBB  A5 10        lda $10                 ; E0 M16 X16 C?
C0:DBBD  20 CA A0     jsr $A0CA               ; E0 M16 X16 C?
C0:DBC0  A5 04        lda $04                 ; E0 M16 X16 C?
C0:DBC2  1A           inc a                   ; E0 M16 X16 C?
C0:DBC3  F0 11        beq $DBD6               ; E0 M16 X16 C?
C0:DBC5  A5 04        lda $04                 ; E0 M16 X16 C?
C0:DBC7  0A           asl a                   ; E0 M16 X16 C?
C0:DBC8  48           pha                     ; E0 M16 X16 C?
C0:DBC9  A5 10        lda $10                 ; E0 M16 X16 C?
C0:DBCB  0A           asl a                   ; E0 M16 X16 C?
C0:DBCC  AA           tax                     ; E0 M16 X16 C?
C0:DBCD  BD 0C 28     lda $280C,x             ; E0 M16 X16 C?
C0:DBD0  FA           plx                     ; E0 M16 X16 C?
C0:DBD1  9D 0C 28     sta $280C,x             ; E0 M16 X16 C?
C0:DBD4  80 09        bra $DBDF               ; E0 M16 X16 C?
Code_C0DBD6:
C0:DBD6  A5 10        lda $10                 ; E0 M16 X16 C?
C0:DBD8  0A           asl a                   ; E0 M16 X16 C?
C0:DBD9  AA           tax                     ; E0 M16 X16 C?
C0:DBDA  BD 0C 28     lda $280C,x             ; E0 M16 X16 C?
C0:DBDD  85 16        sta $16                 ; E0 M16 X16 C?
Code_C0DBDF:
C0:DBDF  A5 16        lda $16                 ; E0 M16 X16 C?
C0:DBE1  1A           inc a                   ; E0 M16 X16 C?
C0:DBE2  D0 9E        bne $DB82               ; E0 M16 X16 C?
Code_C0DBE4:
C0:DBE4  2B           pld                     ; E0 M16 X16 C?
C0:DBE5  60           rts                     ; E0 M16 X16 C?
Queue_DelayedActionTimer:
C0:DBE6  C2 31        rep #$31                ; E0 M16 X16 C?
C0:DBE8  0B           phd                     ; E0 M16 X16 C?
C0:DBE9  48           pha                     ; E0 M16 X16 C?
C0:DBEA  7B           tdc                     ; E0 M16 X16 C?
C0:DBEB  69 EE FF     adc #$FFEE              ; E0 M16 X16 C?
C0:DBEE  5B           tcd                     ; E0 M16 X16 C?
C0:DBEF  68           pla                     ; E0 M16 X16 C?
C0:DBF0  A8           tay                     ; E0 M16 X16 C?
C0:DBF1  A5 20        lda $20                 ; E0 M16 X16 C?
C0:DBF3  85 06        sta $06                 ; E0 M16 X16 C?
C0:DBF5  A5 22        lda $22                 ; E0 M16 X16 C?
C0:DBF7  85 08        sta $08                 ; E0 M16 X16 C?
C0:DBF9  A9 3C 9E     lda #$9E3C              ; E0 M16 X16 C?
C0:DBFC  85 10        sta $10                 ; E0 M16 X16 C?
C0:DBFE  A2 00 00     ldx #$0000              ; E0 M16 X16 C?
C0:DC01  86 0E        stx $0E                 ; E0 M16 X16 C?
C0:DC03  80 13        bra $DC18               ; E0 M16 X16 C?
Code_C0DC05:
C0:DC05  AA           tax                     ; E0 M16 X16 C?
C0:DC06  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:DC09  F0 12        beq $DC1D               ; E0 M16 X16 C?
C0:DC0B  A5 10        lda $10                 ; E0 M16 X16 C?
C0:DC0D  18           clc                     ; E0 M16 X16 C?
C0:DC0E  69 06 00     adc #$0006              ; E0 M16 X16 C0
C0:DC11  85 10        sta $10                 ; E0 M16 X16 C?
C0:DC13  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:DC15  E8           inx                     ; E0 M16 X16 C?
C0:DC16  86 0E        stx $0E                 ; E0 M16 X16 C?
Code_C0DC18:
C0:DC18  E0 04 00     cpx #$0004              ; E0 M16 X16 C?
C0:DC1B  90 E8        bcc $DC05               ; E0 M16 X16 C?
Code_C0DC1D:
C0:DC1D  A5 10        lda $10                 ; E0 M16 X16 C?
C0:DC1F  AA           tax                     ; E0 M16 X16 C?
C0:DC20  98           tya                     ; E0 M16 X16 C?
C0:DC21  9D 00 00     sta $0000,x             ; E0 M16 X16 C?
C0:DC24  A5 10        lda $10                 ; E0 M16 X16 C?
C0:DC26  A8           tay                     ; E0 M16 X16 C?
C0:DC27  C8           iny                     ; E0 M16 X16 C?
C0:DC28  C8           iny                     ; E0 M16 X16 C?
C0:DC29  A5 06        lda $06                 ; E0 M16 X16 C?
C0:DC2B  99 00 00     sta $0000,y             ; E0 M16 X16 C?
C0:DC2E  A5 08        lda $08                 ; E0 M16 X16 C?
C0:DC30  99 02 00     sta $0002,y             ; E0 M16 X16 C?
C0:DC33  A6 0E        ldx $0E                 ; E0 M16 X16 C?
C0:DC35  8A           txa                     ; E0 M16 X16 C?
C0:DC36  2B           pld                     ; E0 M16 X16 C?
C0:DC37  6B           rtl                     ; E0 M16 X16 C?
Clear_DelayedActionTimerSlot:
C0:DC38  C2 31        rep #$31                ; E0 M16 X16 C?
C0:DC3A  0B           phd                     ; E0 M16 X16 C?
C0:DC3B  48           pha                     ; E0 M16 X16 C?
C0:DC3C  7B           tdc                     ; E0 M16 X16 C?
C0:DC3D  69 F2 FF     adc #$FFF2              ; E0 M16 X16 C?
C0:DC40  5B           tcd                     ; E0 M16 X16 C?
C0:DC41  68           pla                     ; E0 M16 X16 C?
C0:DC42  85 04        sta $04                 ; E0 M16 X16 C?
C0:DC44  0A           asl a                   ; E0 M16 X16 C?
C0:DC45  65 04        adc $04                 ; E0 M16 X16 C?
C0:DC47  0A           asl a                   ; E0 M16 X16 C?
C0:DC48  AA           tax                     ; E0 M16 X16 C?
C0:DC49  9E 3C 9E     stz $9E3C,x             ; E0 M16 X16 C?
C0:DC4C  2B           pld                     ; E0 M16 X16 C?
C0:DC4D  6B           rtl                     ; E0 M16 X16 C?
FrameCallback_ProcessDelayedActions:
C0:DC4E  C2 31        rep #$31                ; E0 M16 X16 C?
C0:DC50  0B           phd                     ; E0 M16 X16 C?
C0:DC51  7B           tdc                     ; E0 M16 X16 C?
C0:DC52  69 F0 FF     adc #$FFF0              ; E0 M16 X16 C?
C0:DC55  5B           tcd                     ; E0 M16 X16 C?
C0:DC56  AD 02 00     lda $0002               ; E0 M16 X16 C?
C0:DC59  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:DC5C  D0 08        bne $DC66               ; E0 M16 X16 C?
C0:DC5E  AD 54 9E     lda $9E54               ; E0 M16 X16 C?
C0:DC61  F0 03        beq $DC66               ; E0 M16 X16 C?
C0:DC63  CE 54 9E     dec $9E54               ; E0 M16 X16 C?
Code_C0DC66:
C0:DC66  AD E0 88     lda $88E0               ; E0 M16 X16 C?
C0:DC69  C9 FF FF     cmp #$FFFF              ; E0 M16 X16 C?
C0:DC6C  D0 56        bne $DCC4               ; E0 M16 X16 C?
C0:DC6E  AD 43 96     lda $9643               ; E0 M16 X16 C?
C0:DC71  D0 51        bne $DCC4               ; E0 M16 X16 C?
C0:DC73  AD 60 5D     lda $5D60               ; E0 M16 X16 C?
C0:DC76  D0 4C        bne $DCC4               ; E0 M16 X16 C?
C0:DC78  AD BA 4D     lda $4DBA               ; E0 M16 X16 C?
C0:DC7B  D0 47        bne $DCC4               ; E0 M16 X16 C?
C0:DC7D  A0 3C 9E     ldy #$9E3C              ; E0 M16 X16 C?
C0:DC80  84 0E        sty $0E                 ; E0 M16 X16 C?
C0:DC82  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:DC85  85 02        sta $02                 ; E0 M16 X16 C?
C0:DC87  80 34        bra $DCBD               ; E0 M16 X16 C?
Code_C0DC89:
C0:DC89  B9 00 00     lda $0000,y             ; E0 M16 X16 C?
C0:DC8C  F0 23        beq $DCB1               ; E0 M16 X16 C?
C0:DC8E  BB           tyx                     ; E0 M16 X16 C?
C0:DC8F  3A           dec a                   ; E0 M16 X16 C?
C0:DC90  9D 00 00     sta $0000,x             ; E0 M16 X16 C?
C0:DC93  D0 1C        bne $DCB1               ; E0 M16 X16 C?
C0:DC95  C8           iny                     ; E0 M16 X16 C?
C0:DC96  C8           iny                     ; E0 M16 X16 C?
C0:DC97  B9 00 00     lda $0000,y             ; E0 M16 X16 C?
C0:DC9A  85 06        sta $06                 ; E0 M16 X16 C?
C0:DC9C  B9 02 00     lda $0002,y             ; E0 M16 X16 C?
C0:DC9F  85 08        sta $08                 ; E0 M16 X16 C?
C0:DCA1  48           pha                     ; E0 M16 X16 C?
C0:DCA2  A5 06        lda $06                 ; E0 M16 X16 C?
C0:DCA4  8D BC 00     sta $00BC               ; E0 M16 X16 C?
C0:DCA7  A5 08        lda $08                 ; E0 M16 X16 C?
C0:DCA9  8D BE 00     sta $00BE               ; E0 M16 X16 C?
C0:DCAC  68           pla                     ; E0 M16 X16 C?
C0:DCAD  22 79 92 C0  jsl $C09279             ; E0 M16 X16 C?
Code_C0DCB1:
C0:DCB1  A4 0E        ldy $0E                 ; E0 M16 X16 C?
C0:DCB3  98           tya                     ; E0 M16 X16 C?
C0:DCB4  18           clc                     ; E0 M16 X16 C?
C0:DCB5  69 06 00     adc #$0006              ; E0 M16 X16 C0
C0:DCB8  A8           tay                     ; E0 M16 X16 C?
C0:DCB9  84 0E        sty $0E                 ; E0 M16 X16 C?
C0:DCBB  E6 02        inc $02                 ; E0 M16 X16 C?
Code_C0DCBD:
C0:DCBD  A5 02        lda $02                 ; E0 M16 X16 C?
C0:DCBF  C9 04 00     cmp #$0004              ; E0 M16 X16 C?
C0:DCC2  90 C5        bcc $DC89               ; E0 M16 X16 C?
Code_C0DCC4:
C0:DCC4  2B           pld                     ; E0 M16 X16 C?
C0:DCC5  60           rts                     ; E0 M16 X16 C?
FrameCallback_ProcessCommandStream:
C0:F41E  C2 31        rep #$31                ; E0 M16 X16 C?
C0:F420  0B           phd                     ; E0 M16 X16 C?
C0:F421  7B           tdc                     ; E0 M16 X16 C?
C0:F422  69 DB FF     adc #$FFDB              ; E0 M16 X16 C?
C0:F425  5B           tcd                     ; E0 M16 X16 C?
C0:F426  AD 3B 00     lda $003B               ; E0 M16 X16 C?
C0:F429  CD E3 B4     cmp $B4E3               ; E0 M16 X16 C?
C0:F42C  F0 02        beq $F430               ; E0 M16 X16 C?
C0:F42E  B0 03        bcs $F433               ; E0 M16 X16 C?
Code_C0F430:
C0:F430  4C 5F F8     jmp $F85F               ; E0 M16 X16 C?
Code_C0F433:
C0:F433  AD F7 B4     lda $B4F7               ; E0 M16 X16 C?
C0:F436  85 23        sta $23                 ; E0 M16 X16 C?
C0:F438  AD F7 B4     lda $B4F7               ; E0 M16 X16 C?
C0:F43B  1A           inc a                   ; E0 M16 X16 C?
C0:F43C  85 21        sta $21                 ; E0 M16 X16 C?
C0:F43E  AD F7 B4     lda $B4F7               ; E0 M16 X16 C?
C0:F441  1A           inc a                   ; E0 M16 X16 C?
C0:F442  1A           inc a                   ; E0 M16 X16 C?
C0:F443  29 0F 00     and #$000F              ; E0 M16 X16 C?
C0:F446  8D F7 B4     sta $B4F7               ; E0 M16 X16 C?
C0:F449  AD 3B 00     lda $003B               ; E0 M16 X16 C?
C0:F44C  4A           lsr a                   ; E0 M16 X16 C?
C0:F44D  4A           lsr a                   ; E0 M16 X16 C?
C0:F44E  4A           lsr a                   ; E0 M16 X16 C?
C0:F44F  18           clc                     ; E0 M16 X16 C?
C0:F450  69 1D 00     adc #$001D              ; E0 M16 X16 C0
C0:F453  29 1F 00     and #$001F              ; E0 M16 X16 C?
C0:F456  85 04        sta $04                 ; E0 M16 X16 C?
C0:F458  A9 00 00     lda #$0000              ; E0 M16 X16 C?
C0:F45B  85 02        sta $02                 ; E0 M16 X16 C?
C0:F45D  85 1F        sta $1F                 ; E0 M16 X16 C?
C0:F45F  AD E7 B4     lda $B4E7               ; E0 M16 X16 C?
C0:F462  85 06        sta $06                 ; E0 M16 X16 C?
C0:F464  AD E9 B4     lda $B4E9               ; E0 M16 X16 C?
C0:F467  85 08        sta $08                 ; E0 M16 X16 C?
C0:F469  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F46B  85 1B        sta $1B                 ; E0 M16 X16 C?
C0:F46D  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F46F  85 1D        sta $1D                 ; E0 M16 X16 C?
C0:F471  A5 23        lda $23                 ; E0 M16 X16 C?
C0:F473  0A           asl a                   ; E0 M16 X16 C?
C0:F474  0A           asl a                   ; E0 M16 X16 C?
C0:F475  0A           asl a                   ; E0 M16 X16 C?
C0:F476  0A           asl a                   ; E0 M16 X16 C?
C0:F477  0A           asl a                   ; E0 M16 X16 C?
C0:F478  0A           asl a                   ; E0 M16 X16 C?
C0:F479  18           clc                     ; E0 M16 X16 C?
C0:F47A  69 FE 7D     adc #$7DFE              ; E0 M16 X16 C0
C0:F47D  85 06        sta $06                 ; E0 M16 X16 C?
C0:F47F  8B           phb                     ; E0 M16 X16 C?
C0:F480  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F482  68           pla                     ; E0 M8 X16 C?
C0:F483  85 08        sta $08                 ; E0 M8 X16 C?
C0:F485  64 09        stz $09                 ; E0 M8 X16 C?
C0:F487  C2 20        rep #$20                ; E0 M8 X16 C?
C0:F489  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F48B  85 17        sta $17                 ; E0 M16 X16 C?
C0:F48D  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F48F  85 19        sta $19                 ; E0 M16 X16 C?
C0:F491  A5 21        lda $21                 ; E0 M16 X16 C?
C0:F493  0A           asl a                   ; E0 M16 X16 C?
C0:F494  0A           asl a                   ; E0 M16 X16 C?
C0:F495  0A           asl a                   ; E0 M16 X16 C?
C0:F496  0A           asl a                   ; E0 M16 X16 C?
C0:F497  0A           asl a                   ; E0 M16 X16 C?
C0:F498  0A           asl a                   ; E0 M16 X16 C?
C0:F499  18           clc                     ; E0 M16 X16 C?
C0:F49A  69 FE 7D     adc #$7DFE              ; E0 M16 X16 C0
C0:F49D  85 0A        sta $0A                 ; E0 M16 X16 C?
C0:F49F  8B           phb                     ; E0 M16 X16 C?
C0:F4A0  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F4A2  68           pla                     ; E0 M8 X16 C?
C0:F4A3  85 0C        sta $0C                 ; E0 M8 X16 C?
C0:F4A5  64 0D        stz $0D                 ; E0 M8 X16 C?
C0:F4A7  C2 20        rep #$20                ; E0 M8 X16 C?
C0:F4A9  A7 1B        lda [$1B]               ; E0 M16 X16 C?
C0:F4AB  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F4AE  85 15        sta $15                 ; E0 M16 X16 C?
C0:F4B0  A5 1B        lda $1B                 ; E0 M16 X16 C?
C0:F4B2  85 06        sta $06                 ; E0 M16 X16 C?
C0:F4B4  A5 1D        lda $1D                 ; E0 M16 X16 C?
C0:F4B6  85 08        sta $08                 ; E0 M16 X16 C?
C0:F4B8  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F4BA  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F4BC  85 1B        sta $1B                 ; E0 M16 X16 C?
C0:F4BE  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F4C0  85 1D        sta $1D                 ; E0 M16 X16 C?
C0:F4C2  A5 15        lda $15                 ; E0 M16 X16 C?
C0:F4C4  C9 01 00     cmp #$0001              ; E0 M16 X16 C?
C0:F4C7  F0 23        beq $F4EC               ; E0 M16 X16 C?
C0:F4C9  C9 02 00     cmp #$0002              ; E0 M16 X16 C?
C0:F4CC  D0 03        bne $F4D1               ; E0 M16 X16 C?
C0:F4CE  4C 81 F5     jmp $F581               ; E0 M16 X16 C?
Code_C0F4D1:
C0:F4D1  C9 03 00     cmp #$0003              ; E0 M16 X16 C?
C0:F4D4  D0 03        bne $F4D9               ; E0 M16 X16 C?
C0:F4D6  4C 68 F6     jmp $F668               ; E0 M16 X16 C?
Code_C0F4D9:
C0:F4D9  C9 04 00     cmp #$0004              ; E0 M16 X16 C?
C0:F4DC  D0 03        bne $F4E1               ; E0 M16 X16 C?
C0:F4DE  4C 7A F6     jmp $F67A               ; E0 M16 X16 C?
Code_C0F4E1:
C0:F4E1  C9 FF 00     cmp #$00FF              ; E0 M16 X16 C?
C0:F4E4  D0 03        bne $F4E9               ; E0 M16 X16 C?
C0:F4E6  4C 45 F8     jmp $F845               ; E0 M16 X16 C?
Code_C0F4E9:
C0:F4E9  4C 4B F8     jmp $F84B               ; E0 M16 X16 C?
Code_C0F4EC:
C0:F4EC  AD E3 B4     lda $B4E3               ; E0 M16 X16 C?
C0:F4EF  18           clc                     ; E0 M16 X16 C?
C0:F4F0  69 08 00     adc #$0008              ; E0 M16 X16 C0
C0:F4F3  8D E3 B4     sta $B4E3               ; E0 M16 X16 C?
C0:F4F6  80 39        bra $F531               ; E0 M16 X16 C?
Code_C0F4F8:
C0:F4F8  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F4FB  18           clc                     ; E0 M16 X16 C?
C0:F4FC  69 00 20     adc #$2000              ; E0 M16 X16 C0
C0:F4FF  A6 17        ldx $17                 ; E0 M16 X16 C?
C0:F501  86 06        stx $06                 ; E0 M16 X16 C?
C0:F503  A6 19        ldx $19                 ; E0 M16 X16 C?
C0:F505  86 08        stx $08                 ; E0 M16 X16 C?
C0:F507  87 06        sta [$06]               ; E0 M16 X16 C?
C0:F509  A5 1B        lda $1B                 ; E0 M16 X16 C?
C0:F50B  85 06        sta $06                 ; E0 M16 X16 C?
C0:F50D  A5 1D        lda $1D                 ; E0 M16 X16 C?
C0:F50F  85 08        sta $08                 ; E0 M16 X16 C?
C0:F511  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F513  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F515  85 1B        sta $1B                 ; E0 M16 X16 C?
C0:F517  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F519  85 1D        sta $1D                 ; E0 M16 X16 C?
C0:F51B  A5 17        lda $17                 ; E0 M16 X16 C?
C0:F51D  85 06        sta $06                 ; E0 M16 X16 C?
C0:F51F  A5 19        lda $19                 ; E0 M16 X16 C?
C0:F521  85 08        sta $08                 ; E0 M16 X16 C?
C0:F523  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F525  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F527  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F529  85 17        sta $17                 ; E0 M16 X16 C?
C0:F52B  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F52D  85 19        sta $19                 ; E0 M16 X16 C?
C0:F52F  E6 02        inc $02                 ; E0 M16 X16 C?
Code_C0F531:
C0:F531  A7 1B        lda [$1B]               ; E0 M16 X16 C?
C0:F533  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F536  D0 C0        bne $F4F8               ; E0 M16 X16 C?
C0:F538  A5 02        lda $02                 ; E0 M16 X16 C?
C0:F53A  4A           lsr a                   ; E0 M16 X16 C?
C0:F53B  48           pha                     ; E0 M16 X16 C?
C0:F53C  A5 04        lda $04                 ; E0 M16 X16 C?
C0:F53E  0A           asl a                   ; E0 M16 X16 C?
C0:F53F  0A           asl a                   ; E0 M16 X16 C?
C0:F540  0A           asl a                   ; E0 M16 X16 C?
C0:F541  0A           asl a                   ; E0 M16 X16 C?
C0:F542  0A           asl a                   ; E0 M16 X16 C?
C0:F543  18           clc                     ; E0 M16 X16 C?
C0:F544  69 10 6C     adc #$6C10              ; E0 M16 X16 C0
C0:F547  7A           ply                     ; E0 M16 X16 C?
C0:F548  84 04        sty $04                 ; E0 M16 X16 C?
C0:F54A  38           sec                     ; E0 M16 X16 C?
C0:F54B  E5 04        sbc $04                 ; E0 M16 X16 C1
C0:F54D  85 15        sta $15                 ; E0 M16 X16 C?
C0:F54F  A5 23        lda $23                 ; E0 M16 X16 C?
C0:F551  0A           asl a                   ; E0 M16 X16 C?
C0:F552  0A           asl a                   ; E0 M16 X16 C?
C0:F553  0A           asl a                   ; E0 M16 X16 C?
C0:F554  0A           asl a                   ; E0 M16 X16 C?
C0:F555  0A           asl a                   ; E0 M16 X16 C?
C0:F556  0A           asl a                   ; E0 M16 X16 C?
C0:F557  18           clc                     ; E0 M16 X16 C?
C0:F558  69 FE 7D     adc #$7DFE              ; E0 M16 X16 C0
C0:F55B  85 06        sta $06                 ; E0 M16 X16 C?
C0:F55D  8B           phb                     ; E0 M16 X16 C?
C0:F55E  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F560  68           pla                     ; E0 M8 X16 C?
C0:F561  85 08        sta $08                 ; E0 M8 X16 C?
C0:F563  64 09        stz $09                 ; E0 M8 X16 C?
C0:F565  C2 20        rep #$20                ; E0 M8 X16 C?
C0:F567  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F569  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:F56B  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F56D  85 10        sta $10                 ; E0 M16 X16 C?
C0:F56F  A5 15        lda $15                 ; E0 M16 X16 C?
C0:F571  A8           tay                     ; E0 M16 X16 C?
C0:F572  A5 02        lda $02                 ; E0 M16 X16 C?
C0:F574  0A           asl a                   ; E0 M16 X16 C?
C0:F575  AA           tax                     ; E0 M16 X16 C?
C0:F576  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F578  A9 00        lda #$00                ; E0 M8 X16 C?
C0:F57A  22 C4 EF C4  jsl $C4EFC4             ; E0 M8 X16 C?
C0:F57E  4C 4B F8     jmp $F84B               ; E0 M8 X16 C?
Code_C0F581:
C0:F581  AD E3 B4     lda $B4E3               ; E0 M16 X16 C?
C0:F584  18           clc                     ; E0 M16 X16 C?
C0:F585  69 10 00     adc #$0010              ; E0 M16 X16 C0
C0:F588  8D E3 B4     sta $B4E3               ; E0 M16 X16 C?
C0:F58B  80 44        bra $F5D1               ; E0 M16 X16 C?
Code_C0F58D:
C0:F58D  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F590  18           clc                     ; E0 M16 X16 C?
C0:F591  69 00 24     adc #$2400              ; E0 M16 X16 C0
C0:F594  A6 17        ldx $17                 ; E0 M16 X16 C?
C0:F596  86 06        stx $06                 ; E0 M16 X16 C?
C0:F598  A6 19        ldx $19                 ; E0 M16 X16 C?
C0:F59A  86 08        stx $08                 ; E0 M16 X16 C?
C0:F59C  87 06        sta [$06]               ; E0 M16 X16 C?
C0:F59E  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F5A0  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F5A2  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F5A4  85 17        sta $17                 ; E0 M16 X16 C?
C0:F5A6  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F5A8  85 19        sta $19                 ; E0 M16 X16 C?
C0:F5AA  A7 1B        lda [$1B]               ; E0 M16 X16 C?
C0:F5AC  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F5AF  18           clc                     ; E0 M16 X16 C?
C0:F5B0  69 10 24     adc #$2410              ; E0 M16 X16 C0
C0:F5B3  87 0A        sta [$0A]               ; E0 M16 X16 C?
C0:F5B5  A5 1B        lda $1B                 ; E0 M16 X16 C?
C0:F5B7  85 06        sta $06                 ; E0 M16 X16 C?
C0:F5B9  A5 1D        lda $1D                 ; E0 M16 X16 C?
C0:F5BB  85 08        sta $08                 ; E0 M16 X16 C?
C0:F5BD  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F5BF  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F5C1  85 1B        sta $1B                 ; E0 M16 X16 C?
C0:F5C3  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F5C5  85 1D        sta $1D                 ; E0 M16 X16 C?
C0:F5C7  E6 0A        inc $0A                 ; E0 M16 X16 C?
C0:F5C9  E6 0A        inc $0A                 ; E0 M16 X16 C?
C0:F5CB  E6 02        inc $02                 ; E0 M16 X16 C?
C0:F5CD  A5 02        lda $02                 ; E0 M16 X16 C?
C0:F5CF  85 1F        sta $1F                 ; E0 M16 X16 C?
Code_C0F5D1:
C0:F5D1  A7 1B        lda [$1B]               ; E0 M16 X16 C?
C0:F5D3  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F5D6  D0 B5        bne $F58D               ; E0 M16 X16 C?
C0:F5D8  A5 02        lda $02                 ; E0 M16 X16 C?
C0:F5DA  4A           lsr a                   ; E0 M16 X16 C?
C0:F5DB  85 02        sta $02                 ; E0 M16 X16 C?
C0:F5DD  A5 04        lda $04                 ; E0 M16 X16 C?
C0:F5DF  0A           asl a                   ; E0 M16 X16 C?
C0:F5E0  0A           asl a                   ; E0 M16 X16 C?
C0:F5E1  0A           asl a                   ; E0 M16 X16 C?
C0:F5E2  0A           asl a                   ; E0 M16 X16 C?
C0:F5E3  0A           asl a                   ; E0 M16 X16 C?
C0:F5E4  18           clc                     ; E0 M16 X16 C?
C0:F5E5  69 10 6C     adc #$6C10              ; E0 M16 X16 C0
C0:F5E8  38           sec                     ; E0 M16 X16 C?
C0:F5E9  E5 02        sbc $02                 ; E0 M16 X16 C1
C0:F5EB  85 13        sta $13                 ; E0 M16 X16 C?
C0:F5ED  A5 23        lda $23                 ; E0 M16 X16 C?
C0:F5EF  0A           asl a                   ; E0 M16 X16 C?
C0:F5F0  0A           asl a                   ; E0 M16 X16 C?
C0:F5F1  0A           asl a                   ; E0 M16 X16 C?
C0:F5F2  0A           asl a                   ; E0 M16 X16 C?
C0:F5F3  0A           asl a                   ; E0 M16 X16 C?
C0:F5F4  0A           asl a                   ; E0 M16 X16 C?
C0:F5F5  18           clc                     ; E0 M16 X16 C?
C0:F5F6  69 FE 7D     adc #$7DFE              ; E0 M16 X16 C0
C0:F5F9  85 06        sta $06                 ; E0 M16 X16 C?
C0:F5FB  8B           phb                     ; E0 M16 X16 C?
C0:F5FC  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F5FE  68           pla                     ; E0 M8 X16 C?
C0:F5FF  85 08        sta $08                 ; E0 M8 X16 C?
C0:F601  64 09        stz $09                 ; E0 M8 X16 C?
C0:F603  C2 20        rep #$20                ; E0 M8 X16 C?
C0:F605  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F607  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:F609  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F60B  85 10        sta $10                 ; E0 M16 X16 C?
C0:F60D  A4 13        ldy $13                 ; E0 M16 X16 C?
C0:F60F  A5 1F        lda $1F                 ; E0 M16 X16 C?
C0:F611  85 02        sta $02                 ; E0 M16 X16 C?
C0:F613  0A           asl a                   ; E0 M16 X16 C?
C0:F614  AA           tax                     ; E0 M16 X16 C?
C0:F615  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F617  A9 00        lda #$00                ; E0 M8 X16 C?
C0:F619  22 C4 EF C4  jsl $C4EFC4             ; E0 M8 X16 C?
C0:F61D  A5 04        lda $04                 ; E0 M8 X16 C?
C0:F61F  C9 1F        cmp #$1F                ; E0 M8 X16 C?
C0:F621  00 F0        brk #$F0                ; E0 M8 X16 C?
Code_C0F668:
C0:F668  A7 1B        lda [$1B]               ; E0 M16 X16 C?
C0:F66A  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F66D  0A           asl a                   ; E0 M16 X16 C?
C0:F66E  0A           asl a                   ; E0 M16 X16 C?
C0:F66F  0A           asl a                   ; E0 M16 X16 C?
C0:F670  18           clc                     ; E0 M16 X16 C?
C0:F671  6D E3 B4     adc $B4E3               ; E0 M16 X16 C0
C0:F674  8D E3 B4     sta $B4E3               ; E0 M16 X16 C?
C0:F677  4C 4B F8     jmp $F84B               ; E0 M16 X16 C?
Code_C0F67A:
C0:F67A  A2 01 98     ldx #$9801              ; E0 M16 X16 C?
C0:F67D  86 15        stx $15                 ; E0 M16 X16 C?
C0:F67F  BD 00 00     lda $0000,x             ; E0 M16 X16 C?
C0:F682  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F685  D0 03        bne $F68A               ; E0 M16 X16 C?
C0:F687  4C 31 F8     jmp $F831               ; E0 M16 X16 C?
Code_C0F68A:
C0:F68A  A0 F9 B4     ldy #$B4F9              ; E0 M16 X16 C?
C0:F68D  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F68F  A9 00        lda #$00                ; E0 M8 X16 C?
C0:F691  85 12        sta $12                 ; E0 M8 X16 C?
C0:F693  4C 2A F7     jmp $F72A               ; E0 M8 X16 C?
Code_C0F696:
C0:F696  A5 00        lda $00                 ; E0 M16 X16 C?
C0:F698  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F69B  85 13        sta $13                 ; E0 M16 X16 C?
C0:F69D  C9 AC 00     cmp #$00AC              ; E0 M16 X16 C?
C0:F6A0  F0 0C        beq $F6AE               ; E0 M16 X16 C?
C0:F6A2  C9 AE 00     cmp #$00AE              ; E0 M16 X16 C?
C0:F6A5  F0 1C        beq $F6C3               ; E0 M16 X16 C?
C0:F6A7  C9 AF 00     cmp #$00AF              ; E0 M16 X16 C?
C0:F6AA  F0 2C        beq $F6D8               ; E0 M16 X16 C?
C0:F6AC  80 3F        bra $F6ED               ; E0 M16 X16 C?
Code_C0F6AE:
C0:F6AE  A5 12        lda $12                 ; E0 M16 X16 C?
C0:F6B0  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F6B3  85 02        sta $02                 ; E0 M16 X16 C?
C0:F6B5  98           tya                     ; E0 M16 X16 C?
C0:F6B6  18           clc                     ; E0 M16 X16 C?
C0:F6B7  65 02        adc $02                 ; E0 M16 X16 C0
C0:F6B9  AA           tax                     ; E0 M16 X16 C?
C0:F6BA  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F6BC  A9 7C        lda #$7C                ; E0 M8 X16 C?
C0:F6BE  9D 00 00     sta $0000,x             ; E0 M8 X16 C?
C0:F6C1  80 5D        bra $F720               ; E0 M8 X16 C?
Code_C0F6C3:
C0:F6C3  A5 12        lda $12                 ; E0 M16 X16 C?
C0:F6C5  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F6C8  85 02        sta $02                 ; E0 M16 X16 C?
C0:F6CA  98           tya                     ; E0 M16 X16 C?
C0:F6CB  18           clc                     ; E0 M16 X16 C?
C0:F6CC  65 02        adc $02                 ; E0 M16 X16 C0
C0:F6CE  AA           tax                     ; E0 M16 X16 C?
C0:F6CF  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F6D1  A9 7E        lda #$7E                ; E0 M8 X16 C?
C0:F6D3  9D 00 00     sta $0000,x             ; E0 M8 X16 C?
C0:F6D6  80 48        bra $F720               ; E0 M8 X16 C?
Code_C0F6D8:
C0:F6D8  A5 12        lda $12                 ; E0 M16 X16 C?
C0:F6DA  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F6DD  85 02        sta $02                 ; E0 M16 X16 C?
C0:F6DF  98           tya                     ; E0 M16 X16 C?
C0:F6E0  18           clc                     ; E0 M16 X16 C?
C0:F6E1  65 02        adc $02                 ; E0 M16 X16 C0
C0:F6E3  AA           tax                     ; E0 M16 X16 C?
C0:F6E4  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F6E6  A9 7F        lda #$7F                ; E0 M8 X16 C?
C0:F6E8  9D 00 00     sta $0000,x             ; E0 M8 X16 C?
C0:F6EB  80 33        bra $F720               ; E0 M8 X16 C?
Code_C0F6ED:
C0:F6ED  A5 13        lda $13                 ; E0 M16 X16 C?
C0:F6EF  18           clc                     ; E0 M16 X16 C?
C0:F6F0  E9 90 00     sbc #$0090              ; E0 M16 X16 C0
C0:F6F3  50 04        bvc $F6F9               ; E0 M16 X16 C?
C0:F6F5  10 0E        bpl $F705               ; E0 M16 X16 C?
C0:F6F7  80 02        bra $F6FB               ; E0 M16 X16 C?
Code_C0F6FB:
C0:F6FB  A5 13        lda $13                 ; E0 M16 X16 C?
C0:F6FD  38           sec                     ; E0 M16 X16 C?
C0:F6FE  E9 50 00     sbc #$0050              ; E0 M16 X16 C1
C0:F701  85 13        sta $13                 ; E0 M16 X16 C?
C0:F703  80 08        bra $F70D               ; E0 M16 X16 C?
Code_C0F705:
C0:F705  A5 13        lda $13                 ; E0 M16 X16 C?
C0:F707  38           sec                     ; E0 M16 X16 C?
C0:F708  E9 30 00     sbc #$0030              ; E0 M16 X16 C1
C0:F70B  85 13        sta $13                 ; E0 M16 X16 C?
Code_C0F70D:
C0:F70D  A5 12        lda $12                 ; E0 M16 X16 C?
C0:F70F  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F712  85 02        sta $02                 ; E0 M16 X16 C?
C0:F714  98           tya                     ; E0 M16 X16 C?
C0:F715  18           clc                     ; E0 M16 X16 C?
C0:F716  65 02        adc $02                 ; E0 M16 X16 C0
C0:F718  AA           tax                     ; E0 M16 X16 C?
C0:F719  A5 13        lda $13                 ; E0 M16 X16 C?
C0:F71B  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F71D  9D 00 00     sta $0000,x             ; E0 M8 X16 C?
Code_C0F720:
C0:F720  A6 15        ldx $15                 ; E0 M8 X16 C?
C0:F722  E8           inx                     ; E0 M8 X16 C?
C0:F723  86 15        stx $15                 ; E0 M8 X16 C?
C0:F725  A5 12        lda $12                 ; E0 M8 X16 C?
C0:F727  1A           inc a                   ; E0 M8 X16 C?
C0:F728  85 12        sta $12                 ; E0 M8 X16 C?
Code_C0F72A:
C0:F72A  BD 00 00     lda $0000,x             ; E0 M8 X16 C?
C0:F72D  85 00        sta $00                 ; E0 M8 X16 C?
C0:F72F  C2 20        rep #$20                ; E0 M8 X16 C?
C0:F731  A5 00        lda $00                 ; E0 M16 X16 C?
C0:F733  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F736  F0 03        beq $F73B               ; E0 M16 X16 C?
C0:F738  4C 96 F6     jmp $F696               ; E0 M16 X16 C?
Code_C0F73B:
C0:F73B  AD E3 B4     lda $B4E3               ; E0 M16 X16 C?
C0:F73E  18           clc                     ; E0 M16 X16 C?
C0:F73F  69 10 00     adc #$0010              ; E0 M16 X16 C0
C0:F742  8D E3 B4     sta $B4E3               ; E0 M16 X16 C?
C0:F745  A2 00 00     ldx #$0000              ; E0 M16 X16 C?
C0:F748  80 4B        bra $F795               ; E0 M16 X16 C?
Code_C0F74A:
C0:F74A  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F74D  85 02        sta $02                 ; E0 M16 X16 C?
C0:F74F  29 F0 00     and #$00F0              ; E0 M16 X16 C?
C0:F752  18           clc                     ; E0 M16 X16 C?
C0:F753  65 02        adc $02                 ; E0 M16 X16 C0
C0:F755  18           clc                     ; E0 M16 X16 C?
C0:F756  69 00 24     adc #$2400              ; E0 M16 X16 C0
C0:F759  48           pha                     ; E0 M16 X16 C?
C0:F75A  A5 17        lda $17                 ; E0 M16 X16 C?
C0:F75C  85 06        sta $06                 ; E0 M16 X16 C?
C0:F75E  A5 19        lda $19                 ; E0 M16 X16 C?
C0:F760  85 08        sta $08                 ; E0 M16 X16 C?
C0:F762  68           pla                     ; E0 M16 X16 C?
C0:F763  87 06        sta [$06]               ; E0 M16 X16 C?
C0:F765  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F767  E6 06        inc $06                 ; E0 M16 X16 C?
C0:F769  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F76B  85 17        sta $17                 ; E0 M16 X16 C?
C0:F76D  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F76F  85 19        sta $19                 ; E0 M16 X16 C?
C0:F771  B9 00 00     lda $0000,y             ; E0 M16 X16 C?
C0:F774  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F777  85 02        sta $02                 ; E0 M16 X16 C?
C0:F779  29 F0 00     and #$00F0              ; E0 M16 X16 C?
C0:F77C  18           clc                     ; E0 M16 X16 C?
C0:F77D  65 02        adc $02                 ; E0 M16 X16 C0
C0:F77F  18           clc                     ; E0 M16 X16 C?
C0:F780  69 10 24     adc #$2410              ; E0 M16 X16 C0
C0:F783  87 0A        sta [$0A]               ; E0 M16 X16 C?
C0:F785  E6 0A        inc $0A                 ; E0 M16 X16 C?
C0:F787  E6 0A        inc $0A                 ; E0 M16 X16 C?
C0:F789  C8           iny                     ; E0 M16 X16 C?
C0:F78A  A5 1F        lda $1F                 ; E0 M16 X16 C?
C0:F78C  85 02        sta $02                 ; E0 M16 X16 C?
C0:F78E  E6 02        inc $02                 ; E0 M16 X16 C?
C0:F790  A5 02        lda $02                 ; E0 M16 X16 C?
C0:F792  85 1F        sta $1F                 ; E0 M16 X16 C?
C0:F794  E8           inx                     ; E0 M16 X16 C?
Code_C0F795:
C0:F795  B9 00 00     lda $0000,y             ; E0 M16 X16 C?
C0:F798  29 FF 00     and #$00FF              ; E0 M16 X16 C?
C0:F79B  F0 05        beq $F7A2               ; E0 M16 X16 C?
C0:F79D  E0 18 00     cpx #$0018              ; E0 M16 X16 C?
C0:F7A0  90 A8        bcc $F74A               ; E0 M16 X16 C?
Code_C0F7A2:
C0:F7A2  A5 1F        lda $1F                 ; E0 M16 X16 C?
C0:F7A4  85 02        sta $02                 ; E0 M16 X16 C?
C0:F7A6  4A           lsr a                   ; E0 M16 X16 C?
C0:F7A7  85 02        sta $02                 ; E0 M16 X16 C?
C0:F7A9  A5 04        lda $04                 ; E0 M16 X16 C?
C0:F7AB  0A           asl a                   ; E0 M16 X16 C?
C0:F7AC  0A           asl a                   ; E0 M16 X16 C?
C0:F7AD  0A           asl a                   ; E0 M16 X16 C?
C0:F7AE  0A           asl a                   ; E0 M16 X16 C?
C0:F7AF  0A           asl a                   ; E0 M16 X16 C?
C0:F7B0  18           clc                     ; E0 M16 X16 C?
C0:F7B1  69 10 6C     adc #$6C10              ; E0 M16 X16 C0
C0:F7B4  38           sec                     ; E0 M16 X16 C?
C0:F7B5  E5 02        sbc $02                 ; E0 M16 X16 C1
C0:F7B7  85 13        sta $13                 ; E0 M16 X16 C?
C0:F7B9  A5 23        lda $23                 ; E0 M16 X16 C?
C0:F7BB  0A           asl a                   ; E0 M16 X16 C?
C0:F7BC  0A           asl a                   ; E0 M16 X16 C?
C0:F7BD  0A           asl a                   ; E0 M16 X16 C?
C0:F7BE  0A           asl a                   ; E0 M16 X16 C?
C0:F7BF  0A           asl a                   ; E0 M16 X16 C?
C0:F7C0  0A           asl a                   ; E0 M16 X16 C?
C0:F7C1  18           clc                     ; E0 M16 X16 C?
C0:F7C2  69 FE 7D     adc #$7DFE              ; E0 M16 X16 C0
C0:F7C5  85 06        sta $06                 ; E0 M16 X16 C?
C0:F7C7  8B           phb                     ; E0 M16 X16 C?
C0:F7C8  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F7CA  68           pla                     ; E0 M8 X16 C?
C0:F7CB  85 08        sta $08                 ; E0 M8 X16 C?
C0:F7CD  64 09        stz $09                 ; E0 M8 X16 C?
C0:F7CF  C2 20        rep #$20                ; E0 M8 X16 C?
C0:F7D1  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F7D3  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:F7D5  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F7D7  85 10        sta $10                 ; E0 M16 X16 C?
C0:F7D9  A4 13        ldy $13                 ; E0 M16 X16 C?
C0:F7DB  A5 1F        lda $1F                 ; E0 M16 X16 C?
C0:F7DD  85 02        sta $02                 ; E0 M16 X16 C?
C0:F7DF  0A           asl a                   ; E0 M16 X16 C?
C0:F7E0  AA           tax                     ; E0 M16 X16 C?
C0:F7E1  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F7E3  A9 00        lda #$00                ; E0 M8 X16 C?
C0:F7E5  22 C4 EF C4  jsl $C4EFC4             ; E0 M8 X16 C?
C0:F7E9  A5 04        lda $04                 ; E0 M8 X16 C?
C0:F7EB  C9 1F        cmp #$1F                ; E0 M8 X16 C?
C0:F7ED  00 F0        brk #$F0                ; E0 M8 X16 C?
Code_C0F831:
C0:F831  A5 1B        lda $1B                 ; E0 M16 X16 C?
C0:F833  85 06        sta $06                 ; E0 M16 X16 C?
C0:F835  A5 1D        lda $1D                 ; E0 M16 X16 C?
C0:F837  85 08        sta $08                 ; E0 M16 X16 C?
C0:F839  C6 06        dec $06                 ; E0 M16 X16 C?
C0:F83B  A5 06        lda $06                 ; E0 M16 X16 C?
C0:F83D  85 1B        sta $1B                 ; E0 M16 X16 C?
C0:F83F  A5 08        lda $08                 ; E0 M16 X16 C?
C0:F841  85 1D        sta $1D                 ; E0 M16 X16 C?
C0:F843  80 06        bra $F84B               ; E0 M16 X16 C?
Code_C0F845:
C0:F845  A9 FF FF     lda #$FFFF              ; E0 M16 X16 C?
C0:F848  8D E3 B4     sta $B4E3               ; E0 M16 X16 C?
Code_C0F84B:
C0:F84B  A5 1B        lda $1B                 ; E0 M8 X16 C?
C0:F84D  85 06        sta $06                 ; E0 M8 X16 C?
C0:F84F  A5 1D        lda $1D                 ; E0 M8 X16 C?
C0:F851  85 08        sta $08                 ; E0 M8 X16 C?
C0:F853  E6 06        inc $06                 ; E0 M8 X16 C?
C0:F855  A5 06        lda $06                 ; E0 M8 X16 C?
C0:F857  8D E7 B4     sta $B4E7               ; E0 M8 X16 C?
C0:F85A  A5 08        lda $08                 ; E0 M8 X16 C?
C0:F85C  8D E9 B4     sta $B4E9               ; E0 M8 X16 C?
Code_C0F85F:
C0:F85F  AD E5 B4     lda $B4E5               ; E0 M16 X16 C?
C0:F862  CD 3B 00     cmp $003B               ; E0 M16 X16 C?
C0:F865  B0 33        bcs $F89A               ; E0 M16 X16 C?
C0:F867  AD E5 B4     lda $B4E5               ; E0 M16 X16 C?
C0:F86A  18           clc                     ; E0 M16 X16 C?
C0:F86B  69 08 00     adc #$0008              ; E0 M16 X16 C0
C0:F86E  8D E5 B4     sta $B4E5               ; E0 M16 X16 C?
C0:F871  A9 E8 0B     lda #$0BE8              ; E0 M16 X16 C?
C0:F874  85 0E        sta $0E                 ; E0 M16 X16 C?
C0:F876  A9 C4 00     lda #$00C4              ; E0 M16 X16 C?
C0:F879  85 10        sta $10                 ; E0 M16 X16 C?
C0:F87B  AD 3B 00     lda $003B               ; E0 M16 X16 C?
C0:F87E  4A           lsr a                   ; E0 M16 X16 C?
C0:F87F  4A           lsr a                   ; E0 M16 X16 C?
C0:F880  4A           lsr a                   ; E0 M16 X16 C?
C0:F881  3A           dec a                   ; E0 M16 X16 C?
C0:F882  29 1F 00     and #$001F              ; E0 M16 X16 C?
C0:F885  0A           asl a                   ; E0 M16 X16 C?
C0:F886  0A           asl a                   ; E0 M16 X16 C?
C0:F887  0A           asl a                   ; E0 M16 X16 C?
C0:F888  0A           asl a                   ; E0 M16 X16 C?
C0:F889  0A           asl a                   ; E0 M16 X16 C?
C0:F88A  18           clc                     ; E0 M16 X16 C?
C0:F88B  69 00 6C     adc #$6C00              ; E0 M16 X16 C0
C0:F88E  A8           tay                     ; E0 M16 X16 C?
C0:F88F  A2 40 00     ldx #$0040              ; E0 M16 X16 C?
C0:F892  E2 20        sep #$20                ; E0 M16 X16 C?
C0:F894  A9 03        lda #$03                ; E0 M8 X16 C?
C0:F896  22 C4 EF C4  jsl $C4EFC4             ; E0 M8 X16 C?
Code_C0F89A:
C0:F89A  AD EB B4     lda $B4EB               ; E0 M8 X16 C?
C0:F89D  85 06        sta $06                 ; E0 M8 X16 C?
C0:F89F  AD ED B4     lda $B4ED               ; E0 M8 X16 C?
C0:F8A2  85 08        sta $08                 ; E0 M8 X16 C?
C0:F8A4  18           clc                     ; E0 M8 X16 C?
C0:F8A5  A5 06        lda $06                 ; E0 M8 X16 C0
C0:F8A7  69 00        adc #$00                ; E0 M8 X16 C0
C0:F8A9  40           rti                     ; E0 M8 X16 C?
```

## Warnings

- State mismatch at C0:8334: saw E0 M8 X8 C? and E0 M16 X8 C?
- State mismatch at C0:9299: saw E0 M16 X16 C0 and E0 M16 X16 C?
- State mismatch at C0:F84B: saw E0 M8 X16 C? and E0 M16 X16 C?
- State mismatch at C0:F85F: saw E0 M16 X16 C? and E0 M8 X16 C?
- State mismatch at C0:F89A: saw E0 M8 X16 C? and E0 M16 X16 C?
