# USB check after Justin unplugged the ESP32

Justin reported unplugging the ESP32 on November 7. A new SSH check against
`orangepi5` found only the USB camera among non-hub USB devices. The previously
observed CH340 on USB port 4-1 had disconnected. Its disappearance after this
change suggests the adapter was associated with the ESP32 connection. Positive
identification of the C1 still requires a separate check.

`argus-camera.service` was actively reading `/dev/video0`. Its uStreamer source
reported online at 640 × 480 and 60 captured frames/s at the check. Two JPEG
snapshots from the Pi's loopback service differed, and a fresh frame decoded
at 640 × 480. The ten-second `./argus scan` listener received no scan. SSH
worked. Wheel drive, wireless manual control and object detection were not
exercised during this sensor check.
