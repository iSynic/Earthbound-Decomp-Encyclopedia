; EarthBound C4 battle/inventory status text and lookup tables.
;
; Source-emission status:
; - Prototype level: build-candidate data corridor.
; - ROM bytes are emitted directly as a source-adjacent db block for byte-equivalence validation.
;
; Source units covered:
; - C4:550E..C4:5637 battle text, selector records, and 8-bit powers table.

; ---------------------------------------------------------------------------
; C4:5637

; BattleInventoryStatusTextAndTablesEnd

; ---------------------------------------------------------------------------
; C4:550E

C4550E_BattleInventoryStatusTextAndSelectorTables:
    ; data bytes: C4:550E..C4:5637
    db $00,$00,$00,$00,$0C,$F5,$97,$18,$01,$98,$06,$19,$98,$06,$1F,$98
    db $0C,$25,$98,$84,$31,$98,$84,$35,$98,$05,$CE,$99,$81,$D3,$99,$84
    db $D4,$99,$82,$13,$9A,$82,$15,$9A,$82,$D8,$99,$82,$19,$9A,$82,$1B
    db $9A,$82,$DA,$99,$81,$E3,$99,$81,$E4,$99,$81,$E5,$99,$81,$E6,$99
    db $81,$E7,$99,$81,$E8,$99,$81,$E9,$99,$81,$F0,$99,$81,$EA,$99,$81
    db $EB,$99,$81,$EC,$99,$81,$ED,$99,$81,$EE,$99,$05,$2D,$9A,$81,$32
    db $9A,$84,$33,$9A,$82,$72,$9A,$82,$74,$9A,$82,$37,$9A,$82,$78,$9A
    db $82,$7A,$9A,$82,$39,$9A,$81,$42,$9A,$81,$43,$9A,$81,$44,$9A,$81
    db $45,$9A,$81,$46,$9A,$81,$47,$9A,$81,$48,$9A,$81,$4F,$9A,$81,$49
    db $9A,$81,$4A,$9A,$81,$4B,$9A,$81,$4C,$9A,$81,$4D,$9A,$05,$8C,$9A
    db $81,$91,$9A,$84,$92,$9A,$82,$D1,$9A,$82,$D3,$9A,$82,$96,$9A,$82
    db $D7,$9A,$82,$D9,$9A,$82,$98,$9A,$81,$A1,$9A,$81,$A2,$9A,$81,$A3
    db $9A,$81,$A4,$9A,$81,$A5,$9A,$81,$A6,$9A,$81,$A7,$9A,$81,$AE,$9A
    db $81,$A8,$9A,$81,$A9,$9A,$81,$AA,$9A,$81,$AB,$9A,$81,$AC,$9A,$05
    db $EB,$9A,$81,$F0,$9A,$84,$F1,$9A,$82,$30,$9B,$82,$32,$9B,$82,$F5
    db $9A,$82,$36,$9B,$82,$38,$9B,$82,$F7,$9A,$81,$00,$9B,$81,$01,$9B
    db $81,$02,$9B,$81,$03,$9B,$81,$04,$9B,$81,$05,$9B,$81,$06,$9B,$81
    db $0D,$9B,$81,$07,$9B,$81,$08,$9B,$81,$09,$9B,$81,$0A,$9B,$81,$0B
    db $9B,$01,$02,$04,$08,$10,$20,$40,$80

C45637_BattleInventoryStatusTextAndTablesEnd:
