#!/usr/bin/env python3
"""Validate the durable audio backend adapter contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTRACT = ROOT / "manifests" / "audio-backend-contract.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the audio backend adapter contract.")
    parser.add_argument("contract", nargs="?", default=str(DEFAULT_CONTRACT))
    return parser.parse_args()


def validate(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("schema") != "earthbound-decomp.audio-backend-contract.v1":
        errors.append(f"unexpected schema: {contract.get('schema')}")
    if contract.get("backend_selection", {}).get("default_accuracy_backend") != "ares":
        errors.append("default accuracy backend must be ares")
    input_names = {item.get("name") for item in contract.get("input_artifacts", [])}
    for required in ("renderer_fixture", "apu_ram_seed", "backend_job"):
        if required not in input_names:
            errors.append(f"missing input artifact {required}")
    job_fields = set(contract.get("job_schema", {}).get("required_fields", []))
    for required in ("job_id", "backend_id", "fixture_path", "output_dir", "expected_outputs", "job_path", "result_path"):
        if required not in job_fields:
            errors.append(f"job schema missing field {required}")
    result_fields = set(contract.get("result_schema", {}).get("required_fields", []))
    for required in ("job_id", "backend_id", "status", "outputs", "diagnostics"):
        if required not in result_fields:
            errors.append(f"result schema missing field {required}")
    backends = {backend.get("id") for backend in contract.get("backend_catalog", [])}
    for required in ("ares", "snes_spc", "external_reference"):
        if required not in backends:
            errors.append(f"backend catalog missing {required}")
    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.contract)
    contract = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(contract)
    if errors:
        print("Audio backend contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Audio backend contract validation OK: "
        f"{len(contract['backend_catalog'])} backends, "
        f"{len(contract['input_artifacts'])} input artifacts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
