"""Preview tape steering or explicitly request a bounded ESP32 automatic session."""

import argparse
import json
import math
import re
import time
import urllib.error
import urllib.parse
import urllib.request


class ControlError(RuntimeError):
    def __init__(self, message, status=503):
        super().__init__(message)
        self.status = status


class ESP32AutoClient:
    """One leased automatic session, using the reviewed ESP32 HTTP API."""

    def __init__(self, address, timeout=0.15):
        parsed = urllib.parse.urlsplit(address)
        if parsed.scheme not in ("http", "https") or not parsed.hostname or (
            parsed.username or parsed.password or parsed.path not in ("", "/")
            or parsed.query or parsed.fragment
        ):
            raise ValueError("Use the ESP32 base address, for example http://192.168.4.1")
        self.address = address.rstrip("/")
        self.timeout = timeout
        self.session = None
        self.sequence = 0

    def request(self, endpoint, values=None):
        body = None if values is None else urllib.parse.urlencode(values).encode("ascii")
        request = urllib.request.Request(self.address + endpoint, data=body)
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = response.read(4097)
                if len(payload) > 4096:
                    raise ControlError("Unexpectedly large control response")
                return json.loads(payload) if payload else None
        except urllib.error.HTTPError as error:
            if error.code == 409:
                raise ControlError("Control session ended or another operator took over", 409) from None
            raise ControlError(f"ESP32 rejected the request (HTTP {error.code})", error.code) from None
        except (OSError, ValueError, urllib.error.URLError):
            raise ControlError("ESP32 control connection failed") from None

    def arm(self, expected_epoch=None):
        # Phone-initiated runs must use the epoch captured when Start was
        # pressed, so a later Stop or manual takeover cannot be bypassed.
        if expected_epoch is None:
            state = self.request("/state")
            epoch = state.get("epoch") if isinstance(state, dict) else None
        else:
            epoch = expected_epoch
        if type(epoch) is not int or not 0 <= epoch <= 0xFFFFFFFF:
            raise ControlError("ESP32 does not provide the expected session API")
        result = self.request("/auto/arm", {"epoch": epoch})
        if not isinstance(result, dict):
            raise ControlError("Invalid automatic arm response")
        token = result.get("session")
        if isinstance(token, str) and re.fullmatch("[0-9a-fA-F]{16}", token):
            self.session = token
        if not self.session or result.get("mode") != "auto" or (
            result.get("lease_ms") != 350 or result.get("max_auto_percent") != 35
        ):
            raise ControlError("ESP32 automatic mode configuration differs from the tested profile")
        self.sequence = 0

    def drive(self, left, right):
        if not self.session:
            raise ControlError("Automatic session is not armed")
        if any(type(value) is not int or not 0 <= value <= 35 for value in (left, right)):
            raise ValueError("Tape runs use forward wheel percentages from zero to thirty-five")
        self.sequence += 1
        self.request("/auto/drive", {
            "session": self.session, "seq": self.sequence, "l": left, "r": right,
        })

    def stop(self):
        if self.session:
            try:
                self.request("/auto/stop", {"session": self.session})
            except ControlError:
                pass  # A new manual owner is preserved; an expired lease already stops.
            finally:
                self.session = None

    def close(self):
        pass


def wheel_percentages(error):
    if not math.isfinite(error) or not -1 <= error <= 1:
        raise ValueError("Steering error must be finite and between minus one and one")
    correction = 0
    if abs(error) > 0.10:
        correction = max(1, round(abs(error) * 10))
        if error < 0:
            correction = -correction
    return 25 + correction, 25 - correction


def main(argv=None):
    from .line_preview import SnapshotReader, decide_tape, main as preview_main, positive_seconds, print_decision

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--drive", action="store_true", help="Explicitly arm the new ESP32 automatic firmware")
    link = parser.add_mutually_exclusive_group()
    link.add_argument("--esp32", help="Optional ESP32 HTTP address")
    link.add_argument("--serial", help="ESP32 USB port, default /dev/argus_esp32")
    parser.add_argument("--tape", choices=("black", "white", "blue"), default="black")
    parser.add_argument("--seconds", type=positive_seconds, default=10.0)
    parser.add_argument("--expected-epoch", type=int, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if not args.drive:
        return preview_main(["--tape", args.tape, "--seconds", str(args.seconds)])

    if args.serial:
        from .serial_control import SerialAutoClient
        client = SerialAutoClient(args.serial)
    else:
        client = ESP32AutoClient(args.esp32 or "http://127.0.0.1:8766", timeout=0.30)
    reader = SnapshotReader()
    clear_frames = 0
    ever_armed = False
    deadline = time.monotonic() + args.seconds
    next_frame_at = time.monotonic()
    print("Automatic tape session requested. Keep the operator Stop available.", flush=True)
    try:
        while time.monotonic() < deadline:
            delay = min(next_frame_at - time.monotonic(), deadline - time.monotonic())
            if delay > 0:
                time.sleep(delay)
            if time.monotonic() >= deadline:
                break
            started = time.monotonic()
            next_frame_at = started + 0.10
            frame = reader.read(timeout=min(0.20, deadline - started))
            decision = decide_tape(frame, args.tape)
            print_decision(decision)
            if time.monotonic() >= deadline:
                break
            if decision.state == "STOP" or not reader.is_fresh():
                clear_frames = 0
                if client.session:
                    print("Stopping automatic session because the tape or camera became uncertain.", flush=True)
                    return 1
                continue
            clear_frames += 1
            if clear_frames < 3:
                continue
            if not client.session:
                client.arm(expected_epoch=args.expected_epoch)
                ever_armed = True
                # Acquire another camera frame before the first nonzero request.
                continue
            if not reader.is_fresh():
                raise ControlError("Camera frame expired before steering")
            client.drive(*wheel_percentages(decision.error))
            if args.serial:
                client.relay_camera(frame)
    except KeyboardInterrupt:
        print("Operator ended the automatic session.", flush=True)
    except (ControlError, OSError, ValueError, RuntimeError) as error:
        print(f"STOP  {error}", flush=True)
        return 1
    finally:
        client.stop()
        client.close()
    print("Automatic session finished." if ever_armed else
          "No automatic session started; a clear tape view is required.", flush=True)
    return 0 if ever_armed else 1


if __name__ == "__main__":
    raise SystemExit(main())
