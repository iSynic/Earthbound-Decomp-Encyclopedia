# C0 Task Pool Runtime Polish

Status: first C0 task allocator/runtime polish slice.

This note records the byte-neutral source comments added after
`notes/c0-presentation-queue-runtime-polish.md`. The slice focuses on the
task-slot/task-record allocator core, active task-slot runner, and default
visible task dispatcher.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c0/c0_927c_init_delayed_action_pools.asm` | Bootstraps task-slot and task-record pools and installs C0:DB0F as the default tail dispatcher. |
| `src/c0/c0_9321_init_delayed_action_state.asm` | Allocates one task slot plus first task record, seeds default callbacks, and links the slot active. |
| `src/c0/c0_941e_init_task_record_script_state.asm` | Initializes task-record script offset/bank state, wait counter, and return-stack depth. |
| `src/c0/c0_94aa_process_active_task_slots.asm` | Walks active task slots, runs `$121E/$11A6` callbacks, processes record scripts, and tail-dispatches through `$0A5E`. |
| `src/c0/c0_9c02_alloc_task_slot_or_fail.asm` | Allocates a task slot from `$0A52` in range `$0A4C..$0A4E`, or releases a slot through the local C0:9C3B entry. |
| `src/c0/c0_9c57_link_task_slot_into_active_list.asm` | Appends a slot to the active list rooted at `$0A50`. |
| `src/c0/c0_9c73_detach_task_slot_link.asm` | Detaches a slot from the active list and fixes `$0A50/$0A56`. |
| `src/c0/c0_9c8f_push_task_slot_to_free_list.asm` | Pushes a slot onto the free-slot list rooted at `$0A52`. |
| `src/c0/c0_9c99_restore_task_record_chain.asm` | Restores a slot-owned `$0ADA -> $125A` record chain to the free-record list rooted at `$0A54`. |
| `src/c0/c0_9cd7_compact_task_slot_free_list.asm` | Rebuilds the free-slot list by marking free entries and rechaining them in descending order. |
| `src/c0/c0_9d03_pop_task_record_from_free_list.asm` | Pops one task record from `$0A54`. |
| `src/c0/c0_9d12_push_task_record_to_free_list.asm` | Unlinks a task record from its slot and pushes it onto `$0A54`. |
| `src/c0/c0_9d1f_unlink_task_record_from_slot_chain.asm` | Removes a record from the chain owned by slot X. |
| `src/c0/c0_9d3e_find_task_record_predecessor.asm` | Finds a predecessor in a slot-owned task-record chain. |
| `src/c0/c0_9da1_init_task_record_defaults.asm` | Seeds default task-record callback/state fields. |
| `src/c0/c0_db0f_dispatch_active_task_slots.asm` | Default tail dispatcher; visible entries call C0:A0CA and `$103E == 1` entries are sorted through `$280C`. |

## Evidence Inputs

- `notes/frame-callback-bodies.md`
- `notes/actionscript-dispatch-task-frontier-c08fc2-c09ece.md`
- `notes/task-freeze-position-callbacks-maplookup-c09f3b-c0a26b.md`
- `notes/c0-entity-visual-runtime-polish.md`

## Runtime Pool Contract

The task pool core uses:

- `$0A50`: active task-slot list head
- `$0A52`: free task-slot list head
- `$0A54`: free task-record list head
- `$0A56`: active-list tail/cache field updated by detach
- `$0A5E`: tail dispatcher callback, initialized to C0:DB0F
- `$0A9E[slot]`: task-slot next pointer
- `$0ADA[slot]`: first task-record index owned by a slot
- `$125A[record]`: task-record next pointer or free-list link

The task-slot callback path uses:

- `$121E[slot]`: primary motion/update callback
- `$11A6[slot]`: projection/display-position callback
- `$11E2[slot]`: data/draw callback consumed by C0:A0E3
- `$107A/$10B6`: optional per-slot indirect callback target/flags

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not decode
the full action-script interpreter, script opcode wrappers, or all task data
callback bodies. The open labels remain:

- exact field names for the broader task-slot table family
- action-script opcode semantics around C0:9506 and C0:9B09+
- meaning of `$103E == 1` beyond sorted projected-Y dispatch
- full C0:A0CA/C0:A0E3/C0:A0FA data callback ABI

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
