# Bank C1 Null Hook `C1:E1A2`

This note covers the one remaining addressed C1 reference include that was not in the `unknown/...` bucket:

- `misc/null/C1E1A2.asm`

## Main Result

`C1:E1A2` is a deliberate null far routine:

- `REP #$31`
- `RTL`

`C1:E1A2..E48D` is now source-backed at `src/c1/c1_e1a2_null_far_callback.asm`. The source split keeps `E1A2..E1A5` as the null callback, `E1A5..E47F` as the enemy-select mode loop, and `E47F..E48D` as the enemy-select exit tail.

The `ebsrc-main` symbol list names it `NULL_C1E1A2`, and the bank include order places it between:

- `battle/actions/switch_weapon.asm`
- `battle/actions/switch_armor.asm`
- `battle/enemy_select_mode.asm`

Local xref scan found one direct caller:

- `E1:4E4E -> C1:E1A2`

So this is best treated as a no-op callback/action hook preserved for table compatibility, not as an unresolved logic body.

## Working Names

- `C1:E1A2` = `NullFarCallback`
- `C1:E1A5` = `RunEnemySelectMode`
- `C1:E47F` = `ExitEnemySelectMode`
