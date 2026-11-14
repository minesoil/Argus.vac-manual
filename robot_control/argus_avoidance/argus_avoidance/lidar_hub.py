"""Single C1 scanner owner with a best-effort ESP32 USB map relay.

Navigation reads the original Sweep from ``latest``. The map is display-only:
an absent or disconnecting ESP32 USB port cannot affect the GPIO drive link.
"""

import math
import struct
import threading
import time

from .c1 import C1Reader


C1_PORT = ("/dev/serial/by-id/"
           "usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0")
ESP_PORT = "/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0"
MAP_MAGIC = b"AVL1"
MAP_BINS = 72
MAP_INTERVAL_S = 0.25
SCAN_MAX_AGE_S = 0.6
USB_RETRY_S = 2.0


def map_frame(sweep, front_deg=90.0):
    """Encode raw C1 returns, rotated so bin zero faces robot-forward.

    Each byte is a range from the C1 scan center in 5 cm steps, capped at
    12 m (240). Zero means unknown. The phone draws rays from the sensor's
    +8 cm body offset.
    """
    if not math.isfinite(front_deg) or len(sweep.ranges) != MAP_BINS:
        raise ValueError("Expected finite forward angle and 72 C1 bins")
    first = int((front_deg % 360.0) // 5.0)
    payload = bytearray(MAP_BINS)
    for index in range(MAP_BINS):
        distance = sweep.ranges[(first + index) % MAP_BINS]
        if math.isfinite(distance) and distance > 0:
            payload[index] = min(240, max(1, int(distance * 20 + 0.5)))
    return MAP_MAGIC + struct.pack("<I", MAP_BINS) + payload


class LidarHub:
    """Keep one C1Reader open and send fresh maps over independent USB serial."""

    def __init__(self, lidar_port=C1_PORT, esp_port=ESP_PORT, *,
                 front_deg=90.0, reader_factory=C1Reader, serial_factory=None,
                 clock=time.monotonic):
        if not math.isfinite(front_deg):
            raise ValueError("front_deg must be finite")
        self.lidar_port = lidar_port
        self.esp_port = esp_port
        self.front_deg = front_deg
        self.reader_factory = reader_factory
        self.serial_factory = serial_factory
        self.clock = clock
        self._reader = None
        self._start_error = None
        self._map_port = None
        self.map_error = None
        self._last_sent_sequence = None
        self._last_sent_at = -math.inf
        self._next_usb_attempt = -math.inf
        self._lock = threading.Lock()

    @property
    def latest(self):
        return self._reader.latest if self._reader is not None else None

    @property
    def error(self):
        return self._reader.error if self._reader is not None else self._start_error

    def start(self):
        """Start acquisition once. Let the caller handle C1 startup failure."""
        with self._lock:
            if self._reader is not None:
                return self
            reader = None
            try:
                reader = self.reader_factory(self.lidar_port)
                reader.start()
            except (OSError, ValueError) as exc:
                self._start_error = str(exc)
                if reader is not None:
                    reader.close()
                raise
            self._reader = reader
            self._start_error = None
            return self

    def _open_map_port(self):
        factory = self.serial_factory
        if factory is None:
            from serial import Serial
            factory = Serial
        port = factory(port=None, baudrate=115200, timeout=0,
                       write_timeout=0.15)
        # Set modem lines before opening: ESP32 CH340 auto-reset circuits can
        # toggle EN/BOOT when DTR or RTS is asserted.
        port.dtr = False
        port.rts = False
        port.port = self.esp_port
        try:
            port.open()
        except OSError:
            port.close()
            raise
        self._map_port = port

    def _drop_map_port(self):
        port, self._map_port = self._map_port, None
        if port is not None:
            try:
                port.close()
            except OSError:
                pass

    def open_map_port(self):
        """Best-effort USB open before the GPIO handshake; never open the C1."""
        with self._lock:
            if self._map_port is not None:
                return True
            now = self.clock()
            if now < self._next_usb_attempt:
                return False
            try:
                self._open_map_port()
            except OSError as exc:
                self.map_error = str(exc)
                self._next_usb_attempt = now + USB_RETRY_S
                return False
            self.map_error = None
            return True

    def relay_once(self):
        """Try one fresh, unsent map. USB errors never propagate to navigation."""
        with self._lock:
            reader = self._reader
            sweep = reader.latest if reader is not None and not reader.error else None
            if sweep is None or sweep.sequence == self._last_sent_sequence:
                return False
            now = self.clock()
            age = now - sweep.started
            if age < 0 or age > SCAN_MAX_AGE_S or now - self._last_sent_at < MAP_INTERVAL_S:
                return False
            if self._map_port is None and now < self._next_usb_attempt:
                return False
            try:
                if self._map_port is None:
                    self._open_map_port()
                packet = map_frame(sweep, self.front_deg)
                if self._map_port.write(packet) != len(packet):
                    raise OSError("Incomplete ESP32 map write")
            except OSError as exc:
                self.map_error = str(exc)
                self._next_usb_attempt = now + USB_RETRY_S
                self._drop_map_port()
                return False
            self.map_error = None
            self._last_sent_sequence = sweep.sequence
            self._last_sent_at = now
            return True

    def close(self):
        with self._lock:
            self._drop_map_port()
            reader, self._reader = self._reader, None
            if reader is not None:
                reader.close()
