from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol


@dataclass(frozen=True)
class AudioRenderOptions:
    seconds: float = 30.0
    fade_seconds: float = 5.0
    sample_rate: int = 32000
    channels: int = 2
    output_format: str = "wav"


@dataclass(frozen=True)
class AudioSnapshotRequest:
    track_id: int
    rom_path: Path
    contract_path: Path


@dataclass(frozen=True)
class AudioBackendJob:
    job_id: str
    backend_id: str
    fixture_path: Path
    output_dir: Path
    render_options: AudioRenderOptions
    expected_outputs: tuple[str, ...]


class AudioRendererBackend(Protocol):
    backend_id: str
    license_policy: str

    def build_track_snapshot(self, request: AudioSnapshotRequest) -> Path:
        raise NotImplementedError

    def render_track(self, request: AudioSnapshotRequest, options: AudioRenderOptions, output_path: Path) -> Path:
        raise NotImplementedError

    def play_track(self, request: AudioSnapshotRequest, options: AudioRenderOptions) -> None:
        raise NotImplementedError


class SnapshotStateBuilderBackend(Protocol):
    backend_id: str
    snapshot_state: str

    def build_track_apu_ram(self, request: AudioSnapshotRequest) -> Path:
        raise NotImplementedError


class EarthBoundApuRamSeedBackend:
    backend_id = "earthbound_apu_ram_seed"
    snapshot_state = "apu_ram_only_registers_and_driver_start_not_finalized"

    def build_track_apu_ram(self, request: AudioSnapshotRequest) -> Path:
        import build_audio_track_snapshot
        import rom_tools

        contract = build_audio_track_snapshot.load_contract(request.contract_path)
        track = build_audio_track_snapshot.require_track(contract, request.track_id)
        rom = rom_tools.load_rom(request.rom_path)
        ram, _ = build_audio_track_snapshot.build_apu_ram_image(contract, rom, track)
        output_dir = request.contract_path.parent.parent / "build" / "audio"
        output_dir.mkdir(parents=True, exist_ok=True)
        stem = f"track-{request.track_id:03d}-{track['name'].lower()}"
        stem = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in stem)
        output_path = output_dir / f"{stem}.apu-ram.bin"
        output_path.write_bytes(ram)
        return output_path


class PlannedRendererBackend:
    backend_id = "planned"
    license_policy = "not selected"
    execution_policy = "not implemented"
    implemented = False
    implementation_stage = "not implemented"

    def build_track_snapshot(self, request: AudioSnapshotRequest) -> Path:
        raise NotImplementedError(f"{self.backend_id} snapshot building is not implemented yet")

    def render_track(self, request: AudioSnapshotRequest, options: AudioRenderOptions, output_path: Path) -> Path:
        raise NotImplementedError(f"{self.backend_id} rendering is not implemented yet")

    def play_track(self, request: AudioSnapshotRequest, options: AudioRenderOptions) -> None:
        raise NotImplementedError(f"{self.backend_id} playback is not implemented yet")


class AresRendererBackend(PlannedRendererBackend):
    backend_id = "ares"
    license_policy = "ISC/permissive candidate; review bundled third-party notices before vendoring"
    execution_policy = "external harness first; keep emulator code out of core tools until prototype proves the path"
    implemented = False
    implementation_stage = "native diagnostic harness implemented; accurate PCM/WAV renderer pending"


class SnesSpcRendererBackend(PlannedRendererBackend):
    backend_id = "snes_spc"
    license_policy = "LGPL-2.1; requires LGPL notice and linking/compliance policy"
    execution_policy = "snapshot renderer only after complete SPC state is available"
    implemented = True
    implementation_stage = "libgme SPC renderer implemented out-of-tree; honors backend job render options; source snapshots are fused CHANGE_MUSIC/key-on captures pending emulator oracle comparison"


class ExternalReferenceRendererBackend(PlannedRendererBackend):
    backend_id = "external_reference"
    license_policy = "GPL/noncommercial tools must remain optional and out-of-process unless project licensing changes"
    execution_policy = "optional validation oracle, never a required core dependency"


def renderer_backends() -> dict[str, AudioRendererBackend]:
    backends: list[AudioRendererBackend] = [
        AresRendererBackend(),
        SnesSpcRendererBackend(),
        ExternalReferenceRendererBackend(),
    ]
    return {backend.backend_id: backend for backend in backends}


def snapshot_state_builders() -> dict[str, SnapshotStateBuilderBackend]:
    builders: list[SnapshotStateBuilderBackend] = [
        EarthBoundApuRamSeedBackend(),
    ]
    return {builder.backend_id: builder for builder in builders}


def describe_renderer_backends() -> list[dict[str, Any]]:
    return [
        {
            "id": backend.backend_id,
            "license_policy": backend.license_policy,
            "execution_policy": getattr(backend, "execution_policy", "not specified"),
            "implemented": getattr(backend, "implemented", False),
            "implementation_stage": getattr(backend, "implementation_stage", "not specified"),
        }
        for backend in renderer_backends().values()
    ]


def backend_job_to_dict(job: AudioBackendJob) -> dict[str, Any]:
    return {
        "job_id": job.job_id,
        "backend_id": job.backend_id,
        "fixture_path": str(job.fixture_path),
        "output_dir": str(job.output_dir),
        "render_options": {
            "seconds": job.render_options.seconds,
            "fade_seconds": job.render_options.fade_seconds,
            "sample_rate": job.render_options.sample_rate,
            "channels": job.render_options.channels,
            "output_format": job.render_options.output_format,
        },
        "expected_outputs": list(job.expected_outputs),
    }
