# Class2 Record Consumer Families

This note groups the known `D5:9589` record consumers by behavior instead of by individual field offsets.

See also `notes/class2-005e-record-domain.md`.
See also `notes/class2-end-to-end-gate-path-ab35.md`.
See also `notes/class2-end-to-end-gate-path-5540.md`.

## Current high-level picture

The strongest current reading is that the `D5:9589` records are not passive data blobs. Bank `C2` uses them through a small number of recurring consumer families:

- filter and eligibility checks
- ranking and export passes
- mask-width or control-value selection
- activation or follow-up dispatch
- textbox and audio presentation setup

That is a stronger subsystem statement than any one field name by itself.

## Family A: presentation hooks

Known members:

- `C2:4A4B` / `C2:4CD5` using record `+0x37`
- `C2:4F0D` using record `+0x2D`
- `C2:7550` using record `+0x31`

Current safest reading:

- `+0x37` feeds a bank-`C4` audio-side helper and behaves like an audio cue id
- `+0x2D` feeds the `C1:DC1C -> C1:86B1` path and behaves like a textbox or script-data pointer
- `+0x31` is read as a 32-bit pointer in `C2:7680+` and dispatched through `C1:DC1C`, which makes it look like a second presentation or scripted-action pointer rather than a tiny scalar parameter

This is the clearest evidence that the record family carries presentation payloads, not just abstract selection metadata.

## Family B: ranking and export

Known members:

- `C2:6250` using `+0x29`
- `C2:6334` using `+0x25`
- `C2:6734` using `+0x3C`, then `+0x21` and `+0x3A`

Current safest reading:

- `+0x25` and `+0x29` behave like accumulated contribution values written into running totals such as `$A974/$A976` and `$A978`
- `+0x3C` behaves like a small ranking, limit, or priority byte because the code scans all active records and keeps the maximum
- `+0x21` and `+0x3A` are then exported as a paired byte-parameter set into `AA7E[]` and `AA86[]`

This family looks like a score-and-export pass over the active `9F8C` set.

## Family C: eligibility and gating

Known members:

- `C2:5540` using `+0x56`
- `C2:AB35` using `+0x56`
- `C2:7B10` using `+0x5A`
- `C2:8399` using `+0x44`
- `C2:B0C8` using `+0x5D`

Current safest reading:

- `+0x56` acts like a gate or classification byte checked early while scanning candidate records
- `+0x5A` acts like an enable or action byte that decides whether a separate activation path is entered
- `+0x44` acts like a threshold or mode byte used in a branch-heavy selection path
- `+0x5D` acts like a byte-sized threshold compared against a local count-like value before the heavier follow-up path runs

This family makes the record tail look like compact control-policy data.

## Family D: control-mask selection

Known members:

- `C2:4D71`
- `C2:6446`

Current safest reading:

- these paths read record `+0x58` into `$AA10`
- they then use `+0x57` to choose one of several mask-width tests via repeated calls to `C0:8E9A`
- depending on the mask result, `$AA10` is either preserved or cleared

This looks like a mode-plus-value control pair rather than a pointer family.

## Family E: transform or scaling selection

Known member:

- `C2:BE2E` using `+0x5C`

Current safest reading:

- record `+0x5C` is fed through a helper path and used to shape a later transform instead of being branched on directly
- nearby code then combines that result with record `+0x1C` and the byte at `+0x5B`

This makes `+0x5C` look like a compact table selector or scaling selector.

## What ties the families together

Across all of these caller groups, the same record can contribute:

- a text pointer
- an audio cue id
- ranked contribution bytes
- paired exported byte parameters
- gate, threshold, and control bytes

That is why the current best label remains "presentation or interaction descriptor" rather than something narrower like only a script record or only a battle record.

## Current safest subsystem interpretation

The best current interpretation is:

- bank `C0` builds an upstream list of source ids in `9F8C`
- bank `C2` maps those ids into `D5:9589` records
- bank `C2` then uses those records to filter, rank, parameterize, and finally present or activate a chosen result

That means the `9F8C`-driven class-`2` family now looks like a full descriptor-consumer pipeline rather than a loose bag of helpers.

## Best next target

- See `notes/class2-end-to-end-gate-path-ab35.md` and `notes/class2-end-to-end-gate-path-5540.md` for the two end-to-end anchors. The best next move is to tighten the second-stage selector around `$A970`, `C2:BAC5`, and `C2:BB18`, because that is where the heavier `5540` path stops looking like pure gating and starts looking like an ongoing controller.

## Update: table identity is much less vague now

A later cross-check made the high-level picture sharper.

The `D5:9589` records are now much more likely to be entries in the enemy configuration table than a generic presentation-descriptor family. The strongest anchors are:

- `#$005E` exactly matching `.SIZEOF(enemy_data)` in the `ebsrc` reference
- local extraction from `D5:9589 + 1 + n * 0x5E` decoding to enemy names
- field matches such as `+0x2D -> encounter_text_ptr`, `+0x31 -> death_text_ptr`, `+0x37 -> music`, `+0x4E -> final_action`, and `+0x00 -> the_flag`

That means the consumer families below are best read as battle-side enemy-data consumers rather than abstract record consumers.

See also [class2-d59589-enemy-data-crosswalk.md](notes/class2-d59589-enemy-data-crosswalk.md).
