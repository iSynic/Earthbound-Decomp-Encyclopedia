; EarthBound C4 battle overlay transition data prototype.
;
; Source-emission status:
; - Prototype level: build-candidate data corridor.
; - C4 source-bank scaffold slice.
; - ROM bytes are emitted directly as a source-adjacent db block for byte-equivalence validation.
;
; Source units covered:
; - C4:A591..C4:A67E battle background static transition wave table and
;   battle swirl overlay open/close mode scripts.

; ---------------------------------------------------------------------------
; C4:A67E

; BattleOverlayTransitionDataEnd

; ---------------------------------------------------------------------------
; C4:A591

C4A591_BattleOverlayTransitionDataBlock:
    ; data bytes: C4:A591..C4:A67E
    db $00,$0E,$17,$17,$0C,$FB,$EE,$F0,$00,$0F,$0C,$FA,$F2,$00,$0D,$02
    db $F5,$00,$0A,$FC,$F9,$08,$00,$FA,$07,$FE,$FD,$06,$FB,$03,$00,$FE
    db $03,$FC,$04,$FC,$04,$FD,$03,$FD,$03,$FE,$02,$FF,$00,$01,$FE,$02
    db $FF,$FF,$02,$FF,$00,$01,$FF,$FF,$01,$00,$FF,$00,$01,$3D,$00,$80
    db $00,$70,$00,$00,$00,$00,$00,$00,$00,$00,$00,$E0,$00,$B7,$00,$04
    db $00,$03,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$64,$00,$80,$00,$70,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$E0,$00,$B7,$00,$04,$00,$03,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$3D,$00,$80,$00,$70,$00,$00,$80,$00,$80,$00
    db $00,$00,$00,$20,$FF,$49,$FF,$FC,$FF,$FD,$FF,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
    db $00,$64,$00,$80,$00,$70,$00,$00,$80,$00,$80,$00,$00,$00,$00,$20
    db $FF,$49,$FF,$FC,$FF,$FD,$FF,$00,$00,$00,$00,$00,$00,$00,$00,$00
    db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00

C4A67E_BattleOverlayTransitionDataEnd:
