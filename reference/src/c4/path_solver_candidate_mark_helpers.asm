; EarthBound C4 path-solver candidate footprint marking helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:B923..C4:BAF6.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B923..C4:BAF6 candidate footprint marker over the path scratch grid.

; ---------------------------------------------------------------------------
; External contracts used by this module

C09032_MultiplyAByY                           = $C09032

; ---------------------------------------------------------------------------
; C4:B923

; MarkPathCandidateFootprintsInGrid
C4B923_MarkPathCandidateFootprintsInGrid:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFE8
	TCD
	PLA
	STX.b $16
	STA.b $04
	LDA.w #$0000
	STA.b $14
	BRA.b C4B95C_MarkPathCandidateFootprintsInGrid_CheckClearLoop

C4B938_MarkPathCandidateFootprintsInGrid_ClearLoop:
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.b $14
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FD
	BEQ.b C4B955_MarkPathCandidateFootprintsInGrid_NextClearByte
	LDA.b #$FE
	STA.b [$06]
C4B955_MarkPathCandidateFootprintsInGrid_NextClearByte:
	REP.b #$20
	LDA.b $14
	INC
	STA.b $14
C4B95C_MarkPathCandidateFootprintsInGrid_CheckClearLoop:
	CMP.w $B406
	BCC.b C4B938_MarkPathCandidateFootprintsInGrid_ClearLoop
	LDA.w #$0000
	STA.b $02
	STA.b $12
	JMP.w C4BAE9_MarkPathCandidateFootprintsInGrid_CheckCandidateLoop

C4B96B_MarkPathCandidateFootprintsInGrid_CandidateLoop:
	LDA.b $02
	ASL
	TAY
	LDA.b ($16),Y
	TAY
	STY.b $10
	LDA.w $0000,Y
	BNE.b C4B9AA_MarkPathCandidateFootprintsInGrid_MarkFullRows
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.w $0006,Y
	LDY.w $B402
	JSL.l C09032_MultiplyAByY
	LDY.b $10
	CLC
	ADC.w $0008,Y
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FD
	BNE.b C4B9A3_MarkPathCandidateFootprintsInGrid_MarkSingleCell
	JMP.w C4BADD_MarkPathCandidateFootprintsInGrid_NextCandidateFromM8

C4B9A3_MarkPathCandidateFootprintsInGrid_MarkSingleCell:
	LDA.b #$FF
	STA.b [$06]
	JMP.w C4BADD_MarkPathCandidateFootprintsInGrid_NextCandidateFromM8

C4B9AA_MarkPathCandidateFootprintsInGrid_MarkFullRows:
	LDA.w #$0000
	STA.b $0E
	BRA.b C4B9EE_MarkPathCandidateFootprintsInGrid_CheckTopRows

C4B9B1_MarkPathCandidateFootprintsInGrid_TopRowLoopStart:
	LDX.w #$0000
	BRA.b C4B9E2_MarkPathCandidateFootprintsInGrid_CheckTopRowColumn

C4B9B6_MarkPathCandidateFootprintsInGrid_TopRowColumn:
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	STX.b $02
	LDY.w $B402
	LDA.b $0E
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FD
	BEQ.b C4B9E1_MarkPathCandidateFootprintsInGrid_NextTopRowColumn
	LDA.b #$FF
	STA.b [$06]
C4B9E1_MarkPathCandidateFootprintsInGrid_NextTopRowColumn:
	INX
C4B9E2_MarkPathCandidateFootprintsInGrid_CheckTopRowColumn:
	CPX.w $B402
	BCC.b C4B9B6_MarkPathCandidateFootprintsInGrid_TopRowColumn
	REP.b #$20
	LDA.b $0E
	INC
	STA.b $0E
C4B9EE_MarkPathCandidateFootprintsInGrid_CheckTopRows:
	CMP.w $B404
	BCC.b C4B9B1_MarkPathCandidateFootprintsInGrid_TopRowLoopStart
	LDA.w $B400
	SEC
	SBC.w $B404
	STA.b $0E
	BRA.b C4BA3B_MarkPathCandidateFootprintsInGrid_CheckBottomRows

C4B9FE_MarkPathCandidateFootprintsInGrid_BottomRowLoopStart:
	LDX.w #$0000
	BRA.b C4BA2F_MarkPathCandidateFootprintsInGrid_CheckBottomRowColumn

C4BA03_MarkPathCandidateFootprintsInGrid_BottomRowColumn:
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	STX.b $02
	LDY.w $B402
	LDA.b $0E
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FD
	BEQ.b C4BA2E_MarkPathCandidateFootprintsInGrid_NextBottomRowColumn
	LDA.b #$FF
	STA.b [$06]
C4BA2E_MarkPathCandidateFootprintsInGrid_NextBottomRowColumn:
	INX
C4BA2F_MarkPathCandidateFootprintsInGrid_CheckBottomRowColumn:
	CPX.w $B402
	BCC.b C4BA03_MarkPathCandidateFootprintsInGrid_BottomRowColumn
	REP.b #$20
	LDA.b $0E
	INC
	STA.b $0E
C4BA3B_MarkPathCandidateFootprintsInGrid_CheckBottomRows:
	CMP.w $B400
	BCC.b C4B9FE_MarkPathCandidateFootprintsInGrid_BottomRowLoopStart
	LDX.w #$0000
	BRA.b C4BA82_MarkPathCandidateFootprintsInGrid_CheckLeftColumns

C4BA45_MarkPathCandidateFootprintsInGrid_LeftColumnLoop:
	LDA.w #$0000
	STA.b $14
	BRA.b C4BA7C_MarkPathCandidateFootprintsInGrid_CheckLeftColumnRow

C4BA4C_MarkPathCandidateFootprintsInGrid_LeftColumnRow:
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	STX.b $02
	LDY.w $B402
	LDA.b $14
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FD
	BEQ.b C4BA75_MarkPathCandidateFootprintsInGrid_NextLeftColumnRow
	LDA.b #$FF
	STA.b [$06]
C4BA75_MarkPathCandidateFootprintsInGrid_NextLeftColumnRow:
	REP.b #$20
	LDA.b $14
	INC
	STA.b $14
C4BA7C_MarkPathCandidateFootprintsInGrid_CheckLeftColumnRow:
	CMP.w $B400
	BCC.b C4BA4C_MarkPathCandidateFootprintsInGrid_LeftColumnRow
	INX
C4BA82_MarkPathCandidateFootprintsInGrid_CheckLeftColumns:
	CPX.w $B404
	BCC.b C4BA45_MarkPathCandidateFootprintsInGrid_LeftColumnLoop
	LDA.w $B402
	SEC
	SBC.w $B404
	TAX
	BRA.b C4BACE_MarkPathCandidateFootprintsInGrid_CheckRightColumns

C4BA91_MarkPathCandidateFootprintsInGrid_RightColumnLoop:
	LDA.w #$0000
	STA.b $14
	BRA.b C4BAC8_MarkPathCandidateFootprintsInGrid_CheckRightColumnRow

C4BA98_MarkPathCandidateFootprintsInGrid_RightColumnRow:
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	STX.b $02
	LDY.w $B402
	LDA.b $14
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b #$FD
	BEQ.b C4BAC1_MarkPathCandidateFootprintsInGrid_NextRightColumnRow
	LDA.b #$FF
	STA.b [$06]
C4BAC1_MarkPathCandidateFootprintsInGrid_NextRightColumnRow:
	REP.b #$20
	LDA.b $14
	INC
	STA.b $14
C4BAC8_MarkPathCandidateFootprintsInGrid_CheckRightColumnRow:
	CMP.w $B400
	BCC.b C4BA98_MarkPathCandidateFootprintsInGrid_RightColumnRow
	INX
C4BACE_MarkPathCandidateFootprintsInGrid_CheckRightColumns:
	CPX.w $B402
	BCC.b C4BA91_MarkPathCandidateFootprintsInGrid_RightColumnLoop
	LDY.b $10
	TYX
	STZ.w $0006,X
	TYX
	STZ.w $0008,X
C4BADD_MarkPathCandidateFootprintsInGrid_NextCandidateFromM8:
	REP.b #$20
	LDA.b $12
	STA.b $02
	INC.b $02
	LDA.b $02
	STA.b $12
C4BAE9_MarkPathCandidateFootprintsInGrid_CheckCandidateLoop:
	LDA.b $02
	CMP.b $04
	BCS.b C4BAF4_MarkPathCandidateFootprintsInGrid_Return
	BEQ.b C4BAF4_MarkPathCandidateFootprintsInGrid_Return
	JMP.w C4B96B_MarkPathCandidateFootprintsInGrid_CandidateLoop

C4BAF4_MarkPathCandidateFootprintsInGrid_Return:
	PLD
	RTS
