# C1 roaming prototype — 14 November 2026

Justin requests wall/obstacle avoidance for a room tonight and an outdoor
Hsinchu showcase tomorrow. He later clarifies the outdoor area may be open;
floor tape can mark it for an operator but cannot be sensed by the C1.

Implemented a C1 reader, coverage checks, reactive stop/turn/continue runner,
separate phone roaming Start, and opt-in measured configuration. Unknown or
stale scans stop the session; Stop cannot be automatically overridden. The
example profile disables roaming until physical commissioning is complete.
See `robot_control/LIDAR-ROAMING.md` for method, calibration and limits.

Laptop verification: 114 Python tests passed; C++ host tests exercised actual
firmware routes including separate roaming Start, pivot and Stop; browser tests
passed; ESP32 Arduino target compiled with example configuration (942120 bytes).
An initial full Python run showed one timing-sensitive existing tape test fail;
it passed in isolation and in the later full suite. These are software results.

Justin says motor power is OFF and Pi, Ethernet and C1 are connected. Pi SSH at
192.168.137.195 responds but rejected key-based login; prior credentials were not
recoverable. No new code has been installed, flashed, run on Pi, or tested on
the robot. Sensor orientation and position, footprint, wheel pivot direction,
braking, scan coverage and outdoor performance remain unmeasured. The prior
three-second C1 laptop scan succeeded, but this new reader has not seen live data.

Justin says laptop internet sharing must be switched off and on again after a
laptop restart for sharing to the Pi to work; this restored reachability today.
