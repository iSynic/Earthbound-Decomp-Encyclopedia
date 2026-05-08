# Class2 B6EB Caller Family 4Dxx

This note captures the current best read on the `C2:4D01` / `C2:4D54` caller family for local `C2:B6EB`.

See also [class2-local-enemy-id-to-battler-init-chain.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-local-enemy-id-to-battler-init-chain.md).
See also [class2-battlers-table-layout-9f8a-9fac.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battlers-table-layout-9f8a-9fac.md).
See also [class2-concrete-battle-text-call-paths.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-concrete-battle-text-call-paths.md).

## Main result

The `4Dxx -> 4Fxx` family no longer looks best described as a summon or `CALL_FOR_HELP_COMMON` counterpart.

The stronger local read now is that this region belongs to the battle-start enemy-group initialization flow:

- initialize enemy battlers from `9F8C` through local `C2:B6EB`
- display the lead enemy's encounter text
- optionally emit an extra battle-start message at `EF:78D8`
- then loop over enemy battlers and display start-of-battle status lines

That is a substantially better fit for the full local control flow than the older summon-family hypothesis.

## Why the earlier summon read weakened

The older `CALL_FOR_HELP_COMMON` comparison was driven by two real clues:

- the family calls the shared enemy battler initializer `C2:B6EB`
- `C2:4F3F+` emits `EF:78D8`, which matches `MSG_BTL_NAKAMA_KITA` in the reference text map

Those clues are still real, but the wider local flow now points somewhere else.

The decisive change is that the code immediately after the encounter-text branch does not look like a summon tail. It looks like the ordinary battle-start enemy-status announcement loop.

## Strong local alignment with battle-start flow

### Lead encounter-text path

At `C2:4F00+`, the local code:

- loads the first enemy id from `9F8C`
- maps it through `D5:9589 + 0x2D`
- stages `enemy_data::encounter_text_ptr` into `$0E/$10`
- dispatches it through `C1:DC1C`

That is exactly the shape we expect for the lead-enemy encounter text at battle start.

### Exact enemy-battler loop at `C2:4F52+`

The clearest new proof is the loop beginning at `C2:4F52`.

Current safest read:

- `$31` is the local enemy index
- `A0 4E 00 / JSL C08FF7` computes `index * 0x4E`
- `ADC #$A21C / STA $A972` builds `A972 = 0xA21C + index * 0x4E`

Since `0xA21C = 0x9FAC + 8 * 0x4E`, that is:

- `A972 = BATTLERS_TABLE + 8 * 0x4E + index * 0x4E`
- in other words, a pointer to enemy battler `8 + index`

Immediately after that, the path:

- calls `C2:3D05`
- tests battler bytes `+0x1F`, `+0x21`, and `+0x20`
- dispatches `EF:843F`, `EF:8444`, and `EF:8445`
- increments `$31`
- loops until `$31 == 9F8A`

Those three message pointers are the already-mapped start-of-battle status lines:

- `MSG_BTL_AT_START_NEMURI`
- `MSG_BTL_AT_START_FUUIN`
- `MSG_BTL_AT_START_HEN`

That is an unusually tight local match for the reference `main_battle_routine` battle-start status loop.

## What `EF:78D8` now most likely means

The `EF:78D8` dispatch at `C2:4F3F+` is still important, but it is no longer enough to make the whole family read as call-for-help.

The safer current statement is:

- `EF:78D8` is a real local extra message branch inside the battle-start enemy-init family
- it may correspond to a multi-enemy or cohort-style start-of-battle message
- it may also reflect some shared text reuse with the summon-family wording in the reference project
- by itself, it is not strong enough to override the much broader battle-start alignment of the surrounding code

So the older `MSG_BTL_NAKAMA_KITA` clue should now be treated as a useful but narrower clue, not as the family's primary identity.

## What still looks explicit

The direct battler-init side is still explicit.

Local bytes around `C2:4CD5` / `C2:4D01` and `C2:4D54` still show the family consuming enemy ids from `9F8C` and calling local `C2:B6EB`.

So the corrected high-level read is not "this was wrong and unrelated." It is:

- this is still a real enemy-battler initialization family
- but the surrounding flow looks much more like initial enemy-group setup than like a later summon helper

## What is still open

The remaining open questions are narrower now:

- what exact condition sets `$1D = 1` versus `$1D = 2`
- what local role `$4DBC` plays before the encounter-text branch
- whether the `EF:78D8` branch is best read as a cohort-style battle-start message or as evidence of a shared helper reused elsewhere

Those are still worth tracing, but they are no longer the same thing as proving a call-for-help family.

## Why `760C` should still stay separate

The newer caller trace still showed `C2:760C` as a `C2:B6EB` caller, but that family looks different.

The clearest reason to keep it separate is that the later `7600+` flow runs straight into the death-text-style pointer dispatch at `C2:7680+`, which still feels more like transformation, replacement, or scripted reinitialization than like ordinary battle-start group setup.

So the clean split is now:

- `4Dxx` -> likely battle-start enemy-group init family
- `760C` -> still open, probably a different battler-reinit situation

## Current safest takeaway

The safest takeaway is:

- local `C2:B6EB` is shared by multiple battler-init callers
- the `4Dxx -> 4Fxx` family is best read as a battle-start enemy initialization and status-announcement path
- the earlier `CALL_FOR_HELP_COMMON` comparison is now weaker than the `main_battle_routine` comparison
- `EF:78D8` remains a real local clue, but it no longer defines the whole family
- `760C` should still be treated as a separate unresolved reinit family

## Best next target

The best next move is to trace the setup that feeds `$4DBC` and `$1D`, because that should tell us why this battle-start family sometimes emits the extra `EF:78D8` branch before it enters the ordinary enemy-status loop.
