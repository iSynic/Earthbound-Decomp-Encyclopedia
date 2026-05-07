# C0 Presentation Queue Runtime Polish

Status: first C0 presentation/helper runtime polish slice.

This note records the byte-neutral source comments added after
`notes/c0-teleport-callback-runtime-polish.md`. The slice focuses on the
runtime-to-NMI presentation handoff: VRAM transfer staging, queued versus
immediate DMA, NMI queue drain, scroll-buffer commit, and scroll-shadow publish.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c0/c0_8180_nmi_handler_update_ppu_and_queues.asm` | NMI entry acknowledges `$4210`, disables HDMA, updates heartbeat counters, and enters PPU/queue work. |
| `src/c0/c0_8240_nmi_drain_queued_vram_dma_descriptors.asm` | Drains 8-byte VRAM DMA descriptors queued at `$0400+`. |
| `src/c0/c0_8284_nmi_commit_bg1_scroll_registers.asm` | Commits alternating scroll buffers `$41/$45/...` or `$43/$47/...` into `$210D..$2114`. |
| `src/c0/c0_834e_nmi_post_ppu_bookkeeping.asm` | Resets `$99`, runs frame callbacks under DP `$0200`, toggles staging base `$A1/$A3`, and increments `$A7/$A9`. |
| `src/c0/c0_8b20_publish_runtime_scroll_shadows_to_nmi_buffers.asm` | Publishes runtime scroll shadows `$31/$33/...` into the NMI commit buffers and flips `$2C/$2E`. |
| `src/c0/c0_8529_copy_record_block_and_set_transfer_flag.asm` | Copies table-described record blocks and ORs a NMI-consumed transfer/display flag into `$0030`. |
| `src/c0/c0_8573_submit_transfer_descriptor_list.asm` | Iterates transfer descriptor lists and stages fields into `$91/$93/$95/$97`. |
| `src/c0/c0_8616_queue_vram_transfer_from_dp_source.asm` | Front-end for the `$91/$92/$94/$96/$97` VRAM transfer ABI. |
| `src/c0/c0_8643_submit_queued_or_immediate_vram_transfer.asm` | Common wrapper for the staged transfer ABI. |
| `src/c0/c0_865f_submit_transfer_descriptor_or_immediate_dma.asm` | Appends descriptors to `$0400` when queued, or performs immediate channel-1 DMA when `$0D` is negative. |

## Evidence Inputs

- `notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md`
- `notes/c0-small-utility-frontier-69f7-8c54.md`
- `notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md`
- `notes/c0-entity-visual-runtime-polish.md`
- `notes/c0-teleport-state-runtime-polish.md`

## Runtime Contract

The transfer ABI staged by the C0 helpers is:

- `$91`: descriptor type/template selector
- `$92`: byte count/transfer size
- `$94/$96`: source pointer
- `$97`: destination VRAM address

C0:865F has two modes:

- queued mode when `$0D` is nonnegative: append an 8-byte descriptor at `$0400`
- immediate mode when `$0D` is negative: configure `$4310+`, `$2115/$2116`, and `$420B`

The runtime scroll handoff is:

- movement/runtime writes `$31/$33/$35/...`
- C0:8B20 publishes into `$41/$45/$49/...` or `$43/$47/$4B/...`
- `$2C` marks the NMI-visible buffer and `$2E` flips to the next buffer
- NMI commits the selected buffer to `$210D..$2114`

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not decode
all display renderer queue record formats, landing display records, or battle
background transfer descriptor streams. The open labels remain:

- exact descriptor type names for C0:8FB0/C0:8FB2 transfer templates
- full C0:8B8E display renderer queue record schema
- relationship between `$0030` flag bits and each NMI palette/record transfer
- cost attribution for the remaining overworld walking presentation workload

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
