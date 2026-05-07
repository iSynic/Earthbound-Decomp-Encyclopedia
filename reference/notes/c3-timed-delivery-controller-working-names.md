# C3 timed-delivery controller working-name promotion

## Purpose

This note promotes the C3-side labels inside the shared `499+500_common` timed-delivery event script. The EF helper notes already explain the table fields and state helpers; this pass keeps the C3 names at the event-script phase level.

References:

- `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/499+500_common.asm`
- `notes/timed-delivery-controller-499-500-common.md`
- `notes/delivery-row-helpers-ef0e67-ef0ead.md`
- `notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md`
- `notes/selector-row-config-family-ef0ee8.md`

## Controller phase labels

`EVENT_499_500_COMMON` starts with the primary one-second countdown loop seeded by `EF:0D46` in the entry wrappers. The first internal branch at `C3:443E` is the retry path: it asks `EF:0CA7` whether the row-specific retry threshold has been reached, waits for the row-specific `EF:0D23` retry delay when it has not, and returns to the readiness gate.

`C3:444D` is the readiness gate over `EF:0F60`. A true result enters the success path at `C3:4457`; a false result jumps back to the retry path at `C3:443E`.

`C3:4457` is the success-side gate/setup block. It still has two broader engine guards (`C2:FF9A` and `C0:C19B`) before committing to arrival handling. Once those pass, it starts the arrival movement task, arms timed-delivery success state through `EF:0FDB`, prepares the actor for presentation, queues delivery pointer 1 through `EF:0D8D`, then enters the departure movement phase.

`C3:447D` is the failure-side teardown branch. It runs `EF:0FF6`, queues delivery pointer 2 through `EF:0DFA`, and exits through the shared event tail.

## Movement and presentation subphases

`C3:447A` is the tiny task entry that shortcalls the arrival movement phase at `C3:44DE`.

`C3:4488` prepares the delivery actor for visible movement: set animation `0`, start the walking-animation pulse task at `C3:A09F`, refresh the slot visual profile, and seed action-script variables `V2` and `V3` to `#$0016`. Its loop at `C3:4499` waits on `V4` and repeatedly calls the C4-side helper until the prep phase is complete; `C3:44A7` is the local return point.

`C3:44A8` is the departure movement phase. It stops velocity, ends the active tasks, starts `C3:43DB`, optionally applies the row's exit speed through `EF:0E8A` and `C0:A685`, loops movement/visual updates at `C3:44C1`, then finishes at `C3:44D2` by stopping velocity, resetting timed-delivery state with `EF:0FF6`, and yielding to text.

`C3:44DE` is the arrival movement phase. It applies the row's enter speed through `EF:0E67` and `C0:A685`, clears `V4`, loops movement/visual updates at `C3:44EE`, then sets `V4 = 1` at `C3:44FF` and holds there. That makes `C3:44FF` the completion hold for the concurrently started arrival task.

## Source-form pilot

The controller proper is now emitted as a C3 event/actionscript source-form
pilot:

- generator: `tools/build_c3_event_script_source_pilot.py --family timed-delivery-controller`
- source: `src/c3/event_scripts/timed_delivery_controller.asar.asm`
- report: `notes/c3-timed-delivery-source-pilot.md`

The pilot covers `C3:43DB..C3:4508`: the departure pulse task, event `499` and
`500` setup paths, the shared countdown/retry/readiness loop, success/failure
branches, and the paired arrival/departure movement loops. The adjacent
`C3:4508..C3:48C4` service-event movement scripts now have their own follow-up
pilot in `notes/c3-service-event-movement-source-pilot.md`.

## Placeholder table

`C3:FDBD` is a four-word fallback descriptor table:

```text
0037 004E 004F 0034
```

Both `EF:0EAD` and `EF:0EE8` use it when a delivery row's sprite/object descriptor id is zero. They call `C0:8E9A`, mask the result with `#0003`, and index this table before calling `C0:1E49`.

## Working Names

- `C3:443E` = `TimedDeliveryRetryWaitLoop`
- `C3:444D` = `TimedDeliveryReadinessGate`
- `C3:4457` = `TimedDeliverySuccessGateAndPresentationSetup`
- `C3:447A` = `StartTimedDeliveryArrivalMovementTask`
- `C3:447D` = `TimedDeliveryFailureTeardown`
- `C3:4488` = `PrepareTimedDeliveryActorForPresentation`
- `C3:4499` = `WaitTimedDeliveryActorPresentationPrep`
- `C3:44A7` = `ReturnFromTimedDeliveryActorPrep`
- `C3:44A8` = `RunTimedDeliveryDepartureMovement`
- `C3:44C1` = `LoopTimedDeliveryDepartureMovement`
- `C3:44D2` = `FinishTimedDeliveryDepartureAndYieldText`
- `C3:44DE` = `RunTimedDeliveryArrivalMovement`
- `C3:44EE` = `LoopTimedDeliveryArrivalMovement`
- `C3:44FF` = `HoldTimedDeliveryArrivalCompletion`
- `C3:FDBD` = `DeliveryPlaceholderSpriteTable`

## Remaining questions

- `C3:43DB` is adjacent to the departure movement path and should be handled in a neighboring movement-task pass rather than folded into the timed-delivery note.
- The C4 helpers used by the prep and movement loops are still named from call shape only. Their precise visual/update contracts belong in a later C4 pass.
