; EarthBound C4 Sound Stone presentation table prototype.
;
; Source-emission status:
; - Prototype level: build-candidate data corridor.
; - C4 source-bank scaffold slice.
; - ROM bytes are emitted as source-adjacent table rows for byte-equivalence validation.
;
; Source units covered:
; - C4:AC57..C4:ACCE Sound Stone EF payload pointer table and local
;   presentation coordinate/control tables.
;
; The controller at C4:ACCE indexes these tables directly. Keep these labels
; table-local: the C1 callers enter the controller, while C4 owns the layout.

; ---------------------------------------------------------------------------
; C4:ACCE

; SoundStonePresentationTablesEnd

; ---------------------------------------------------------------------------
; C4:AC57

C4AC57_SoundStonePresentationDataBlock:
C4AC57_SoundStonePresentationTableBlock = C4AC57_SoundStonePresentationDataBlock
C4AC57_SoundStonePresentationEfPayloadPointerTable:
    ; Nine 4-byte long pointers into EF presentation payload rows. The
    ; controller indexes these as low word + bank byte + padding byte.
C4AC57_SoundStonePresentationEfPayloadPointer0:
    dw $4A40
    db $EF,$00
C4AC5B_SoundStonePresentationEfPayloadPointer1:
    dw $4AD0
    db $EF,$00
C4AC5F_SoundStonePresentationEfPayloadPointer2:
    dw $4B3A
    db $EF,$00
C4AC63_SoundStonePresentationEfPayloadPointer3:
    dw $4BA4
    db $EF,$00
C4AC67_SoundStonePresentationEfPayloadPointer4:
    dw $4C0E
    db $EF,$00
C4AC6B_SoundStonePresentationEfPayloadPointer5:
    dw $4C78
    db $EF,$00
C4AC6F_SoundStonePresentationEfPayloadPointer6:
    dw $4CE2
    db $EF,$00
C4AC73_SoundStonePresentationEfPayloadPointer7:
    dw $4D4C
    db $EF,$00
C4AC77_SoundStonePresentationEfPayloadPointer8:
    dw $4DB6
    db $EF,$00

C4AC7B_SoundStonePresentationTileXTable:
    db $80,$B8,$C8,$B8,$80,$48,$38,$48

C4AC83_SoundStonePresentationTileYTable:
    db $28,$38,$70,$A8,$B8,$A8,$70,$38

C4AC8B_SoundStonePresentationSpriteXTable:
    db $00,$04,$08,$0C,$44,$40,$48,$4C

C4AC93_SoundStonePresentationSpriteYTable:
    db $01,$04,$04,$02,$02,$01,$02,$03

C4AC9B_SoundStonePresentationSpriteOffsetXTable:
    db $00,$04,$08,$0C,$24,$20,$28,$2C

C4ACA3_SoundStonePresentationSpriteOffsetYTable:
    db $01,$03,$01,$02,$02,$01,$02,$03

C4ACAB_SoundStonePresentationMelodyIdTable:
    db $A0,$A1,$A2,$A3,$A4,$A5,$A6,$A7,$A8

C4ACB4_SoundStonePresentationPhraseLengthTable:
    ; Nine entries: eight Sanctuary timings plus the sentinel/count path.
    dw $0121,$00D2,$00D1,$00D2,$00D2,$00D1,$00D2,$00D2,$00D2

C4ACC6_SoundStonePresentationSanctuaryEventTable:
    db $B6,$B7,$B9,$B8,$BA,$BB,$BC,$BD

C4ACCE_SoundStonePresentationTablesEnd = USE_SOUND_STONE
