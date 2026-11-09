"""
virtual_mega.py - Software twin of mega-controller.ino's serial behavior.

Used by test_protocol.py and test_lidar.py so hardware is never required to
prove the Pi<->Mega contract. Mirrors: boot banner (HALTED), P/S/B/V/H/G
handling, R threat packets with AUTO-HALT at risk >= AUTO_HALT_RISK, ERR on
unknown commands.
"""
import socket
import threading

AUTO_HALT_RISK = 85  # keep identical to firmware #define


class VirtualMega:
    def __init__(self, port=0):
        srv = socket.socket()
        srv.bind(("127.0.0.1", port))
        self.port = srv.getsockname()[1]
        srv.listen(1)
        srv.settimeout(5.0)
        self.srv = srv
        self.log = []           # ("TX"/"RX", line) in order
        self.log_lock = threading.Lock()
        self.halted = True
        self.running = True

    def start(self):
        threading.Thread(target=self._serve, daemon=True).start()

    def _serve(self):
        conn, _ = self.srv.accept()
        conn.settimeout(0.2)
        self.conn = conn
        self._emit("ARGUS-MEGA up. HALTED. Send P to ping.")
        buf = b""
        while self.running:
            try:
                data = conn.recv(256)
            except socket.timeout:
                continue
            except OSError:
                break
            if not data:
                break
            buf += data
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                self._handle(line.decode("ascii", "replace").strip())

    def _emit(self, msg):
        try:
            self.conn.sendall((msg + "\n").encode("ascii"))
        except OSError:
            pass
        with self.log_lock:
            self.log.append(("TX", msg))

    def _handle(self, line):
        with self.log_lock:
            self.log.append(("RX", line))
        parts = line.split(" ")
        cmd = parts[0] if parts else ""
        arg = parts[1] if len(parts) > 1 else ""
        rest = parts[1:] if len(parts) > 1 else []

        if cmd == "P":
            self._emit("ACK ARGUS-MEGA ready")
        elif cmd == "H":
            self.halted = True
            self._emit("HALT latched")
        elif cmd == "G":
            self.halted = False
            self._emit("Halt released (actuators still OFF until commanded)")
        elif cmd == "S":
            if not self.halted and arg == "1":
                self._emit("Drive ON")
            else:
                self._emit("Drive OFF")
        elif cmd == "B":
            self._emit("Brushes ON" if (not self.halted and arg == "1") else "Brushes OFF")
        elif cmd == "V":
            self._emit("Vacuum ON" if (not self.halted and arg == "1") else "Vacuum OFF")
        elif cmd == "R":
            name = rest[0] if rest else "-"
            try:
                risk = int(rest[1]) if len(rest) > 1 else 0
            except ValueError:
                risk = 0
            if risk >= AUTO_HALT_RISK and not self.halted:
                self.halted = True
                self._emit(f"AUTO-HALT: camera threat {name} risk {risk}")
            else:
                self._emit(f"Threat noted: {name} {risk}")
        else:
            self._emit("ERR unknown command")


class SocketSerial:
    """Duck-types the pyserial Serial object for v10._serial_send()."""

    def __init__(self, port):
        self.sock = socket.create_connection(("127.0.0.1", port), timeout=5)
        self.sock.settimeout(0.1)

    def write(self, data: bytes):
        self.sock.sendall(data)

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass
