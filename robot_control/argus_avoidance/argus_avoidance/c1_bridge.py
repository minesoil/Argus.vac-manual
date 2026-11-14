"""Read C1 revolutions from the Pi bridge, which owns the lidar serial port."""

import json
import math
import urllib.request

from .c1 import Sweep


class BridgeC1Reader:
    def __init__(self, url="http://127.0.0.1:8766/lidar/sweep", timeout=0.20):
        self.url = url
        self.timeout = timeout
        self.error = None

    def start(self):
        return self

    @property
    def latest(self):
        try:
            with urllib.request.urlopen(self.url, timeout=self.timeout) as response:
                data = json.load(response)
            value = data.get("sweep")
            if value is None:
                return None
            ranges = tuple(math.nan if item is None else float(item)
                           for item in value["ranges"])
            if (len(ranges) != 72 or type(value["sequence"]) is not int or
                    value["sequence"] <= 0):
                raise ValueError("Invalid bridged C1 sweep")
            return Sweep(value["sequence"], float(value["started"]),
                         float(value["finished"]), ranges, int(value["nodes"]))
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise OSError("C1 bridge unavailable or invalid") from error

    def close(self):
        pass
