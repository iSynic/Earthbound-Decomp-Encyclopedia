; EarthBound C4 attached landing-display child lookup helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/landing-display-assembly-cluster-c007b6-c4b26b.md and
;   direct ROM decode of C4:B4BE..C4:B587.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B4BE..C4:B4FE attached-child clear helper.
; - C4:B4FE..C4:B587 attached-child spawn/clear resolver wrappers.

; ---------------------------------------------------------------------------
; External contracts used by this module

C02140_ClearEntitySlot                       = $C02140
C46028_FindEntitySlotByCachedPoseDescriptorId = $C46028
C4605A_FindEntitySlotByVisualTypeId          = $C4605A
C4608C_ResolveEntitySlotFromOverworldTypeRegistryCode = $C4608C
C4B3D0_SpawnAttachedChildEntityFromParentSlot = $C4B3D0
C4B4BE_ClearAttachedChildEntitiesByParentSlot = $C4B4BE

; ---------------------------------------------------------------------------
; C4:B4BE

; ClearAttachedChildEntitiesByParentSlot
C4B4BE_ClearAttachedChildEntitiesByParentSlot:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFF0
	TCD
	PLA
	CMP.w #$FFFF
	BEQ.b C4B4FC_ClearAttachedChildEntitiesByParentSlot_Return
	ORA.w #$C000
	STA.b $02
	LDY.w #$0000
	STY.b $0E
	BRA.b C4B4F7_ClearAttachedChildEntitiesByParentSlot_CheckLoop

C4B4D9_ClearAttachedChildEntitiesByParentSlot_Loop:
	TYA
	ASL
	CLC
	ADC.w #$103E
	TAX
	LDA.w $0000,X
	CMP.b $02
	BNE.b C4B4F2_ClearAttachedChildEntitiesByParentSlot_Next
	LDA.w #$0000
	STA.w $0000,X
	TYA
	JSL.l C02140_ClearEntitySlot
C4B4F2_ClearAttachedChildEntitiesByParentSlot_Next:
	LDY.b $0E
	INY
	STY.b $0E
C4B4F7_ClearAttachedChildEntitiesByParentSlot_CheckLoop:
	CPY.w #$001E
	BCC.b C4B4D9_ClearAttachedChildEntitiesByParentSlot_Loop
C4B4FC_ClearAttachedChildEntitiesByParentSlot_Return:
	PLD
	RTL

; ---------------------------------------------------------------------------
; C4:B4FE

; SpawnAttachedChildForRegistryTypeCode
C4B4FE_SpawnAttachedChildForRegistryTypeCode:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFF0
	TCD
	PLA
	TXY
	STY.b $0E
	TAX
	JSL.l C4608C_ResolveEntitySlotFromOverworldTypeRegistryCode
	LDY.b $0E
	TYX
	JSL.l C4B3D0_SpawnAttachedChildEntityFromParentSlot
	PLD
	RTL

; ClearAttachedChildForRegistryTypeCode
C4B519_ClearAttachedChildForRegistryTypeCode:
	REP.b #$31
	JSL.l C4608C_ResolveEntitySlotFromOverworldTypeRegistryCode
	JSL.l C4B4BE_ClearAttachedChildEntitiesByParentSlot
	RTL

; SpawnAttachedChildForVisualTypeId
C4B524_SpawnAttachedChildForVisualTypeId:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFF0
	TCD
	PLA
	TXY
	STY.b $0E
	TAX
	JSL.l C4605A_FindEntitySlotByVisualTypeId
	LDY.b $0E
	TYX
	JSL.l C4B3D0_SpawnAttachedChildEntityFromParentSlot
	PLD
	RTL

; ClearAttachedChildForVisualTypeId
C4B53F_ClearAttachedChildForVisualTypeId:
	REP.b #$31
	JSL.l C4605A_FindEntitySlotByVisualTypeId
	JSL.l C4B4BE_ClearAttachedChildEntitiesByParentSlot
	RTL

; SpawnAttachedChildForPoseDescriptorId
C4B54A_SpawnAttachedChildForPoseDescriptorId:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFF0
	TCD
	PLA
	TXY
	STY.b $0E
	TAX
	JSL.l C46028_FindEntitySlotByCachedPoseDescriptorId
	LDY.b $0E
	TYX
	JSL.l C4B3D0_SpawnAttachedChildEntityFromParentSlot
	PLD
	RTL

; ClearAttachedChildForPoseDescriptorId
C4B565_ClearAttachedChildForPoseDescriptorId:
	REP.b #$31
	JSL.l C46028_FindEntitySlotByCachedPoseDescriptorId
	JSL.l C4B4BE_ClearAttachedChildEntitiesByParentSlot
	RTL

; SpawnDefaultAttachedChildForBaseSlot18
C4B570_SpawnDefaultAttachedChildForBaseSlot18:
	REP.b #$31
	LDX.w #$0001
	LDA.w #$0018
	JSL.l C4B3D0_SpawnAttachedChildEntityFromParentSlot
	RTL

; ClearDefaultAttachedChildForBaseSlot18
C4B57D_ClearDefaultAttachedChildForBaseSlot18:
	REP.b #$31
	LDA.w #$0018
	JSL.l C4B4BE_ClearAttachedChildEntitiesByParentSlot
	RTL
