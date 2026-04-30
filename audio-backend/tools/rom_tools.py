from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

EXPECTED_ROM_NAME = "EarthBound (USA).sfc"
EXPECTED_SHA1 = "d67a8ef36ef616bc39306aa1b486e1bd3047815a"
EXPECTED_SIZE = 0x300000
EXPECTED_TITLE = "EARTH BOUND"
EXPECTED_MAP_MODE = 0x31
EXPECTED_CART_TYPE = 0x02
EXPECTED_BANK_SIZE = 0x10000
HIROM_CANONICAL_START_BANK = 0xC0
VECTOR_BANK = 0x00
HEADER_OFFSET = 0xFFC0
VECTOR_TABLE = {
    "native_cop": 0xFFE4,
    "native_brk": 0xFFE6,
    "native_abort": 0xFFE8,
    "native_nmi": 0xFFEA,
    "native_irq": 0xFFEE,
    "emulation_cop": 0xFFF4,
    "emulation_abort": 0xFFF8,
    "emulation_nmi": 0xFFFA,
    "emulation_reset": 0xFFFC,
    "emulation_irqbrk": 0xFFFE,
}


@dataclass(frozen=True)
class RomInfo:
    path: Path
    size: int
    sha1: str
    title: str
    map_mode: int
    cart_type: int
    rom_size_code: int
    sram_size_code: int
    country_code: int
    license_code: int
    version: int
    complement_check: int
    checksum: int

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["path"] = str(self.path)
        data["map_mode"] = f"0x{self.map_mode:02X}"
        data["cart_type"] = f"0x{self.cart_type:02X}"
        data["rom_size_code"] = f"0x{self.rom_size_code:02X}"
        data["sram_size_code"] = f"0x{self.sram_size_code:02X}"
        data["country_code"] = f"0x{self.country_code:02X}"
        data["license_code"] = f"0x{self.license_code:02X}"
        data["version"] = f"0x{self.version:02X}"
        data["complement_check"] = f"0x{self.complement_check:04X}"
        data["checksum"] = f"0x{self.checksum:04X}"
        return data


@dataclass(frozen=True)
class VectorInfo:
    name: str
    header_offset: int
    vector_bank: int
    target_address: int
    rom_file_offset: int | None
    canonical_bank: int | None

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "name": self.name,
            "header_offset": f"0x{self.header_offset:04X}",
            "vector_bank": f"0x{self.vector_bank:02X}",
            "target_address": f"0x{self.target_address:04X}",
            "cpu_long_address": f"0x{self.vector_bank:02X}{self.target_address:04X}",
        }
        if self.rom_file_offset is not None:
            payload["rom_file_offset"] = f"0x{self.rom_file_offset:06X}"
        else:
            payload["rom_file_offset"] = None
        if self.canonical_bank is not None:
            payload["canonical_bank"] = f"0x{self.canonical_bank:02X}"
            payload["canonical_long_address"] = (
                f"0x{self.canonical_bank:02X}{self.target_address:04X}"
            )
        else:
            payload["canonical_bank"] = None
            payload["canonical_long_address"] = None
        return payload


def workspace_root() -> Path:
    return Path(__file__).resolve().parent.parent


def candidate_rom_paths() -> list[Path]:
    root = workspace_root()
    candidates = [
        root / EXPECTED_ROM_NAME,
        root / "baserom" / EXPECTED_ROM_NAME,
    ]

    for search_root in (root, root / "baserom"):
        if not search_root.exists():
            continue
        for pattern in ("*.sfc", "*.smc"):
            for path in sorted(search_root.glob(pattern)):
                if path not in candidates:
                    candidates.append(path)

    return candidates


def find_rom(explicit_path: str | None = None) -> Path:
    if explicit_path:
        path = Path(explicit_path).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"ROM not found: {path}")
        return path

    for path in candidate_rom_paths():
        if path.is_file():
            return path

    searched = "\n".join(f"- {path}" for path in candidate_rom_paths())
    raise FileNotFoundError(
        "Unable to find a ROM file. Looked in:\n"
        f"{searched}\n"
        "Pass --rom to point at a specific file."
    )


def load_rom(path: Path) -> bytes:
    data = path.read_bytes()
    if len(data) < 0x10000:
        raise ValueError(f"ROM is too small to contain a valid SNES header: {path}")
    return data


def read_u16_le(data: bytes, offset: int) -> int:
    return data[offset] | (data[offset + 1] << 8)


def hirom_is_rom_address(bank: int, address: int) -> bool:
    normalized_bank = bank & 0x7F
    if normalized_bank < 0x40:
        return address >= 0x8000
    return True


def hirom_to_file_offset(bank: int, address: int, rom_size: int | None = None) -> int | None:
    if not hirom_is_rom_address(bank, address):
        return None

    normalized_bank = bank & 0x7F
    if normalized_bank < 0x40:
        file_offset = (normalized_bank << 16) + address
    else:
        file_offset = ((normalized_bank - 0x40) << 16) + address

    if rom_size is not None and file_offset > rom_size:
        return None
    return file_offset


def canonical_bank_for_file_offset(file_offset: int) -> int:
    return HIROM_CANONICAL_START_BANK + (file_offset // EXPECTED_BANK_SIZE)


def read_rom_info(path: Path) -> RomInfo:
    data = load_rom(path)
    title = data[0xFFC0:0xFFD5].decode("ascii", errors="ignore").rstrip()
    return RomInfo(
        path=path,
        size=len(data),
        sha1=hashlib.sha1(data).hexdigest(),
        title=title,
        map_mode=data[0xFFD5],
        cart_type=data[0xFFD6],
        rom_size_code=data[0xFFD7],
        sram_size_code=data[0xFFD8],
        country_code=data[0xFFD9],
        license_code=data[0xFFDA],
        version=data[0xFFDB],
        complement_check=read_u16_le(data, 0xFFDC),
        checksum=read_u16_le(data, 0xFFDE),
    )


def read_vectors(path: Path) -> list[VectorInfo]:
    data = load_rom(path)
    vectors: list[VectorInfo] = []
    for name, header_offset in VECTOR_TABLE.items():
        target_address = read_u16_le(data, header_offset)
        rom_file_offset = hirom_to_file_offset(VECTOR_BANK, target_address, len(data))
        canonical_bank = (
            canonical_bank_for_file_offset(rom_file_offset)
            if rom_file_offset is not None
            else None
        )
        vectors.append(
            VectorInfo(
                name=name,
                header_offset=header_offset,
                vector_bank=VECTOR_BANK,
                target_address=target_address,
                rom_file_offset=rom_file_offset,
                canonical_bank=canonical_bank,
            )
        )
    return vectors


def verify_earthbound_us(info: RomInfo) -> list[str]:
    problems: list[str] = []
    if info.size != EXPECTED_SIZE:
        problems.append(
            f"expected size {EXPECTED_SIZE} bytes, found {info.size} bytes"
        )
    if info.sha1 != EXPECTED_SHA1:
        problems.append(
            f"expected SHA-1 {EXPECTED_SHA1.upper()}, found {info.sha1.upper()}"
        )
    if info.title.strip() != EXPECTED_TITLE:
        problems.append(
            f"expected title '{EXPECTED_TITLE}', found '{info.title or '<empty>'}'"
        )
    if info.map_mode != EXPECTED_MAP_MODE:
        problems.append(
            f"expected map mode 0x{EXPECTED_MAP_MODE:02X}, found 0x{info.map_mode:02X}"
        )
    if info.cart_type != EXPECTED_CART_TYPE:
        problems.append(
            f"expected cart type 0x{EXPECTED_CART_TYPE:02X}, found 0x{info.cart_type:02X}"
        )
    if (info.checksum ^ info.complement_check) != 0xFFFF:
        problems.append("header checksum and complement do not xor to 0xFFFF")
    return problems


def bank_count(info: RomInfo, bank_size: int = EXPECTED_BANK_SIZE) -> int:
    return (info.size + bank_size - 1) // bank_size


def snes_bank_number(index: int) -> int:
    return HIROM_CANONICAL_START_BANK + index
