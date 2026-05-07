; EarthBound C4 path-solver scratch cursor helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - C4 source-bank scaffold slice.
; - Derived from notes/pathfinding-frontier-c0b9bc-c0ba35.md and direct ROM
;   decode of C4:B587..C4:B59F.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c4-build-candidate-ranges.json.
;
; Source units covered:
; - C4:B587..C4:B595 scratch cursor allocator.
; - C4:B595..C4:B59F scratch usage reporter.

; ---------------------------------------------------------------------------
; C4:B587

; AllocPathSolverScratchWords
C4B587_AllocPathSolverScratchWords:
	REP.b #$31
	LDX.w $B43A
	CLC
	ADC.w $B43A
	STA.w $B43A
	TXA
	RTS

; ---------------------------------------------------------------------------
; C4:B595

; GetPathSolverScratchUsage
C4B595_GetPathSolverScratchUsage:
	REP.b #$31
	LDA.w $B43A
	SEC
	SBC.w $B438
	RTL
