# Argus robot control

Current maintained Pi and ESP32 source, tests, configuration examples and
dated reports. Start with [PROJECT-STATUS.md](PROJECT-STATUS.md).

- [Pi commands and phone operation](argus_avoidance/START-HERE.md)
- [Camera-assisted manual prototype](ASSISTED-MANUAL.md)
- [Pi/ESP32 wiring](argus_avoidance/PI-ESP32-WIRING.md)
- [ESP32 source](firmware/esp32_wifi_controlcam_auto/README.md)
- [Rebuild and learning handbook](https://github.com/minesoil/Argus.vac-manual/tree/main/handbook)

The physical camera/manual route uses Python and GPIO UART. ROS 2 Humble is
installed for a separate, output-disabled LiDAR preview; it does not currently
control this drive route. The LiDAR is unavailable. Keep historical test
reports separate from new physical results.
