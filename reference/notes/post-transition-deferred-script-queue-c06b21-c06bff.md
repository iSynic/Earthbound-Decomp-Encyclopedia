# Post-Transition Deferred Script Queue (`C06B21`, `C06B3D`, `C06BFF`)

This note tightens one of the weaker spots around the `D5:F645` delivery-table work: how deferred script pointers survive and resume around transitions.

## Working Names

- `C0:6B21` = `RunPostTransitionScriptHookAndSelectorPass`
- `C0:6B3D` = `PreserveDeferredScriptPointersAcrossTransition`
- `C0:6BFF` = `RunDeferredScriptPointerAndRefreshTransitionState`

## Core picture

The block around `C06B21`, `C06B3D`, and `C06BFF` now looks much more like a post-transition deferred script subsystem than a movement-only helper family.

The strongest current local read is:

- queue type `#$0002` = pointer payload routed into `C06BFF`
- queue type `#$000A` = pointer payload routed through `C10004` and preserved across transition-side processing
- `C06B21` = shared post-transition hook that runs a fixed Andonuts-scene script and then the `D5:F645` selector-table pass

## `C06B21`: post-transition hook plus selector-table pass

`C06B21` does exactly two things:

1. run fixed script `C5:EA35` through `EB_ProcessTextboxData_Main`
2. call `EF:0EE8`

That matches the earlier scene anchor:

- the fixed script aligns with `EEVENT5::_DKFD_END_ANDONUT_3_NO`
- `EF:0EE8` then scans the 10-entry `D5:F645` table and seeds `0A38`

So `C06B21` still looks best as a shared post-transition or post-setup hook, not a delivery-only helper.

## `C06BFF`: pointer-driven script runner with transition follow-up

`C06BFF` starts from the far pointer in `$28/$2A`, resolves and executes it through `C10004`, then performs a larger transition/setup sequence.

The important local anchors are:

- `C10004` is the immediate far-pointer script dispatch step.
- after that dispatch, the routine clears `5DAA` and `5DA8`.
- it performs flag-membership checks through `C21628`.
- it refreshes transition/traversal state through helpers like `C068F4`, `C013F6`, `C03FA9`, and `C069AF`.
- near the end, it calls `C065A3`, then `C06B21`, and finally clears `5DC2`.

So `C06BFF` is no longer best read as a plain script executor. It looks like a pointer-driven transition script runner with explicit post-script world-state refresh and post-transition hook processing.

## `C06B3D`: preserve queued type-`#$000A` pointers across the transition path

The adjacent helper `C06B3D` scans the 4-entry WRAM queue for entries of type `#$000A`.

For each matching entry:

- it pulls the payload pointer via `C0654E`
- stores the pointer into a temporary 4-entry buffer at `5E58`
- advances the queue read index while scanning

After the scan:

- it null-terminates the temporary buffer
- walks that buffer
- re-enqueues each saved pointer as queue type `#$000A` via `C064E3`

That is a strong local match for “preserve deferred script-pointer entries across a transition-side queue drain.”

## Type `#$000A` is now better read as a deferred script-pointer class

The older note in `staged-movement-queue.md` treated type `#$000A` as just another queue subtype that happened to call `C10004`.

The newer local picture is stronger than that:

- `C06B3D` treats type `#$000A` entries as raw far pointers worth saving and restoring.
- `C06BFF` is a pointer-driven script runner.
- `C0:DCF8` explicitly enqueues `DATA_C7D33E` as type `#$000A` when several global conditions are satisfied, then sets `9E56 = 1`.
- `C7:D33E` is a real phone/text-side script, not movement data.

So the safest current reinterpretation is:

- queue type `#$000A` = deferred far script pointer

That is still cautious, but it is materially better than the older movement-centric wording.

## How this fits the delivery-table work

This does not yet prove that the `D5:F645` script-pointer pairs are fed through queue type `#$000A`.

But it does give a much healthier runtime model for how service- or event-style script pointers can be deferred across transitions:

- pointer payload is queued
- transition-side script runner executes and refreshes world state
- type-`#$000A` deferred script pointers are preserved
- post-transition hook `C06B21` runs, including the `D5:F645` selector-table pass

So the delivery-table side and the deferred-script-queue side are now plausibly adjacent runtime families, even though the exact direct bridge is still unpinned.

## Best next target

- Trace additional producers of queue type `#$000A`, especially the ones outside `C0:DCF8`, and see whether any of them recover or derive pointers from the `D5:F645` delivery table.

## Stronger producer-side constraint for type `#$000A`

A pass over the apparent `#$000A` sites separated the real queue producers from unrelated counter logic.

The important correction is that most literal `#$000A` loads in the wider codebase are **not** queue producers at all. For the shared WRAM queue, the currently pinned type-`#$000A` producers are narrow:

- `C06B3D` re-enqueues preserved deferred pointers as type `#$000A`
- `C0:DCF8` enqueues `DATA_C7D33E` as type `#$000A`

By contrast, many other `#$000A` literals are just local bounds, counters, or non-queue selector values.

So the current safest producer-side summary is:

- type `#$000A` is not a broadly emitted general-purpose queue type
- it is a relatively specialized deferred-script-pointer class

## A useful queue-family split

The real queue call sites now support a cleaner split:

- type `#$0000` and `#$0002` are produced by the movement-trigger helpers around `C06A1B` / `C06ACA`
- type `#$0009` is produced by `C07443` from a neighboring pointer-table family
- type `#$000A` is produced by the deferred-script side (`C06B3D`, `C0:DCF8`)

That makes the old "movement queue" label too broad for the whole `$5DEA` family.

The stronger current read is:

- a shared 4-entry deferred-action / deferred-pointer queue
- used by both movement-transition helpers and deferred script pointers

## `C06BFF` and `C06B3D` fit together cleanly now

This producer pass also strengthens the local runtime story:

- `C06BFF` runs a far pointer through `C10004`, refreshes world/transition state, then calls `C06B21`
- `C06B3D` preserves only type-`#$000A` entries across that path
- `C06B21` then runs the fixed post-transition script hook and the `D5:F645` selector-table scan

So the deferred-script queue interpretation is no longer just based on one odd consumer. It now has a narrow and coherent producer set too.
