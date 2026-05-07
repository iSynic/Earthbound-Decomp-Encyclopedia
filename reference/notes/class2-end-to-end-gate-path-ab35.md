# Class2 End-To-End Gate Path AB35

This note captures the current ROM-first picture of one full descriptor-consumer path: the gate family rooted around `C2:AB35`.

See also `notes/class2-record-consumer-families.md`.

## Why this path matters

Among the known descriptor-consumer families, the `AB35` path is one of the clearest because it does not stop at field checks. It eventually bottoms out in concrete script-dispatch behavior.

That makes it a better first end-to-end anchor than the noisier `C2:5540` family.

## Current high-level flow

Current safest reading:

1. scan the active candidate pool rooted at `7E:9FAC`
2. keep only entries whose local runtime metadata passes a narrow gate
3. require the descriptor's `+0x56` byte to be nonzero
4. compare a signed or centered byte derived through bank `D5` data against a local threshold-style value
5. if the gate passes, dispatch one of several hardcoded script paths through `C1:DC1C`
6. continue with local slot or state updates in the `72xx/73xx` helper family

## Candidate scan and gate

The scan rooted at `C2:AB14` walks the 32 candidate rows at `9FAC + 0x4E * n`.

The strongest current local gates are:

- candidate row `+0x0C` must be nonzero
- candidate row `+0x0E` must equal `1`
- descriptor byte `D5:9589 + 0x56` must be nonzero

That makes this path look like a filtered subset of active descriptors rather than a global unconditional dispatcher.

## Descriptor-side comparison step

After the `+0x56` gate, the path uses additional data derived from the descriptor-linked domain:

- it maps through bank `D5` again using selector `#$0027`
- it reads byte `D5:5000 + 0x1F` for the selected value family
- it converts that byte through a centered or signed comparison shape
- it compares the result against a local threshold-style value produced through
  `C2:6A2D` / `GetRandomBelow`

The exact gameplay meaning of that comparison is still open, but structurally it looks like a position, distance, or band-pass style test rather than a plain id lookup.

## Concrete script dispatch outcome

When the path succeeds, it clearly enters scripted presentation behavior.

Known concrete calls include hardcoded script pointers through `C1:DC1C` with addresses in bank `C9`, including:

- `C9:FE41`
- `C9:FE9D`
- `C9:FEE3`

That is the strongest current evidence that this descriptor family can drive direct text or scripted interaction outcomes, not just ranking and background state.

## What this path suggests about the record family

This one path supports a stronger subsystem interpretation than the field map alone:

- descriptors are scanned from the active `9F8C`-backed pool
- descriptor tail bytes like `+0x56` act as eligibility controls
- descriptor-linked `D5` bytes help shape a threshold or comparison test
- success leads to explicit script dispatch, not only hidden state updates

So at least one major consumer family uses the `D5:9589` records as script-bearing interaction descriptors.

## What is still unresolved

Still open:

- what real gameplay condition the `D5:5000 + 0x1F` comparison represents
- whether the `+0x56` gate corresponds to a specific object class, interaction type, or encounter mode
- how this `AB35` path relates to the sibling `C2:5540` gate family that appears to rank and select before a similar follow-up stage

## Current safest takeaway

The safest current takeaway is:

- `AB35` is a real end-to-end descriptor path
- it filters candidate descriptors using both runtime state and descriptor-side control bytes
- it culminates in hardcoded script dispatch through `C1:DC1C`

That is enough to say the class-`2` descriptor system is tied directly to scripted interaction behavior.

## Best next target

- trace the sibling gate family rooted at `C2:5540` and see whether it converges on the same `C1:DC1C` script-dispatch stage or on a different presentation path.
