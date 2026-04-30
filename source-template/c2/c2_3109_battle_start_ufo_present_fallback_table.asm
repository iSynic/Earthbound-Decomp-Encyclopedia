; EarthBound C2 battle-start UFO present fallback table.
;
; Source-emission status:
; - Prototype level: source-locked data table.
; - Two 9-byte records: enemy id, then eight fallback present candidates.
;
; Source unit covered:
; - C2:3109..C2:311B BattleStartUfoPresentFallbackTable

; ---------------------------------------------------------------------------
; C2:3109

C23109_BattleStartUfoPresentFallbackTable:
    db $84,$58,$59,$5A,$5B,$5C,$5D,$5F,$00
    db $85,$6A,$6B,$6C,$6D,$6E,$6F,$70,$00

; ---------------------------------------------------------------------------
; C2:311B

C2311B_BattleStartUfoPresentFallbackTable_End:
