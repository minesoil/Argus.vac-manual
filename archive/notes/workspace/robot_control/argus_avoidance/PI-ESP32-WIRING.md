# Orange Pi to ESP32: three-wire serial connection

This connection keeps camera processing and automatic control on the Pi.
The phone stays on the ESP32 hotspot; the ESP32 keeps its existing Mega link.
The GPIO wires carry commands and replies at 115200 baud. USB supplies ESP32
power; the automatic bridge uses `/dev/ttyS0` instead of the USB adapter.

Turn motor power off. Shut the Pi down, then disconnect its power and the
ESP32's USB power before adding these wires.

| Orange Pi 5 physical header pin | ESP32 printed GPIO label | Purpose |
| --- | --- | --- |
| **8 — TXD.0** | **25** | Pi transmits; ESP32 receives. |
| **10 — RXD.0** | **26** | ESP32 transmits; Pi receives. |
| **6 — GND** | **GND** | Shared signal ground. |

Pi numbers are physical header positions. ESP32 numbers are the printed GPIO
labels. Find the Pi header's pin-1 marker first: the pairs are 1/2, 3/4, 5/6,
7/8, 9/10 and so on. Pins 6, 8 and 10 are the third, fourth and fifth pins in
the even-numbered row or column, counted from the pin-2 end. Justin's stated
orientation has two horizontal rows of 13 pins, with 2 at the top-left and 25
at the bottom-right. In that orientation the top row runs 2, 4, 6, 8, 10 through
26 from left to right; the bottom row runs 1, 3, 5 through 25. The three wires
therefore go on the top row: third from left is 6/GND, fourth is 8/TX to ESP25,
and fifth is 10/RX from ESP26. These are 3.3 V signals;
the three-wire connection includes no 5 V or 3.3 V power pin.

Correction, November 8: the installed wiringOP display reverses the UART0
RX/TX names. Use the manufacturer's physical pad mapping and the Rockchip
[UART0 M2 definitions](https://github.com/torvalds/linux/blob/master/arch/arm64/boot/dts/rockchip/rk3588-base-pinctrl.dtsi):
GPIO4_A3 (physical8) is TX; GPIO4_A4 (physical10) is RX.
The earlier guide had these reversed; no physical jumper installation was confirmed.
The firmware configures ESP32 `Serial1` with RX=25 and TX=26 using the
[Espressif serial API](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/serial.html).

After wiring, restore Pi and ESP32 USB power and keep motor power off for the
communication and phone Stop checks. The Pi's `uart0-m2` overlay is enabled in
`/boot/orangepiEnv.txt`; the serial bridge is configured for `/dev/ttyS0`.
The phone video relay remains paused. The Pi still processes 640 × 480 images.

USB disconnections were observed on both Pi USB controllers. GPIO bypasses the
USB data adapter; testing must still establish whether the ESP32's own power
stays stable. A board power reset would also interrupt the GPIO connection.

Preview is `./argus follow`. After physical direction and Stop checks, an
explicit bounded run is `./argus follow --drive --seconds 3`. The ESP32 starts
stopped and its 350 ms command lease remains active on this transport.
