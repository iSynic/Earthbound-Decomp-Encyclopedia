# Sprite Pose Descriptor Cache (`2A06..2CD6`)

This note captures the current best local correction for the visual-state write path that seeds `2A06`, `29CA`, `2A42`, `2A7E`, `2ABA`, and `2CD6`.

See also [overlay-init-descriptor-fields.md](notes/overlay-init-descriptor-fields.md).
See also [entity-overlay-ram-block-layout.md](notes/entity-overlay-ram-block-layout.md).
See also [mushroomized-overlay-gate-words.md](notes/mushroomized-overlay-gate-words.md).
See also [secondary-visual-descriptor-c42b0d.md](notes/secondary-visual-descriptor-c42b0d.md).

## Main result

A useful correction finally clicked.

The write path that seeds `2A06`, `29CA`, `2A42`, `2A7E`, `2ABA`, and `2CD6` is not loading a tiny overlay-only descriptor. It is caching data from a richer sprite-pose descriptor family.

Two sources are involved:

- a per-entity pose descriptor at `[$23:$25]`
- a long-pointer table at `EF:133F` (`DATA_EF133F` in the legacy project), indexed by `$2B`

The strongest current local read is:

- `2ABA` = pose descriptor byte `+0`, used as a per-frame piece count
- `2A7E` = pose descriptor byte `+1`, shifted left once, used as the frame-record stride
- `2A42` = pose descriptor byte `+8`, used as the bank byte for the actual frame-record data
- `2CD6` = the selected pose-table index (`$2B`)
- `2A06` = the bank byte of the selected pose descriptor record from `EF:133F`
- `29CA` = low-word pointer to the directional frame-word list inside that pose descriptor, starting at descriptor offset `+9`

That is materially better than the earlier wording that treated `2CD6` as a generic overlay-family index.

## Local write chain

The clearest local write chain is the block reflected in the legacy disassembly around the `STA $2A7E,Y` / `STA $2ABA,Y` / `STA $2A42,Y` / `STA $2CD6,Y` / `STA $2A06,Y` / `STA $29CA,Y` cluster.

The sequence is:

1. Read byte `+1` from `[$23:$25]`, zero-extend it, `ASL`, and store it to `2A7E`.
2. Read byte `+0` from `[$23:$25]` and store it to `2ABA`.
3. Read byte `+8` from `[$23:$25]` and store it to `2A42`.
4. Use `$2B` to index `EF:133F` as a 4-byte long-pointer table.
5. Store `$2B` itself to `2CD6`.
6. Store the selected long pointer's bank byte to `2A06`.
7. Store the selected long pointer's low word plus `9` to `29CA`.

That is the strongest local proof so far that these fields belong to a cached pose-descriptor path.

## Why `+9` now makes sense

The earlier `29CA = pointer + 9` detail looked arbitrary until the pose-descriptor layout became visible.

The sampled pose descriptors in the legacy disassembly have this shape:

- bytes `+0..+7` = 8 one-byte header fields
- byte `+8` = bank for the frame-record data
- words starting at `+9` = directional / state frame-word list

So storing `descriptor_low_word + 9` into `29CA` is exactly what we would expect if later code needs to read the frame-word list directly.

That turns the old unexplained bias into a good structural clue.

## Why `EF:133F` now looks like a pose table

The local ROM bytes at `EF:133F` are clearly a 4-byte pointer table.

The legacy disassembly labels it `DATA_EF133F`, and the early entries point to:

- `EB_SpritePoseData_NessWalking`
- `EB_SpritePoseData_NessWalking`
- `EB_SpritePoseData_PaulaWalking`
- `EB_SpritePoseData_JeffWalking`
- `EB_SpritePoseData_PooWalking`

Later entries also include object/effect-style pose records such as:

- `EB_SpritePoseData_SweatDrops`
- `EB_SpritePoseData_Mushroom`
- `EB_SpritePoseData_SmallWaterRipples`
- `EB_SpritePoseData_BigWaterRipples`

So the safest current local statement is:

- `EF:133F` is a sprite-pose descriptor pointer table, not a tiny overlay-data table

## `2C22` now looks like a major visual-state selector

A useful side result surfaced from the `C07A56` setup path and the later refresh logic.

That setup path:

- writes caller-provided value `A` into `2C22`
- updates flags in `1002`
- then leaves the rest of the visual refresh to the normal `A780/A794` path

Later, `C0:A6E3` does:

- `LDA $2C22,X`
- `XBA`
- `ORA $2AF6,X`
- `CMP $3456,X`

and only refreshes the visual state if that combined word changed.

So the safest current statement is:

- `2AF6` is the low-byte pose/frame selector we were already following
- `2C22` is a higher-level visual-state selector packed into the high byte of the same cached fingerprint
- `3456` is best read as a cached visual fingerprint word, not just a random scratch compare value

That makes `2C22` look much more like a major animation/variant selector than any kind of body-divide count.

## `2C22` is caller-driven, not pose-derived

The first useful caller samples sharpen that further.

At several call sites, `C07A56` is fed like this:

- `A` comes from per-entity or caller-side tables such as `0E5E,X`
- `X` comes from a pose/sprite-table lookup
- `Y` carries the target entity index

That means `2C22` is not simply another byte copied out of the pose descriptor itself.

So the safest current statement is:

- the pose descriptor family provides the low-level piece/frame data
- `2C22` is a caller-selected higher-level display variant layered on top of that pose family

That is a better fit for the later `2C22:2AF6 -> 3456` fingerprint compare.

## What this changes

This corrects a few earlier phrases.

- `2CD6` is better read as a pose-table index than a generic overlay-family index.
- `2A06` is better read as the bank byte of the pose descriptor record, not the bank byte of the final frame data.
- `29CA` is better read as the cached low-word pointer to the pose descriptor's frame-word list.
- `2A42` remains the bank byte of the actual frame-record data, but now that comes from pose descriptor byte `+8` explicitly.
- `2C22` is better read as a major visual-state selector than as a geometry or overlay parameter.
- `3456` is better read as a cached visual fingerprint word.

## What still remains open

A few header/state bytes still need names.

- pose descriptor bytes `+2..+7` are not fully pinned yet
- nearby arrays like `2B6E`, `3366`, `33A2`, `33DE`, and `1A4A` clearly receive more of this header/state, but their exact semantic names still need care
- the broad `0x3C`-stride RAM block still exists, but its exact one-to-one mapping to the `ebsrc` overlay arrays should now be treated more cautiously
- the exact symbolic meaning of `2C22`'s selector values is still open

## Best next target

The best next move is to decode what concrete variant family `2C22` is selecting at those call sites. That should let us describe how the generic pose-descriptor cache feeds later state-driven display variants without mixing the layers together.

## Update: `2C22` is now a row selector, not a final pose id

The current best follow-up is in [visual-selector-family-c0780f-c3f2b5.md](notes/visual-selector-family-c0780f-c3f2b5.md).

The useful correction is that `2C22` and the persistent per-entity field `0E5E` now look like the same higher-level visual selector family. `C0780F` resolves that selector through an 8-entry row in `C3:F2B5`, using a smaller local bucket state to choose the final pose-table index. That means `2C22` is best read as a visual-selector row id or pose-family selector, while `2AF6` remains the lower-level per-family pose/frame selector already feeding the `3456` cached fingerprint.
