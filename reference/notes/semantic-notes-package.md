# Semantic Notes Package

This note defines the current documentation package for semantic work after the
bank first-pass sweep. The `bank-*-first-pass.md` files are retained as
historical inventory notes: they prove every configured bank was classified, but
they are no longer the right place for ongoing subsystem findings.

## Current Package Layers

| Layer | Role | Primary Notes |
| --- | --- | --- |
| Historical bank inventory | First-pass bank classification and artifact lists. Treat as stable background, not the live work log. | `notes/bank-first-pass-coverage-index.md`, `notes/bank-*-first-pass.md` |
| Structural/source closure | Byte-equivalence, preserved-corridor closure, and source-readiness state. | `notes/source-scaffold-status.md`, `notes/readable-source-bank-closure.md`, `notes/source-readiness-triage.md` |
| Phase-2 semantic status | Live map of subsystem understanding, weak zones, and next semantic lanes. | `notes/phase-2-semantic-closure-plan.md`, `notes/phase-2-semantic-status.md`, `notes/project-status.md` |
| Runtime semantic polish | C0/C1/C2/C4/EF subsystem execution plans and follow-up notes. | `notes/runtime-semantic-polish-plans.md`, `notes/c0-runtime-semantic-polish-plan.md`, `notes/c1-runtime-semantic-polish-plan.md`, `notes/c2-runtime-semantic-polish-plan.md`, `notes/c4-runtime-semantic-polish-plan.md`, `notes/ef-runtime-semantic-polish-plan.md` |
| C-port feedback intake | Port-side discoveries folded back into decomp action lanes, especially C1/C2 battle contracts and trace-oracle candidates. | `notes/c-port-feedback-intake.md`, `notes/c2-runtime-proof-promotion-closeout.md`, `notes/c2-battle-trace-oracle-plan.md`, `notes/c2-battle-trace-oracle-index.md`, `notes/c2-battle-trace-oracle-packet.md`, `notes/c2-battle-trace-oracle-emulator-handoff.md`, `notes/c2-battle-trace-oracle-mesen-runner.md`, ignored runner assets under `build/c2/battle-trace-oracles/mesen-runner-assets/`, `notes/c2-battle-trace-oracle-results-summary.md`, `notes/c2-b930-controlled-snapshot-export.md`, `notes/c2-snapshot-export-natural-scout.md`, `notes/c2-resource-amount-controlled-comparison.md`, `notes/c2-resource-amount-natural-candidates.md`, `notes/c2-save-state-battler-scout.md`, `notes/c2-scripted-battle-fixture-workahead.md` |
| VM and localization semantics | Event/actionscript, text-command, localization, and script export semantics. | `notes/c3-actionscript-semantics-audit.md`, `notes/text-command-semantics-manifest.md`, `notes/text-vm-localization-semantics-closeout.md` |
| Data and asset contracts | Table, subrecord, audio, graphics, and source-emission contracts. | `notes/asset-data-contract-frontier.md`, `notes/battle-action-row-crosswalk.md`, `notes/ui-font-town-map-asset-contracts.md`, `notes/audio-sequence-command-semantics.md`, bank-specific contract notes |
| Community/reference alignment | ebsrc and EB-M2 compatibility, aliases, and conflict review. | `notes/ebsrc-community-crosswalk.md`, `notes/ebsrc-knowns-integration-candidates.md`, `notes/eb-m2-name-crosswalk.md`, `notes/eb-m2-needs-review-triage.md` |

## Naming Policy Going Forward

- Do not append new semantic discoveries to a `bank-*-first-pass.md` note unless
  the discovery corrects the original inventory.
- Use subsystem notes for live work: `c2-*-runtime-polish.md`,
  `c4-*-presentation-contracts.md`, `ef-*-runtime-closure.md`, and similar
  names that say what was studied.
- Use `phase-2` only for orientation/status notes, not every leaf note. Leaf
  notes should be named by subsystem or evidence target.
- If a note supersedes an old first-pass claim, link both ways and state that
  the newer note is authoritative for semantics.
- Keep generated dashboards generated. Human-written status notes should point
  to generated reports rather than duplicate all of their tables.
- Fold C-port discoveries into the decomp as intake evidence first. Use
  `notes/c-port-feedback-intake.md` and
  `notes/c2-battle-trace-oracle-plan.md` to route port-side findings toward
  local trace oracles and subsystem notes before promoting source-facing claims.
  The generated `notes/c2-battle-trace-oracle-index.md` is the compact queue
  for runner/worktree assignment; `notes/c2-battle-trace-oracle-packet.md`
  defines the ignored local job/result paths and stub runner contract. The
  generated emulator handoff defines the first-pass real-runner breakpoints and
  scenario setup; ignored runner assets add Mesen Lua skeletons, operator
  checklists, command snippets, and a reviewed-result assembler path. The
  results summary separates runner-completed stub plumbing from proof-grade
  trace evidence. `notes/c2-runtime-proof-promotion-closeout.md` is the
  compact index of C2 evidence that has crossed from raw runtime capture into
  source-facing contract guidance. The generated `notes/battle-action-row-crosswalk.md`
  is the row-table navigation layer for joining D5 action rows to C1/C2/EF
  battle-text contracts without treating table shape as runtime proof.

## How To Read The Old First-Pass Notes

The first-pass notes answer:

- What spans/assets/code regions did we identify first?
- What references or generated manifests were available at that time?
- What was the original follow-up queue?

They should not be read as the latest semantic truth for a subsystem. For live
semantic confidence, start with `notes/phase-2-semantic-closure-plan.md` and
`notes/phase-2-semantic-status.md`, then follow the runtime, VM, data-contract,
or crosswalk note listed there.
