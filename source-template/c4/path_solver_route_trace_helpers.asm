; EarthBound C4 path-solver route trace helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:BD9A..C4:BF7F.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:BD9A..C4:BF7F route tracing from propagated grid distances into a
;   step-list buffer.

; ---------------------------------------------------------------------------
; External contracts used by this module

C09032_MultiplyAByY                           = $C09032

; ---------------------------------------------------------------------------
; C4:BD9A

; TracePathGridRouteIntoStepList
C4BD9A_TracePathGridRouteIntoStepList:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFD2
	TCD
	PLA
	STY.b $2C
	STX.b $2A
	TAX
	LDA.w $0000,X
	STA.b $28
	LDA.w $0002,X
	STA.b $26
	LDY.w #$0000
	STY.b $24
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDY.w $B402
	LDA.b $28
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $26
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	STA.b $00
	CMP.b #$FB
	BCC.b C4BDE7_TracePathGridRouteIntoStepList_CheckRequestedLength
	BEQ.b C4BDE7_TracePathGridRouteIntoStepList_CheckRequestedLength
	REP.b #$20
	LDA.w #$0000
	JMP.w C4BF7D_TracePathGridRouteIntoStepList_Return

C4BDE7_TracePathGridRouteIntoStepList_CheckRequestedLength:
	REP.b #$20
	LDA.b $2A
	BNE.b C4BDF3_TracePathGridRouteIntoStepList_SeedFirstPoint
	LDA.w #$0000
	JMP.w C4BF7D_TracePathGridRouteIntoStepList_Return

C4BDF3_TracePathGridRouteIntoStepList_SeedFirstPoint:
	LDX.b $2C
	LDA.b $28
	STA.w $0000,X
	LDA.b $26
	STA.w $0002,X
	LDA.w #$0001
	STA.b $22
	JMP.w C4BF71_TracePathGridRouteIntoStepList_CheckDistance

C4BE07_TracePathGridRouteIntoStepList_FindPreviousStep:
	LDA.w #$029A
	STA.b $20
	STA.b $1E
	SEP.b #$20
	LDA.b $00
	DEC
	STA.b $00
	LDY.b $24
	STY.b $02
	REP.b #$20
	LDA.b $02
	STA.b $1C
	STZ.b $24
	JMP.w C4BF16_TracePathGridRouteIntoStepList_CheckNeighborLoop

C4BE24_TracePathGridRouteIntoStepList_NeighborLoop:
	LDA.b $02
	ASL
	ASL
	TAY
	LDA.w $B418,Y
	CLC
	ADC.b $28
	TAX
	LDA.w $B41A,Y
	CLC
	ADC.b $26
	STA.b $1A
	LDA.b $02
	INC
	AND.w #$0003
	STA.b $04
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.b $1A
	STA.b $02
	LDY.w $B402
	TXA
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b $00
	BEQ.b C4BE69_TracePathGridRouteIntoStepList_FoundDistanceNeighbor
	JMP.w C4BF0C_TracePathGridRouteIntoStepList_NextNeighbor

C4BE69_TracePathGridRouteIntoStepList_FoundDistanceNeighbor:
	REP.b #$20
	LDA.b $20
	CMP.w #$029A
	BNE.b C4BE7E_TracePathGridRouteIntoStepList_TestSecondLookahead
	LDA.b $1C
	STA.b $02
	STA.b $20
	STX.b $0E
	LDA.b $1A
	STA.b $10
C4BE7E_TracePathGridRouteIntoStepList_TestSecondLookahead:
	LDA.b $1C
	STA.b $02
	ASL
	ASL
	TAX
	LDA.w $B428,X
	CLC
	ADC.b $28
	STA.b $18
	LDA.w $B42A,X
	CLC
	ADC.b $26
	TAY
	STY.b $16
	LDA.b $00
	AND.w #$00FF
	DEC
	PHA
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	STY.b $02
	LDY.w $B402
	LDA.b $18
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	LDA.b [$06]
	AND.w #$00FF
	PLY
	STY.b $02
	CMP.b $02
	BNE.b C4BF0C_TracePathGridRouteIntoStepList_NextNeighbor
	LDA.b $04
	ASL
	ASL
	TAX
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.w $B41A,X
	CLC
	ADC.b $26
	STA.b $02
	LDY.w $B402
	LDA.w $B418,X
	CLC
	ADC.b $28
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	CMP.b $00
	BNE.b C4BF0C_TracePathGridRouteIntoStepList_NextNeighbor
	REP.b #$20
	LDA.b $1C
	STA.b $02
	STA.b $1E
	LDA.b $18
	STA.b $12
	LDY.b $16
	STY.b $14
	BRA.b C4BF22_TracePathGridRouteIntoStepList_SelectCandidate

C4BF0C_TracePathGridRouteIntoStepList_NextNeighbor:
	REP.b #$20
	LDA.b $04
	STA.b $02
	STA.b $1C
	INC.b $24
C4BF16_TracePathGridRouteIntoStepList_CheckNeighborLoop:
	LDA.b $24
	CMP.w #$0004
	BCS.b C4BF22_TracePathGridRouteIntoStepList_SelectCandidate
	BEQ.b C4BF22_TracePathGridRouteIntoStepList_SelectCandidate
	JMP.w C4BE24_TracePathGridRouteIntoStepList_NeighborLoop

C4BF22_TracePathGridRouteIntoStepList_SelectCandidate:
	LDA.b $1E
	CMP.w #$029A
	BEQ.b C4BF3E_TracePathGridRouteIntoStepList_UseFirstLookahead
	LDA.b $12
	STA.b $28
	LDA.b $14
	STA.b $26
	LDY.b $1E
	STY.b $24
	SEP.b #$20
	LDA.b $00
	DEC
	STA.b $00
	BRA.b C4BF51_TracePathGridRouteIntoStepList_AppendPoint

C4BF3E_TracePathGridRouteIntoStepList_UseFirstLookahead:
	LDA.b $20
	CMP.w #$029A
	BEQ.b C4BF7B_TracePathGridRouteIntoStepList_ReturnCount
	LDA.b $0E
	STA.b $28
	LDA.b $10
	STA.b $26
	LDY.b $20
	STY.b $24
C4BF51_TracePathGridRouteIntoStepList_AppendPoint:
	REP.b #$20
	LDA.b $2A
	CMP.b $22
	BNE.b C4BF5D_TracePathGridRouteIntoStepList_StoreNextPoint
	LDA.b $22
	BRA.b C4BF7D_TracePathGridRouteIntoStepList_Return

C4BF5D_TracePathGridRouteIntoStepList_StoreNextPoint:
	LDA.b $22
	ASL
	ASL
	CLC
	ADC.b $2C
	TAX
	LDA.b $28
	STA.w $0000,X
	LDA.b $26
	STA.w $0002,X
	INC.b $22
C4BF71_TracePathGridRouteIntoStepList_CheckDistance:
	LDA.b $00
	AND.w #$00FF
	BEQ.b C4BF7B_TracePathGridRouteIntoStepList_ReturnCount
	JMP.w C4BE07_TracePathGridRouteIntoStepList_FindPreviousStep

C4BF7B_TracePathGridRouteIntoStepList_ReturnCount:
	LDA.b $22
C4BF7D_TracePathGridRouteIntoStepList_Return:
	PLD
	RTS
