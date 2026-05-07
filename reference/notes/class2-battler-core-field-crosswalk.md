# Class2 Battler Core Field Crosswalk

This note extends the earlier affliction-only battler comparison into the lower row fields that have been surfacing in the local battle-text and selected-row controller work.

See also [class2-battler-affliction-crosswalk.md](notes/class2-battler-affliction-crosswalk.md).
See also [class2-battlers-table-layout-9f8a-9fac.md](notes/class2-battlers-table-layout-9f8a-9fac.md).
See also [class2-concrete-battle-text-call-paths.md](notes/class2-concrete-battle-text-call-paths.md).
See also [class2-psi-thunder-reflection-branch.md](notes/class2-psi-thunder-reflection-branch.md).
See also [class2-reflected-hit-side-buffer-flags.md](notes/class2-reflected-hit-side-buffer-flags.md).

## Main result

The lower row fields are no longer all equally speculative.

Current safest local read:

- row byte `+0x0C` behaves strongly like `battler::consciousness`
- row byte `+0x10` behaves strongly like `battler::row` in the Thunder reflection branch
- row byte `+0x0B` still looks like an article or name-formatting flag that fits `battler::the_flag`, but that match is narrower than the other two

The new structural point is important: the row family is no longer just battler-layout-compatible in the abstract. The reference `battler` size is exactly `0x4E`, which matches the local `9FAC + 0x4E * n` table exactly. So these field matches now sit inside a battler-sized WRAM region, not just an offset-compatible one.

## Reference battler layout

From the `ebsrc` `battler` struct:

- `battler::the_flag` is at `+0x0B`
- `battler::consciousness` is at `+0x0C`
- `battler::row` is at `+0x10`
- `battler::afflictions` starts at `+0x1D`
- `.SIZEOF(battler) = 78 = 0x4E`

The affliction part of that layout was already pinned down by the `C2:4F62+` status-announcement path. The question here is whether the lower fields keep fitting. The exact `0x4E` stride match now says they live in the right-sized region too.

## `+0x0C` now looks strongly like `battler::consciousness`

This is the strongest of the three lower-field matches.

Reference-side behavior:

- `TARGET_ROW` first checks `battler::consciousness` and skips unconscious battlers entirely
- `RENDER_BATTLE_SPRITE_ROW` first checks `battler::consciousness` and skips battlers that are not active
- many other battle helpers in `ebsrc` use `battler::consciousness` as the simple "is this battler currently present/active" gate

Local-side behavior already established in our notes:

- the heavy `C2:5540` scan requires candidate row `+0x0C` to be nonzero before the row can participate in scoring
- the `C2:7294` and `C2:7318` controller helpers require selected-row byte `+0x0C == 1`
- multiple later controller and late-phase paths only mark or iterate rows whose `+0x0C` byte is nonzero

That is a very good behavioral fit for `consciousness`.

## `+0x10` now looks strongly like `battler::row` in the Thunder path

The best local anchor here is the Thunder reflection branch.

Reference-side `PSI_THUNDER_COMMON` does this in its Franklin Badge branch:

- load the current target battler
- read `battler::row`
- increment it
- use that row-plus-one value as part of the possession or inventory check before displaying the reflection text

Local-side `C2:966B` does the same shape in the special branch documented in [class2-psi-thunder-reflection-branch.md](notes/class2-psi-thunder-reflection-branch.md):

- load the selected row from `$A972`
- read row byte `+0x10`
- increment it
- pass that value together with fixed `1` through `C4:5683`
- on success, display `EF:7160`, set `$AA96 = 1`, and swap attacker and target context through `C2:7E8A`

That row-byte-plus-one check is an unusually close local fit for the reference use of `battler::row`.

This does not yet prove that every non-Thunder `+0x10` use is also purely a battler row selector. Some later controller notes still show `+0x10` participating in row-local bookkeeping and linked-id updates. But in this battle-action path, `+0x10` now reads much more like the real battler row byte than like a generic subtype.

## `+0x0B` still looks like `battler::the_flag`, but more narrowly

This one improved, but it is still the weakest of the three.

Reference-side clue:

- `BATTLE_INIT_ENEMY_STATS` stores the result of `UNKNOWN_C2B66A(enemyID)` into `battler::the_flag`
- that makes `the_flag` look like enemy-specific naming or article metadata carried into the battler struct at setup time

Source follow-up (2026-05-06): the local `C2:B6EB` initializer now calls that
helper as `ReadBattlerNameVariantFlag`, matching the already named
`C2:3BCF/3D05` text-context consumers that use the same flag for article/name
formatting.

Local-side clue:

- `C2:3BCF` only enters its small optional-token append path when selected-row byte `+0x0B == 1`
- on that branch it appends byte `0x50`, then byte `0x70 + row[+0x0B]`, and sets `$5E77 = 1`
- later bank-`C3` code resolves the resulting token path into article fragments like `"The "` versus `"the "`

That is a very good thematic fit for `the_flag`: a per-enemy or per-name article/capitalization control byte.

What is still missing is a stronger second local use that is as direct as the `+0x0C` presence gating or the `+0x10` Thunder row check. So I think the right wording is:

- `+0x0B` is now a strong article/name-formatting clue consistent with `battler::the_flag`
- but it is not yet as fully behavior-locked as `+0x0C` and the Thunder-side `+0x10` use

## Updated safest interpretation

The safest current interpretation is:

- the `$A970/$A972` selected-row family now sits inside a battler-sized WRAM region that matches `BATTLERS_TABLE`
- `+0x0C` is best read as a `consciousness`-style active or present byte
- `+0x10` is best read as `row` in the local Thunder reflection branch
- `+0x0B` is best read as an article or naming flag consistent with `the_flag`, though that match is still narrower

That is a materially stronger statement than our earlier "maybe these lower bytes line up too" wording.

## What is still unresolved

Still open:

- whether every `$A970/$A972` row should now be named as a battler unconditionally in all notes, or whether a few controller-specific fields still deserve temporary neutral labels until more local paths are checked
- whether all `+0x10` uses should be renamed to `row`, since some controller notes still make it look partly like a linked local selector outside the Thunder path
- whether we can find a second clear local consumer of `+0x0B` that confirms the article-flag reading without leaning on the later token formatter

## Current safest takeaway

The current best takeaway is:

- the affliction crosswalk was not a one-off coincidence
- the lower-field battler interpretation is holding up
- `+0x0C` and `+0x10` now have strong local behavioral support
- `+0x0B` is still slightly softer, but it is pointing in the same direction
- the exact `0x4E` stride match now places those observations inside the right WRAM structure too

That makes the local battle row work much less anonymous than it was even a few steps ago.
