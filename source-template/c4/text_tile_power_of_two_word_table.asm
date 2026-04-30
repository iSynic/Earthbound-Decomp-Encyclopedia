; EarthBound C4 text tile bit-mask / power-of-two word table.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Preserved as data for byte-equivalence validation.
;
; Source units covered:
; - C4:4C6C..C4:4C8C TextTilePowerOfTwoWordTable

; ---------------------------------------------------------------------------
; C4:4C6C

C44C6C_TextTileBitMaskTable:
    dw $0001,$0002,$0004,$0008,$0010,$0020,$0040,$0080
    dw $0100,$0200,$0400,$0800,$1000,$2000,$4000,$8000
