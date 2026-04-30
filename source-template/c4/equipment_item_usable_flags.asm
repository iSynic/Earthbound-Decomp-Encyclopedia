; EarthBound C4 equipment item usable flags.
;
; Source-emission status:
; - Prototype level: build-candidate data corridor.
; - ROM bytes are emitted directly as a source-adjacent db block for byte-equivalence validation.
;
; Source units covered:
; - C4:58AB..C4:58AF four-byte item/equipment usable flag mask table.

; ---------------------------------------------------------------------------
; C4:58AF

; EquipmentItemUsableFlagsEnd

; ---------------------------------------------------------------------------
; C4:58AB

C458AB_EquipmentItemUsableFlags:
    ; data bytes: C4:58AB..C4:58AF
    db $01,$02,$04,$08

C458AF_EquipmentItemUsableFlagsEnd:
