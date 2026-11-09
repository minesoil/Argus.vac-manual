"""Shared ASCII/CRC wire contract. Keep in sync with firmware/protocol.h."""

from dataclasses import dataclass
import math


def crc16(data):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            crc = ((crc << 1) ^ (0x1021 if crc & 0x8000 else 0)) & 0xFFFF
    return crc


def frame(payload):
    raw = payload.encode("ascii")
    return raw + f",{crc16(raw):04X}\n".encode("ascii")


def command(sequence, enabled, left, right):
    if not 0 <= sequence <= 65535 or any(
        isinstance(x, bool) or not isinstance(x, int) or abs(x) > 16000
        for x in (left, right)
    ):
        raise ValueError("Command outside protocol limits.")
    return frame(f"V1,{sequence},{1 if enabled else 0},{left},{right}")


@dataclass(frozen=True)
class Status:
    sequence: int
    armed: bool
    fault: int
    left_steps: int
    right_steps: int


def parse_status(raw):
    if len(raw) > 80:
        raise ValueError("Status frame too long.")
    payload, checksum = raw.rstrip(b"\r\n").rsplit(b",", 1)
    if len(checksum) != 4 or int(checksum, 16) != crc16(payload):
        raise ValueError("Invalid status checksum.")
    fields = payload.decode("ascii").split(",")
    if len(fields) != 6 or fields[0] != "S1":
        raise ValueError("Invalid status frame.")
    numbers = [int(x) for x in fields[1:]]
    if (
        not 0 <= numbers[0] <= 65535
        or numbers[1] not in (0, 1)
        or not 0 <= numbers[2] <= 3
        or any(not -(2**31) <= x < 2**31 for x in numbers[3:])
    ):
        raise ValueError("Invalid status values.")
    return Status(numbers[0], bool(numbers[1]), *numbers[2:])


def wheel_rates(v, w, radius, separation, steps_per_rev, max_rate=16000):
    if (
        any(not math.isfinite(x) for x in (v, w, radius, separation))
        or radius <= 0
        or separation <= 0
        or steps_per_rev <= 0
    ):
        raise ValueError("Invalid wheel geometry or velocity.")
    scale = steps_per_rev / (2 * math.pi * radius)
    rates = [(v - w * separation / 2) * scale, (v + w * separation / 2) * scale]
    # Scale both wheels together to preserve curvature when a pulse limit is hit.
    factor = min(1, max_rate / max(max(abs(x) for x in rates), 1))
    return tuple(round(x * factor) for x in rates)


def count_delta(current, previous):
    return (current - previous + 2**31) % 2**32 - 2**31
