; EarthBound C4 Sound Stone presentation table prototype.
;
; Source-emission status:
; - Prototype level: build-candidate data corridor.
; - C4 source-bank scaffold slice.
; - ROM bytes are emitted directly as a source-adjacent db block for byte-equivalence validation.
;
; Source units covered:
; - C4:AC57..C4:ACCE Sound Stone EF payload pointer table and local
;   presentation coordinate/control tables.

; ---------------------------------------------------------------------------
; C4:ACCE

; SoundStonePresentationTablesEnd

; ---------------------------------------------------------------------------
; C4:AC57

C4AC57_SoundStonePresentationTableBlock:
    ; data bytes: C4:AC57..C4:ACCE
    db $40,$4A,$EF,$00,$D0,$4A,$EF,$00,$3A,$4B,$EF,$00,$A4,$4B,$EF,$00
    db $0E,$4C,$EF,$00,$78,$4C,$EF,$00,$E2,$4C,$EF,$00,$4C,$4D,$EF,$00
    db $B6,$4D,$EF,$00,$80,$B8,$C8,$B8,$80,$48,$38,$48,$28,$38,$70,$A8
    db $B8,$A8,$70,$38,$00,$04,$08,$0C,$44,$40,$48,$4C,$01,$04,$04,$02
    db $02,$01,$02,$03,$00,$04,$08,$0C,$24,$20,$28,$2C,$01,$03,$01,$02
    db $02,$01,$02,$03,$A0,$A1,$A2,$A3,$A4,$A5,$A6,$A7,$A8,$21,$01,$D2
    db $00,$D1,$00,$D2,$00,$D2,$00,$D1,$00,$D2,$00,$D2,$00,$D2,$00,$B6
    db $B7,$B9,$B8,$BA,$BB,$BC,$BD

C4ACCE_SoundStonePresentationTablesEnd:
