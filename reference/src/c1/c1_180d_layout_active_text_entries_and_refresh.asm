; EarthBound C1 active text-entry layout wrapper.
;
; Source-emission status:
; - Prototype level: build-candidate
; - Hand-polished from tools/emit_linear_source_module.py output, then
;   intended for byte-equivalence validation.
;
; Source unit covered:
; - C1:180D..C1:181B LayoutActiveTextEntriesAndRefresh

; ---------------------------------------------------------------------------
; External contracts used by this module
; - Thin wrapper around C4:51FA active text-entry chain layout followed by the
;   C1:163C active-chain render/refresh path.
; - Used by broad menu/text-command paths that need to recompute $89D4 row/page
;   metadata before displaying entries.

C1163C_RefreshTextEntryChainState       = $163C
C451FA_LayoutActiveTextEntryChain       = $C451FA

InitialEntryChainIndex = $0000

; ---------------------------------------------------------------------------
; C1:180D

C1180D_LayoutActiveTextEntriesAndRefresh:
    rep #$31
    txy
    ldx.w #InitialEntryChainIndex
    jsl C451FA_LayoutActiveTextEntryChain
    jsr C1163C_RefreshTextEntryChainState
    rts
