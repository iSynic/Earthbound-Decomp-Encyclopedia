; EarthBound C4 battle overlay script stepper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from the legacy disassembly with ROM decode correction at C4:AB32.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:A7B0..C4:AC57 battle overlay script state per-frame stepper.

; ---------------------------------------------------------------------------
; External contracts used by this module

C0AE34_StepBattleOverlayAnimationParity       = $C0AE34
C0AFCD_ApplyBattleOverlayPaletteOrState      = $C0AFCD
C0B01A_ClearBattleOverlayWindowState         = $C0B01A
C0B047_ApplyBattleOverlayTileState           = $C0B047
C0B0B8_ApplyBattleOverlayFrameTiles          = $C0B0B8
C2DE96_ClearBattleVisualOverlayState         = $C2DE96

; ---------------------------------------------------------------------------
; C4:A7B0

; StepBattleOverlayScriptState
label_C4A7B0:
	REP.b #$31
	PHD
	TDC
	ADC.w #$FFE9
	TCD
	LDA.w $AEC2
	AND.w #$00FF
	BNE.b label_C4A7C3
	JMP.w label_C4AC53

label_C4A7C3:
	LDY.w #$AECC
	LDA.w #$0000
	STA.b $06
	LDA.w #$0000
	STA.b $08
	LDA.w $0000,Y
	STA.b $0A
	LDA.w $0002,Y
	STA.b $0C
	CMP.b $08
	BNE.b label_C4A7E2
	LDA.b $0A
	CMP.b $06
label_C4A7E2:
	BNE.b label_C4A7E7
	JMP.w label_C4AA1A

label_C4A7E7:
	LDX.w #$AEC2
	SEP.b #$20
	LDA.w $0000,X
	DEC
	STA.w $AEC2
	REP.b #$20
	AND.w #$00FF
	BEQ.b label_C4A7FD
	JMP.w label_C4A915

label_C4A7FD:
	LDA.w $0000,Y
	STA.b $0A
	LDA.w $0002,Y
	STA.b $0C
	SEP.b #$20
	LDA.b [$0A]
	STA.w $AEC2
	REP.b #$20
	AND.w #$00FF
	BNE.b label_C4A822
	LDA.b $06
	STA.w $0000,Y
	LDA.b $08
	STA.w $0002,Y
	JMP.w label_C4AC53

label_C4A822:
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDY.w #$0002
	LDA.b [$06],Y
	CMP.w #$8000
	BEQ.b label_C4A839
	STA.w $AED0
label_C4A839:
	LDA.w $AECC
	STA.b $06
	LDA.w $AECE
	STA.b $08
	LDY.w #$0004
	LDA.b [$06],Y
	CMP.w #$8000
	BEQ.b label_C4A850
	STA.w $AED2
label_C4A850:
	LDA.w $AECC
	STA.b $06
	LDA.w $AECE
	STA.b $08
	LDY.w #$0006
	LDA.b [$06],Y
	CMP.w #$8000
	BEQ.b label_C4A867
	STA.w $AED4
label_C4A867:
	LDA.w $AECC
	STA.b $06
	LDA.w $AECE
	STA.b $08
	LDY.w #$0008
	LDA.b [$06],Y
	CMP.w #$8000
	BEQ.b label_C4A87E
	STA.w $AED6
label_C4A87E:
	LDY.w #$AECC
	STY.b $15
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDY.w #$000A
	LDA.b [$06],Y
	STA.w $AED8
	LDY.b $15
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDY.w #$000C
	LDA.b [$06],Y
	STA.w $AEDA
	LDY.b $15
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDY.w #$000E
	LDA.b [$06],Y
	STA.w $AEDC
	LDY.b $15
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDY.w #$0010
	LDA.b [$06],Y
	STA.w $AEDE
	LDY.b $15
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDY.w #$0012
	LDA.b [$06],Y
	STA.w $AEE0
	LDY.b $15
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDY.w #$0014
	LDA.b [$06],Y
	STA.w $AEE2
	LDY.b $15
	LDA.w $0000,Y
	STA.b $06
	LDA.w $0002,Y
	STA.b $08
	LDA.w #$0016
	CLC
	ADC.b $06
	STA.b $06
	STA.w $0000,Y
	LDA.b $08
	STA.w $0002,Y
label_C4A915:
	LDX.w #$AED0
	LDA.w $0000,X
	CLC
	ADC.w $AED8
	STA.w $0000,X
	LDX.w #$AED2
	LDA.w $0000,X
	CLC
	ADC.w $AEDA
	STA.w $0000,X
	LDX.w #$AEDC
	LDA.w $0000,X
	CLC
	ADC.w $AEE0
	STA.w $0000,X
	LDY.w #$AEDE
	LDA.w $0000,Y
	CLC
	ADC.w $AEE2
	STA.w $0000,Y
	LDA.w $0000,X
	STA.b $15
	STA.b $02
	LDA.w #$0000
	CLC
	SBC.b $02
	BVC.b label_C4A95C
	BPL.b label_C4A978
	BRA.b label_C4A95E

label_C4A95C:
	BMI.b label_C4A978
label_C4A95E:
	LDX.w #$AED4
	LDA.b $15
	EOR.w #$FFFF
	INC
	STA.b $02
	LDA.w $0000,X
	CMP.b $02
	BCS.b label_C4A978
	LDA.w #$0000
	STA.w $0000,X
	BRA.b label_C4A985

label_C4A978:
	LDX.w #$AED4
	LDA.w $0000,X
	CLC
	ADC.w $AEDC
	STA.w $0000,X
label_C4A985:
	LDA.w $AEDE
	STA.b $15
	STA.b $02
	LDA.w #$0000
	CLC
	SBC.b $02
	BVC.b label_C4A998
	BPL.b label_C4A9B4
	BRA.b label_C4A99A

label_C4A998:
	BMI.b label_C4A9B4
label_C4A99A:
	LDX.w #$AED6
	LDA.b $15
	EOR.w #$FFFF
	INC
	STA.b $02
	LDA.w $0000,X
	CMP.b $02
	BCS.b label_C4A9B4
	LDA.w #$0000
	STA.w $0000,X
	BRA.b label_C4A9C1

label_C4A9B4:
	LDX.w #$AED6
	LDA.w $0000,X
	CLC
	ADC.w $AEDE
	STA.w $0000,X

label_C4A9C1:
	LDA.w $AED4
	BNE.b label_C4A9E1
	LDA.w $AED6
	BNE.b label_C4A9E1
	SEP.b #$20
	STZ.w $AEC2
	REP.b #$20
	LDA.w #$0000
	STA.w $AECC
	LDA.w #$0000
	STA.w $AECE
	JMP.w label_C4AC53

label_C4A9E1:
	LDA.w $AED6
	XBA
	AND.w #$00FF
	STA.b $0E
	LDA.w $AED4
	XBA
	AND.w #$00FF
	TAY
	LDX.w $AED2
	LDA.w $AED0
	JSL.l $C0B149
	LDX.w #$0041
	LDA.w #$0003
	JSL.l $C0B0EF
	LDA.w $AEC6
	AND.w #$00FF
	TAX
	LDA.w $AEC8
	AND.w #$00FF
	JSL.l C0B047_ApplyBattleOverlayTileState
	JMP.w label_C4AC53

label_C4AA1A:
	LDX.w #$AEC2
	SEP.b #$20
	LDA.w $0000,X
	DEC
	STA.w $AEC2
	REP.b #$20
	AND.w #$00FF
	BEQ.b label_C4AA30
	JMP.w label_C4AC53

label_C4AA30:
	LDX.w #$AEC4
	STX.b $15
	REP.b #$20
	LDA.w $0000,X
	AND.w #$00FF
	BNE.b label_C4AA42
	JMP.w label_C4AB20

label_C4AA42:
	SEP.b #$20
	LDA.w $AEC3
	STA.w $AEC2
	LDY.w #$AEC9
	STY.b $13
	REP.b #$20
	LDA.w $0000,Y
	AND.w #$00FF
	INC
	INC
	INC
	JSL.l C0AE34_StepBattleOverlayAnimationParity
	LDY.b $13
	SEP.b #$20
	LDA.w $0000,Y
	INC
	STA.w $0000,Y
	AND.b #$01
	STA.w $0000,Y
	REP.b #$20
	LDA.w $AEC7
	AND.w #$00FF
	BNE.b label_C4AAC3
	LDX.w #$AEC5
	STX.b $15
	SEP.b #$20
	LDA.w $0000,X
	STA.b $12
	REP.b #$20
	LDA.w #$0000
	STA.b $06
	LDA.w #$00CE
	STA.b $08
	LDA.b $12
	AND.w #$00FF
	ASL
	TAX
	LDA.l $CEDC45,X
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b $12
	INC
	LDX.b $15
	STA.w $0000,X
	REP.b #$20
	LDA.b $06
	STA.b $0E
	LDA.b $08
	STA.b $10
	LDA.w $0000,Y
	AND.w #$00FF
	INC
	INC
	INC
	JSL.l C0B0B8_ApplyBattleOverlayFrameTiles
	BRA label_C4AB00

label_C4AAC3:
	LDX.w #$AEC5
	SEP.b #$20
	LDA.w $0000,X
	DEC
	STA.b $12
	STA.w $0000,X
	REP.b #$20
	LDA.w #$0000
	STA.b $06
	LDA.w #$00CE
	STA.b $08
	LDA.b $12
	AND.w #$00FF
	ASL
	TAX
	LDA.l $CEDC45,X
	CLC
	ADC.b $06
	STA.b $06
	STA.b $0E
	LDA.b $08
	STA.b $10
	LDA.w $0000,Y
	AND.w #$00FF
	INC
	INC
	INC
	JSL.l C0B0B8_ApplyBattleOverlayFrameTiles
label_C4AB00:
	LDA.w $AEC6
	AND.w #$00FF
	TAX
	LDA.w $AEC8
	AND.w #$00FF
	JSL.l C0B047_ApplyBattleOverlayTileState
	LDX.w #$AEC4
	SEP.b #$20
	LDA.w $0000,X
	DEC
	STA.w $0000,X
	JMP.w label_C4AC53

label_C4AB20:
	LDA.w #$AEE4
	STA.b $02
	LDX.b $02
	LDA.w $0000,X
	AND.w #$00FF
	BNE.b label_C4AB32
	JMP.w label_C4AC07

label_C4AB32:
	LDY.w #$AEE6
	SEP.b #$20
	LDA.w $0000,Y
	DEC
	STA.w $0000,Y
	REP.b #$20
	AND.w #$00FF
	BEQ.b label_C4ABB0
	LDA.w #$DD41
	STA.b $06
	LDA.w #$00CE
	STA.b $08
	LDX.b $02
	LDA.w $0000,X
	AND.w #$00FF
	ASL
	ASL
	INC
	INC
	LDX.b $06
	STX.b $0A
	LDX.b $08
	STX.b $0C
	CLC
	ADC.b $0A
	STA.b $0A
	SEP.b #$20
	LDA.b [$0A]
	LDX.b $15
	STA.w $0000,X
	LDY.w #$AEC5
	LDX.b $02
	REP.b #$20
	LDA.w $0000,X
	AND.w #$00FF
	ASL
	ASL
	INC
	CLC
	ADC.b $06
	STA.b $06
	SEP.b #$20
	LDA.b [$06]
	STA.b $12
	STA.w $0000,Y
	REP.b #$20
	LDA.w $AEC7
	AND.w #$00FF
	BNE.b label_C4AB9C
	JMP.w label_C4AA30

label_C4AB9C:
	LDX.b $15
	SEP.b #$20
	LDA.w $0000,X
	STA.b $00
	LDA.b $12
	CLC
	ADC.b $00
	STA.w $0000,Y
	JMP.w label_C4AA30

label_C4ABB0:
	LDX.w #$AEE5
	SEP.b #$20
	LDA.w $0000,X
	INC
	STA.w $0000,X
	REP.b #$20
	AND.w #$00FF
	CMP.w #$0001
	BEQ.b label_C4ABD2
	CMP.w #$0002
	BEQ.b label_C4ABE0
	CMP.w #$0003
	BEQ.b label_C4ABEE
	BRA.b label_C4ABFA

label_C4ABD2:
	SEP.b #$20
	LDA.b #$04
	STA.w $0000,Y
	LDA.b #$03
	STA.w $AEC3
	BRA.b label_C4ABFA

label_C4ABE0:
	SEP.b #$20
	LDA.b #$06
	STA.w $0000,Y
	LDA.b #$02
	STA.w $AEC3
	BRA.b label_C4ABFA

label_C4ABEE:
	SEP.b #$20
	LDA.b #$0C
	STA.w $0000,Y
	LDA.b #$01
	STA.w $AEC3
label_C4ABFA:
	REP.b #$20
	LDA.w $AEE6
	AND.w #$00FF
	BEQ.b label_C4AC07
	JMP.w label_C4AA30

label_C4AC07:
	LDX.w #$AECA
	LDA.w $0000,X
	AND.w #$00FF
	BEQ.b label_C4AC22
	SEP.b #$20
	LDA.b #$01
	STA.w $AEC2
	LDA.w $0000,X
	DEC
	STA.w $0000,X
	BRA.b label_C4AC53

label_C4AC22:
	LDA.w $AECB
	AND.w #$00FF
	BEQ.b label_C4AC53
	LDA.w $AEC9
	AND.w #$00FF
	INC
	INC
	INC
	JSL.l C0AE34_StepBattleOverlayAnimationParity
	LDX.w #$0000
	TXA
	JSL.l C0B047_ApplyBattleOverlayTileState
	JSL.l C2DE96_ClearBattleVisualOverlayState
	LDY.w #$0000
	TYX
	TYA
	JSL.l C0B01A_ClearBattleOverlayWindowState
	LDA.w $AD8A
	JSL.l C0AFCD_ApplyBattleOverlayPaletteOrState

label_C4AC53:
	REP.b #$20
	PLD
	RTL
