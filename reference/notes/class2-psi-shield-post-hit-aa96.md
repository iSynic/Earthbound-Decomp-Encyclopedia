# Class2 PSI Shield Post-Hit AA96 Path

This note captures the current best local interpretation of `C2:941D` and `C2:94CE`, the helpers that consume `$AA96` after the Thunder-family reflection branch.

See also `notes/class2-psi-thunder-reflection-branch.md`.
See also `notes/class2-psi-thunder-common-local-flow.md`.
See also `notes/class2-reflected-hit-context-rebuild.md`.

## Current strongest claim

The `$AA96` consumers are not generic cleanup helpers. They now look like a local PSI-shield post-hit resolution path with separate branches for:

- reflected PSI shield handling
- non-reflecting PSI shield handling
- shield-hp decrement and shield-break text

This is still partly inferential, but the local flow now matches the reference `PSI_SHIELD_NULLIFY` plus shield-weakening behavior closely enough to treat that as the best working model.

## Why `C2:941D` looks PSI-specific

`C2:941D` begins by setting `$AA94 = 1`, then reads the selected row from `$A970` and computes a `D5:7B68` entry address from row byte `+0x04`.

Source polish now names those mechanical pieces directly:
`$A970` is the active selected battler row pointer, `$A972` is the active target
battler row pointer, selected row `+0x04` is the action id, selected row
`+0x08` is the action argument byte staged through `C1:DD7C`, action row `+2`
is the type byte, and type `3` is the PSI action type for this blocker.

The important local check is:

- load `D5:7B68 + selector * 12 + 2`
- mask to the low byte
- compare with `3`

Given the earlier `D5:7B68` action-table work, that low byte is best read as the action type byte. Value `3` matches `ACTION_TYPE::PSI` in the `ebsrc` constants.

So `C2:941D` only continues its special handling for PSI-type actions.

## Target-row byte `+0x23` now reads like a PSI-shield subtype

After confirming a PSI action, `C2:941D` branches on target-row byte `+0x23`:

- `+0x23 == 1` -> one branch
- `+0x23 == 2` -> second branch
- anything else -> returns `0`

That shape fits the reference PSI shield split unusually well:

- `PSI_SHIELD_POWER` -> reflect PSI
- `PSI_SHIELD` -> absorb or nullify PSI without reflection

I am not claiming the field name is proven yet, but selected-row byte `+0x23` now reads much more like a mirrored PSI-shield mode than like a generic controller phase.

## Branch `+0x23 == 1`: reflected PSI path

When byte `+0x23 == 1`, `C2:941D` does this:

- dispatches `EF:70D2` through `C1:DC1C`
- sets `$AA96 = 1`
- calls `C2:7E8A`
- returns success

This lines up well with the reference `PSI_SHIELD_NULLIFY` reflect branch, which displays `MSG_BTL_PSYPOWER_TURN`, marks damage as reflected, and swaps attacker and target.

The match is stronger now because:

- `C2:7E8A` already looks like a context-swap and refresh helper
- `$AA96` is immediately consumed by the follow-up helper `C2:94CE`

So the best current reading is:

- `EF:70D2` is likely the local counterpart to the PSI-power-shield reflection text
- `$AA96 = 1` is the reflected-PSI marker used to finish shield weakening after the reflected hit resolves

## Branch `+0x23 == 2`: non-reflecting PSI shield path

When byte `+0x23 == 2`, `C2:941D` does this instead:

- dispatches `EF:70FA` through `C1:DC1C`
- decrements selected-row byte `+0x25`
- if the decremented value reaches zero:
  - clears selected-row byte `+0x23`
  - dispatches `EF:7099` through `C1:DC1C`
- returns success

That matches the reference non-reflecting PSI-shield path much better than a generic battle-state update would:

- display the shield-turn message
- decrement shield HP
- if the shield is exhausted, clear the shield status and display the shield-off text

So the best current reading is:

- selected-row byte `+0x25` behaves like shield HP or remaining shield charges
- `EF:70FA` is likely the local counterpart to the non-reflecting PSI shield message
- `EF:7099` is likely the local counterpart to the shield-break or shield-off message

## `C2:94CE` looks like delayed shield weakening for reflected PSI

`C2:94CE` starts by clearing `$AA94`, then checks `$AA96`.

If `$AA96 == 0`, it returns immediately.

If `$AA96 != 0`, it:

- calls `C2:7E8A`
- decrements selected-row byte `+0x25`
- if the value reaches zero:
  - clears selected-row byte `+0x23`
  - dispatches `EF:7099` through `C1:DC1C`
- clears `$AA96`
- returns

This is a very good fit for the reflected-PSI version of shield weakening:

- reflection happens first
- the reflected attack resolves in swapped context
- only after that does the original shield lose one shield-hp unit
- if the shield is exhausted, the shield-off text is shown

That delayed decrement is exactly what we would expect if the reflected branch needed to postpone shield weakening until the reflected hit finished resolving.

## What `$AA94` now seems to be doing

`C2:941D` sets `$AA94 = 1`, and `C2:94CE` clears it at entry.

That suggests `$AA94` is a transient "PSI-shield post-hit resolution in progress" marker rather than a long-lived gameplay state. I do not think we have enough yet to name it more strongly than that.

## Current safest takeaway

The safest current takeaway is:

- `C2:941D` and `C2:94CE` form a PSI-shield post-hit resolution helper pair
- selected-row byte `+0x23` behaves like a PSI-shield subtype field with reflect and non-reflect variants
- selected-row byte `+0x25` behaves like shield HP or remaining shield charges
- `EF:70D2`, `EF:70FA`, and `EF:7099` are strong candidates for the local PSI-shield reflect, absorb, and shield-off texts
- `$AA96` behaves like a reflected-PSI continuation marker used to delay shield weakening until the reflected hit resolves

That is a much more specific and useful model than "post-hit cleanup after reflection."

## Best next target

The best next move is to tighten the context-refresh helpers behind the reflected path, especially `C2:3BCF` and `C2:3D05`, because they are the remaining black box between "reflection happened" and "battle selection state was rebuilt for the reflected hit."
