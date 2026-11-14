"""Bounded C1 serial acquisition. Invalid returns remain unknown, never clear."""

from dataclasses import dataclass
import math
import struct
import threading
import time

from .core import Scan


@dataclass(frozen=True)
class Sweep:
    sequence: int
    started: float
    finished: float
    ranges: tuple
    nodes: int

    def scan(self, front_deg=0.0, x=0.0, y=0.0):
        # C1 angles increase clockwise. Core uses CCW from robot forward.
        return Scan(self.ranges, -math.pi / len(self.ranges), -math.tau / len(self.ranges),
                    0.05, 12.0, self.started, x, y, math.radians(front_deg))


class C1Reader:
    def __init__(self, port, serial_factory=None, clock=time.monotonic):
        if serial_factory is None:
            from serial import Serial
            serial_factory = Serial
        self.clock = clock
        self.port = serial_factory(port=None, baudrate=460800, timeout=0.03,
                                   write_timeout=0.15)
        self.port.dtr = self.port.rts = False
        self.port.port = port
        self.latest = None
        self.error = None
        self.ended = threading.Event()
        self.thread = None
        self.info = None

    def command(self, code):
        if self.port.write(bytes((0xA5, code))) != 2:
            raise OSError("Incomplete C1 command write")

    def exact(self, length, timeout=2.0):
        result = bytearray()
        deadline = self.clock() + timeout
        while len(result) < length and self.clock() < deadline:
            result.extend(self.port.read(length - len(result)))
        if len(result) != length:
            raise OSError("C1 response timed out")
        return bytes(result)

    def response(self, code, kind, length):
        self.port.reset_input_buffer()
        self.command(code)
        header = self.exact(7)
        if header[:2] != b"\xa5\x5a" or header[6] != kind or (
                struct.unpack("<I", header[2:6])[0] != length):
            raise OSError("Unexpected C1 response descriptor")
        return self.exact(length)

    def start(self):
        try:
            self.port.open()
            self.command(0x25)
            time.sleep(0.1)
            info = self.response(0x50, 4, 20)
            if info[0] != 0x41:
                raise OSError("Expected the commissioned C1 model 0x41")
            self.info = {"model": info[0], "firmware": f"{info[2]}.{info[1]:02d}"}
            health = self.response(0x52, 6, 3)
            if health != b"\0\0\0":
                raise OSError("C1 health is not OK")
            self.port.reset_input_buffer()
            self.command(0x20)
            if self.exact(7) != b"\xa5\x5a\x05\0\0\x40\x81":
                raise OSError("C1 normal scan format differs from the bench test")
            self.thread = threading.Thread(target=self._read, daemon=True)
            self.thread.start()
            return self
        except BaseException:
            self.close()
            raise

    @staticmethod
    def node(data):
        first, second, third, low, high = data
        if (first & 1) == ((first >> 1) & 1) or not second & 1:
            return None
        angle = ((second >> 1) | (third << 7)) / 64.0
        if angle >= 360:
            return None
        distance = (low | high << 8) / 4000.0
        return bool(first & 1), angle, distance, first >> 2

    def _read(self):
        buffer = bytearray()
        bins, started, count, sequence = None, None, 0, 0
        try:
            while not self.ended.is_set():
                if self.port.in_waiting > 4096:
                    raise OSError("C1 serial backlog; acquisition is no longer fresh")
                buffer.extend(self.port.read(min(4096, max(1, self.port.in_waiting))))
                if len(buffer) > 10000:
                    raise OSError("C1 acquisition backlog")
                while len(buffer) >= 5:
                    node = self.node(buffer[:5])
                    if node is None:
                        del buffer[0]
                        # A corrupt stream invalidates the current revolution.
                        bins = None
                        continue
                    del buffer[:5]
                    start, angle, distance, quality = node
                    now = self.clock()
                    if start:
                        if bins is not None and count >= 100:
                            sequence += 1
                            self.latest = Sweep(sequence, started, now, tuple(bins), count)
                        bins, started, count = [math.nan] * 72, now, 0
                    if bins is None:
                        continue
                    count += 1
                    if quality and 0.05 <= distance <= 12.0:
                        index = int(angle // 5)
                        if math.isnan(bins[index]) or distance < bins[index]:
                            bins[index] = distance
        except Exception as error:
            self.error = str(error)
            self.latest = None

    def close(self):
        self.ended.set()
        if self.thread:
            self.thread.join(timeout=0.5)
        try:
            if self.port.is_open:
                self.command(0x25)
        except OSError:
            pass  # A lost USB link cannot receive Stop; drive cleanup is separate.
        finally:
            self.port.close()

