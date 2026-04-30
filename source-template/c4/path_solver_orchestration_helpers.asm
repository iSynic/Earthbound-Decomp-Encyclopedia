; EarthBound C4 path-solver orchestration helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:B59F..C4:B7A5.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B59F..C4:B7A5 path-solver state setup and candidate-group orchestration.

; ---------------------------------------------------------------------------
; External contracts used by this module

C09032_MultiplyAByY                           = $C09032
C4B587_AllocPathSolverScratchWords_Addr       = $B587
C4B7A5_MarkPathGridBorderBlocked_Addr         = $B7A5
C4B859_SortPathCandidatePointersByGridPosition_Addr = $B859
C4B923_MarkPathCandidateFootprintsInGrid_Addr = $B923
C4BAF6_PropagatePathGridCandidateRoutes_Addr  = $BAF6
C4BD9A_TracePathGridRouteIntoStepList_Addr    = $BD9A
C4BF7F_CompressCollinearPathStepList_Addr     = $BF7F

; ---------------------------------------------------------------------------
; C4:B59F

; RunPathGridCandidateSolver
C4B59F_RunPathGridCandidateSolver:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFCC
	TCD
	PLA
	STY.b $04
	STX.b $02
	STA.b $32
	LDA.b $54
	STA.b $30
	LDY.b $52
	STY.b $2E
	LDA.b $50
	STA.b $2C
	LDA.b $4E
	STA.b $2A
	LDX.b $4C
	STX.b $28
	LDA.b $4A
	STA.b $26
	LDA.b $48
	STA.b $24
	LDX.b $46
	STX.b $22
	LDA.b $42
	STA.b $06
	LDA.b $44
	STA.b $08
	STZ.b $20
	LDA.b $02
	STA.w $B438
	LDA.b $02
	STA.w $B43A
	LDA.b $02
	CLC
	ADC.b $32
	STA.w $B43C
	LDX.b $04
	LDA.w $0000,X
	STA.w $B400
	LDX.b $04
	LDY.w $0002,X
	STY.w $B402
	LDX.b $22
	STX.w $B404
	JSL.l C09032_MultiplyAByY
	STA.w $B406
	LDA.b $06
	STA.w $B3FC
	LDA.b $08
	STA.w $B3FE
	LDA.b $30
	ASL
	STA.b $02
	INC
	INC
	JSR.w C4B587_AllocPathSolverScratchWords_Addr
	STA.b $1E
	STA.w $B408
	CLC
	ADC.b $02
	STA.w $B40A
	LDA.b $1E
	STA.w $B40E
	STA.w $B40C
	LDA.w $B402
	EOR.w #$FFFF
	INC
	STA.w $B410
	LDA.w #$0001
	STA.w $B412
	LDA.w $B402
	STA.w $B414
	LDA.w #$FFFF
	STA.w $B416
	STA.w $B418
	STZ.w $B41A
	STZ.w $B41C
	LDA.w #$0001
	STA.w $B41E
	STA.w $B420
	STZ.w $B422
	STZ.w $B424
	LDA.w #$FFFF
	STA.w $B426
	STA.w $B428
	LDA.w #$0001
	STA.w $B42A
	STA.w $B42C
	STA.w $B42E
	STA.w $B430
	LDA.w #$FFFF
	STA.w $B432
	STA.w $B434
	STA.w $B436
	LDA.b $2E
	CMP.w #$00FB
	BCC.b C4B692_RunPathGridCandidateSolver_AllocateSortedCandidates
	LDA.w #$00FB
	STA.b $2E
C4B692_RunPathGridCandidateSolver_AllocateSortedCandidates:
	LDA.b $28
	ASL
	JSR.w C4B587_AllocPathSolverScratchWords_Addr
	STA.b $1C
	LDY.b $1C
	LDX.b $2A
	LDA.b $28
	JSR.w C4B859_SortPathCandidatePointersByGridPosition_Addr
	LDA.b $2E
	ASL
	ASL
	JSR.w C4B587_AllocPathSolverScratchWords_Addr
	STA.b $2A
	JSR.w C4B7A5_MarkPathGridBorderBlocked_Addr
	STZ.b $1A
	STZ.b $18
	LDA.w #$0000
	STA.b $04
	JMP.w C4B796_RunPathGridCandidateSolver_CheckCandidateLoop

C4B6BB_RunPathGridCandidateSolver_CandidateLoop:
	LDA.b $04
	ASL
	TAY
	LDA.b ($1C),Y
	STA.b $02
	STA.b $32
	LDX.b $02
	LDA.w $0002,X
	CMP.b $1A
	BNE.b C4B6D7_RunPathGridCandidateSolver_StartGroup
	LDX.b $02
	LDA.w $0004,X
	CMP.b $18
	BEQ.b C4B734_RunPathGridCandidateSolver_TraceAndCompact

C4B6D7_RunPathGridCandidateSolver_StartGroup:
	LDY.w #$0001
	STY.b $16
	LDX.b $02
	LDA.w $0002,X
	STA.b $1A
	LDX.b $02
	LDA.w $0004,X
	STA.b $18
	LDA.b $04
	INC
	STA.b $1E
	BRA.b C4B70E_RunPathGridCandidateSolver_CheckGroupScan

C4B6F1_RunPathGridCandidateSolver_GroupScan:
	ASL
	TAY
	LDA.b ($1C),Y
	TAX
	LDA.w $0002,X
	CMP.b $1A
	BNE.b C4B712_RunPathGridCandidateSolver_GroupComplete
	LDA.w $0004,X
	CMP.b $18
	BNE.b C4B712_RunPathGridCandidateSolver_GroupComplete
	LDY.b $16
	INY
	STY.b $16
	LDA.b $1E
	INC
	STA.b $1E
C4B70E_RunPathGridCandidateSolver_CheckGroupScan:
	CMP.b $28
	BCC.b C4B6F1_RunPathGridCandidateSolver_GroupScan
C4B712_RunPathGridCandidateSolver_GroupComplete:
	LDA.b $04
	ASL
	CLC
	ADC.b $1C
	TAX
	LDY.b $16
	TYA
	JSR.w C4B923_MarkPathCandidateFootprintsInGrid_Addr
	LDY.b $16
	STY.b $0E
	LDA.b $2E
	STA.b $10
	LDA.b $2C
	STA.b $12
	LDY.b $02
	LDX.b $26
	LDA.b $24
	JSR.w C4BAF6_PropagatePathGridCandidateRoutes_Addr
C4B734_RunPathGridCandidateSolver_TraceAndCompact:
	LDY.b $2A
	LDX.b $2E
	LDA.b $02
	CLC
	ADC.w #$0006
	JSR.w C4BD9A_TracePathGridRouteIntoStepList_Addr
	LDX.b $02
	STA.w $000E,X
	LDX.b $2A
	JSR.w C4BF7F_CompressCollinearPathStepList_Addr
	STA.b $14
	ASL
	ASL
	JSR.w C4B587_AllocPathSolverScratchWords_Addr
	STA.b $22
	STZ.b $1E
	BRA.b C4B778_RunPathGridCandidateSolver_CheckCopyPathLoop

C4B758_RunPathGridCandidateSolver_CopyPathLoop:
	LDA.b $1E
	ASL
	ASL
	TAX
	STX.b $02
	LDA.b $22
	CLC
	ADC.b $02
	TAY
	TXA
	CLC
	ADC.b $2A
	TAX
	LDA.w $0000,X
	STA.w $0000,Y
	LDA.w $0002,X
	STA.w $0002,Y
	INC.b $1E
C4B778_RunPathGridCandidateSolver_CheckCopyPathLoop:
	LDA.b $1E
	CMP.b $14
	BCC.b C4B758_RunPathGridCandidateSolver_CopyPathLoop
	LDA.b $14
	LDX.b $32
	STX.b $02
	STA.w $000A,X
	LDA.b $22
	LDX.b $02
	STA.w $000C,X
	LDA.b $14
	BEQ.b C4B794_RunPathGridCandidateSolver_NextCandidate
	INC.b $20
C4B794_RunPathGridCandidateSolver_NextCandidate:
	INC.b $04
C4B796_RunPathGridCandidateSolver_CheckCandidateLoop:
	LDA.b $04
	CMP.b $28
	BCS.b C4B7A1_RunPathGridCandidateSolver_Return
	BEQ.b C4B7A1_RunPathGridCandidateSolver_Return
	JMP.w C4B6BB_RunPathGridCandidateSolver_CandidateLoop

C4B7A1_RunPathGridCandidateSolver_Return:
	LDA.b $20
	PLD
	RTL
