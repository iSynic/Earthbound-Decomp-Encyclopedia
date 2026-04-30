# Audio Dependency Policy

Status: audio dependency and distribution policy recorded.

This policy keeps the audio backend useful for the local Electron app and porter tooling without boxing the project into an accidental license posture.

## Dependencies

| Dependency | Status | Role | Commit | License policy | Integration policy |
| --- | --- | --- | --- | --- | --- |
| `ares` | `local_external_checkout_used_by_diagnostic_harness` | accuracy-first SNES/APU runtime and capture backend prototype | `6f6786e0` | ISC/permissive for core ares; bundled third-party notices must be reviewed before vendoring or binary distribution. | External checkout/build for now. Future submodule is acceptable after license-notice review; avoid copying a carved subset until the boundary is stable. |
| `libgme` | `local_external_checkout_used_by_snes_spc_render_harness` | lightweight SPC snapshot playback/export renderer | `dd3182a8` | LGPL-2.1; dynamic/external linkage preferred for app distribution, with notices and relinkability/source obligations respected. | External checkout/build for now. Keep the renderer swappable and avoid GPL-only optional components in the core path. |
| `bsnes_higan_mesen2_mednafen` | `reference_only_not_core_dependency` | optional reference oracles for accuracy comparison | `` | GPL or mixed/non-core policies; keep optional and out-of-process unless the project intentionally changes license posture. | Use for comparison captures, not required app playback/export. |

## Release Gates

- Generated ROM-derived SPC/WAV/PCM/sample outputs must stay ignored and out of commits.
- Dependency notices must be included before distributing binaries that invoke or link renderer backends.
- LGPL renderer integration must preserve relinkability or remain external/plugin-like.
- GPL reference tools must remain optional or out-of-process unless the whole relevant distribution adopts compatible terms.
- Public docs must state that end users provide their own ROM and that audio exports are generated locally.
