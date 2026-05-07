# C1 Text Entry Runtime Polish

Status: second C1 text/menu-core polish slice.

This note records byte-neutral source comments added after
`notes/c1-text-gates-runtime-polish.md`. The slice focuses on the `$89D4`
active text-entry record table, record constructors, active-chain rendering,
selection helpers, and current-window clear worker.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c1/c1_0f40_clear_window_content_by_focus_index.asm` | Resolves a focus index through `$88E4 -> $8650`, clears the descriptor tile/state buffer from descriptor `+35`, and resets descriptor cursor fields `+0E/+10`. |
| `src/c1/c1_0c49_count_text_entry_chain_records.asm` | Far-call redirects for local `$89D4` chain count and bounded string length helpers. |
| `src/c1/c1_138d_count_text_entry_chain_records_local.asm` | Counts a `$89D4` text-entry chain by following record `+02` links, with `FFFF` as empty/end sentinel. |
| `src/c1/c1_13d1_install_text_entry_record.asm` | Allocates/installs a live `$89D4` record, links it into the current `$8650` descriptor chain, copies companion pointer metadata, and copies body text into record `+13`. |
| `src/c1/c1_14b1_create_text_entry_record_with_display_metadata.asm` | Wrapper around C1:13D1 that writes record display metadata at `+08/+0A` and optional packed subfield `+2C`. |
| `src/c1/c1_153b_create_typed_text_entry_record.asm` | Typed constructor that stores caller selector/value at record `+0C` and marks record `+00 = 2`. |
| `src/c1/c1_1596_create_typed_text_entry_record_with_extra_byte.asm` | Typed constructor variant that stores one extra caller byte at record `+0E`. |
| `src/c1/c1_15f4_create_typed_text_entry_record_direct.asm` | Direct typed constructor plus C1:163C active-chain renderer over `$89D4` records. |
| `src/c1/c1_33b0_rebuild_open_menu_text_entry_records.asm` | Open-menu caller surface now names the text-entry source pointer slots, selected-character staging, Goods/Talk interaction-context installs, status/check/talk feedback text sources, and debug decimal/fixed-string display sources. |
| `src/c1/c1_17e2_measure_bounded_string_length.asm` | Bounded byte-string length helper using caller pointer plus maximum count. |
| `src/c1/c1_180d_layout_active_text_entries_and_refresh.asm` | Thin wrapper over C4:51FA active-chain layout plus C1:163C render/refresh. |
| `src/c1/c1_181b_select_active_text_entry_by_y.asm` | Selects an active `$89D4` entry by ordinal in `Y`, then copies record `+06` into descriptor `+33`. |
| `src/c1/c1_1887_select_active_text_entry_by_a.asm` | Selects by ordinal in `A` and contains the reusable active text-entry selection/menu loop at C1:196A. |

## Evidence Inputs

- `notes/text-entry-builder-c113d1-89d4.md`
- `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`
- `notes/active-text-entry-chain-layout-c451fa.md`
- `notes/text-command-family-18-windows-and-selection.md`
- `notes/text-command-family-1c-print-display.md`

## Runtime Contract

The `$89D4` table stores active text/menu entry records with 0x2D-byte stride.
This slice keeps field names cautious but pins the fields repeatedly consumed by
source-backed C1/C4 paths:

- record `+00`: active/type marker
- record `+02`: next text-entry index, `FFFF` terminates chains
- record `+04`: previous or tail-side chain field
- record `+06`: row/page/group field copied into descriptor `+33`
- record `+08/+0A`: display position metadata
- record `+0C`: caller selector/value returned by typed menu records
- record `+0E`: optional extra byte
- record `+0F`: optional companion text pointer
- record `+13`: copied NUL-terminated body text
- record `+2C`: optional packed display subfield

The active `$8650` descriptor side uses:

- descriptor `+2B`: active chain head record index
- descriptor `+2D`: active chain tail/current record index
- descriptor `+2F`: current selected ordinal
- descriptor `+33`: selected row/page/group field

## Promotion Boundary

This slice promotes comments and runtime wording only. It does not fully close
the broad C1:196A menu loop, final names for every `$89D4` field, or every
descriptor field in `$8650`. The goal is to make later text-command and menu
work point at a stable record/descriptor contract.

Open followups:

- split or further comment C1:196A movement/cursor subpaths after C2:0B65 is
  polished
- cross-correlate `$89D4` record fields with C4:51FA layout writes and C4 text
  rendering helpers
- carry this record contract into text-command family notes for window and
  selection opcodes

## Open-Menu Caller Contract

The open-menu controller builds on the same text-entry helpers but also feeds
menu results back into the text VM and interaction-context layer. Current source
names in `C1:33B0..4103` distinguish the local `$0E/$10` scratch pair as entry
source pointers, feedback text pointers, decimal print sources, and
primary/secondary context-install sources. `$1F/$21` holds the selected
character value reused by Goods, Status, and Talk branches, while the active
context record offsets `+17/+1B/+21` carry the primary pointer, selected
inventory slot, and destination character fields for later text/menu work.

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\c1\bank_c1_helpers_asar.asm --strict
```
