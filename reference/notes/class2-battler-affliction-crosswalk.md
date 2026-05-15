# Class2 Battler Affliction Crosswalk

This note captures the strongest current crosswalk between the `$A972`-anchored row fields used in `C2:4F62+` and the `ebsrc` `battler` affliction layout.

See also [class2-concrete-battle-text-call-paths.md](notes/class2-concrete-battle-text-call-paths.md).
See also [class2-battle-text-dispatch-stack.md](notes/class2-battle-text-dispatch-stack.md).
See also [class2-battler-core-field-crosswalk.md](notes/class2-battler-core-field-crosswalk.md).
See also [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md).
See also [class2-concentration-seal-family-c28d5a-c2a3d1.md](notes/class2-concentration-seal-family-c28d5a-c2a3d1.md).
See also [class2-persistent-status-action-pair-c28bbe-c28bfd.md](notes/class2-persistent-status-action-pair-c28bbe-c28bfd.md).
See also [class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md](notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md).
See also [class2-asleep-family-c29f06-c29f57.md](notes/class2-asleep-family-c29f06-c29f57.md).
See also [class2-strange-status-family-c28d3a-c28dbb-c2a056.md](notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md).

## Main result

The local row bytes around `+0x1D` line up unusually well with the `ebsrc` `battler::afflictions` layout.

From the reference `battler` struct:

- `battler::afflictions` starts at offset `0x1D`
- `battler::afflictions+1` is at offset `0x1E`
- `battler::afflictions+2` is at offset `0x1F`
- `battler::afflictions+3` is at offset `0x20`
- `battler::afflictions+4` is at offset `0x21`

From the local `C2:4F62+` status-announcement path:

- row byte `+0x1F` is compared against `1` before displaying `MSG_BTL_AT_START_NEMURI`
- row byte `+0x21` is tested for nonzero before displaying `MSG_BTL_AT_START_FUUIN`
- row byte `+0x20` is compared against `1` before displaying `MSG_BTL_AT_START_HEN`

That is an unusually clean fit.

The newer apply-helper pass in [class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md) now makes that field map stronger instead of just consistent. `C2:724A` writes directly to `row + 0x1D + X`, and its pinned callers now give a broader concrete value map:

- `X = 0`, `Y = 2` -> row `+0x1D = 2` -> diamondized
- `X = 0`, `Y = 3` -> row `+0x1D = 3` -> numbness
- `X = 0`, `Y = 4` -> row `+0x1D = 4` -> nausea
- `X = 0`, `Y = 5` -> row `+0x1D = 5` -> poison
- `X = 0`, `Y = 7` -> row `+0x1D = 7` -> cold
- `X = 1`, `Y = 1` -> row `+0x1E = 1` -> mushroomized
- `X = 1`, `Y = 2` -> row `+0x1E = 2` -> possessed
- `X = 2`, `Y = 1` -> row `+0x1F = 1` -> asleep
- `X = 2`, `Y = 2` -> row `+0x1F = 2` -> crying
- `X = 2`, `Y = 3` -> row `+0x1F = 3` -> could-not-move state
- `X = 2`, `Y = 4` -> row `+0x1F = 4` -> solidified
- `X = 3`, `Y = 1` -> row `+0x20 = 1` -> strange
- later action-entry family `C2:A056 / 8D3A / 8DBB` now gives this subgroup a concrete late-table anchor too
- direct local writers `C2:8D82` and `C2:A3E9` set row `+0x21 = 4` when it is still zero, then display `EF:6C0B` = `@{target} was not able to concentrate! @{target} was not able to use PSI!`

## Why this matters

The `ebsrc` battle-start flow in `main_battle_routine.asm` does the same three checks on the same three affliction groups:

- `battler::afflictions+2 == STATUS_2::ASLEEP` -> display `MSG_BTL_AT_START_NEMURI`
- `battler::afflictions+4 != 0` -> display `MSG_BTL_AT_START_FUUIN`
- `battler::afflictions+3 == STATUS_3::STRANGE` -> display `MSG_BTL_AT_START_HEN`

So the local `C2:4F62+` path is no longer just "status-like." It now matches the reference battle-start affliction checks field-for-field.

The apply side now helps too, because it gives a real local bridge for `battler::afflictions+1` at `+0x1E`, not just the `+2/+3/+4` groups that were easiest to see from the start-of-battle text path. The later action-entry note [class2-persistent-status-action-pair-c28bbe-c28bfd.md](notes/class2-persistent-status-action-pair-c28bbe-c28bfd.md) now strengthens that bridge again by pinning two live `D5:7B68` entries to `+0x1E = 1` and `+0x1E = 2` through the mushroomized and possessed success texts.

The `+0x1F` group is also stronger now than it was before the earlier helper-only pass. The later action-entry notes [class2-asleep-family-c29f06-c29f57.md](notes/class2-asleep-family-c29f06-c29f57.md) and [class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md](notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md) now give this subgroup a real late-table ladder: `C2:9F06 / 9F57` anchor value `1` as asleep, `C2:8C69 / 8DFC` anchor value `2` as crying, `C2:8CB8` anchors value `3` as immobilized or could-not-move, and `C2:8CF1` anchors value `4` as solidified.

The `+0x20` group is also stronger now than it used to be. The focused action-entry note [class2-strange-status-family-c28d3a-c28dbb-c2a056.md](notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md) now shows that `C2:A056`, its thin wrapper `C2:8D3A`, and sibling `C2:8DBB` all converge on the same write `X = 3`, `Y = 1 -> row + 0x20 = 1` and the same success text `EF:6C3A`. That gives the strange subgroup a real late-table family instead of only Flash-side and start-of-battle reader anchors. `C2:A056` is also the strongest current reference-backed candidate for the canonical PSI-side strange writer, because entry `0x003A` (`58`) is a one-target enemy PSI action that aligns well with `BTLACT_BRAINSHOCK_A`.

The `+0x21` group is also stronger now than it was before this pass. Two local wrappers at `C2:8D82` and `C2:A3E9` do a direct zero-check on row `+0x21`, write value `4`, and then display the `EF:6C0B` concentration or PSI-seal text. The paired parent action-entry note [class2-concentration-seal-family-c28d5a-c2a3d1.md](notes/class2-concentration-seal-family-c28d5a-c2a3d1.md) now shows that those wrappers belong to two live `D5:7B68` entries, one enemy-side `other` action at `C2:8D5A` and one enemy-side `item` action at `C2:A3D1`, both of which share the same `+0x21 = 4` success path. The reference `BTLACT_DISTRACT` body matches that same write pattern unusually well. That makes local value `4` a strong fit for the concentration or PSI-seal state, matching reference `STATUS_4::CANT_CONCENTRATE4 = 4`. No local `value 1` writer for this group has surfaced yet in the current ROM.

## Safest interpretation

The safest interpretation is:

- row byte `+0x1D` is now a strong local fit for the primary one-byte ailment enum in the recovery family documented in [battle-affliction-recovery-family-c29aea-a39d.md](notes/battle-affliction-recovery-family-c29aea-a39d.md), where values `1..7` behave like unconscious, diamondized, numbness, nausea, poison, sunstroke, and cold
- in the `C2:4F62+` path, the row anchored by `$A972` is battler-backed or at least battler-layout-compatible for these offsets
- row byte `+0x1E` is best read as `battler::afflictions+1`
  - local value `1` is now the strongest current fit for mushroomized
  - local value `2` is now the strongest current fit for possessed
- row byte `+0x1F` is best read as `battler::afflictions+2`
  - value `1` is the asleep-style status used by `MSG_BTL_AT_START_NEMURI`
  - values `2`, `3`, and `4` are now locally pinned as crying, could-not-move, and solidified
- row byte `+0x20` is best read as `battler::afflictions+3`
  - value `1` is strongly pinned as strange
- row byte `+0x21` is best read as `battler::afflictions+4`
  - nonzero values feed the sealed-style group used by `MSG_BTL_AT_START_FUUIN`
  - local value `4` is now a strong fit for the concentration or PSI-seal state from `EF:6C0B`, matching reference `STATUS_4::CANT_CONCENTRATE4`
  - no local writer for value `1` has surfaced yet in the current ROM

I am still keeping the wording slightly cautious because we have not yet proven that every other `$A972` field should be read as a full `battler` struct. The main remaining wrinkle is narrower now than it used to be. The broader selected-row controller at `C2:7550` also writes `+0x1D = 1`, but the newer local reader set now points the same way rather than against the ailment model: `state == 1` is the only consistently hard-blocked case in party-level scans, while `1` and `2` form the strongest special-handling pair. So the safest current wording is that the ailment-enum behavior is strongly pinned for the battle curative and battle-text status paths, and value `1` also fits the broader collapse-side startup path well; what is still not globally proved is the exact shared meaning of every nonzero value outside those battle-heavy paths.

## Broader clue for other row fields

That broader question has improved since the original affliction-only pass.

The separate note [class2-battler-core-field-crosswalk.md](notes/class2-battler-core-field-crosswalk.md) now captures the stronger lower-field picture:

- row byte `+0x0C` now behaves strongly like a `consciousness`-style active or present gate
- row byte `+0x10` now behaves strongly like `battler::row` in the local Thunder reflection branch
- row byte `+0x0B` still looks like an article or naming flag consistent with `battler::the_flag`, though that match remains narrower than the other two

So the affliction match no longer stands alone. The battler-layout interpretation is now holding up in multiple parts of the same row family.

## Current safest takeaway

The safest takeaway is:

- `C2:4F62+` is a target-side start-of-battle status-announcement path
- row byte `+0x1D` now has a strong local ailment-enum read in the battle curative family, even though broader selected-row controller paths still keep that promotion slightly scoped
- its tested bytes `+0x1E`, `+0x1F`, `+0x20`, and `+0x21` line up cleanly with `battler::afflictions+1/+2/+3/+4`
- that makes the `$A972`-anchored row look battler-backed or battler-layout-compatible at least for the status-related portion of the struct
- the newer lower-field comparison in [class2-battler-core-field-crosswalk.md](notes/class2-battler-core-field-crosswalk.md) now strengthens that broader battler-layout reading

## Phase 2 status-writer lanes

The C-port intake adds pressure for a Phase 2 trace-oracle pass, but the local
crosswalk should keep behavior claims tied to pinned readers, writers, and EF
texts. The caller-matrix columns belong in
[class2-affliction-apply-helper-724a.md](notes/class2-affliction-apply-helper-724a.md):
caller, selected row source, `X` subgroup slot, `Y` value,
chance/resistance gate, and EF text result.

Current lane split for that matrix:

- `C2:724A` lanes cover solidification, late status payloads, Flash body numbness,
  item-side status leaves that reach the slot writer, and the resist-checked
  PSI status trio.
- concentration seal is adjacent but distinct: local evidence has
  `C2:8D5A/A3D1` writing row `+0x21 = 4` directly and emitting `EF:6C0B`,
  so it should be traced in the same affliction/status lane without being
  counted as a `724A` caller.
- diary-only details from the C port are trace candidates, especially selected
  row provenance and gate ordering for item-side statuses and the
  resist-checked PSI trio.

## Best next target

The best next move is to map more `724A` callers using the Phase 2 matrix so
the remaining subgroup values can be named from local behavior, especially the
callers that use `X = 1`, `2`, or `3` outside the current battle-heavy clusters.









