; EarthBound C3 HP / PP adjustment helper prototype.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Assembler contract: pilot-ready
; - Assembler-ready pilot; not yet linked into a full assembler ROM build.
; - Derived from notes/c3-source-emission-plan.md and
;   notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md.
; - Build-candidate conventions are documented in
;   notes/c3-build-candidate-source-conventions.md.
; - Original instruction flow is preserved in address order with symbolic
;   comments for local direct-page variables and WRAM fields.
; - ROM byte range, SHA-1, and source signature are tracked by
;   build/c3-build-candidate-ranges.json and
;   build/c3-source-signature-validation.json.
;
; Source units covered:
; - C3:EC1F..C3:EC8B DepleteCharacterHp
; - C3:EC8B..C3:ED2C RecoverCharacterHp
; - C3:ED2C..C3:ED98 DepleteCharacterPp
; - C3:ED98..C3:EE14 RecoverCharacterPp
;
; Evidence:
; - notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md
; - notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md
; - notes/text-command-family-1e-stat-recovery.md

; ---------------------------------------------------------------------------
; External contracts used by this module

C08FF7_Multiply16                 = $C08FF7
C09086_PercentNumeratorMultiply   = $C09086
C090FF_DivideOrScaleByHundred     = $C090FF

; C0:8FF7 Multiply16
;   Input:  A = multiplicand, Y = multiplier
;   Output: A = product

; C0:9086 PercentNumeratorMultiply
;   Uses caller DP $06/$08 and $0A/$0C as a 32-bit multiply/ratio numerator
;   staging area while resolving max_stat * percent.

; C0:90FF DivideOrScaleByHundred
;   Uses caller DP $06/$08 and $0A/$0C; here $0A/$0C is set to 100.

; ---------------------------------------------------------------------------
; Local data contracts and WRAM fields

CHARACTER_RECORD_STRIDE        = $005F
PERCENT_DENOMINATOR            = $0064

CHARACTER_MAX_HP_BASE          = $99D8
CHARACTER_MAX_PP_BASE          = $99DA
CHARACTER_HP_MARKER_BASE       = $9A13
CHARACTER_CURRENT_HP_BASE      = $9A15
CHARACTER_CURRENT_PP_BASE      = $9A1B

; Shared entry contract for all four workers:
;   A = 1-based character id; A == 0 exits without changing state
;   X = direct amount or percent value
;   Y = 0 for percent mode, nonzero for direct amount mode
;
; Shared local shape:
;   $02 = resolved amount, initially X
;   $04/$0E/$10 = zero-based character index or multiplied record offset
;   $06/$08 and $0A/$0C = percent helper staging
;   $12 = scratch max/current value in recovery workers

; ---------------------------------------------------------------------------
; C3:EC1F

; DepleteCharacterHp
;
; Source contract:
;   current_hp = max(current_hp - resolved_amount, 0)
C3EC1F_DepleteCharacterHp:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    stx $02                         ; amount_or_percent = X
    tax
    beq C3EC89_DepleteCharacterHp_Return
    txa
    dec A
    sta $0E                         ; zero-based character index
    cpy #$0000
    bne C3EC64_DepleteCharacterHp_ApplyDirectAmount

    ; Percent mode: amount = max_hp * X / 100.
    lda $02
    sta $0A
    stz $0C
    lda $0E
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16           ; C0:8FF7 Multiply16
    tax
    lda CHARACTER_MAX_HP_BASE,X
    sta $06
    stz $08
    jsl C09086_PercentNumeratorMultiply ; C0:9086 PercentNumeratorMultiply
    lda #PERCENT_DENOMINATOR
    sta $0A
    lda #$0000
    sta $0C
    jsl C090FF_DivideOrScaleByHundred ; C0:90FF DivideOrScaleByHundred
    lda $06
    sta $02

C3EC64_DepleteCharacterHp_ApplyDirectAmount:
    lda $0E
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16           ; record_offset
    tay
    clc
    adc #CHARACTER_CURRENT_HP_BASE
    tax
    lda $0000,X
    sec
    sbc $02
    sta $0000,X
    cmp CHARACTER_MAX_HP_BASE,Y      ; underflow/wrap lands above max
    bcc C3EC89_DepleteCharacterHp_Return
    beq C3EC89_DepleteCharacterHp_Return
    lda #$0000
    sta $0000,X

C3EC89_DepleteCharacterHp_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:EC8B

; RecoverCharacterHp
;
; Source contract:
;   current_hp = min(current_hp + resolved_amount, max_hp)
;   hp_marker = 1 if hp_marker == 0
C3EC8B_RecoverCharacterHp:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEC
    tcd
    pla
    stx $02                         ; amount_or_percent = X
    tax
    bne C3EC9D_RecoverCharacterHp_NonzeroCharacter
    jmp C3ED2A_RecoverCharacterHp_Return

C3EC9D_RecoverCharacterHp_NonzeroCharacter:
    txa
    dec A
    sta $04                         ; zero-based character index
    cpy #$0000
    bne C3ECD3_RecoverCharacterHp_ApplyDirectAmount

    ; Percent mode: amount = max_hp * X / 100.
    lda $02
    sta $0A
    stz $0C
    lda $04
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda CHARACTER_MAX_HP_BASE,X
    sta $06
    stz $08
    jsl C09086_PercentNumeratorMultiply
    lda #PERCENT_DENOMINATOR
    sta $0A
    lda #$0000
    sta $0C
    jsl C090FF_DivideOrScaleByHundred
    lda $06
    sta $02

C3ECD3_RecoverCharacterHp_ApplyDirectAmount:
    lda $04
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    sta $12                         ; record_offset
    clc
    adc #CHARACTER_CURRENT_HP_BASE
    tax
    lda $0000,X
    clc
    adc $02
    sta $0000,X

    lda $12
    clc
    adc #CHARACTER_HP_MARKER_BASE
    tax
    lda $0000,X
    bne C3ECFE_RecoverCharacterHp_MarkerReady
    lda #$0001
    sta $0000,X

C3ECFE_RecoverCharacterHp_MarkerReady:
    lda $04
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    sta $10                         ; record_offset
    clc
    adc #CHARACTER_CURRENT_HP_BASE
    tax
    stx $0E                         ; current HP pointer
    lda $10
    tax
    lda CHARACTER_MAX_HP_BASE,X
    sta $12
    sta $02
    ldx $0E
    lda $0000,X
    cmp $02
    bcc C3ED2A_RecoverCharacterHp_Return
    beq C3ED2A_RecoverCharacterHp_Return
    lda $12
    sta $0000,X

C3ED2A_RecoverCharacterHp_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:ED2C

; DepleteCharacterPp
;
; Source contract:
;   current_pp = max(current_pp - resolved_amount, 0)
C3ED2C_DepleteCharacterPp:
    rep #$31
    phd
    pha
    tdc
    adc #$FFF0
    tcd
    pla
    stx $02                         ; amount_or_percent = X
    tax
    beq C3ED96_DepleteCharacterPp_Return
    txa
    dec A
    sta $0E                         ; zero-based character index
    cpy #$0000
    bne C3ED71_DepleteCharacterPp_ApplyDirectAmount

    ; Percent mode: amount = max_pp * X / 100.
    lda $02
    sta $0A
    stz $0C
    lda $0E
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda CHARACTER_MAX_PP_BASE,X
    sta $06
    stz $08
    jsl C09086_PercentNumeratorMultiply
    lda #PERCENT_DENOMINATOR
    sta $0A
    lda #$0000
    sta $0C
    jsl C090FF_DivideOrScaleByHundred
    lda $06
    sta $02

C3ED71_DepleteCharacterPp_ApplyDirectAmount:
    lda $0E
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tay
    clc
    adc #CHARACTER_CURRENT_PP_BASE
    tax
    lda $0000,X
    sec
    sbc $02
    sta $0000,X
    cmp CHARACTER_MAX_PP_BASE,Y      ; underflow/wrap lands above max
    bcc C3ED96_DepleteCharacterPp_Return
    beq C3ED96_DepleteCharacterPp_Return
    lda #$0000
    sta $0000,X

C3ED96_DepleteCharacterPp_Return:
    pld
    rtl

; ---------------------------------------------------------------------------
; C3:ED98

; RecoverCharacterPp
;
; Source contract:
;   current_pp = min(current_pp + resolved_amount, max_pp)
;   Unlike HP recovery, this routine does not write the paired $9A19 field.
C3ED98_RecoverCharacterPp:
    rep #$31
    phd
    pha
    tdc
    adc #$FFEE
    tcd
    pla
    stx $02                         ; amount_or_percent = X
    tax
    beq C3EE12_RecoverCharacterPp_Return
    txa
    dec A
    sta $10                         ; zero-based character index
    cpy #$0000
    bne C3EDDD_RecoverCharacterPp_ApplyDirectAmount

    ; Percent mode: amount = max_pp * X / 100.
    lda $02
    sta $0A
    stz $0C
    lda $10
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    tax
    lda CHARACTER_MAX_PP_BASE,X
    sta $06
    stz $08
    jsl C09086_PercentNumeratorMultiply
    lda #PERCENT_DENOMINATOR
    sta $0A
    lda #$0000
    sta $0C
    jsl C090FF_DivideOrScaleByHundred
    lda $06
    sta $02

C3EDDD_RecoverCharacterPp_ApplyDirectAmount:
    lda $10
    ldy #CHARACTER_RECORD_STRIDE
    jsl C08FF7_Multiply16
    sta $10                         ; record_offset
    clc
    adc #CHARACTER_CURRENT_PP_BASE
    tay
    lda $0000,Y
    clc
    adc $02
    tax
    stx $0E                         ; provisional current_pp
    txa
    sta $0000,Y
    lda $10
    tax
    lda CHARACTER_MAX_PP_BASE,X
    sta $10
    sta $02
    ldx $0E
    txa
    cmp $02
    bcc C3EE12_RecoverCharacterPp_Return
    beq C3EE12_RecoverCharacterPp_Return
    lda $10
    sta $0000,Y

C3EE12_RecoverCharacterPp_Return:
    pld
    rtl
