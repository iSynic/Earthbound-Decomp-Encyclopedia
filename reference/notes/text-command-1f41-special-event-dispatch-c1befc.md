# Text Command `[1F 41]` Special Event Dispatch `C1:BEFC`

This note covers the unknown include at `C1:BEFC`.

See also [text-command-family-1f-deferred-callbacks.md](notes/text-command-family-1f-deferred-callbacks.md).
See also [overworld-position-context-byte-c1ad7d.md](notes/overworld-position-context-byte-c1ad7d.md).
See also [bicycle-transition-and-party-registry-c03c25-c03f1e.md](notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md).

## Main Result

`C1:BEFC` is the runtime body for text command `[1F 41 XX]`, the special-event dispatcher.

## Working Names

- `C1:BEFC` = `DispatchTextCommand1F41SpecialEvent`
- `C1:BE4D` = `AttemptHomesicknessResult`
- `C1:BEC6` = `RunGetOffBicycleMessageAndExit`

The local direct caller is `C1:72DA`, which receives the text command operand in `X`, transfers it to `A`, calls `C1:BEFC`, then stores the returned signed word into active text memory via `C1:045D`.

That local wrapper is now source-backed in `src/c1/c1_7274_stage_bank_deposit_accumulator_text_value.asm` as `HandleTextCommand1F41`.

That exactly matches the community reference description for `[1F 41 XX]`:

- it runs a special event chosen by `XX`
- unless stated otherwise, it returns `0`
- cases `0x11` and `0x12` return a meaningful result

## Dispatch Table

`C1:BEFC` is a linear compare-and-jump dispatcher for cases `1..18`.

Current local mapping:

- `01`: `C4:9D6A(0)`, then return `0`
- `02`: `C4:9D6A(1)`, then return `0`
- `03`: `C1:EAA6(0)` (`RunNameEntrySpecialEventPrelude`), then return `0`
- `04`: `C1:EAA6(1)` (`RunNameEntrySpecialEventPrelude`), then return `0`
- `05`: `C4:3344(1)` (`SetSpecialEventRestrictionLatch5d98`), then return `0`
- `06`: check event flag `0x0049` through `C2:1628`, pass result to `C4:3344` (`SetSpecialEventRestrictionLatch5d98`), then return `0`
- `07`: call `C4:D681` (`DisplayCurrentPositionTownMap`), return its result
- `08`: call `C3:FB09`, return its result
- `09`: `C4:ACCE(1)`, then return `0`
- `0A`: `C3:F3C5(1)`, then return `0`
- `0B`: `C4:ED0E`, then return `0`
- `0C`: `C4:F554`, then return `0`
- `0D`: `C1:2D17(1)`, then return `0`
- `0E`: `C1:2D17(0)`, then return `0`
- `0F`: clear 0x80 bytes at `$9C08..$9C87`, then return `0`
- `10`: `C4:ACCE(0)`, then return `0`
- `11`: call `C1:BE4D`, return its result
- `12`: if `$9883 == 3`, call `C0:3CFD` and return `1`; otherwise return `0`

The shared return-at-zero path at `C1:C040` resets accumulator width with `REP #$20`, loads `0`, and returns. The result-preserving path returns directly through `C1:C045`.

Source polish follow-up (2026-05-06): `src/c1/c1_befc_dispatch_text_command1_f41_special_event.asm`
now uses the named `C1:EAA6` contract for cases `03/04`, names the shared
zero/one scene arguments, the event-flag clear span at `$9C08..$9C87`, the
homesickness restriction flag `0x0049`, and the bicycle-state predicate used by
case `12`. The adjacent name-entry sources now name the `$9801/$97F5/$9C9F`
buffers, text-input window ids, and the `EAA6 -> EB4C` preview-entry handoff.
Case `11` now calls the existing `C1BE4D_AttemptHomesicknessResult` contract by
name, and the neighboring naming commit flow calls `C1E57F_RunTextInputDialog`
directly instead of the legacy local entry alias.

## Reference Corroboration

The community docs for `[1F 41 XX]` give this same high-level case list:

- `01/02`: coffee and tea scenes
- `03/04`: name-entry menus
- `05/06`: overworld status suppression set/clear behavior, with the same flag `49 00` caveat in case `06`
- `07`: town map
- `08`: action-user side check
- `09`: normal Sound Stone
- `0A`: title-screen still image
- `0B`: Cast scene
- `0C`: Credits/photos scene
- `0D/0E`: final-Magicant HP/PP meter randomization and reset
- `0F`: clear all event flags
- `10`: final Sound Stone
- `11`: attempt homesickness and return success
- `12`: kick Ness out of bicycle mode and return success

The C4 side of case `07` is documented in `notes/town-map-selection-rendering-c4d274-c4d744.md`; it derives the current town-map id from `$9877/$987B`, loads the matching map data, runs the interactive map display, and returns the one-based map id.

That gives `C1:BEFC` one of the stronger reference-backed identities in this bank strip.

## Neighbor Helpers

`C1:BCAB..BEFC` is now source-backed at `src/c1/c1_bcab_execute_teleport_destination.asm`, so the two neighbor helpers below are no longer byte-preserved.

`C1:BE4D` is the helper for case `0x11`.

It reads Ness's current level from `$99D3` and the first character status/class byte from `$99DC`, scans a small six-entry threshold table at `C4:5C8A`, checks each candidate through `C4:5F7B`, and calls `C4:58FE(A=1, X=6, Y=2)` when homesickness is successfully inflicted. It returns `1` only on that success path.

`C1:BEC6` is the named get-off-bicycle script wrapper. It opens/sets text context, displays text at `C7:C95E`, waits/closes through `C1:0084` and `C1:2DD5`, then calls the C0 bicycle-exit routine `C0:3CFD`.
