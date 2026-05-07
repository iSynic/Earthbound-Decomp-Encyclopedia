# Reference-first workflow

This note defines the faster C3+ working style: use the quarantined refs first, then require local proof before promoting names.

## Rule of thumb

Use refs as accelerators, not authority.

- `ref-suggested`: a name, source path, struct, table, or domain exists in a reference, but local bytes have not been checked yet.
- `local-confirmed`: local callers, control flow, WRAM offsets, table stride, or data shape support the identity.
- `corroborated`: local-confirmed and at least one ref independently agrees.

Only `local-confirmed` and `corroborated` names should flow into source-label artifacts. `ref-suggested` names are allowed in notes, but they should be clearly marked as candidates.

## Generated index

Build the reference index with:

```powershell
python tools\build_ref_index.py --output build\ref-index.json
```

Inspect the index summary with:

```powershell
python tools\lookup_ref_context.py --summary
```

Build a bank-specific frontier report before picking a seam:

```powershell
python tools\build_ref_bank_report.py C3 --output notes\bank-c3-reference-frontier.md --limit 160
```

Current first-pass index scope:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/*.asm` include entries
- `refs/ebsrc-main/ebsrc-main/include/symbols/*.asm` globals
- `refs/ebsrc-main/ebsrc-main/src/**/*.asm` source labels
- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm` address labels
- `refs/eb-decompile-4ef92/**/*.yml` table/data assets
- focused local `notes/*.md` address mentions, excluding generated frontier/proposal/audit/closure reports
- local `build/working-names-c0-c3.json`
- local `build/data-contracts-c0-c3.json`
- local `build/script-payloads-c3.json`

Additional ignored refs that are useful but not currently part of the generated
index:

- `refs/starmen-earthbound-script/EarthBound_Script_Symbolized.txt`: Starmen's
  symbolized text-script dump. Prefer this version for evidence: it preserves
  control codes that explain where and how text appears, and it includes some
  unused lines that are missing from Tomato's older text dumps. Use it to
  correlate queued text pointers, `MSG_EVT_*` names, event flags, and
  higher-level text control flow.
- `refs/starmen-earthbound-script/script.txt`: raw companion text-script dump.
- `refs/starmen-earthbound-script/script.htm`: text script without control
  nodes, useful for quickly checking dialogue wording but not sufficient as the
  sole source of context.

These Starmen files describe EarthBound text scripts, not C3 event/actionscript
bytecode. They should accelerate C5-C9/EF text-command work and help explain C3
`ActionScript_QueueTextPointer` targets, but they should not be treated as opcode
evidence for the C3 action VM.

Single-format clue:

- `notes/earthbound-localization-script-authoring-format.md`: user-supplied
  screenshot/transcription of one original-format localization script record.
  It shows `;@...` metadata tying habitat, person, figure, appearance key,
  actionscript description, goods/check/message hooks, and a `MSG_*` text label
  together in one authoring record. Use it as a schema clue for future
  map-object/text-script crosswalks, not as byte-level proof.

## Lookup loop

Before starting a new chunk, run:

```powershell
python tools\lookup_ref_context.py C3:0188
```

For field-heavy data or WRAM/table addresses, also run:

```powershell
python tools\lookup_data_contract.py D5:9589+0x46 "BATTLERS_TABLE[3].afflictions" '$ADD4+0x61'
```

For semantic names seen in refs, run:

```powershell
python tools\lookup_ref_context.py DISPLAY_ANTI_PIRACY_SCREEN
```

For C3-style event/actionscript bytecode, decode the local ROM bytes with:

```powershell
python tools\decode_event_script.py C3:0295 C3:AB59
```

The decoder uses a small, explicit `EVENT_CALLROUTINE` argument-count map. If it stops at an unknown target, corroborate the macro in `refs/ebsrc-main/ebsrc-main/include/eventmacros.asm`, add the target arity, and rerun the same address.

To rebuild the promoted C3 script-payload manifest:

```powershell
python tools\build_script_payload_manifest.py
```

## Note checklist

Every new note should start with a compact reference/context block:

- local target address or range
- `lookup_ref_context.py` result summary
- direct local callers or data xrefs
- contract matches, if any
- borrowed ref names and their source paths
- what was locally confirmed
- what remains only ref-suggested
- event-script decode output when the bytes are action/event bytecode rather than CPU code

## Why this helps

The C0-C2 passes proved the slow path works. The index lets us start later banks with:

- ebsrc include/source context
- legacy address labels
- known table/data assets
- existing local note coverage
- working-name and data-contract status

That should reduce repeated rediscovery while still keeping the project honest.
