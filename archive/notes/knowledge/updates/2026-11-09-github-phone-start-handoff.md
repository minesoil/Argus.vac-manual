# GitHub and phone Start handoff — 2026-11-09

Justin selects minesoil/Argus.vac-manual for code/documentation records and
cannot reconnect the Pi now. Ethernet is disconnected. Published 55 reviewed
files under robot_control/ on main, preserving the existing README and website.
Verified PROJECT-STATUS.md by reading it back through the GitHub connector.
Commit: https://github.com/minesoil/Argus.vac-manual/commit/5287f98aeed327e59bbe068f0f162f3f81e00a1c

Includes source, tests, placeholder configurations, setup notes and progress.
Excludes real ESP config.h, firmware binaries, private raw archives and caches.
Future work should finish with a reviewed commit/push and dated progress entry.
No background synchronization service was installed.

Phone Start passed 88 local Python tests plus actual-sketch C++ and browser
tests; ESP32 target compile used 938244 bytes. Pi modules were copied and bridge
stopped on November 8. Pi tests did not run because the assumed interpreter
path was absent. ESP32 flash, bridge restart and live checks remain pending.
No new robot motion was commanded during this handoff.

Resume with motor power OFF: reconnect Ethernet, inspect actual service Python,
run checks, identify/flash ESP, verify upload, test phone Start/Stop without motor
power, restore bank-powered ESP, then raised-wheel and supervised floor checks.

Justin wants camera obstacle warning/stop after tape following. Documented next
step: stationary detector preview and measured misses/latency, then a shared
automatic stop gate; detours need verified clearance/range. No current obstacle
detection or navigation performance is claimed.
