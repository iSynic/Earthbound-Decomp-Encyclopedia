# C2 source-promotion candidates (workahead)

This note is a **scout / planning** artifact: it points at small or well-bounded bank-`C2` corridors that are likely to promote cleanly into **readable 65816 assembly**, while preserving exact ROM bytes.

The bank-`C2` scaffold is already byte-equivalent (`build/c2-byte-equivalence-validation.json` reports `OK`). In practice there are two promotion shapes in this repo:

- **Remaining byte-corridor (data-gap) modules** (`subsystem=working-name-byte-corridor`, `source_size=0` in `build/c2-build-candidate-ranges.json`): `src/c2/*.asm` is a label-only stub and promotion means emitting real code/data for the range.
- **Already-emitted prototype modules** (`source_size=size`): `src/c2/*.asm` already contains decoded assembly from `tools/emit_linear_source_module.py`; promotion means humanization (naming/structure/splits/contracts) rather than filling missing bytes.

## Quick tooling reminders

Decode a snippet (useful to confirm boundaries + width toggles):

- `python tools/decode_snippet.py C2:0266 --count 40 --show-state`
- `python tools/decode_snippet.py C2:1628 --count 70 --show-state`

Reference context search (fast way to see whether `ebsrc`/legacy disasm treats an address as code vs data):

- `python tools/lookup_ref_context.py C2:077D --window 30`
- `python tools/lookup_ref_context.py C2:0958 --window 30`

Data-table byte peek (when `decode_snippet.py` is lying because the range is data):

- `python tools/inspect_table.py C2:0958 --stride 2 --count 36 --raw-bytes 2`

Byte-equivalence validation (module substring matches `source_path`/range rows in `build/c2-build-candidate-ranges.json`):

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0266 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --combined --strict`

## Current Source-Gap Status

As of the current `build/c2-build-candidate-ranges.json`, there are no remaining true `source_size=0` code corridors in bank `C2`. The only `source_size=0` entries left are intentional source-locked data tables:

- `C2:0912..0958` (`src/c2/c2_0912_name_entry_grid_character_offset_table.asm`)
- `C2:0958..09A0` (`src/c2/c2_0958_menu_or_name_entry_mask_table.asm`)

The former top three true byte corridors have been promoted and validated:

- `C2:C6F0..CFE5` split into `C2:C6F0..C8C8`, `C2:C8C8..C92D`, and `C2:C92D..CFE5`
- `C2:0000..00D1` split into `C2:0000..00B9` code and `C2:00B9..00D1` data tail
- `C2:E6B3..E6B6` represented as literal prefix bytes before the callable `C2:E6B6` body

Historical notes below are retained as evidence for the promotions and for future cleanup/humanization passes.

Semantic humanization update:

- 2026-05-01: the ranked HP/PP window redraw + refresh cluster
  (`C2:077D..0A20`), managed text-event snapshot/restore pair
  (`C2:0A20..0B65`), directional menu scanner (`C2:0B65..0D3F`), and HP/PP
  roller prelude (`C2:0F58..109F`) received byte-neutral local aliases and
  contract constants. See
  `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`.
- 2026-05-01: the equipment-preview slot setup helpers
  (`C2:2562..26C5`), temporary party source save/restore pair
  (`C2:3008..30F3`), and respawn/warp target snapshot helper (`C2:30F3`)
  received byte-neutral local aliases and contract constants. See
  `notes/equipment-preview-slot-block-9cd0-9cd6.md`,
  `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`, and
  `notes/respawn-warp-target-snapshot-helper-c230f3.md`.
- 2026-05-01: the window-title microcluster (`C2:0266..038B`) and HP/PP
  tilemap reset helper (`C2:038B`) received byte-neutral local aliases for the
  title tile buffer, window-record title upload fields, registered upload-slot
  table, C4 upload helper join, and HP/PP clear ranges. See
  `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`.
- 2026-05-01: the status-tile lookup helpers (`C2:23D9..2562`) received
  byte-neutral local aliases for the status-slice scan order, C4 lookup tables,
  no-status fallback values, and item-byte `+0x19` equipment subtype classifier
  tails. See `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`.
- 2026-05-01: the decimal digit / HP-PP tile-buffer strip (`C2:0D3F..0F58`)
  received byte-neutral local aliases for the digit staging bytes, tile-buffer
  roots, digit tile source offsets, blank/visible digit offsets, and HP/PP
  wrapper entries. See `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`.

## Completed True Byte-Corridor Promotions

### G1) Final Prayer finale controller (split recommended) (`C2:C6F0..C2:CFE5`)

**Current manifest range (stub)**

- `C2:C6F0..C2:CFE5` (`2293` bytes; `0x02C6F0..0x02CFE5`; SHA-1 `0fe8dd137ff19e0d65e55c6448b3791f3a205058`)
  - `src/c2/c2_c6f0_run_final_prayer_finale.asm`
  - Label: `C2C6F0_RunFinalPrayerFinale`

**Suggested split points (decoder-confirmed routine boundaries)**

- `C2:C6F0..C2:C8C8` (ends with `PLD; RTL` at `C2:C8C6..C2:C8C7`)
- `C2:C8C8..C2:C92D` (ends with `PLD; RTL` at `C2:C92B..C2:C92C`)
- `C2:C92D..C2:CFE5` (ends with `PLD; RTL` at `C2:CFE3..C2:CFE4`)

These boundaries fall on clean prologues (`REP #$31; PHD; ...`) at `C2:C6F0`, `C2:C8C8`, and `C2:C92D`, and let you validate each piece independently.

**Evidence**

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md` (phase-9 summary + high-confidence caller mapping)
- `python tools/decode_snippet.py C2:C6F0 --count 120 --show-state` (shows the early text+damage ladder shape)
- `python tools/decode_snippet.py C2:C8C8 --count 120 --show-state` and `python tools/decode_snippet.py C2:C92D --count 120 --show-state` (clean routine starts)

**Force-width risks / emission gotchas**

- Around `C2:C7D8` and `C2:C7F3`, the code calls `JSL $C2F8F9` while in an `M8` window (`SEP #$20`). The immediately-following bytes strongly suggest the callee returns with `M16`, so naive linear decoding desyncs unless you force width at the post-call sites.
  - Example raw sequence starting at `C2:C7DC`: `A9 31 FF 85 0E A9 C8 00 85 10 22 1C DC C1` reads cleanly as `LDA.w #$FF31; STA $0E; LDA.w #$00C8; STA $10; JSL $C1DC1C` only if `M16` is in effect.
- If you emit via `tools/emit_linear_source_module.py`, expect to need `--force-m16-at` at least at `C2:C7DC` and `C2:C7F7` (and potentially other post-`JSL $C2F8F9` sites if you keep the full `C6F0..C8C8` piece as one module).

**Suggested validation**

- `python tools/decode_snippet.py C2:C6F0 --count 200 --show-state`
- `python tools/inspect_table.py C2:C7D0 --stride 1 --count 64 --raw-bytes 1` (sanity-check the post-`JSL $C2F8F9` bytes when reasoning about width)
- After splitting/emitting, validate each new module:
  - `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_c6f0 --strict`
  - `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_c8c8 --strict`
  - `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_c92d --strict`

---

### G2) Bank prefix corridor before first working-name anchor (`C2:0000..C2:00D1`)

This is the synthetic prelude before the first anchored build-candidate at `C2:00D1`. It contains at least one real callable routine and then a trailing data tail.

**Range**

- `C2:0000..C2:00D1` (`209` bytes; `0x020000..0x0200D1`; SHA-1 `5b5da18cb4b057ca58d8dcf8bc5caf11d63acc3e`)
  - `src/c2/c2_0000_bank_prefix_byte_corridor.asm`
  - Label: `C20000_BankPrefixByteCorridor`

**Likely internal split**

- `C2:0000..C2:00B9` looks like code (ends with `PLD; RTL` at `C2:00B7..C2:00B8`)
- `C2:00B9..C2:00D1` looks like a small data table / padding tail (treat as `.byte`/`.word` rather than trying to decode as code)

**Force-width risks**

- Contains a short `M8` window around `C2:009C` (`SEP #$20`) for single-byte struct updates; keep the exact width windowing.

**Suggested validation**

- `python tools/decode_snippet.py C2:0000 --count 140 --show-state`
- `python tools/inspect_table.py C2:00B9 --stride 1 --count 24 --raw-bytes 1`
- After emitting, validate:
  - `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0000 --strict`

---

### G3) PSI animation prefix bytes before the callable body (`C2:E6B3..C2:E6B6`)

This 3-byte range is immediately before the real prologue at `C2:E6B6` (`AdvancePsiAnimationFrameAndPaletteStateBody`). Local notes already treat it as padding / inline bytes, not the callable entry.

**Range**

- `C2:E6B3..C2:E6B6` (`3` bytes; `0x02E6B3..0x02E6B6`; SHA-1 `bbe0b447f3ad331c5d2dea6e8427616cbeb3fad3`)
  - `src/c2/c2_e6b3_advance_psi_animation_frame_and_palette_state.asm`
  - Label: `C2E6B3_AdvancePsiAnimationFrameAndPaletteState`

**Evidence**

- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md` (explicitly calls out `C2:E6B3` as padding and `C2:E6B6` as the callable body)

**Suggested validation**

- `python tools/inspect_table.py C2:E6B3 --stride 1 --count 3 --raw-bytes 1`
- After emitting as literal bytes, validate:
  - `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_e6b3 --strict`

## Manifest / stub hygiene (unreferenced byte-corridor stubs)

These `src/c2/*.asm` "build-candidate byte corridor" stubs exist on disk but do **not** appear in the current `build/c2-build-candidate-ranges.json` `source_path` list (likely historical split-stubs / renamed modules). Treat them as cleanup candidates, not promotion candidates, until reconciled:

- `src/c2/c2_4f52_initialize_enemy_battler_loop_for_encounter.asm`
- `src/c2/c2_4f62_display_battle_start_status_messages.asm`
- `src/c2/c2_9ac6_run_lifeup_alpha_healing_action.asm`
- `src/c2/c2_9acf_run_lifeup_beta_healing_action.asm`
- `src/c2/c2_9ad8_run_lifeup_gamma_healing_action.asm`
- `src/c2/c2_9ae1_run_lifeup_omega_healing_action.asm`
- `src/c2/c2_e9ed_clear_battle_overlay_and_reset_layer_effects.asm`
- `src/c2/c2_ea15_begin_battle_swirl_overlay_script.asm`
- `src/c2/c2_ea74_switch_battle_swirl_overlay_to_closing_script.asm`

To re-check this list:

- `powershell -c \"$j=Get-Content -Raw build/c2-build-candidate-ranges.json | ConvertFrom-Json; $paths=@{}; foreach($r in $j.ranges){$paths[$r.source_path]=1}; Get-ChildItem -File src/c2 | ?{(Get-Content -TotalCount 20 $_.FullName) -match 'build-candidate byte corridor'} | %{$rel='src/c2/'+$_.Name; if(-not $paths.ContainsKey($rel)){$rel}}\"`

## Ranked candidates (already-emitted prototypes; high ROI humanization)

These are good next promotions once the true data-gap corridors above are gone: they are already byte-equivalent prototype modules in `src/c2/*.asm`, but they are small or well-bounded enough to split/rename/humanize safely while keeping `--strict` byte checks green.

### 1) HP/PP window redraw + refresh stub cluster (`C2:077D..C2:0A20`)

These are already emitted prototypes, but they’re tightly bounded, already partially described in local notes, and they line up with the reference include order in `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`.

**Ranges**

- `C2:077D..C2:07B6` (`57` bytes; `0x02077D..0x0207B6`; SHA-1 `d28488e532e7d132bd37cc1e2e936f1da228783d`)
  - `src/c2/c2_077d_redraw_dirty_party_hp_pp_windows.asm`
  - Label: `C2077D_RedrawDirtyPartyHpPpWindows`
- `C2:07B6..C2:07E1` (`43` bytes; `0x0207B6..0x0207E1`; SHA-1 `217fcfac31b685fbfc33f5f89c190f31e2ea55c4`)
  - `src/c2/c2_07b6_mark_and_redraw_party_hp_pp_window.asm`
  - Label: `C207B6_MarkAndRedrawPartyHpPpWindow`
- `C2:07E1..C2:087C` (`155` bytes; `0x0207E1..0x02087C`; SHA-1 `3f05438cf373c96faa99ea073fd8f30a4037311c`)
  - `src/c2/c2_07e1_clear_party_hp_pp_window_tiles.asm`
  - Label: `C207E1_ClearPartyHpPpWindowTiles`
- `C2:087C..C2:08B8` (`60` bytes; `0x02087C..0x0208B8`; SHA-1 `4672e2ffa90fe13791a4b1d26e4b614d36661244`)
  - `src/c2/c2_087c_refresh_dirty_hp_pp_and_open_text_windows.asm`
  - Label: `C2087C_RefreshDirtyHpPpAndOpenTextWindows`
- `C2:0958..C2:09A0` (`72` bytes; `0x020958..0x0209A0`; SHA-1 `1576e7ce0b6915b7b2bdbf15c9b82646475d71e6`)
  - `src/c2/c2_0958_menu_or_name_entry_mask_table.asm`
  - Label: `C20958_MenuOrNameEntryMaskTable` (treat as data; see below)
- `C2:09A0..C2:0A20` (`128` bytes; `0x0209A0..0x020A20`; SHA-1 `a2ad845571b082dce16a84129d4174f16a0bf18f`)
  - `src/c2/c2_09a0_close_and_clear_current_window_tilemap.asm`
  - Label: `C209A0_CloseAndClearCurrentWindowTilemap`

**Evidence**

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md` (working names + behavior model for this corridor)
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm` (places these stubs adjacent to the named window/HPPP code)
- `python tools/lookup_ref_context.py C2:077D --window 30` (shows both `ebsrc` include anchor and legacy disasm labels)

**Force-width risks**

- `C2:07B6` does `SEP #$30` then `REP #$20` and returns with **`X8` still in effect**; don’t “clean up” the width on return.
- `C2:07E1` toggles `X` width (`SEP #$10` / `REP #$10`) mid-routine; preserve the exact ordering.
- `C2:09A0` uses `SEP #$20` for the `STZ $003B/$003C` slot fields; keep those as 8-bit stores.
- `C2:0958` is treated as **data** by refs (`DATA_C20958`); don’t try to decode it as code.

**Suggested validation**

- `python tools/decode_snippet.py C2:077D --count 40 --show-state`
- `python tools/decode_snippet.py C2:07B6 --count 60 --show-state`
- `python tools/decode_snippet.py C2:09A0 --count 60 --show-state`
- `python tools/inspect_table.py C2:0958 --stride 2 --count 36 --raw-bytes 2`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_077d --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_07b6 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_07e1 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_087c --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_09a0 --strict`

---

### 2) Managed text-event slot snapshot/restore pair (`C2:0A20..C2:0B65`)

These two are already emitted prototypes but are already strongly described as a save/restore pair for the managed text-event slot system.

**Ranges**

- `C2:0A20..C2:0ABC` (`156` bytes; `0x020A20..0x020ABC`; SHA-1 `a1f8c3ccb4770f87e8f1dbb365315d9cf20d3574`)
  - `src/c2/c2_0a20_snapshot_managed_text_event_slot_state.asm`
  - Label: `C20A20_SnapshotManagedTextEventSlotState`
- `C2:0ABC..C2:0B65` (`169` bytes; `0x020ABC..0x020B65`; SHA-1 `923b9cf34a4137d9a46284126a9695bda8811c79`)
  - `src/c2/c2_0abc_restore_managed_text_event_slot_state.asm`
  - Label: `C20ABC_RestoreManagedTextEventSlotState`

**Evidence**

- `notes/timed-event-slot-block-7440-and-c20abc.md` (field-by-field snapshot layout + caller counts)

**Force-width risks**

- `C2:0A20` uses `SEP #$20` for the one-byte `8662+` read/write; keep that exact `M8` window.

**Suggested validation**

- `python tools/decode_snippet.py C2:0A20 --count 70 --show-state`
- `python tools/decode_snippet.py C2:0ABC --count 70 --show-state`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0a20 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0abc --strict`

---

### 3) Respawn / warp target snapshot helper (`C2:30F3..C2:3109`)

Ultra-small, clean, and already pinned to a specific text command leaf. Great “first corridor completion” candidate because it has only a single width hazard.

**Range**

- `C2:30F3..C2:3109` (`22` bytes; `0x0230F3..0x023109`; SHA-1 `907ed58d9fa1d060c13ea03d6fe27c85022cfb2f`)
  - `src/c2/c2_30f3_snapshot_respawn_warp_target_state.asm`
  - Label: `C230F3_SnapshotRespawnWarpTargetState`

**Evidence**

- `notes/respawn-warp-target-snapshot-helper-c230f3.md`

**Force-width risks**

- Starts with `REP #$31`, then uses `SEP #$20` only for `STA $98B8`, then returns to `REP #$20`. Keep the `STA $98B8` 8-bit.

**Suggested validation**

- `python tools/decode_snippet.py C2:30F3 --count 15 --show-state`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_30f3 --strict`

---

### 4) Equipment-preview slot-block setup helpers (`C2:2562..C2:26C5`)

Four small, structurally repetitive stubs that are already behavior-described via the `$9CD0..$9CD6` preview block. These are good “batch promote” targets.

**Ranges**

- `C2:2562..C2:25AC` (`74` bytes; `0x022562..0x0225AC`; SHA-1 `bdf83b54a0569478ee8705dce0b2d965772e3f5d`)
  - `src/c2/c2_2562_setup_weapon_equipment_preview_block.asm`
- `C2:25AC..C2:260D` (`97` bytes; `0x0225AC..0x02260D`; SHA-1 `28ebcf030315d446aa420aa733a4437c60927ea1`)
  - `src/c2/c2_25ac_setup_charm_equipment_preview_block.asm`
- `C2:260D..C2:2673` (`102` bytes; `0x02260D..0x022673`; SHA-1 `f4c7796928b376b92c1fd2fd626fa00959aff15e`)
  - `src/c2/c2_260d_setup_bracelet_equipment_preview_block.asm`
- `C2:2673..C2:26C5` (`82` bytes; `0x022673..0x0226C5`; SHA-1 `cf8033dabde9bafd1722742450b222a03f5a5105`)
  - `src/c2/c2_2673_setup_headgear_equipment_preview_block.asm`

**Evidence**

- `notes/equipment-preview-slot-block-9cd0-9cd6.md`

**Force-width risks**

- Each helper mixes `REP #$20` and `SEP #$20` for byte writes into `$9CD0..$9CD3`; keep those `M8` stores as-is.

**Suggested validation**

- `python tools/decode_snippet.py C2:2562 --count 60 --show-state`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_2562 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_25ac --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_260d --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_2673 --strict`

---

### 5) Final Prayer ladder (opening + phase-2..8) (`C2:C572..C2:C6F0`) + shared helpers (`C2:C37A..C2:C41F`)

The early ladder steps are tiny (most are 41 bytes) and are already strongly modeled in notes. They also have very regular structure, so they’re good “promote as a set” candidates.

**Ranges**

- `C2:C37A..C2:C3E2` (`104` bytes; `0x02C37A..0x02C3E2`; SHA-1 `63ceed81816707c83e3031b65029d01b4dc349a7`)
  - `src/c2/c2_c37a_run_final_prayer_stage_transition.asm`
- `C2:C3E2..C2:C41F` (`61` bytes; `0x02C3E2..0x02C41F`; SHA-1 `30a6c99b0d9e62e6f64f318486b5e3dc13337a8f`)
  - `src/c2/c2_c3e2_apply_final_prayer_damage_step.asm`
- `C2:C572..C2:C5D1` (`95` bytes; `0x02C572..0x02C5D1`; SHA-1 `9d5370808e4ee3994e171f8cac9f0a1465f4c95b`)
  - `src/c2/c2_c572_run_final_prayer_opening_transition.asm`
- `C2:C5D1..C2:C6D0` (phase ladder; each routine is `41` or `50` bytes; see individual modules)
  - `src/c2/c2_c5d1_run_final_prayer_damage_phase2.asm` (`C2:C5D1..C2:C5FA`)
  - `src/c2/c2_c5fa_run_final_prayer_damage_phase3.asm` (`C2:C5FA..C2:C623`)
  - `src/c2/c2_c623_run_final_prayer_damage_phase4.asm` (`C2:C623..C2:C64C`)
  - `src/c2/c2_c64c_run_final_prayer_damage_phase5.asm` (`C2:C64C..C2:C675`)
  - `src/c2/c2_c675_run_final_prayer_damage_phase6.asm` (`C2:C675..C2:C69E`)
  - `src/c2/c2_c69e_run_final_prayer_damage_phase7.asm` (`C2:C69E..C2:C6D0`)
- `C2:C6D0..C2:C6F0` (`32` bytes; `0x02C6D0..0x02C6F0`; SHA-1 `e927376cc80fa997fc95c6c75f0cf57466f114ca`)
  - `src/c2/c2_c6d0_run_final_prayer_narrative_phase8.asm`

**Evidence**

- `notes/class2-final-prayer-family-c2c572-c2c6f0.md`
- `notes/class2-prayer-common-helpers-c2c37a-c2c3e2-c2c41f.md`

**Force-width risks**

- These routines use the common `REP #$31` + `PHD/TDC/ADC #$FFEE|#$FFF0` direct-page frame; preserve the exact immediate values (frame size differs per routine).

**Suggested validation**

- `python tools/decode_snippet.py C2:C5D1 --count 30 --show-state`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_c572 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_c5d1 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_c37a --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_c3e2 --strict`

---

### 6) Battle consequence leaves (stat change + PP target loss) (`C2:B2E0..C2:BD13`)

These are small stubs with unusually strong local writeups that include pseudo-asm and field naming. Good candidates when you want “battle-side” progress without committing to a huge corridor.

**Ranges (selected)**

- `C2:B2E0..C2:B573` (stat-change consequence dispatcher + leaves; see individual modules)
  - `src/c2/c2_b2e0_dispatch_battle_stat_change_consequence.asm` (`C2:B2E0..C2:B342`, `98` bytes)
  - `src/c2/c2_b342_apply_battle_hp_recovery_consequence.asm` (`C2:B342..C2:B360`, `30` bytes)
  - `src/c2/c2_b360_apply_battle_pp_recovery_consequence.asm` (`C2:B360..C2:B3D8`, `120` bytes)
  - `src/c2/c2_b3d8_apply_battle_iq_increase_consequence.asm` (`C2:B3D8..C2:B43F`, `103` bytes)
  - `src/c2/c2_b43f_apply_battle_guts_increase_consequence.asm` (`C2:B43F..C2:B4A6`, `103` bytes)
  - `src/c2/c2_b4a6_apply_battle_speed_increase_consequence.asm` (`C2:B4A6..C2:B50D`, `103` bytes)
  - `src/c2/c2_b50d_apply_battle_vitality_increase_consequence.asm` (`C2:B50D..C2:B573`, `102` bytes)
- `C2:BCB9..C2:BD13` (`90` bytes; `0x02BCB9..0x02BD13`; SHA-1 `611ed76fd2511c7777a27280c9f1ce88dd4907ee`)
  - `src/c2/c2_bcb9_apply_battler_pp_target_loss.asm`

**Evidence**

- `notes/battle-action-stat-change-family-c2b2e0-b5d7.md`
- `notes/c2-pp-loss-and-call-for-help-width-helpers-c2bcb9-c2bd13.md`

**Force-width risks**

- Several leaves do `SEP #$20` for one-byte battler/slot fields; ensure byte-vs-word accesses match the note contracts.

**Suggested validation**

- `python tools/decode_snippet.py C2:B2E0 --count 60 --show-state`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_b2e0 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_bcb9 --strict`

---

### 7) `C2:E6B3` PSI animation pre-body padding (`C2:E6B3..C2:E6B6`)

This is only 3 bytes, but it’s a good “paper cut” completion target because it’s an easy place to accidentally mis-decode as code. The local note already suggests the callable body begins at `C2:E6B6`.

**Range**

- `C2:E6B3..C2:E6B6` (`3` bytes; `0x02E6B3..0x02E6B6`; SHA-1 `bbe0b447f3ad331c5d2dea6e8427616cbeb3fad3`)
  - `src/c2/c2_e6b3_advance_psi_animation_frame_and_palette_state.asm`

**Evidence**

- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md` (argues `C2:E6B6` is the real routine start)

**Force-width risks**

- Don’t “force decode” this range as executable code; treat it as literal bytes/padding unless a ref says otherwise.

**Suggested validation**

- `python tools/decode_snippet.py C2:E6B3 --count 10 --show-state`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_e6b3 --strict`

## Manifest/stub hygiene notes

While scouting stubs, a small potential confusion hazard showed up: some `src/c2/*.asm` files look like “byte corridor” stubs but do not appear in `build/c2-build-candidate-ranges.json` (and therefore are not included in `src/c2/bank_c2_helpers_asar.asm`).

Current examples (verify with `Select-String build/c2-build-candidate-ranges.json -Pattern <name>`):

- `src/c2/c2_e9ed_clear_battle_overlay_and_reset_layer_effects.asm` (claims `C2:E9ED..C2:EA15`)
- `src/c2/c2_ea15_begin_battle_swirl_overlay_script.asm` (claims `C2:EA15..C2:EA74`)
- `src/c2/c2_ea74_switch_battle_swirl_overlay_to_closing_script.asm` (claims `C2:EA74..C2:EACF`)

The manifest-backed, validated range for this area currently appears to be:

- `C2:E9ED..C2:EACF` in `src/c2/c2_e9ed_clear_battle_swirl_overlay_state.asm` (`source_size=size`, emitted prototype)

Recommendation (scout-only): either remove/relocate the unreferenced split-stubs, or add a short header note in each explaining that they are historical/unused, to avoid future promotion work accidentally targeting non-manifest modules.

## Secondary candidates (already emitted prototypes; polish)

### 1) Window-title microcluster (`C2:0266..C2:03C3`)

These are tiny, high-confidence routines with clean local notes and crisp `REP/SEP` behavior. Promoting them yields immediate readability for the window-title path and stabilizes the early window/HPPP corridor.

**Ranges**

- `C2:0266..C2:0293` (`45` bytes; `0x020266..0x020293`; SHA-1 `5e3b26328f0bac27bfc7411d94e926fcac0dac7b`)
  - `src/c2/c2_0266_load_default_title_upload_tiles.asm`
  - Labels: `C20266_LoadDefaultTitleUploadTiles` / `C20293_LoadDefaultTitleUploadTiles_End`
- `C2:0293..C2:02AC` (`25` bytes; `0x020293..0x0202AC`; SHA-1 `eef318131a7aaa9c4835c3d601b3c2d7337d8ebd`)
  - `src/c2/c2_0293_clear_default_title_upload_tiles.asm`
  - Labels: `C20293_ClearDefaultTitleUploadTiles` / `C202AC_ClearDefaultTitleUploadTiles_End`
- `C2:02AC..C2:032B` (`127` bytes; `0x0202AC..0x02032B`; SHA-1 `0656b690211665397d2c044febb7150825346872`)
  - `src/c2/c2_02ac_register_and_upload_window_title_buffer.asm`
  - Labels: `C202AC_RegisterAndUploadWindowTitleBuffer` / `C2032B_RegisterAndUploadWindowTitleBuffer_End`
- `C2:032B..C2:038B` (`96` bytes; `0x02032B..0x02038B`; SHA-1 `db46622debfb52e1da3b737fba352fd7da0f73fa`)
  - `src/c2/c2_032b_write_window_title_and_upload.asm`
  - Labels: `C2032B_WriteWindowTitleAndUpload` / `C2038B_WriteWindowTitleAndUpload_End`
- `C2:038B..C2:03C3` (`56` bytes; `0x02038B..0x0203C3`; SHA-1 `89e677ba14731a7e32ed3d97160d4df6335449c3`)
  - `src/c2/c2_038b_reset_hp_pp_tilemap_buffers.asm`
  - Labels: `C2038B_ResetHpPpTilemapBuffers` / `C203C3_ResetHpPpTilemapBuffers_End`

**Evidence**

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`
- Reference ordering corroboration: `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm`
- Decoder sanity (already clean and self-terminating):
  - `python tools/decode_snippet.py C2:0266 --count 60 --show-state`
  - `python tools/decode_snippet.py C2:02AC --count 90 --show-state`

**Force-width risks**

- `C2:02AC` uses `SEP #$20` for the `$003B` slot write and then returns to `REP #$20`; keep the `M8` store byte-accurate.
- `C2:0266`/`C2:0293` are clean `M16/X16` loops; do not “optimize” increments (the double `INC` / double `INY` matters).

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0266 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_02ac --strict`

---

### 2) Event-flag helpers (`C2:1628..C2:16AD`)

These are widely referenced and already described precisely (bitfield root `$9C08`, 8-bit mask table `C4:562F`). They are also small and have obvious `RTL` endings.

**Ranges**

- `C2:1628..C2:165E` (`54` bytes; `0x021628..0x02165E`; SHA-1 `3f48f0ad40712500ccf95077ce8a2e890a0f9564`)
  - `src/c2/c2_1628_test_event_flag.asm`
  - Labels: `C21628_TestEventFlag` / `C2165E_TestEventFlag_End`
- `C2:165E..C2:16AD` (`79` bytes; `0x02165E..0x0216AD`; SHA-1 `53220a016966d48cd8ad4aec6f50714999a232c6`)
  - `src/c2/c2_165e_set_or_clear_event_flag.asm`
  - Labels: `C2165E_SetOrClearEventFlag` / `C216AD_SetOrClearEventFlag_End`

**Evidence**

- `notes/text-command-07-check-event-flag.md` (ties `0x07` opcode to `C2:1628`)
- `notes/text-command-04-set-event-flag.md` / `notes/text-command-05-clear-event-flag.md` (ties `0x04/0x05` to `C2:165E`)
- `notes/selector-row-config-family-ef0ee8.md` (spells out the `$9C08` + mask-table mechanism)
- Decoder sanity:
  - `python tools/decode_snippet.py C2:1628 --count 40 --show-state`

**Force-width risks**

- Both helpers use `SEP #$20` for the actual bitfield byte read/modify; ensure the 8-bit `LDA/AND/ORA/STA` stays 8-bit.
- Do not accidentally treat the mask load as 16-bit (`LDA long,X` must remain `M8` for the exact `AND` behavior).

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_1628 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_165e --strict`

---

### 3) `$9C88` flag wrappers (`C2:26C5..C2:26EB`)

Two extremely small, high-confidence wrappers that directly call the helpers above; they’re ideal “first promotions” because the disassembly is essentially one screen of code.

**Ranges**

- `C2:26C5..C2:26D0` (`11` bytes; `0x0226C5..0x0226D0`; SHA-1 `9ad2cd3672dccf845d7227bb1abecc4b6372700a`)
  - `src/c2/c2_26c5_set_current9_c88_flag_and_refresh5_d64.asm`
  - Label: `C226C5_SetCurrent9C88FlagAndRefresh5D64`
- `C2:26E6..C2:26EB` (`5` bytes; `0x0226E6..0x0226EB`; SHA-1 `6bb9319c041fddf95b8619ec44534145e6f55bc2`)
  - `src/c2/c2_26e6_get_current9_c88_flag.asm`
  - Label: `C226E6_GetCurrent9C88Flag`

**Evidence**

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md` (documents both wrappers and their direct callers)
- Decoder sanity:
  - `python tools/decode_snippet.py C2:26C5 --count 25 --show-state`
  - `python tools/decode_snippet.py C2:26E6 --count 10 --show-state`

**Force-width risks**

- These start with `REP #$31` and treat `$9C88` as a 16-bit flag id (`LDA $9C88` in `M16`); don’t “helpfully” narrow it.

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_26c5 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_26e6 --strict`

---

### 4) Menu-cell classifier + cursor scanner (`C2:08B8..C2:0D3F`)

This is larger than the tiny wrappers above, but the behavior is strongly pinned: one classifier (`C2:08B8`) plus a directional scanner (`C2:0B65`) with many callers.

**Ranges**

- `C2:08B8..C2:0958` (`160` bytes; `0x0208B8..0x020958`; SHA-1 `f06d268feec3602b1ea5f6f7623b5aebe3ee6589`)
  - `src/c2/c2_08b8_classify_menu_tile_for_cursor_scan.asm`
  - Label: `C208B8_ClassifyMenuTileForCursorScan`
- `C2:0B65..C2:0D3F` (`474` bytes; `0x020B65..0x020D3F`; SHA-1 `29d1d68f48b4432fc6f3d369026f9811b866e0c9`)
  - `src/c2/c2_0b65_find_next_selectable_menu_cell.asm`
  - Label: `C20B65_FindNextSelectableMenuCell`

**Evidence**

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md` (documents return values, wrapping rules, and callsites)

**Force-width risks**

- This corridor mixes 16-bit pointer math with 8-bit tile id tests; confirm with `decode_snippet.py` and keep the existing `REP/SEP` transitions.

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_08b8 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0b65 --strict`

---

### 5) Decimal-digit split prelude (`C2:0D3F..C2:0F58`)

Moderate-sized but mechanically simple (divide by 10 repeatedly; stage digits to `$8966..$8968`). Useful because it sits in a named HP/PP window helper cluster.

**Range**

- `C2:0D3F..C2:0F58` (`537` bytes; `0x020D3F..0x020F58`; SHA-1 `88642c89553bdf1783ebdb636559e01c7a76ae07`)
  - `src/c2/c2_0d3f_split_value_into_three_decimal_digits_at8966.asm`
  - Label: `C20D3F_SplitValueIntoThreeDecimalDigitsAt8966`

**Evidence**

- `notes/c2-symbol-only-stragglers-c200d1-c20d3f.md` (documents `C2:0D3F` behavior + direct callers)
- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md` (ties this into the HP/PP helper ordering)

**Force-width risks**

- Depends on divider helpers and staged-digit stores; ensure accumulator width matches each helper’s contract when emitting readable code (avoid refactors until byte-equivalence is locked).

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0d3f --strict`

---

### 6) HP/PP roller prelude micro-routines (`C2:0F58..C2:108C`) + split for `C2:108C`

`C2:0F58`, `C2:0F9A`, and `C2:1034` are already well-bounded, small modules. `C2:108C` is currently the *start label* of a much larger corridor, but the actual latch-clear routine has a clean boundary at `C2:109F`.

**Ranges (already small / bounded)**

- `C2:0F58..C2:0F9A` (`66` bytes; `0x020F58..0x020F9A`; SHA-1 `ac08e1b1092be7cad2d3214182b47b611a0d52b5`)
  - `src/c2/c2_0f58_select_hp_pp_roll_delta.asm`
- `C2:0F9A..C2:1034` (`154` bytes; `0x020F9A..0x021034`; SHA-1 `dfbaead209df0faf8ef4750ad2eaffa2af00f662`)
  - `src/c2/c2_0f9a_clamp_hp_pp_roll_targets_to_live_values.asm`
- `C2:1034..C2:108C` (`88` bytes; `0x021034..0x02108C`; SHA-1 `4da4e71558c26297a69bf1ecfe46ef6f0b85d0e0`)
  - `src/c2/c2_1034_are_all_hp_pp_rollers_settled.asm`

**Range (needs a manifest split before it becomes “small”)**

- Current corridor: `C2:108C..C2:1628` (`1436` bytes; `0x02108C..0x021628`; SHA-1 `c5a58e87395c6d15d3f819a666b8d2754e821445`)
  - `src/c2/c2_108c_clear_hp_pp_roll_dirty_latch_if_settled.asm`
  - Decoder boundary proof:
    - `python tools/decode_snippet.py C2:108C --count 30 --show-state` shows `RTL` at `C2:109E`, then a new routine prologue at `C2:109F`.
  - Proposed split boundary: **`C2:108C..C2:109F`** (latch-clear), with the next corridor starting at **`C2:109F`** (HP/PP roller body entry).

**Evidence**

- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md` (documents the full prelude contract and latch behavior)

**Force-width risks**

- The latch-clear itself flips `M8` briefly to `STZ $9696` and returns to `M16`; keep that exact `SEP/REP` behavior.

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0f58 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_0f9a --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_1034 --strict`

---

### 7) `C2:3008` / `C2:307B` save/restore pair (`C2:3008..C2:30F3`)

Small paired routines with a clear reversible contract. Good candidate for promotion as a pair because callers will naturally treat them together.

**Ranges**

- `C2:3008..C2:307B` (`115` bytes; `0x023008..0x02307B`; SHA-1 `2b8e294be7cffd279bb59519ff56f4bb8f9bd299`)
  - `src/c2/c2_3008_save_and_clear_temporary_party_source_state.asm`
- `C2:307B..C2:30F3` (`120` bytes; `0x02307B..0x0230F3`; SHA-1 `d4ada9ad5651260b23e3db8e0c2252b6c9f9c830`)
  - `src/c2/c2_307b_restore_temporary_party_source_state.asm`

**Evidence**

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md` (documents field-by-field behavior and the `$986F` mutation)

**Force-width risks**

- Likely mixes byte and word copies; confirm with `decode_snippet.py` before emitting readable stores so the byte/word boundaries stay exact.

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_3008 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_307b --strict`

---

### 8) Status-tile lookup helpers (`C2:23D9..C2:2562`)

Moderate-sized, caller-visible helpers used during HP/PP tilemap composition; behavior is documented and table-driven.

**Ranges**

- `C2:23D9..C2:2474` (`155` bytes; `0x0223D9..0x022474`; SHA-1 `75acf3739bfe94580ee762d90a835e3145cfea53`)
  - `src/c2/c2_23d9_lookup_status_tile_value_for_hp_pp_window.asm`
- `C2:2474..C2:2562` (`238` bytes; `0x022474..0x022562`; SHA-1 `e3190ba56bd21be3cb81e59269e641b5ec69a819`)
  - `src/c2/c2_2474_lookup_status_tile_width_or_offset_for_hp_pp_window.asm`

**Evidence**

- `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md` (documents scan order, table choices, and default return values)

**Force-width risks**

- Table indexing and `(status_byte - 1)` math are common footguns if you accidentally widen loads; keep byte reads as byte reads.

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_23d9 --strict`
- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_2474 --strict`

---

### 9) Battle background config-to-runtime bridge (`C2:CFE5..C2:D0AC`)

Small, well-described helper in a battle-visual corridor. Good “standalone” candidate that doesn’t require pulling in the larger letterbox/palette machinery yet.

**Range**

- `C2:CFE5..C2:D0AC` (`199` bytes; `0x02CFE5..0x02D0AC`; SHA-1 `dbd6c4690b987a8a1081ce4f51d98338a72a9461`)
  - `src/c2/c2_cfe5_init_loaded_battle_bg_layer_from_config.asm`
  - Label: `C2CFE5_InitLoadedBattleBgLayerFromConfig`

**Evidence**

- `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md` (documents inputs and exact field copies)

**Force-width risks**

- Heavy on structured byte copies into `loaded_bg_data`; ensure byte-vs-word fields match the struct offsets.

**Suggested validation**

- `python tools/validate_source_bank_byte_equivalence.py --bank C2 --module c2_cfe5 --strict`

## “Split first” watchlist (good targets, but current module boundaries are too coarse)

### `C2:16AD..C2:16DB` combined wrapper strip

The current `C2:16AD..16DB` corridor contains multiple back-to-back tiny `RTL` wrappers (decoder shows additional routine prologues at `C2:16C9` and `C2:16D0`). This is still promotable as-is, but it will read better if split into separate labeled routines first.

- Current range: `C2:16AD..C2:16DB` (`46` bytes; `0x0216AD..0x0216DB`; SHA-1 `b3783284e369801ad34cb6008c7902e5f2a76c56`)
  - `src/c2/c2_16ad_apply_music_state_and_mirror_to5_dd4.asm`
  - Decoder: `python tools/decode_snippet.py C2:16AD --count 25 --show-state`

### `C2:108C..C2:1628` HP/PP roller + meter corridor

As noted above, `C2:108C` is a small latch-clear routine, but the current manifest corridor continues until `C2:1628`. This is a very strong candidate for **range splitting** before attempting a promotion of the `hp_pp_roller` body (starts cleanly at `C2:109F`).
