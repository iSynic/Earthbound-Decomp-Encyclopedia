# Class2 Dispatch Family

This note captures the current ROM-first model for how the class-`2` C2 handlers appear to fit into a broader per-slot dispatch family.

## No direct callers to `C2:26D0` or `C2:26EB`

A direct-call scan found no `JSL` or same-bank `JSR` call sites for either routine.

That strongly suggests these handlers are reached indirectly, most likely through a table-driven or state-driven dispatch path inside bank `C2`.

## The nearby `99DC` family behaves like per-slot selector state

Several routines around the `26D0` region consult WRAM tables rooted at `99DC+` after mapping a slot through `C0:8FF7` with selector `#$005F`.

The stronger current reading is that `99DC` is the first byte of the seven-byte party-character affliction/status group. It still behaves like a per-slot state selector to many C1/C2 consumers, but the root identity is now less generic: `lookup_wram_field.py` maps `$99CE` as `PARTY_CHARACTERS`, stride `$005F`, and `$99DC` as record offset `+$0E`, `afflictions[0]`.

`C0:329F` is the clean local reset helper for that group: it maps a character selector through `C0:8FF7` with `Y = #$005F`, then clears `$99DC..$99E2` for that character record. See `notes/character-affliction-clear-c0329f.md`.

Why that reading fits:

- `C2:26F0` scans active slots and returns the first slot whose `99DC` byte is `1`
- `C2:2730` scans active slots and counts how many have `99DC` values other than `1` or `2`
- other bank `C0` routines also branch on `99DC == 1` or `99DC == 2`
- the class-`2` event-flag handlers sit in the middle of this same local C2 routine cluster

## Confirmed companion routines

Current best working names:

- `C2:26F0` -> `Find_FirstSlotWithState1`
- `C2:2730` -> `Count_SlotsNotInState1Or2`
- `C2:277C` -> `Find_FirstSlotNotInState1Or2`
- `C2:27C8` -> `Accumulate_StateToBitmask`

These names are intentionally conservative, but they match the observed control flow.

`C2:26F0` returns the first party slot whose `$99DC` byte is exactly `1`.

`C2:2730` counts party slots whose `$99DC` value is neither `1` nor `2`.

`C2:277C` is the mirror finder: it returns the first party slot whose `$99DC` value is neither `1` nor `2`, or `0` if none are found.

`C2:27C8` is a 4-way switch on `$99DC` that ORs a bit into WRAM `$9839`:

- `99DC == 1` -> `$9839 |= 0x0001`
- `99DC == 2` -> `$9839 |= 0x0002`
- `99DC == 3` -> `$9839 |= 0x0004`
- `99DC == 4` -> `$9839 |= 0x0008`

That makes `$9839` a compact party-wide presence bitmask for which `$99DC` states `1..4` are currently represented across the party.

## Safest current value split

The local reader set is now strong enough to promote a narrower value-behavior summary even though the final global name of `$99DC` should stay cautious.

Safest current split:

- `0` = default or inactive side
- `1` = the only consistently hard-blocked state; this is the strongest current fit for unconscious or collapsed state
- `2` = the strongest current sibling of `1`; it is grouped with `1` in party-level bookkeeping, but it is not blocked by every `state == 1` gate
- `3` = a nonzero active-side state in at least one menu or setup path
- `4` = a nonzero but inactive-side state in that same path

Why this split is the safest current one:

- `C2:B298` still treats only `state == 1` as the direct action-blocking or "It did not work!" case
- `C2:2730`, `C2:277C`, and `C0:353E` group `1` and `2` together as the special-handling pair
- `C4:A19E` excludes only `1` from the low-HP or curative target scan
- `C1:366B` groups `1`, `2`, and `3` together on the active side, while `0` and `4` fall to the inactive side

So `$99DC` is now healthier as a real per-slot state byte with a partly recovered value map, not just a generic selector.

## The `99xx` cluster now looks like a timed transition family

See `notes/class2-state-machine-99xx.md`, `notes/class2-slot-fields-and-transition-start.md`, and `notes/class2-handoff-4477-4703.md` for the focused writeups.

The important gain is that the nearby `C2:99A7` / `99E8` / `9A2E` / `9A79` cluster no longer reads like a vague dispatcher. It behaves like a shared per-slot transition controller:

- it gates through `C2:7CFD` and `C2:98A1`
- it chooses among several small state-specific text or transition helpers
- it converges on `C2:94CE`, which behaves like a countdown tick and expiry cleanup path
- nearby helpers `C2:9A80` and `C2:9AB8` are parameterized transition installers that feed the same family
- the shared helper `C2:7550` now reads better as the startup branch that installs one selected battler into a collapse or affliction-handling path for the same family
- the handoff through `C2:4477` and `C2:4703` now looks like a derived-action builder and dispatcher rather than a direct text path

This does not prove the exact gameplay identity yet, but it does sharpen `99DC` from a generic selector into a real control byte in a timed battler-state family, and it makes selected-row `+1D` look less like a generic active flag and more like part of the broader affliction or collapse-state side.

## What this says about class `2`

Taken together with the earlier findings:

- class `2` stores an event-flag id in `$9C88`
- `C2:26EB` tests that flag
- `C2:26D0` sets or clears that flag, then refreshes the raw target in `$5D64`
- `C0:C30C` re-tests the same flag and writes `$2AF6,target = 0` or `4`
- the surrounding C2 family consults per-slot selector/state bytes in `99DC+`

Current best interpretation:

- class `2` belongs to a broader per-slot interactable-object state machine
- the event flag is one input to that state machine
- the refresh path pushes the target into one of two local visual or behavior variants

## Remaining unknowns

- the exact semantic split among selector values `1`, `2`, `3`, and `4` in `99DC`, even though `1` is now much healthier as the blocked or collapsed side and `2` as a non-blocking sibling state
- whether `99DC` is best named as behavior class, state id, or handler selector
- what exact gameplay family the timed `99xx` transition controller belongs to
- what indirect bank `C2` dispatcher actually lands on `26D0` and `26EB`

## Best next target

- See `notes/class2-mask-helper-family.md` for the decoded bitset layer. The best next move is to map the candidate list rooted at `9FAC` or decode the metadata tables around `9FC9`, so the `99DC` selector values can be named from concrete behavior.
