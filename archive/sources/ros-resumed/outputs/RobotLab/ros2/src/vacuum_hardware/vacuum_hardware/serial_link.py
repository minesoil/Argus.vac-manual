"""Bounded serial I/O worker with an independent caller heartbeat.

The ROS timer cannot block on USB. If it stops updating commands, this worker
disables motion even while the serial thread itself is still running.
"""

import threading
import time
from .protocol import command, parse_status


class SerialLink:
    def __init__(self, port, baud=115200, factory=None):
        self.port, self.baud, self.factory = port, baud, factory
        self.lock = threading.Lock()
        self.stop = threading.Event()
        self.desired = (False, 0, 0)
        self.updated = 0
        self.status = None
        self.received = 0
        self.connected = False
        self.error = "Connecting"
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def update(self, enabled, left, right):
        with self.lock:
            self.desired = (bool(enabled), int(left), int(right))
            self.updated = time.monotonic()

    def snapshot(self):
        with self.lock:
            return self.connected, self.status, self.received, self.error

    def close(self):
        self.update(False, 0, 0)
        self.stop.set()
        self.thread.join(2)

    def run(self):
        sequence = 0
        while not self.stop.is_set():
            serial = None
            try:
                if self.factory is None:
                    from serial import Serial

                    serial = Serial(
                        self.port,
                        self.baud,
                        timeout=0,
                        write_timeout=0.1,
                        exclusive=True,
                    )
                else:
                    serial = self.factory()
                # Opening the Mega USB port may reset it. Zero frames cover its boot delay.
                with self.lock:
                    self.connected = True
                    self.status = None
                    self.error = "Waiting for Mega"
                    self.desired = (False, 0, 0)
                buffer = b""
                while not self.stop.is_set():
                    with self.lock:
                        desired, updated = self.desired, self.updated
                    if time.monotonic() - updated > 0.2:
                        desired = (False, 0, 0)
                    packet = command(sequence, *desired)
                    if serial.write(packet) != len(packet):
                        raise OSError("Incomplete serial write")
                    sequence = (sequence + 1) & 0xFFFF
                    buffer += serial.read(min(serial.in_waiting, 4096))
                    if len(buffer) > 4096:
                        buffer = b""
                        raise OSError("Malformed serial stream")
                    while b"\n" in buffer:
                        raw, buffer = buffer.split(b"\n", 1)
                        try:
                            status = parse_status(raw)
                        except (ValueError, UnicodeError):
                            raise OSError("Mega checksum or status error")
                        with self.lock:
                            self.status = status
                            self.received = time.monotonic()
                            self.error = ""
                    self.stop.wait(0.02)
            except Exception as exc:
                with self.lock:
                    self.connected = False
                    self.status = None
                    self.error = str(exc)
                    self.desired = (False, 0, 0)
                self.stop.wait(1)
            finally:
                if serial:
                    try:
                        serial.write(command(sequence, False, 0, 0))
                        serial.close()
                    except Exception:
                        pass
