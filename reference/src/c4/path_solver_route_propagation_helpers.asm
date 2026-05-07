; EarthBound C4 path-solver route propagation helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:BAF6..C4:BD9A.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:BAF6..C4:BD9A route propagation over the path scratch grid.

; ---------------------------------------------------------------------------
; External contracts used by this module

C09032_MultiplyAByY                           = $C09032
C0915B_ScaleOrDivideAngleMagnitude           = $C0915B
C09231_ShiftRightByYPreserveWidth            = $C09231

; ---------------------------------------------------------------------------
; C4:BAF6

; PropagatePathGridCandidateRoutes
C4BAF6_PropagatePathGridCandidateRoutes:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFDB
	TCD
	PLA
	STY.b $23
	STX.b $04
	STA.b $02
	STA.b $21
	LDY.b $37
	STY.b $1F
	LDA.b $35
	STA.b $1D
	LDX.b $33
	STX.b $1B
	LDY.w #$0002
	LDA.b ($23),Y
	STA.b $19
	LDY.w #$0004
	LDA.b ($23),Y
	STA.b $17
	STZ.b $15
	STZ.b $13
	LDX.w $B408
	STX.w $B40E
	STX.w $B40C
	LDA.w #$0000
	STA.b $11
	BRA.b C4BB6E_PropagatePathGridCandidateRoutes_CheckSeedLoop

C4BB36_PropagatePathGridCandidateRoutes_SeedLoop:
	ASL
	ASL
	STA.b $02
	LDA.b $04
	CLC
	ADC.b $02
	TAX
	LDY.w $B402
	LDA.w $0000,X
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.w $0002,X
	LDX.w $B40E
	STA.w $0000,X
	LDA.w $B40E
	CMP.w $B40A
	BNE.b C4BB61_PropagatePathGridCandidateRoutes_AdvanceSeedTail
	LDX.w $B408
	BRA.b C4BB66_PropagatePathGridCandidateRoutes_StoreSeedTail

C4BB61_PropagatePathGridCandidateRoutes_AdvanceSeedTail:
	LDX.w $B40E
	INX
	INX
C4BB66_PropagatePathGridCandidateRoutes_StoreSeedTail:
	STX.w $B40E
	LDA.b $11
	INC
	STA.b $11
C4BB6E_PropagatePathGridCandidateRoutes_CheckSeedLoop:
	LDX.b $21
	STX.b $02
	CMP.b $02
	BCC.b C4BB36_PropagatePathGridCandidateRoutes_SeedLoop
	JMP.w C4BD8B_PropagatePathGridCandidateRoutes_CheckQueue

C4BB79_PropagatePathGridCandidateRoutes_DequeueCell:
	LDX.w $B40C
	LDA.w $0000,X
	STA.b $02
	LDA.w $B40C
	CMP.w $B40A
	BNE.b C4BB8E_PropagatePathGridCandidateRoutes_AdvanceQueueHead
	LDX.w $B408
	BRA.b C4BB93_PropagatePathGridCandidateRoutes_StoreQueueHead

C4BB8E_PropagatePathGridCandidateRoutes_AdvanceQueueHead:
	LDX.w $B40C
	INX
	INX
C4BB93_PropagatePathGridCandidateRoutes_StoreQueueHead:
	STX.w $B40C
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	STA.b $00
	CMP.b #$FE
	BCS.b C4BBB6_PropagatePathGridCandidateRoutes_TestFootprint
	BEQ.b C4BBB6_PropagatePathGridCandidateRoutes_TestFootprint
	JMP.w C4BD8B_PropagatePathGridCandidateRoutes_CheckQueue

C4BBB6_PropagatePathGridCandidateRoutes_TestFootprint:
	LDY.w #$0001
	LDX.b $02
	REP.b #$20
	LDA.w #$0000
	STA.b $11
	BRA.b C4BC00_PropagatePathGridCandidateRoutes_CheckFootprintRows

C4BBC4_PropagatePathGridCandidateRoutes_FootprintRow:
	LDA.w #$0000
	STA.b $04
	BRA.b C4BBEF_PropagatePathGridCandidateRoutes_CheckFootprintColumns

C4BBCB_PropagatePathGridCandidateRoutes_FootprintColumn:
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	TXA
	CLC
	ADC.b $04
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FD
	BNE.b C4BBEB_PropagatePathGridCandidateRoutes_NextFootprintColumn
	LDY.w #$0000
	BRA.b C4BC04_PropagatePathGridCandidateRoutes_FootprintOpenResult

C4BBEB_PropagatePathGridCandidateRoutes_NextFootprintColumn:
	REP.b #$20
	INC.b $04
C4BBEF_PropagatePathGridCandidateRoutes_CheckFootprintColumns:
	LDA.b $04
	CMP.b $17
	BCC.b C4BBCB_PropagatePathGridCandidateRoutes_FootprintColumn
	TXA
	CLC
	ADC.w $B402
	TAX
	LDA.b $11
	INC
	STA.b $11
C4BC00_PropagatePathGridCandidateRoutes_CheckFootprintRows:
	CMP.b $19
	BCC.b C4BBC4_PropagatePathGridCandidateRoutes_FootprintRow
C4BC04_PropagatePathGridCandidateRoutes_FootprintOpenResult:
	CPY.w #$0000
	BNE.b C4BC25_PropagatePathGridCandidateRoutes_FootprintIsOpen
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b #$FC
	STA.b [$06]
	JMP.w C4BD8B_PropagatePathGridCandidateRoutes_CheckQueue

C4BC25_PropagatePathGridCandidateRoutes_FootprintIsOpen:
	SEP.b #$20
	LDA.b $00
	CMP.b #$FF
	BNE.b C4BC54_PropagatePathGridCandidateRoutes_SetExpansionSentinel
	REP.b #$20
	INC.b $15
	LDA.b ($23)
	CMP.w #$0001
	BNE.b C4BC54_PropagatePathGridCandidateRoutes_SetExpansionSentinel
	LDY.w $B402
	LDA.b $02
	JSL.l C0915B_ScaleOrDivideAngleMagnitude
	LDY.w #$0006
	STA.b ($23),Y
	LDY.w $B402
	LDA.b $02
	JSL.l C09231_ShiftRightByYPreserveWidth
	LDY.w #$0008
	STA.b ($23),Y
C4BC54_PropagatePathGridCandidateRoutes_SetExpansionSentinel:
	SEP.b #$20
	LDA.b #$FC
	STA.b $00
	LDX.w #$0000
	STX.b $0F
	JMP.w C4BCE9_PropagatePathGridCandidateRoutes_CheckNeighborLoop

C4BC62_PropagatePathGridCandidateRoutes_NeighborLoop:
	REP.b #$20
	TXA
	ASL
	TAX
	LDA.b $02
	CLC
	ADC.w $B410,X
	STA.b $11
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.b $11
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	STA.b $01
	CMP.b #$FE
	BCC.b C4BCD8_PropagatePathGridCandidateRoutes_TrackBestNeighbor
	REP.b #$20
	LDA.w $B40C
	CMP.w $B408
	BNE.b C4BCA4_PropagatePathGridCandidateRoutes_TestQueueGap
	LDY.w #$0000
	LDA.w $B40E
	CMP.w $B40A
	BNE.b C4BCB4_PropagatePathGridCandidateRoutes_CheckQueueFull
	LDY.w #$0001
	BRA.b C4BCB4_PropagatePathGridCandidateRoutes_CheckQueueFull

C4BCA4_PropagatePathGridCandidateRoutes_TestQueueGap:
	LDY.w #$0000
	LDA.w $B40E
	INC
	INC
	CMP.w $B40C
	BNE.b C4BCB4_PropagatePathGridCandidateRoutes_CheckQueueFull
	LDY.w #$0001
C4BCB4_PropagatePathGridCandidateRoutes_CheckQueueFull:
	CPY.w #$0000
	BNE.b C4BCE4_PropagatePathGridCandidateRoutes_NextNeighbor
	LDA.b $11
	LDX.w $B40E
	STA.w $0000,X
	LDA.w $B40E
	CMP.w $B40A
	BNE.b C4BCCE_PropagatePathGridCandidateRoutes_AdvanceQueueTail
	LDY.w $B408
	BRA.b C4BCD3_PropagatePathGridCandidateRoutes_StoreQueueTail

C4BCCE_PropagatePathGridCandidateRoutes_AdvanceQueueTail:
	LDY.w $B40E
	INY
	INY
C4BCD3_PropagatePathGridCandidateRoutes_StoreQueueTail:
	STY.w $B40E
	BRA.b C4BCE4_PropagatePathGridCandidateRoutes_NextNeighbor

C4BCD8_PropagatePathGridCandidateRoutes_TrackBestNeighbor:
	LDA.b $00
	CMP.b $01
	BCC.b C4BCE4_PropagatePathGridCandidateRoutes_NextNeighbor
	BEQ.b C4BCE4_PropagatePathGridCandidateRoutes_NextNeighbor
	LDA.b $01
	STA.b $00
C4BCE4_PropagatePathGridCandidateRoutes_NextNeighbor:
	LDX.b $0F
	INX
	STX.b $0F
C4BCE9_PropagatePathGridCandidateRoutes_CheckNeighborLoop:
	CPX.w #$0004
	BCS.b C4BCF3_PropagatePathGridCandidateRoutes_FinishNeighbors
	BEQ.b C4BCF3_PropagatePathGridCandidateRoutes_FinishNeighbors
	JMP.w C4BC62_PropagatePathGridCandidateRoutes_NeighborLoop

C4BCF3_PropagatePathGridCandidateRoutes_FinishNeighbors:
	REP.b #$20
	LDA.b $00
	AND.w #$00FF
	CMP.w #$00FC
	BNE.b C4BD18_PropagatePathGridCandidateRoutes_WriteDistance
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b #$00
	STA.b [$06]
	BRA.b C4BD79_PropagatePathGridCandidateRoutes_NextWave

C4BD18_PropagatePathGridCandidateRoutes_WriteDistance:
	SEP.b #$20
	LDA.b $00
	INC
	STA.b $0E
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b $0E
	STA.b [$06]
	REP.b #$20
	AND.w #$00FF
	CMP.b $1D
	BNE.b C4BD79_PropagatePathGridCandidateRoutes_NextWave
	LDA.w #$0000
	STA.b $11
	BRA.b C4BD74_PropagatePathGridCandidateRoutes_CheckCandidateNeighbors

C4BD48_PropagatePathGridCandidateRoutes_CandidateNeighbor:
	ASL
	TAX
	LDA.b $02
	CLC
	ADC.w $B410,X
	TAX
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	TXA
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FE
	BCC.b C4BD6D_PropagatePathGridCandidateRoutes_NextCandidateNeighbor
	LDA.b #$FC
	STA.b [$06]
C4BD6D_PropagatePathGridCandidateRoutes_NextCandidateNeighbor:
	REP.b #$20
	LDA.b $11
	INC
	STA.b $11
C4BD74_PropagatePathGridCandidateRoutes_CheckCandidateNeighbors:
	CMP.w #$0004
	BCC.b C4BD48_PropagatePathGridCandidateRoutes_CandidateNeighbor
C4BD79_PropagatePathGridCandidateRoutes_NextWave:
	REP.b #$20
	INC.b $13
	LDA.b $1F
	CMP.b $13
	BCC.b C4BD98_PropagatePathGridCandidateRoutes_Return
	BEQ.b C4BD98_PropagatePathGridCandidateRoutes_Return
	LDA.b $15
	CMP.b $1B
	BEQ.b C4BD98_PropagatePathGridCandidateRoutes_Return
C4BD8B_PropagatePathGridCandidateRoutes_CheckQueue:
	REP.b #$20
	LDA.w $B40C
	CMP.w $B40E
	BEQ.b C4BD98_PropagatePathGridCandidateRoutes_Return
	JMP.w C4BB79_PropagatePathGridCandidateRoutes_DequeueCell

C4BD98_PropagatePathGridCandidateRoutes_Return:
	PLD
	RTS
