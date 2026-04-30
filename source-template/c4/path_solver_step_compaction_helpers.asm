; EarthBound C4 path-solver step-list compaction helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:BF7F..C4:C05E.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:BF7F..C4:C05E collinear step-list compaction for path output.

; ---------------------------------------------------------------------------
; C4:BF7F

; CompressCollinearPathStepList
C4BF7F_CompressCollinearPathStepList:
	REP.b #$31
	PHD
	PHA
	TDC
	ADC.w #$FFE0
	TCD
	PLA
	STX.b $1E
	STA.b $1C
	CMP.w #$0003
	BCS.b C4BF97_CompressCollinearPathStepList_Begin
	BEQ.b C4BF97_CompressCollinearPathStepList_Begin
	JMP.w C4C05A_CompressCollinearPathStepList_ReturnCount

C4BF97_CompressCollinearPathStepList_Begin:
	LDA.w $0004,X
	STA.b $04
	LDA.w $0006,X
	STA.b $02
	STA.b $1A
	LDA.w $0000,X
	STA.b $02
	LDA.b $04
	SEC
	SBC.b $02
	STA.b $18
	LDA.b $1A
	STA.b $02
	SEC
	SBC.w $0002,X
	STA.b $16
	LDA.w #$0001
	STA.b $14
	LDA.w #$0002
	STA.b $12
	JMP.w C4C04A_CompressCollinearPathStepList_CheckLoop

C4BFC6_CompressCollinearPathStepList_Loop:
	LDA.b $12
	ASL
	ASL
	STA.b $02
	LDX.b $1E
	TXA
	CLC
	ADC.b $02
	TAY
	LDA.w $0000,Y
	STA.b $10
	LDA.w $0002,Y
	TAY
	STY.b $0E
	LDA.b $10
	STA.b $02
	LDA.b $04
	CLC
	ADC.b $18
	CMP.b $02
	BNE.b C4C013_CompressCollinearPathStepList_EmitCorner
	LDA.b $1A
	STA.b $02
	CLC
	ADC.b $16
	STY.b $02
	CMP.b $02
	BNE.b C4C013_CompressCollinearPathStepList_EmitCorner
	LDA.b $14
	ASL
	ASL
	STA.b $04
	TXA
	CLC
	ADC.b $04
	STA.b $02
	LDA.b $10
	LDX.b $02
	STA.w $0000,X
	TYA
	LDX.b $02
	STA.w $0002,X
	BRA.b C4C03E_CompressCollinearPathStepList_AdvanceLoop

C4C013_CompressCollinearPathStepList_EmitCorner:
	INC.b $14
	LDA.b $14
	ASL
	ASL
	STA.b $02
	TXA
	CLC
	ADC.b $02
	STA.b $18
	LDA.b $10
	STA.b ($18)
	TYA
	LDY.w #$0002
	STA.b ($18),Y
	LDA.b $10
	SEC
	SBC.b $04
	STA.b $18
	LDA.b $1A
	STA.b $02
	LDY.b $0E
	TYA
	SEC
	SBC.b $02
	STA.b $16
C4C03E_CompressCollinearPathStepList_AdvanceLoop:
	LDA.b $10
	STA.b $04
	STY.b $02
	LDA.b $02
	STA.b $1A
	INC.b $12
C4C04A_CompressCollinearPathStepList_CheckLoop:
	LDA.b $12
	CMP.b $1C
	BCS.b C4C055_CompressCollinearPathStepList_StoreCount
	BEQ.b C4C055_CompressCollinearPathStepList_StoreCount
	JMP.w C4BFC6_CompressCollinearPathStepList_Loop

C4C055_CompressCollinearPathStepList_StoreCount:
	LDA.b $14
	INC
	STA.b $1C
C4C05A_CompressCollinearPathStepList_ReturnCount:
	LDA.b $1C
	PLD
	RTS
