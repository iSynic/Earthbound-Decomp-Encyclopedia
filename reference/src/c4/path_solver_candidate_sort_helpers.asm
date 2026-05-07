; EarthBound C4 path-solver candidate pointer-sort helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:B859..C4:B923.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B859..C4:B923 candidate pointer list builder/sorter.

; ---------------------------------------------------------------------------
; C4:B859

; SortPathCandidatePointersByGridPosition
C4B859_SortPathCandidatePointersByGridPosition:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFE0
	TCD
	PLA
	STY.b $1E
	STA.b $1C
	DEC
	STA.b $1A
	LDA.w #$0000
	STA.b $18
	BRA.b C4B88A_SortPathCandidatePointersByGridPosition_CheckInitLoop

C4B871_SortPathCandidatePointersByGridPosition_InitLoop:
	ASL
	TAY
	LDA.b $18
	STA.b $04
	ASL
	ASL
	ASL
	ADC.b $04
	ASL
	STA.b $02
	TXA
	CLC
	ADC.b $02
	STA.b ($1E),Y
	LDA.b $18
	INC
	STA.b $18
C4B88A_SortPathCandidatePointersByGridPosition_CheckInitLoop:
	CMP.b $1C
	BCC.b C4B871_SortPathCandidatePointersByGridPosition_InitLoop
	LDA.b $1C
	CMP.w #$0001
	BEQ.b C4B897_SortPathCandidatePointersByGridPosition_ReturnJump
	BCS.b C4B89A_SortPathCandidatePointersByGridPosition_BeginSort
C4B897_SortPathCandidatePointersByGridPosition_ReturnJump:
	JMP.w C4B921_SortPathCandidatePointersByGridPosition_Return

C4B89A_SortPathCandidatePointersByGridPosition_BeginSort:
	LDA.w #$0000
	STA.b $04
	BRA.b C4B916_SortPathCandidatePointersByGridPosition_CheckOuterLoop

C4B8A1_SortPathCandidatePointersByGridPosition_OuterLoop:
	LDA.w #$FFFF
	STA.b $16
	STA.b $14
	LDY.b $04
	STY.b $12
	BRA.b C4B8F2_SortPathCandidatePointersByGridPosition_CheckInnerLoop

C4B8AE_SortPathCandidatePointersByGridPosition_InnerLoop:
	TYA
	ASL
	TAY
	LDA.b ($1E),Y
	TAX
	LDA.w $0002,X
	STA.b $10
	LDA.w $0004,X
	STA.b $02
	LDA.b $10
	CMP.b $16
	BEQ.b C4B8D0_SortPathCandidatePointersByGridPosition_CompareY
	LDX.w #$0000
	CMP.b $16
	BCS.b C4B8DC_SortPathCandidatePointersByGridPosition_TestBetter
	LDX.w #$0001
	BRA.b C4B8DC_SortPathCandidatePointersByGridPosition_TestBetter

C4B8D0_SortPathCandidatePointersByGridPosition_CompareY:
	LDX.w #$0000
	LDA.b $02
	CMP.b $14
	BCS.b C4B8DC_SortPathCandidatePointersByGridPosition_TestBetter
	LDX.w #$0001
C4B8DC_SortPathCandidatePointersByGridPosition_TestBetter:
	CPX.w #$0000
	BEQ.b C4B8ED_SortPathCandidatePointersByGridPosition_NextInner
	LDA.b $10
	STA.b $16
	LDA.b $02
	STA.b $14
	LDY.b $12
	STY.b $0E
C4B8ED_SortPathCandidatePointersByGridPosition_NextInner:
	LDY.b $12
	INY
	STY.b $12
C4B8F2_SortPathCandidatePointersByGridPosition_CheckInnerLoop:
	CPY.b $1C
	BCC.b C4B8AE_SortPathCandidatePointersByGridPosition_InnerLoop
	LDA.b $04
	ASL
	CLC
	ADC.b $1E
	TAY
	LDA.w $0000,Y
	STA.b $18
	LDA.b $0E
	ASL
	CLC
	ADC.b $1E
	TAX
	LDA.w $0000,X
	STA.w $0000,Y
	LDA.b $18
	STA.w $0000,X
	INC.b $04
C4B916_SortPathCandidatePointersByGridPosition_CheckOuterLoop:
	LDA.b $04
	CMP.b $1A
	BCS.b C4B921_SortPathCandidatePointersByGridPosition_Return
	BEQ.b C4B921_SortPathCandidatePointersByGridPosition_Return
	JMP.w C4B8A1_SortPathCandidatePointersByGridPosition_OuterLoop

C4B921_SortPathCandidatePointersByGridPosition_Return:
	PLD
	RTS
