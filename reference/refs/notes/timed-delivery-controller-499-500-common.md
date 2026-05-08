# Timed Delivery Controller (`499+500_common`)

This note summarizes the current local read of the shared service-event script at [499+500_common.asm](/F:/Earthbound%20Decomp%20-%20Codex/refs/ebsrc-main/ebsrc-main/src/data/events/scripts/499+500_common.asm).

See also [delivery-row-helpers-ef0e67-ef0ead.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/delivery-row-helpers-ef0e67-ef0ead.md).
See also [selector-row-config-family-ef0ee8.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/selector-row-config-family-ef0ee8.md).
See also [timed-delivery-state-helpers-ef0f60-fdb-ff6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md).
See also [timed-delivery-row-index-command-1f-d3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-row-index-command-1f-d3.md).

## Main result

The shared `499+500_common` event script now reads like a real timed-delivery controller for the `D5:F645` table, not just a generic service-event loop.

The local bridge from the bank-`01` text-command side is stronger now too: the `0x1F D3` leaf returns callback low word `C1:7440`, and `C1:7440` immediately forwards `X` into `EF:0EAD`. That gives the timed-delivery controller a direct ROM-level callback link from the deferred text-event machinery into the delivery-row helper family.

The broad shape is:

1. seed a delivery countdown
2. wait for that countdown to expire
3. test a readiness condition
4. if not ready, retry on a bounded wait loop
5. on success, queue the immediate success pointer and run the arrival movement
6. on failure, queue the deferred failure pointer and tear the service state down

## Entry-side setup

The wrapper script [499.asm](/F:/Earthbound%20Decomp%20-%20Codex/refs/ebsrc-main/ebsrc-main/src/data/events/scripts/499.asm) calls `EVENT_UNKNOWN_EF0D46` during setup.

That helper seeds the per-row countdown from `D5:F645` record word `4`, so the row-specific `delivery_time` is part of the controller from the start.

## Phase 1: delivery countdown

The common script begins:

1. `EVENT_PAUSE 1*SECOND`
2. `EVENT_UNKNOWN_EF0D73`
3. loop back until that helper returns zero / false

Since `EF:0D73` decrements the row-local `B525` countdown seeded by `EF:0D46`, this is now a strong local match for the primary delivery wait timer.

## Phase 2: readiness test

After the countdown, the script reaches `UNKNOWN_C3444D` and calls `EVENT_UNKNOWN_EF0F60`.

The current safest read for `EF:0F60` is:

- it is the delivery/service readiness predicate for this controller family

The helper clearly returns a boolean, but its internals still mix delivery-local state with broader world, controller, and presentation busy state, so some exact variable names should stay tentative for now.

## Phase 3: bounded retry loop

If `EF:0F60` does **not** take the success branch, the script falls into `UNKNOWN_C3443E`:

1. `EVENT_UNKNOWN_EF0CA7`
2. if that threshold helper says the limit has been reached, branch out to the failure path
3. otherwise `EVENT_UNKNOWN_EF0D23`
4. `EVENT_LOOP_TEMPVAR` with `EVENT_PAUSE 1*SECOND`
5. then jump back to the readiness test

That is the key proof for the middle table fields:

- record word `2` = retry-attempt threshold
- record word `3` = retry wait in seconds

So the common script is doing exactly what the data suggests: try again after a row-specific wait, but only up to a row-specific retry limit.

## Success branch

If the readiness predicate succeeds, the script enters `UNKNOWN_C34457` and then:

- runs `EVENT_UNKNOWN_EF0FDB`
- queues pointer `1` through `EVENT_UNKNOWN_EF0D8D`
- enters the arrival/approach movement branch using `EVENT_UNKNOWN_EF0E67`

The important runtime detail is that pointer `1` is queued as type `#$0008`, and the shared queue consumer at `C0:75DD` handles type `8` through the direct `JSL $C10004` pointer-dispatch path.

That makes the strongest current read:

- `EF:0FDB` = begin success-side delivery/service state
- `EF:0D8D` = queue the immediate success-side text or presentation pointer from `D5:F645`
- `EF:0E67` = fetch the arrival-side movement speed

## Failure / teardown branch

If the readiness loop gives up, the script reaches `UNKNOWN_C3447D` and then:

- runs `EVENT_UNKNOWN_EF0FF6`
- queues pointer `2` through `EVENT_UNKNOWN_EF0DFA`
- exits through the common event tail

Here the queue type matters just as much: pointer `2` is queued as type `#$000A`, and that queue class now reads best as the shared deferred far-script-pointer family preserved and resumed around transitions.

So the strongest current read is:

- `EF:0FF6` = begin failure-side teardown / reset state
- `EF:0DFA` = queue the deferred failure-side or retry-over pointer from `D5:F645`

That gives the pointer pair a much more concrete split than before:

- pointer `1` = immediate success-side text/presentation pointer
- pointer `2` = deferred failure-side follow-up pointer

## Movement pair

The movement side now fits the branch split neatly:

- `EF:0E67` supplies record word `8` for the arrival-side movement branch
- `EF:0E8A` supplies record word `9` for the departure-side movement branch

So the trailing table pair still reads best as:

- word `8` = `enter_speed`
- word `9` = `exit_speed`

## Data-side cross-check

The third reference project at [timed_delivery_table.yml](/F:/Earthbound%20Decomp%20-%20Codex/refs/eb-decompile-4ef92/timed_delivery_table.yml) lines up well with the local controller picture.

Its exposed fields already match:

- event flag
- sprite group / descriptor id domain
- timer
- success pointer
- failure pointer

And its two remaining anonymous byte groups map neatly onto the locally decoded words:

- `Unknown = 6,0,15,0` matches the common `word2 = 6`, `word3 = 15` rows
- `Unknown2 = 128,1,128,1` matches the common `word8 = 0x0180`, `word9 = 0x0180` rows

So the external data dump is a useful confirmation of the local struct sketch, not just a parallel guess.

## Current best full struct sketch

For the shared timed-delivery rows in `D5:F645`, the best current local sketch is:

- word `0` = sprite/object descriptor id
- word `1` = event-flag gate
- word `2` = retry threshold
- word `3` = retry wait in seconds
- word `4` = delivery countdown
- pointer `1` = immediate success-side text/presentation pointer
- pointer `2` = deferred failure-side follow-up pointer
- word `8` = enter speed
- word `9` = exit speed

That is a much stronger end-to-end interpretation than the earlier "service-flavored table with several unresolved scalars" wording.


