# Offline checks — 10 November 2026

These checks ran on the laptop against the sanitized handbook source copy.
No robot connection, flash or motor command occurred.

| Check | Result |
|---|---|
| Python suite using `py -3.12 -m unittest discover -s tests -v` | 103 tests passed in18.932s; no skipped tests |
| Actual-sketch C++ host check | Passed |
| Phone Start C++ check | Passed |
| Embedded browser JavaScript check | Passed |
| ESP32 target compile, dummy configuration | Passed with core3.3.11, nodemcu-32s |
| Dashboard browser checks using existing Playwright test | Passed: rendering, safe input, discovery, search, links, mobile width and fallback paths |

The Python suite was run in `code/robot_control/argus_avoidance`. Python3.12
has the required NumPy and OpenCV here. These results check software behavior;
they do not complete the pending real-camera held-joystick stop test.

See [the firmware check detail](OFFLINE_FIRMWARE_CHECKS.md) for exact host
and target-compile commands, outputs and the dummy-build hash. The example
configuration build differs from the private binary uploaded on November9.

All 74 file hashes/sizes and 72 comparisons against maintained source passed
an independent review. The dashboard README deployment template intentionally
uses repository-root links; other handbook links are checked in their local
context. A fresh spare-Pi installation remains untested.
