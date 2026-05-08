# Class2 End-To-End Gate Path 5540

This note captures the current ROM-first picture of the sibling descriptor-consumer path rooted around `C2:5540`.

See also `notes/class2-end-to-end-gate-path-ab35.md`.
See also `notes/class2-record-consumer-families.md`.

## Why this path matters

The `5540` family appears to be the heavier sibling of `AB35`.

Where `AB35` looks like a relatively direct gate-to-script path, `5540` looks more like a multi-stage selection and presentation controller:

- it scans candidate descriptors
- it ranks or filters them using descriptor bytes and local runtime metadata
- it emits several hardcoded script calls through `C1:DC1C`
- it continues into local state and slot-management helpers instead of ending immediately

## Current high-level flow

Current safest reading:

1. scan the active candidate rows at `9FAC + 0x4E * n`
2. require a narrow combination of candidate-row state and descriptor byte `+0x56`
3. keep the best candidate according to a small score-like comparison
4. branch into one of at least two immediate hardcoded script outcomes through `C1:DC1C`
5. if the path continues, move into a second-stage selector that writes the chosen row into `$A970`
6. drive additional local state transitions, script dispatch, and follow-up helper families in the `44xx/47xx/6Axx/72xx/73xx` regions, including a collapse or affliction-handling startup path

## Candidate scan and scoring stage

The early scan around `C2:5510` through `55B0` looks like a scored filter over the active descriptor-backed rows.

The strongest current local gates are:

- candidate row `+0x0C` must be nonzero
- candidate row `+0x0F` must be zero
- candidate row `+0x0E` must equal `1`
- descriptor byte `D5:9589 + 0x56` must be nonzero

The path then compares candidate-row values like `+0x1D`, `+0x1F`, and `+0x2A` and keeps best-so-far values in locals such as `$04`, `$1B`, and `$21`.

That makes this first stage look like a real best-candidate search, not just a yes-or-no gate.

## Early hardcoded script outcomes

After the first scoring stage, the path can already emit explicit script calls through `C1:DC1C`.

Known examples include hardcoded script pointers in bank `EF`, including:

- `EF:84F3`
- `EF:8511`

These appear before the deeper second-stage controller, which suggests they are immediate feedback or presentation outcomes of the early gate.

## Second-stage selector and chosen-row state

If the early stage does not terminate, the path continues through helpers such as:

- `C2:BB18`
- `C2:BAC5`
- `C1:DD53`

The strongest current structural result is that the chosen row gets written to `$A970`, and subsequent logic treats that as the active working row for follow-up behavior.

This is the clearest sign that `5540` is not a one-shot script gate. It promotes a selected descriptor-backed battler row into a deeper local controller path, and the newer `BB18/7550` evidence suggests that path is at least partly collapse- or affliction-oriented rather than a neutral generic controller.

## Deeper follow-up behavior

Later parts of the path branch through multiple local controller families, including:

- `C2:4477`
- `C2:4703`
- `C2:6A2D`
- `C2:7250` / `C2:7294` / `C2:7318`

It also continues to emit hardcoded `C1:DC1C` script calls from several points, including script addresses in banks `EF` and `7x` regions.

The exact meaning of each branch is still open, but the overall pattern is clear: this is a staged controller that alternates between descriptor-driven decisions and explicit presentation or scripted outcomes.

## Comparison with `AB35`

The two end-to-end paths now look related but distinct.

`AB35`:

- narrower gate
- simpler descriptor-side threshold test
- quick arrival at hardcoded script dispatch

`5540`:

- wider best-candidate scan
- explicit best-so-far comparison state
- early script feedback plus a deeper selected-row controller
- more evidence of slot or phase management after selection

So the safest current reading is that `5540` is the heavier interactive controller, while `AB35` is a simpler descriptor-trigger path.

## Current safest takeaway

The safest current takeaway is:

- `5540` is a second real end-to-end descriptor path
- it uses descriptor byte `+0x56` as one gate among several local runtime filters
- it performs a best-candidate style scan rather than a simple accept or reject test
- it can emit immediate scripts through `C1:DC1C`
- it also promotes a chosen battler row into deeper local controller state, with the best current evidence pointing toward collapse or affliction handling in at least one major branch

That strengthens the broader interpretation that the `D5:9589` records are interaction descriptors feeding a full presentation and control pipeline.

## What is still unresolved

Still open:

- the exact gameplay meaning of the best-candidate score built from row fields like `+0x1D`, `+0x1F`, and `+0x2A`
- the detailed post-selection controller phases that run after `$A970` is established, especially how much of that path should now be described as collapse or affliction handling
- whether the early `EF:84F3` / `EF:8511` scripts are failure, warning, staging, or success outcomes

## Best next target

- See `notes/class2-second-stage-selector-a970.md` for the selector layer. The best next move is to trace the controller phases that run after `$A970` is set, especially the branches keyed by row fields `+1D`, `+1E`, `+1F`, `+20`, and `+23`.
