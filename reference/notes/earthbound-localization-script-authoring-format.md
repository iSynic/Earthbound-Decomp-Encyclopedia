# EarthBound localization script authoring-format clue

This note started as a user-supplied screenshot/transcription of one documented
EarthBound localization script in what appeared to be its original authoring
format. We now also have a local copy of recovered localization script source,
extracted from `EarthBound_Script_Source_1995-03-25.zip`, under the ignored
`refs/earthbound-script-source-1995-03-25/` directory.

The recovered source files are intentionally not checked in. The useful public
artifact for this project is the surrounding record shape and structural index:
how text, NPC metadata, and actionscript labels were described together by the
original tools or localization workflow.

Run `python tools/index_localization_script_source.py` to regenerate
`notes/localization-script-source-index.md` and the ignored
`build/localization-script-source-index.json` metadata index.

Run `python tools/build_localization_script_metadata_manifest.py` for the local
analysis manifest:

- `build/localization-script-metadata-records.json`
- `build/localization-actionscript-descriptors.tsv`

Those generated files intentionally stay ignored because they preserve recovered
source metadata values. The tracked note/index files keep only structural
counts and workflow guidance.

Run `python tools/build_localization_map_object_crosswalk.py` to join recovered
source records to ROM-backed placed map objects by text label and pointer. The
tracked summary is `notes/localization-map-object-crosswalk.md`; the detailed
ignored output is `build/localization-map-object-crosswalk.json`.

Run `python tools/build_localization_movement_evidence.py` to summarize that
crosswalk into `notes/localization-movement-evidence.md`, a public-safe movement
ID prioritization report for C3 naming and promotion work.

Current local manifest summary:

- Parsed NPC-style metadata records: `653`.
- Unique `;@ActionScript:` descriptors: `94`.
- Unique `;@Figure:` values: `189`.
- Unique top-level habitat prefixes: `22`.
- Referenced symbol prefixes seen in metadata-record bodies: `ANIM`, `BGM`,
  `FLG`, `GOODS`, `MSG`, `OBJFX`, and `PRSN`.

Current local reference summary:

- Archive SHA-256:
  `61798a4d78fc5b7d6fc9788391639489ff81ad18ded399913ccde1cc16e94f13`.
- Extracted `.MSG` files: `57`.
- Text encoding: `cp932` / Shift-JIS.
- Labels: `6049`, including `3257` `MSG_*` labels.
- Metadata records: `653` `;@Message:` records and `653` `;@ActionScript:`
  behavior descriptors.
- The archive includes `EDEBUG.MSG`, which is the strongest reference found so
  far for the debug text/menu script source, even though retail ROM reachability
  is still a separate code-path question.
- Unlike the Starmen symbolized/raw text dumps in
  `refs/starmen-earthbound-script/`, this recovered source preserves the
  original-style `;@...` NPC metadata records.

## Observed Record Shape

- Records can be separated by semicolon comment rulers.
- Metadata fields appear as semicolon-prefixed keys:
  - `;@Habitat:`
  - `;@Person:`
  - `;@Figure:`
  - `;@AppearanceKey:`
  - `;@ActionScript:`
  - `;@GoodsMessage:`
  - `;@CheckMessage:`
  - `;@Message:`
- The message body starts at a symbolic label such as `MSG_*`, with a
  semicolon comment after the label for a short place/context note.
- English dialogue uses inline control commands such as `@KEY()` and ends with
  `@KEYNP()`.
- The screenshot shows visible line/paragraph markers in the dialogue body.
  That supports using control-code-preserving dumps as the primary text-script
  evidence.
- The original Japanese lines are preserved as `;jpn:` comments after the
  localized text.
- `;@ActionScript:` carries a human-readable behavior description for the NPC.
  This likely corresponds to a map-object behavior/actionscript selection, not
  necessarily a direct C3 event-bytecode address by itself.

## Why It Matters

This is the first authoring-format clue we have that places these concepts in
one source record:

- habitat/map context
- person/NPC role
- figure/sprite identity
- appearance key
- actionscript behavior descriptor
- goods/check/message hooks
- localized text label and original Japanese companion text

For the current project, that suggests the most useful public-facing bridge is
not just "decode the text bytes." It is a crosswalk from map object records to:

- sprite/figure identifiers
- appearance keys
- action/event script selectors
- check/goods/message pointers
- symbolic `MSG_*` names from text-script refs

## Practical Use

When working on C5-C9/EF text-command semantics or map-object contracts:

- Prefer symbolized/control-code-preserving script dumps over flattened text.
- Preserve message labels and text commands exactly when building manifests.
- Keep `;@ActionScript:` style descriptions as candidate behavior names only
  until they are tied back to local map-object records or C3 bytecode.
- Use `tools/index_localization_script_source.py` for `;@...` metadata and
  command inventory. Extend it into a crosswalk only when joining to
  ROM-backed map-object, sprite, action-script, and message-pointer records.
- Use `tools/build_localization_script_metadata_manifest.py` when you need a
  local queryable manifest of records, labels, commands, symbols, and
  `;@ActionScript:` descriptors.
- Use `tools/build_localization_map_object_crosswalk.py` when you need to join
  recovered source records back to placed map objects, movement IDs, and
  behavior buckets.
- Use `tools/build_localization_movement_evidence.py` for a quick public-safe
  view of which movement IDs have the most localization-derived naming evidence.

This clue does not change the C3 event/actionscript VM decoder directly, but it
does strengthen the naming model for NPC behavior contracts and eventual
romhacker-facing documentation.
