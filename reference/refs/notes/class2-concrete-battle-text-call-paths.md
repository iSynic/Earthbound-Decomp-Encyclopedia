# Class2 Concrete Battle Text Call Paths

This note captures the first concrete local bridges between the enemy text-pointer call sites and the nearby battle-text context refresh family.

See also [class2-battle-text-dispatch-stack.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-text-dispatch-stack.md).
See also [class2-enemy-text-pointer-consumers.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-enemy-text-pointer-consumers.md).
See also [class2-reflected-hit-context-rebuild.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-context-rebuild.md).
See also [class2-battler-affliction-crosswalk.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battler-affliction-crosswalk.md).

## Main result

We now have concrete local bridges for both halves of the nearby battle-text context family:

- an encounter-text path that runs through `C2:3BCF -> C1:DD70` before calling `C1:DC1C`
- a companion path that runs through `C2:3D05 -> C1:DD76` and then immediately emits hardcoded battle-text pointers through `C1:DC1C`

That is the strongest local evidence so far that the `DD70/DD76` pair really does prepare battle text context for the `DC1C` display wrapper.

## Concrete bridge A: `C2:4F00+`

Local bytes at `C2:4F00+` show this sequence:

1. `JSL C2:3BCF`
2. load `D5:9589 + 0x2D` from the active `9F8C` enemy id
3. read the resulting 32-bit pointer into `$06/$08`
4. copy it into `$0E/$10`
5. `JSL C1:DC1C`

Immediately after that, the same path can emit a second hardcoded battle-text pointer through `C1:DC1C` when `$1D == 1`.

That is the clearest local proof so far that `C1:DC1C` consumes a far text pointer supplied in `$0E/$10`.

## Why `C2:3BCF` matters here

Our earlier reflected-hit notes already established that:

- `C2:3BCF` rebuilds a side-local text buffer
- it clears and fills work buffer `A983`
- it uses `$5E77` as the companion late-token flag
- it ends through `C1:DD70`

So `C2:4F00+` gives us a real local chain, not just a neighborhood guess:

- first refresh battle text context through `C2:3BCF -> C1:DD70`
- then dispatch the enemy encounter-text pointer through `C1:DC1C`

## Concrete bridge B: `C2:4F62+`

A second local bridge gives us the missing companion-side proof.

Local bytes at `C2:4F62+` show this sequence:

1. `JSL C2:3D05`
2. test selected-row bytes from the row anchored by `$A972`
3. stage hardcoded far pointers like `EF:843F`, `EF:8444`, and `EF:8445` into `$0E/$10`
4. `JSL C1:DC1C` after each staged pointer

This is not an enemy-record pointer load like `C2:4F00+`. But it is exactly the companion bridge we needed:

- `C2:3D05` runs first
- our earlier notes already tie `C2:3D05` to `C1:DD76`
- then the path immediately emits battle-text pointers through the same `C1:DC1C` wrapper

That makes the `DD76` side much less hypothetical. We now have a concrete local path where target-side context refresh and `C1:DC1C` display calls occur back-to-back.

## What the `EF:843F / 8444 / 8445` messages are

This message family turned out to be much more specific than just "hardcoded battle text."

From the `ebsrc` YAML battle-text map:

- `EF:843F` is the start of `EBATTLE0`
- `EBATTLE0 + 0x0000` = `MSG_BTL_AT_START_NEMURI`
- `EBATTLE0 + 0x0005` = `MSG_BTL_AT_START_FUUIN`
- `EBATTLE0 + 0x0006` = `MSG_BTL_AT_START_HEN`

So the `C2:4F62+` path now looks like a real battle-start status-announcement path, not a generic text branch.

That lines up very nicely with the `ebsrc` battle-start flow in `main_battle_routine.asm`, where the game:

1. fixes target name
2. checks target status groups
3. displays start-of-battle messages for asleep, sealed, and strange states

## Exact field match for the tested bytes

This part tightened further.

The `ebsrc` `battler` struct places the affliction groups at:

- `afflictions` at `+0x1D`
- `afflictions+2` at `+0x1F`
- `afflictions+3` at `+0x20`
- `afflictions+4` at `+0x21`

Those are exactly the three bytes tested locally in `C2:4F62+`.

That means the local status checks now line up field-for-field with the reference battle-start logic:

- row byte `+0x1F` is best read as the asleep-style group feeding `MSG_BTL_AT_START_NEMURI`
- row byte `+0x21` is best read as the sealed-style group feeding `MSG_BTL_AT_START_FUUIN`
- row byte `+0x20` is best read as the strange-style group feeding `MSG_BTL_AT_START_HEN`

The safest broader phrasing is that the `$A972`-anchored row is battler-backed or at least battler-layout-compatible for this status region.

## Concrete bridge C: `C2:7680+`

Local bytes at `C2:7680+` show the late selected-row controller doing this:

1. load the active `9F8C` enemy id
2. map through stride `#$005E`
3. add record offset `+0x31`
4. read the resulting 32-bit pointer into `$06/$08`
5. copy it into `$0E/$10`
6. `JSL C1:DC1C`

This remains the cleanest local death-text style call site we have so far.

Unlike `C2:4F00+`, the small visible snippet does not itself show a direct `C2:3BCF` or `C2:3D05` call immediately before `C1:DC1C`. So it is a weaker bridge to the `DD70/DD76` family. But it still gives us one more concrete fact about `C1:DC1C`: the wrapper is fed the same `$0E/$10` far-pointer calling convention in both the encounter-text and death-text cases.

## What this improves in the stack model

These three call sites sharpen the earlier stack note in six ways:

- `C1:DC1C` directly consumes far pointers staged in `$0E/$10`
- `C2:4F00+` proves one concrete path where `C2:3BCF -> C1:DD70` happens immediately before a `C1:DC1C` display call
- `C2:4F62+` proves the companion pattern where `C2:3D05 -> C1:DD76` happens immediately before multiple `C1:DC1C` display calls
- the hardcoded `EF:843F / 8444 / 8445` family is specifically the battle-start status message cluster from `EBATTLE0`
- the `C2:4F62+` tested bytes line up exactly with `battler::afflictions+2/+3/+4`
- the enemy encounter and death text pointers both use the same pointer-staging convention before dispatch

That is enough to replace more of the remaining abstract wording with a tighter local model.

## Current safest takeaway

The safest takeaway is:

- `C1:DC1C` is very likely a battle-text display wrapper that consumes a far pointer from `$0E/$10`
- `C2:4F00+` is a concrete local encounter-text path that first refreshes battle text context through `C2:3BCF -> C1:DD70`, then calls `C1:DC1C`
- `C2:4F62+` is the concrete companion path that first refreshes through `C2:3D05 -> C1:DD76`, then emits target-side battle-start status messages through `C1:DC1C`
- in that `C2:4F62+` path, row bytes `+0x1F/+0x20/+0x21` are best read as the battler affliction groups for asleep, strange, and sealed-style status checks
- `C2:7680+` is a concrete local death-text style path that loads `enemy_data::death_text_ptr` and dispatches it through the same `C1:DC1C` wrapper

## Best next target

The best next move is to follow the same battler-layout clue into row bytes `+0x0B`, `+0x0C`, and `+0x10`, or to prove whether `C1:DC1C` and `DISPLAY_IN_BATTLE_TEXT` are the exact same entry point rather than just the same local family.
