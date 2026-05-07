# Foppy / Fobby Battle Actions

## Foppy's Wasted Turn

The Foppy action that prints the "is being absentminded" message is:

- Action enum: `BATTLE_ACTIONS::BE_ABSENTMINDED`
- Action id: `126`
- Message pointer: `MSG_BTL_BOOTTO`
- Handler: `BTLACT_NULL2`
- PP cost: `0`
- Target: none

`MSG_BTL_BOOTTO` renders as:

```text
@{performer} is being
  absentminded.
```

Because the action handler is `BTLACT_NULL2`, this is a pure no-op/flavor action.

## Enemy Rows

Normal Foppy is `ENEMY::FOPPY_1 = 98`.

Its action table:

1. `BATTLE_ACTIONS::BASH`
2. `BATTLE_ACTIONS::BE_ABSENTMINDED`
3. `BATTLE_ACTIONS::PSI_BRAINSHOCK_ALPHA`
4. `BATTLE_ACTIONS::PSI_MAGNET_ALPHA`

This row starts with `INITIAL_STATUS::CANT_CONCENTRATE`, so its PSI actions may also fail through the status system, but the explicit flavor "waste" action is `BE_ABSENTMINDED`.

Fobby is `ENEMY::FOBBY = 99`. Its second action is `BATTLE_ACTIONS::HP_SUCKER`, not `BE_ABSENTMINDED`.

There is also `ENEMY::FOPPY_2 = 207`, a later duplicate-looking Foppy row whose four actions are all `BATTLE_ACTIONS::NO_EFFECT`; do not confuse it with the normal Cave of the Past Foppy behavior.

## Source Pointers

- Enemy constants: `refs/ebsrc-main/ebsrc-main/include/constants/enemies.asm`
- Action constants: `refs/ebsrc-main/ebsrc-main/include/constants/actions.asm`
- Enemy rows: `refs/ebsrc-main/ebsrc-main/src/data/battle/enemies.asm`
- Action row: `refs/ebsrc-main/ebsrc-main/src/data/battle/action_table.asm`
- Text: `refs/EB-M2-Listing-v1/US/bank2F.txt` at `EF:81D7`
