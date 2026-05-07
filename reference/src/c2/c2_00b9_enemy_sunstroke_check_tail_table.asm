; EarthBound C2 enemy sunstroke check tail table.
;
; Source-emission status:
; - Prototype level: source-locked data tail.
; - This table follows the callable C2:0000..00B9 routine.
;
; Source unit covered:
; - C2:00B9..C2:00D1 EnemySunstrokeCheckTailTable

; ---------------------------------------------------------------------------
; C2:00B9

C200B9_EnemySunstrokeCheckTailTable:
    db $F8,$FF,$00,$00,$07,$00
    db $F8,$FF,$00,$00,$07,$00
    db $00,$00,$00,$00,$00,$00
    db $07,$00,$07,$00,$07,$00

; ---------------------------------------------------------------------------
; C2:00D1

C200D1_EnemySunstrokeCheckTailTable_End:
