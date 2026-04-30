; EarthBound C4 path-solver grid border helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:B7A5..C4:B859.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B7A5..C4:B859 path-grid border blocker.

; ---------------------------------------------------------------------------
; External contracts used by this module

C09032_MultiplyAByY                           = $C09032

; ---------------------------------------------------------------------------
; C4:B7A5

; MarkPathGridBorderBlocked
C4B7A5_MarkPathGridBorderBlocked:
	REP.b #$31
	PHD
	TDC
	ADC.w #$FFF1
	TCD
	LDX.w #$0000
	BRA.b C4B800_MarkPathGridBorderBlocked_CheckHorizontalLoop

C4B7B2_MarkPathGridBorderBlocked_HorizontalLoop:
	SEP.b #$20
	LDA.b #$FD
	STA.b $0E
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDA.w $B402
	DEC
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
	LDA.b $0E
	STA.b [$06]
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	LDY.w $B402
	TXA
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b $0E
	STA.b [$06]
	INX
C4B800_MarkPathGridBorderBlocked_CheckHorizontalLoop:
	CPX.w $B400
	BCC.b C4B7B2_MarkPathGridBorderBlocked_HorizontalLoop
	LDX.w #$0000
	BRA.b C4B850_MarkPathGridBorderBlocked_CheckVerticalLoop

C4B80A_MarkPathGridBorderBlocked_VerticalLoop:
	SEP.b #$20
	LDA.b #$FD
	STA.b $0E
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	STX.b $02
	LDY.w $B402
	LDA.w $B400
	DEC
	JSL.l C09032_MultiplyAByY
	CLC
	ADC.b $02
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b $0E
	STA.b [$06]
	REP.b #$20
	LDA.w $B3FC
	STA.b $06
	LDA.w $B3FE
	STA.b $08
	TXA
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b $0E
	STA.b [$06]
	INX
C4B850_MarkPathGridBorderBlocked_CheckVerticalLoop:
	CPX.w $B402
	BCC.b C4B80A_MarkPathGridBorderBlocked_VerticalLoop
	REP.b #$20
	PLD
	RTS
