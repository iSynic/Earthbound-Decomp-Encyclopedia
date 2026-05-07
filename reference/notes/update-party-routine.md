# UPDATE_PARTY

`UPDATE_PARTY` is at `C0:34D6` in the local scaffold:

- source: `src/c0/c0_34d6_sort_and_export_mushroomized_walking_entries.asm`
- alias: `C034D6_SortAndExport_MushroomizedWalkingEntries`

Despite the broad name, it does not primarily copy battle HP/PP back to the
character structs. In `CHECK_DEAD_PLAYERS`, that copy happens before the call.
`UPDATE_PARTY` then rebuilds/export-sorts the overworld party bookkeeping from
the current party member list and character affliction state.

Main effects visible in the routine:

- reads party count from `$98A3` (`game_state::party_count`)
- walks the current party member IDs from the `$9891` region
- checks each character's affliction/status bytes in `PARTY_CHARACTERS`
- builds sort keys that push certain status/object classes later in the list
- sorts the party-related arrays
- exports the sorted records back into `$988B`, `$9891`, `$9897`
- updates `$9889` from the first sorted `$9897` entry
- refreshes dependent overworld systems via `$C032EC`, `$C02C3E`, and
  `C47F87_RefreshWindowFlavorPalette`

In `CHECK_DEAD_PLAYERS`, the call at the end of each player-battler pass is
there so that once the battle-side HP/PP/afflictions have been synchronized back
to `PARTY_CHARACTERS`, the overworld party order/leader metadata is immediately
rebuilt to reflect dead/unconscious/statused party members.

This matters for hacks that use "party position 1" as a text argument: after a
death/status update, `UPDATE_PARTY` may have rebuilt which character is treated
as the first/leading overworld party member. That is still "first after the
party refresh," not literally "last character who died."
