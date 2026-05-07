# Text Command Parser Artifact Frontier

This note tracks the parsed-only text-command family hits that currently look
more like decoder artifacts than live text VM commands.

## Why This Exists

The text banks contain real script streams mixed with pointer-like tables,
compressed-bank byte runs, and other data payloads. When a linear text decoder
walks into one of those regions, ordinary data bytes can resemble family
commands such as `1D C7` or `1F 4E`.

These rows are not deleted from the manifest. They are marked as
`parsed_artifact_candidate` so they remain visible, but they no longer compete
with runtime-backed unknown commands for naming work.

## Current Candidate Set

| Command | Segment | Local neighborhood | Current read |
| --- | --- | --- | --- |
| `18 A3` | `EDEBUG` | near `C5:997C` | Pointer/table-like run with repeated text/control-looking fragments |
| `19 4F` | `ENEWS` | near `C8:4A49` | Pointer/table-like run adjacent to `1F 4E` |
| `1A 48` | `ENEWS` | near `C8:4345` | Pointer/table-like run before ordinary text resumes |
| `1D 1C` | `EBATTLE8` | near `EF:79DF` | Compressed/overlap artifact after battle text |
| `1D 85` | `EDEBUG` | near `C5:849F` | Pointer/table or compressed-bank overlap after `16 85` |
| `1D C7` | `EHINT` | near `C7:00EF` | Part of a clustered pointer/table-looking run |
| `1E C7` | `EHINT` | near `C7:00F7` | Same clustered pointer/table-looking run |
| `1F 4E` | `ENEWS` | near `C8:4A59` | Same pointer/table-like neighborhood as `19 4F` |
| `1F C7` | `EHINT` | near `C7:00FF` | Same clustered pointer/table-looking run |

## Promotion Rule

A parsed-only family command should be promoted out of this bucket only when at
least one of these becomes true:

- it gains a live C1 dispatcher case
- it appears in a coherent source-syntax record from the recovered `.MSG`
  authoring material
- its surrounding ROM bytes decode as a stable command stream rather than a
  table, pointer run, or compressed-bank overlap

Until then, the best next use of these rows is parser-boundary cleanup, not
runtime command naming.
