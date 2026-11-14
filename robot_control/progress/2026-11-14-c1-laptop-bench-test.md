# C1 laptop bench test — 2026-11-14

Justin reports completing C1-to-CP2102 wiring, plugging into the laptop and seeing the adapter LED. Windows identifies Silicon Labs CP210x USB to UART Bridge on COM3 (VID 10C4, PID EA60).

At 460800 baud, 8N1, with hardware flow control and DTR/RTS disabled, live GET_INFO returned a valid 20-byte payload (model byte 0x41, firmware 1.02, hardware byte 0x12). GET_HEALTH returned status 0 and error code 0.

A bounded three-second normal SCAN returned 22,927 bytes, the expected 5-byte-node/0x81 stream descriptor, 4,584 structurally valid measurement nodes, nine revolution markers and 4,153 positive-distance samples with nonzero quality. Observed ranges were 138.5–3376 mm (mean 791.9 mm). This is live scanner data, not a simulated result or a calibration/accuracy test.

STOP was sent in cleanup; a subsequent 300 ms idle check found zero streaming bytes. A fresh GET_HEALTH again returned status 0/error 0. Serial port closed. No robot drive commands were sent. Physical motor standstill was not directly observed; ask Justin if needed.

This supersedes unknown C1 communication/function and adapter-only-LED evidence: bidirectional UART, device health and a short live ranging stream now pass through the new adapter/wiring. Sustained power margin, calibrated accuracy, stable target scan rate, mechanical installation and Orange Pi/ROS integration remain unverified. Exact soldering/pin placement and voltage/current were not physically inspected or measured. Earlier failed component remains unidentified.
