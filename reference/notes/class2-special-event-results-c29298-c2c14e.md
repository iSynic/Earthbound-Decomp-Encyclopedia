# Class2 Special Event Results C29298 C2C14E

This note captures the strongest current local model for the special none-target result slice around `C2:9298`, `C2:92EE`, and `C2:C14E`.

See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-late-normalization-and-odor-family-c29051-c29254.md](notes/class2-late-normalization-and-odor-family-c29051-c29254.md).
See also [class2-final-prayer-family-c2c572-c2c6f0.md](notes/class2-final-prayer-family-c2c572-c2c6f0.md).

## Working Names

- `C2:9298` = `RunRunawayFiveClumsyRobotSpecialEvent`
- `C2:92EE` = `RunMasterBarfPooStarstormSpecialEvent`
- `C2:C14E` = `RunRainbowColorsSpecialEvent`

## Main result

The late `D5:7B68` rows around `243`, `244`, and `290` are not ordinary attack or status handlers.

The safest current split is:

- `C2:9298` = Runaway Five or Clumsy Robot special event controller
- `C2:92EE` = Master Barf defeat or Poo swoop / Starstorm event result
- `C2:C14E` = rainbow-colors special event family with strong Master Belch-side transformation evidence

## `C2:9298` is the Runaway Five or Clumsy Robot special event controller

`C2:9298` is a live `D5:7B68` row:

- entry `243` -> target `none`, type `other`, text `EF:72F6`

The local message side is now much healthier than before.

The text block at `EF:72F6` is actually a two-branch event sequence:

- `EF:72F7` = `Black smoke poured from [user]'s body!`
- nearby continuation = `[user] was overcome by the smoke!`
- nearby continuation = `You can't see a thing!`
- alternate block `EF:733D` = `All of a sudden, some guys rushed into the room!`
- the same alternate block continues with explicit `Runaway Five` text and the robot switch gag

The local body matches that split:

- reads `D5:7A2C`
- calls `C2:1628`
- if the result is nonzero, displays `EF:733D`
- then calls `C0:DD53` with selector pair `0E = 3`, `A = 0x0F`
- otherwise, displays `EF:72F7`
- then calls `C0:DD53` with selector pair `0E = 3`, `A = 0x0D`
- then writes `$AA0E = 1`

So the healthiest current local name is no longer Belch-side anything. It is a Runaway Five or Clumsy Robot event controller with a smoke-side branch and a Runaway Five rescue branch.

The reference action-table alignment also supports that direction:

- entry `243` in `ebsrc` is `RUNAWAY_FIVE_EVENT`

I am still keeping the exact final symbolic name one notch cautious because the local body is a two-branch event controller rather than a single simple cutscene stub.

## `C2:92EE` is the Master Barf defeat or Poo swoop / Starstorm event result

`C2:92EE` is the next live `D5:7B68` row:

- entry `244` -> target `none`, type `other`, text `EF:7415`

That text block is unusually explicit:

- `EF:7415` = `REALIZE_PSI 0x04`
- nearby `EF:7419` = `Suddenly, [char 4] swooped down from the sky!`
- nearby `EF:743B` = `[char 4] used his new power, PSI Starstorm!`

The local body also behaves like a staged event result rather than a normal action:

- saves and swaps `A970/A972`
- calls `C1:DD41`
- calls `C2:28F8` with literal `4`
- iterates active battler rows using `consciousness` at `+0x0C` and side byte `+0x0E`
- routes selected rows through `C2:B930` and `C1:DD3B`
- scans party registry `$986F` for id `4`
- calls `C1:DDCC` when that party id is present
- prints `EF:743B`
- applies the scripted Starstorm damage through `C2:7EAF` /
  `RunHitResolutionAndStatusActionCluster`
- restores the saved `A970/A972` context

The reference action-table alignment is now strong enough to tighten the wording further:

- entry `244` in `ebsrc` is `MASTER_BARF_DEFEAT`

So the healthiest current local name is:

- Master Barf defeat or Poo swoop / Starstorm event result

## `C2:C14E` is a rainbow-colors special event family

`C2:C14E` is also a live `D5:7B68` row:

- entry `290` -> target `none`, type `other`, text `EF:8DDE`

The local message side is already distinctive:

- `EF:8DDE` begins with `All of a sudden, [user] glowed rainbow colors!`

The body is much richer than a plain text tail:

- reads and rewrites battler `sprite_x`, `sprite_y`, and `vram_sprite_index` at `+0x44`, `+0x45`, and `+0x43`
- stores the current row pointer and calls `C2:B6EB`
- writes battler `+0x0D` and global latch `$AA92`
- its sibling block at `C2:C1BD` scans battler rows in `$A21C`
- that scan looks for live enemy-side rows with ids `0x00C0` or `0x005D`
- it rewrites those rows to id `0x00A9`
- then prints `C8:F8C0` or `C8:F8FD`

Those `C8:F8C0/F8FD` texts are the strongest current anchor here, because they explicitly mention `Master Belch grabbed ...`
The C2 source now names them as `C8MSG_BelchGrabbedSuccess` and
`C8MSG_BelchGrabbedFailure`, both dispatched through the `C1:DC1C`
direct battle-text pointer ABI.

So the safest current local interpretation is:

- `C2:C14E` belongs to a rainbow-colors special event family with strong Master Belch-side transformation or replacement evidence

I am keeping the exact final symbolic name cautious because the full surrounding `C1BD..C2:C32A` family is larger than one single row body.

Source follow-up (2026-05-06): the presentation-transition blocks inside
`C2:C14E` now call the battle overlay helpers by role:
`C2:E8C4` / `StartBattleSwirlOverlayAndRecordMode`, `C2:E9C8` /
`PollBattleTransitionComplete`, and `C1:2DD5` / `WindowTick`. That makes the
event's two overlay waits read as ordinary presentation lifecycle waits around
the battle-background reload instead of raw long-call glue.

## Current takeaway

The current takeaway is that this late slice should not be lumped into the ordinary attack families.

Instead, it contains special event results:

- `9298` = strong local Runaway Five / Clumsy Robot event controller
- `92EE` = strong local Master Barf defeat / Poo swoop event result
- `C14E` = strong local rainbow-colors / Master Belch-side special event family

## EF source-anchor update

A later EF payload split promoted the local event text anchors behind the first
two families:

- `EF:72F6`, `EF:72F7`, and `EF:733D` now name the Runaway Five break-in root,
  failed, and succeeded scripts.
- `EF:7415` and `EF:743B` now name the Poo break-in / PSI Starstorm reveal
  scripts.

That keeps the C2 special-event row bodies and their EF text payloads visible as
one contract while the EBATTLE4 bytecode remains ROM-preserved data.

## What is still open

Still open:

- the exact final symbolic name for `C2:9298`
- the exact final symbolic name for `C2:C14E`
- whether `C2:C14E` should be split into one row body plus a larger sibling controller family
- what exact semantic role battler ids `0x00C0`, `0x005D`, and `0x00A9` play in that Belch-side transformation lane
