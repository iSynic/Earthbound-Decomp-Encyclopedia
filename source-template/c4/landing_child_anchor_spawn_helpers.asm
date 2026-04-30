; EarthBound C4 landing display child-anchor/spawn helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/landing-display-assembly-cluster-c007b6-c4b26b.md and
;   direct ROM decode of C4:B329..C4:B4BE.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B329..C4:B3D0 landing-display child-anchor geometry adjustment.
; - C4:B3D0..C4:B4BE attached landing-display child spawn helper.

; ---------------------------------------------------------------------------
; External contracts used by this module

EntityFootprintXOffsetTable                  = $C42A1F
EntityFootprintYOffsetTable                  = $C42A41
LandingDisplayChildDefinitionTable           = $C40DE8
C01E49_SpawnEntityAtCurrentSlotAnchor        = $C01E49

; ---------------------------------------------------------------------------
; C4:B329

; AdjustChildEntityAnchorForParentGeometry
C4B329_AdjustChildEntityAnchorForParentGeometry:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFF0
	TCD
	PLA
	STX.b $0E
	CMP.w #$0001
	BEQ.b C4B358_AdjustChildEntityAnchorForParentGeometry_ShiftUpLeft
	CMP.w #$0004
	BEQ.b C4B36E_AdjustChildEntityAnchorForParentGeometry_ShiftLeft
	CMP.w #$0002
	BEQ.b C4B388_AdjustChildEntityAnchorForParentGeometry_ShiftUpTight
	CMP.w #$0005
	BNE.b C4B34C_AdjustChildEntityAnchorForParentGeometry_CheckDown
	JMP.w C4B3CE_AdjustChildEntityAnchorForParentGeometry_Return

C4B34C_AdjustChildEntityAnchorForParentGeometry_CheckDown:
	CMP.w #$0003
	BEQ.b C4B3A0_AdjustChildEntityAnchorForParentGeometry_ShiftUpWide
	CMP.w #$0006
	BEQ.b C4B3B6_AdjustChildEntityAnchorForParentGeometry_ShiftLeftWide
	BRA.b C4B3CE_AdjustChildEntityAnchorForParentGeometry_Return

C4B358_AdjustChildEntityAnchorForParentGeometry_ShiftUpLeft:
	TXA
	ASL
	TAX
	LDA.l EntityFootprintYOffsetTable,X
	CLC
	ADC.w #$0008
	STA.b $02
	LDA.w $B3FA
	SEC
	SBC.b $02
	STA.w $B3FA
C4B36E_AdjustChildEntityAnchorForParentGeometry_ShiftLeft:
	LDX.b $0E
	TXA
	ASL
	TAX
	LDA.l EntityFootprintXOffsetTable,X
	SEC
	SBC.w #$0008
	STA.b $02
	LDA.w $B3F8
	SEC
	SBC.b $02
	STA.w $B3F8
	BRA.b C4B3CE_AdjustChildEntityAnchorForParentGeometry_Return

C4B388_AdjustChildEntityAnchorForParentGeometry_ShiftUpTight:
	TXA
	ASL
	TAX
	LDA.l EntityFootprintYOffsetTable,X
	SEC
	SBC.w #$0008
	STA.b $02
	LDA.w $B3FA
	SEC
	SBC.b $02
	STA.w $B3FA
	BRA.b C4B3CE_AdjustChildEntityAnchorForParentGeometry_Return

C4B3A0_AdjustChildEntityAnchorForParentGeometry_ShiftUpWide:
	TXA
	ASL
	TAX
	LDA.l EntityFootprintYOffsetTable,X
	CLC
	ADC.w #$0008
	STA.b $02
	LDA.w $B3FA
	SEC
	SBC.b $02
	STA.w $B3FA
C4B3B6_AdjustChildEntityAnchorForParentGeometry_ShiftLeftWide:
	LDX.b $0E
	TXA
	ASL
	TAX
	LDA.l EntityFootprintXOffsetTable,X
	CLC
	ADC.w #$0008
	STA.b $02
	LDA.w $B3F8
	SEC
	SBC.b $02
	STA.w $B3F8
C4B3CE_AdjustChildEntityAnchorForParentGeometry_Return:
	PLD
	RTS

; ---------------------------------------------------------------------------
; C4:B3D0

; SpawnAttachedChildEntityFromParentSlot
C4B3D0_SpawnAttachedChildEntityFromParentSlot:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFEA
	TCD
	PLA
	TXY
	STA.b $02
	CMP.w #$FFFF
	BNE.b C4B3E5_SpawnAttachedChildEntityFromParentSlot_CheckParentSlot
	JMP.w C4B4BC_SpawnAttachedChildEntityFromParentSlot_Return

C4B3E5_SpawnAttachedChildEntityFromParentSlot_CheckParentSlot:
	LDA.b $02
	ASL
	TAX
	LDA.w $0A62,X
	CMP.w #$FFFF
	BNE.b C4B3F4_SpawnAttachedChildEntityFromParentSlot_LoadParentState
	JMP.w C4B4BC_SpawnAttachedChildEntityFromParentSlot_Return

C4B3F4_SpawnAttachedChildEntityFromParentSlot_LoadParentState:
	LDA.w $2B6E,X
	STA.b $14
	LDA.w #LandingDisplayChildDefinitionTable
	STA.b $06
	LDA.w #LandingDisplayChildDefinitionTable>>16
	STA.b $08
	TYA
	STA.b $04
	ASL
	ASL
	ADC.b $04
	CLC
	ADC.b $06
	STA.b $06
	LDA.w $0B8E,X
	STA.w $B3F8
	LDA.w $0BCA,X
	STA.w $B3FA
	LDA.b $14
	TAX
	SEP.b #$20
	LDY.w #$0002
	LDA.b [$06],Y
	REP.b #$20
	AND.w #$00FF
	JSR.w C4B329_AdjustChildEntityAnchorForParentGeometry
	SEP.b #$20
	LDY.w #$0003
	LDA.b [$06],Y
	REP.b #$20
	AND.w #$00FF
	AND.w #$0080
	BEQ.b C4B443_SpawnAttachedChildEntityFromParentSlot_PositiveXOffset
	LDX.w #$FF00
	BRA.b C4B446_SpawnAttachedChildEntityFromParentSlot_StoreXOffsetSign

C4B443_SpawnAttachedChildEntityFromParentSlot_PositiveXOffset:
	LDX.w #$0000
C4B446_SpawnAttachedChildEntityFromParentSlot_StoreXOffsetSign:
	STX.b $04
	SEP.b #$20
	LDY.w #$0003
	LDA.b [$06],Y
	REP.b #$20
	AND.w #$00FF
	ORA.b $04
	CLC
	ADC.w $B3F8
	STA.w $B3F8
	SEP.b #$20
	LDY.w #$0004
	LDA.b [$06],Y
	REP.b #$20
	AND.w #$00FF
	AND.w #$0080
	BEQ.b C4B473_SpawnAttachedChildEntityFromParentSlot_PositiveYOffset
	LDX.w #$FF00
	BRA.b C4B476_SpawnAttachedChildEntityFromParentSlot_StoreYOffsetSign

C4B473_SpawnAttachedChildEntityFromParentSlot_PositiveYOffset:
	LDX.w #$0000
C4B476_SpawnAttachedChildEntityFromParentSlot_StoreYOffsetSign:
	STX.b $04
	SEP.b #$20
	LDY.w #$0004
	LDA.b [$06],Y
	REP.b #$20
	AND.w #$00FF
	ORA.b $04
	CLC
	ADC.w $B3FA
	STA.b $12
	STA.w $B3FA
	LDA.w $B3F8
	STA.b $0E
	LDA.b $12
	STA.b $10
	LDY.w #$FFFF
	LDX.w #$0311
	LDA.b [$06]
	JSL.l C01E49_SpawnEntityAtCurrentSlotAnchor
	ASL
	TAX
	STX.b $12
	LDA.b $02
	ORA.w #$C000
	STA.w $103E,X
	LDA.b $02
	ASL
	TAX
	LDA.w $2BAA,X
	LDX.b $12
	STA.w $2BAA,X
C4B4BC_SpawnAttachedChildEntityFromParentSlot_Return:
	PLD
	RTL
