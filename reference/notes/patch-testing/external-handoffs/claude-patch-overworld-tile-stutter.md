# Patch: Overworld Tile-Load Stutter Fix

**Patch file:** `EarthBound (USA) - patched.sfc`
**Status:** Applied and boot-fixed. Ready for emulator testing.
**Last touched:** 2026-03-26

---

## Problem

Walking on the overworld causes periodic stuttering. The stutter correlates with tile/CHR data being loaded into VRAM as the player moves through new map regions.

**Root cause:** The VRAM block-transfer routine `C0:85B7` (call it `VRAM_BlockTransfer`) is synchronous and blocking. It:

1. Writes transfer parameters into WRAM slots (`$0091`/`$0092`/`$0094`/`$0096`/`$0097`)
2. Spin-waits on `$0099` (total queued bytes) until the NMI has capacity
3. Calls `C0:8643` to append an 8-byte DMA record into the NMI queue at `$0400,Y`
4. For transfers larger than `$1200` bytes, it loops — spin-waiting again for each `$1200`-byte chunk

During the loading paths at `C0:09D1` and `C0:09EA`, the game queues `$7000`-byte and `$4000`-byte VRAM transfers. A `$7000` byte transfer requires `ceil($7000 / $1200)` = 10 spin-wait/enqueue cycles, each burning a full NMI period. The engine stalls for potentially 10+ frames while the CPU is stuck waiting on DMA completion, which manifests as a visible stutter.

---

## NMI / DMA queue background

- The NMI handler (`C0:8170` → `NMI_FrameUpdate`) processes the DMA queue at `C0:8240` (`NMI_ProcessTransferQueue`)
- Queue records live in WRAM `$0400+X`, 8 bytes each
- `$0099` is the running total of bytes currently queued; the NMI decrements it as records are processed
- DMA channel 0 is used by the queue (controlled via `$420B` bit 0)
- `C0:8643` appends one 8-byte record and adds the transfer size to `$0099`

---

## Patch design

The patch replaces the two blocking `JSL C0:85B7` call sites with a deferred system:

- **Call sites:** store transfer parameters immediately and return — no waiting, no queueing
- **NMI hook:** each NMI processes up to `$1200` bytes of any pending deferred transfer via DMA channel 1

This spreads a large transfer (e.g., `$7000` bytes) across ~10 NMI periods transparently, instead of blocking the main-loop thread for ~10 frames.

---

## Hook inventory

### Hook 1: `C0:8012` — boot/init hook

**Original:** `A9 00 1F 5B` = `LDA #$1F00; TCD`
**Patched:** `5C 14 CD EF` = `JML $EFCD14`

`EF:CD14` runs the replaced instructions (`LDA #$1F00; TCD`) then clears `$00B0` (the pending-transfer size) and jumps back to `C0:8016`.

**Purpose:** Initialises `$00B0 = 0` at boot so the first NMI doesn't see garbage as a pending transfer.

---

### Hook 2: `C0:09D1` — VRAM transfer call site 1

**Original:** `22 B7 85 C0` = `JSL $C085B7`
**Patched:** `22 9B CC EF` = `JSL $EFCC9B`

**Context before call:** `X = $7000` (bytes), `Y = $0000` (VRAM word address), `DP+$0E` = source address, `DP+$10` = source bank byte.

`EF:CC9B` (`SaveTransferContext`) saves these parameters to WRAM scratch and RTLs immediately without calling `C0:85B7`.

---

### Hook 3: `C0:09EA` — VRAM transfer call site 2

**Original:** `22 B7 85 C0` = `JSL $C085B7`
**Patched:** `22 9B CC EF` = `JSL $EFCC9B`

Same redirect. Note: `C0:09D5` (`BRA $09EE`) means this call site is skipped on the common path; it is patched defensively in case it is reached via an alternate entry.

---

### Hook 4: `C0:834E` — per-NMI transfer hook

**Original:** `C2 30 64 99` = `REP #$30; STZ $99,dp`
**Patched:** `5C B2 CC EF` = `JML $EFCCB2`

`EF:CCB2` (`NMI_DeferredTransferChunk`) runs the replaced instructions as its prologue, then checks `$00B0` and performs one chunk of deferred DMA if a transfer is pending.

---

## Patch code at `EF:CC9B` (132 bytes used)

All patch code lives in previously-unused (`$FF`-filled) space at `EF:CC9B`. The patch slightly extends into 4 bytes of data at `EF:CD1B`–`EF:CD1E` which were originally a sequential count table (`00 01 02 03`); these bytes are overwritten by the `JML $C08016` tail of the boot hook.

### `EF:CC9B` — `SaveTransferContext` (23 bytes, called via JSL)

```
EF:CC9B  REP #$30
EF:CC9D  STX $00B0      ; save X = remaining byte count
EF:CCA0  STY $00B6      ; save Y = VRAM word destination
EF:CCA3  LDA $0E,dp     ; load DMA source address (16-bit)
EF:CCA5  STA $00B2      ; save source address
EF:CCA8  SEP #$20
EF:CCAA  LDA $10,dp     ; load DMA source bank (8-bit)
EF:CCAC  STA $00B4      ; save source bank
EF:CCAF  REP #$20
EF:CCB1  RTL
```

WRAM scratch layout after this call:
| Address | Content |
|---------|---------|
| `$00B0` (16-bit) | remaining byte count |
| `$00B2` (16-bit) | source address |
| `$00B4` (8-bit)  | source bank |
| `$00B6` (16-bit) | VRAM word destination |

---

### `EF:CCB2` — `NMI_DeferredTransferChunk` (94 bytes, entered via JML from NMI)

```
EF:CCB2  REP #$30           ; [replaces original C0:834E] 16-bit A and X
EF:CCB4  STZ $99,dp         ; [replaces original C0:8350] clear DP+$99
EF:CCB6  LDA $00B0           ; load remaining byte count
EF:CCB9  BEQ $CD10           ; if 0, no transfer pending — skip to JML
EF:CCBB  CMP #$1201          ; compare against $1201
EF:CCBE  BCC $CCC3           ; if count <= $1200, use as-is
EF:CCC0  LDA #$1200          ; else cap chunk at $1200 bytes
EF:CCC3  PHA                 ; push this_chunk_size
EF:CCC4  LDA $00B0
EF:CCC7  SEC
EF:CCC8  SBC $01,S           ; subtract this_chunk from remaining
EF:CCCA  STA $00B0           ; store updated remaining count
         ; --- Set up DMA channel 1 ---
EF:CCCD  LDA $01,S           ; reload this_chunk_size
EF:CCCF  STA $4315           ; DAS1 = transfer size (16-bit)
EF:CCD2  LDA $00B2
EF:CCD5  STA $4312           ; A1T1 = source address
EF:CCD8  LDA $00B6
EF:CCDB  STA $2116           ; VMAIN dest = VRAM word address
EF:CCDE  SEP #$20
EF:CCE0  LDA $00B4
EF:CCE3  STA $4314           ; A1B1 = source bank
EF:CCE6  LDA #$01
EF:CCE8  STA $4310           ; DMAP1 = mode 1 (fixed dest, word)
EF:CCEB  LDA #$18
EF:CCED  STA $4311           ; BBAD1 = $2118 (VRAM data port)
EF:CCF0  LDA #$80
EF:CCF2  STA $2115           ; VMAIN = word-increment mode
EF:CCF5  LDA #$02
EF:CCF7  STA $420B           ; MDMAEN bit 1 = kick DMA channel 1
         ; --- Advance source and dest for next chunk ---
EF:CCFA  REP #$20
EF:CCFC  LDA $01,S           ; reload this_chunk_size
EF:CCFE  CLC
EF:CCFF  ADC $00B2
EF:CD02  STA $00B2           ; advance source address by chunk bytes
EF:CD05  LDA $01,S
EF:CD08  LSR                 ; bytes / 2 = VRAM word count
EF:CD09  CLC
EF:CD0A  ADC $00B6
EF:CD0D  STA $00B6           ; advance VRAM dest by word count
EF:CD0F  PLA                 ; pop this_chunk_size
EF:CD10  JML $C08352         ; return to NMI continuation
```

**`$CD10` is also the BEQ target** for the `$00B0 == 0` fast path — no PHA was done in that case, so no PLA is needed.

---

### `EF:CD14` — boot hook continuation (11 bytes)

```
EF:CD14  LDA #$1F00   ; [replaces original C0:8012]
EF:CD17  TCD          ; [replaces original C0:8015]
EF:CD18  STZ $00B0    ; clear pending transfer flag
EF:CD1B  JML $C08016  ; return to C0:8016 (post-patch-site)
```

---

## Known limitations / potential issues

1. **Only one deferred transfer at a time.** `SaveTransferContext` unconditionally overwrites `$00B0`–`$00B6`. If a second `JSL` fires before the first deferred transfer is fully drained (i.e., before `$00B0` reaches 0), the first transfer is silently abandoned. In practice, both call sites are separated by a `BRA` in the common path and the transfer size is bounded.

2. **DMA channel 1 assumed free during NMI.** The original DMA queue uses channel 0. No check is made for channel 1 conflicts. If the game later uses channel 1 elsewhere during NMI, this could corrupt in-flight transfers.

3. **`$00B0`–`$00B7` assumed free as scratch.** These addresses were chosen as unused WRAM; no cross-reference search has been done to confirm nothing else reads/writes them.

4. **Tiles may be partially visible mid-transfer.** The deferred design means VRAM updates happen over multiple frames. If the game engine relies on the tile load being complete before it scrolls to that area, there may be a one-frame tile-glitch window. The original synchronous design made this impossible by construction.

---

## Change summary (byte-level)

| File offset | CPU addr | Original | Patched | Purpose |
|-------------|----------|----------|---------|---------|
| `0x008012` | `C0:8012` | `A9 00 1F 5B` | `5C 14 CD EF` | Boot hook JML |
| `0x0083 4E` | `C0:834E` | `C2 30 64 99` | `5C B2 CC EF` | NMI hook JML |
| `0x0009D2` | `C0:09D2` | `B7 85 C0` | `9B CC EF` | JSL target addr bytes |
| `0x0009EB` | `C0:09EB` | `B7 85 C0` | `9B CC EF` | JSL target addr bytes |
| `0x2FCC9B`–`0x2FCD1E` | `EF:CC9B`–`EF:CD1E` | `FF…FF 00 01 02 03` | patch code | New routines |
| `0x00FFDC`–`0x00FFDF` | `C0:FFDC` | `B7 BF 48 40` | checksum | Updated checksum |

---

## Boot bug that was preventing the ROM from starting

The original patched ROM had a 1-byte error: the `JML` at `EF:CD10` was assembled as only 3 bytes (`5C 52 83`), missing the bank byte. The CPU read the first byte of the following instruction (`A9` = `LDA #imm` opcode) as the bank byte, producing `JML $A98352`. In HiROM, bank `$A9` mirrors ROM bank `$E9`, so execution jumped to file offset `0x298352` (contents: `32 43 21 EF …`) — garbage — and crashed immediately on the first NMI.

**Fix:** 7 bytes changed in the patched ROM:
- `EF:CD13`: `A9 → C0` (bank byte for `JML $C08352`)
- `EF:CD14`–`CD19`: shift boot hook bytes forward by one position
- `EF:CD1A`: `5C → 00` (high byte of `STZ $00B0` absolute)
- `EF:CD1B`–`CD1E`: `JML $C08016` shifted 1 byte forward
- `C0:8013`: `13 → 14` (boot hook JML target updated from `$EFCD13` → `$EFCD14`)
