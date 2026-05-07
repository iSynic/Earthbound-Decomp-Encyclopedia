# C4 Party State Reset And Callback Tables `C4:30EC-C4:3317`

## Scope

This note covers the setup cluster after the visual descriptor tables and before the menu/text helper run. The reference include map already gives one strong clue: `C4:30EC` sits under `overworld/set_party_tick_callbacks.asm`, while `C4:32B1` and `C4:3317` remain generic unknown chunks.

The local code makes the cluster read as early party/runtime setup:

- `C4:30EC` initializes per-party callback/vector tables from compact C3 data.
- `C4:32B1` clears per-slot visual masks and party-character state bytes.
- `C4:3317` rebuilds a six-entry pointer table to `$99CE + n * #$005F` records.
- `C4:3344`, immediately after this setup cluster, is the tiny setter for the shared `$5D98` restriction/status latch used by text command `[1F 41]` cases `05/06`.

## `C4:30EC` callback/vector table initializer

Direct caller:

- `C0:2D7E`, immediately after clearing `$98A4/$98A3`

The routine loops 14 entries. For each entry it reads two 4-byte vector-like records from:

- `C3:E0BC`
- `C3:E0F4`

Then it writes signed and negated variants into several 32-byte-spaced table families rooted around:

- `$4DD6`
- `$4DDE`
- `$4DE2`
- `$4DE6`
- `$4DEA`
- `$4DEE`
- `$4DF2`
- `$4F96`
- `$4F9A`
- `$4F9E`
- `$4FA2`
- `$4FA6`
- `$4FAA`
- `$4FAE`
- `$4FB2`

The safest local wording is that this builds per-party tick/callback vector tables, likely movement/update deltas or callback parameter pairs. The exact field names inside the target tables remain open, but the table-writing shape is no longer opaque.

## `C4:32B1` party visual/status reset

Direct callers:

- `C0:B553`, in a file-select/display initialization path
- `C4:DAF4`, in another broader C4 reset/setup path

The routine first clears `$2BAA` for 30 word-indexed slots:

```text
for i in 0..29:
    $2BAA[i] = 0
```

Then it clears seven bytes at `$99DC + character_index * #$005F` for six party-character records. `C0:329F` has the same byte span pattern for a single character, and the local C0 notes identify `$99DC + 0..6` as a compact affliction/status/state byte family.

Finally it clears byte `$9840`.

So the strongest local read is:

- clear per-slot visual/footprint mask state
- clear the six party records' seven-byte status/affliction family
- clear the global `$9840` gate/flag

## `C4:3317` party record pointer table rebuild

Direct caller:

- `C0:B7E0`, at the start of a broader party/menu refresh path

The routine loops six entries. For each index it multiplies by stride `#$005F` through `C0:8FF7`, adds `$99CE`, and stores that word into `$4DC8 + index*2`.

That makes `$4DC8` a compact table of party-character record base pointers for this path:

```text
$4DC8[i] = $99CE + i * #$005F
```

Other notes have seen `$4DC8` used in object/party-facing lookup paths; this routine pins one setup-time identity for the table as a six-entry pointer cache into the party-character record area.

## `C4:3344` `$5D98` latch setter

Direct callers:

- `C1:BFBC`, text command `[1F 41 05]`, with `A = 1`
- `C1:BFCA`, text command `[1F 41 06]`, with `A = eventFlag(0x0049)`

The body is intentionally tiny:

```text
REP #$31
STA $5D98
RTL
```

The surrounding notes give `$5D98` a broader identity than a local text flag:

- `notes/text-command-1f41-special-event-dispatch-c1befc.md` identifies cases `05/06` as the status-suppression special events.
- `notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md` shows timed-delivery and service/pending-arrival logic preserving or testing `$5D98`.
- `C2:0000` branches away from one special controller family when `$5D98 != 0`.

So the safest local name is a mechanical setter for the shared special-event/status restriction latch rather than a delivery-only or menu-only helper.

## Working Names

- `C4:30EC` = `InitializePartyTickCallbackTables`
- `C4:32B1` = `ResetPartyVisualMasksAndStatusBytes`
- `C4:3317` = `RebuildPartyCharacterRecordPointerTable4dc8`
- `C4:3344` = `SetSpecialEventRestrictionLatch5d98`

## Confidence boundaries

### Locally proved

- `C4:30EC` writes a 14-entry family of paired/negated vector values into `$4DD6..4FB2`
- `C4:32B1` clears `$2BAA` across 30 slots, clears seven bytes in each of six `$99CE`-stride records, and clears `$9840`
- `C4:3317` writes six `$99CE + index * #$005F` base pointers into `$4DC8`
- `C4:3344` only stores caller `A` into `$5D98`

### Still open

- exact field names for the `$4DD6..4FB2` target tables
- exact global meaning of `$9840`, though surrounding notes already show it acts as a runtime gate in movement/teleport/display contexts
- whether `$4DC8` should ultimately be named as a party-character-record pointer table globally or as a broader party/object pointer cache with multiple setup modes
- final global name for `$5D98`; "special-event restriction latch" is intentionally conservative
