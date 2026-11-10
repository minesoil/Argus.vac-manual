# Recorded Orange Pi commands

This is a selected command ledger recovered on 10 November 2026 from the saved work-session records. These commands were actually issued during Argus setup. Line breaks and indentation have been cleaned up; passwords, transfer payloads and unrelated computer commands are omitted. It is **not a complete terminal history or a script to run from top to bottom**.

The Pi already had Linux, ROS 2 Humble, camera software, VS Code Server and lidar workspaces when this work started. Their original installation commands have not been recovered. Repeating the commands below on a blank SD card would not recreate that existing installation.

Commands use the permissions of their recorded session. Package, boot and system-service changes were issued from a root shell. Application checks normally used the `orangepi` account. `sudo -u orangepi` runs a command as that regular account. Do not replace `/usr/bin/python3` with the old missing `~/argus/venv/bin/python` path.

## Evidence key

`L7` means the saved session ending `01a1b518-9f37-7e92-8d7a-cd8140a300da.jsonl`, stored under the private local Codex session folder for 7 November. `L8` means the saved session ending `01a1bac1-3afd-7f60-a548-811be13216bf.jsonl`, stored under 8 November; that record continues through 9 November. Event references below are JSONL line numbers at the time of this audit. These raw files contain private conversation and authentication material and are **not included in this handbook**.

Times below are the recorded UTC event times. Taiwan time is UTC + 8 hours. The human-readable project reports are:

- `knowledge/updates/2026-11-07-verified-orange-pi.md`
- `knowledge/updates/2026-11-07-esp32-unplug-camera.md`
- `knowledge/updates/2026-11-08-usb-tape-following.md`
- `knowledge/updates/2026-11-09-phone-start-installed.md`
- `workspace/robot_control/argus_avoidance/reports/ORANGE-PI-CHECK.md`

Those reports preserve milestones, but some earlier status paragraphs were superseded during the same long session. The source files and later commissioning evidence take precedence over an earlier pending-status paragraph.

## 1. What was already on the Pi

Verified board details: Orange Pi 5, hostname `orangepi5`, Orange Pi image 1.2.2, Ubuntu 22.04.5 Jammy ARM64, Python 3.10.12, ROS 2 Humble in `/opt/ros/humble`, regular account `orangepi`. The project was installed in `/home/orangepi/argus/avoidance`.

The existing camera service ran **uStreamer 4.9**. Its observed executable and arguments were:

```bash
/usr/bin/ustreamer --device=/dev/video0 --format=MJPEG --resolution=640x480 --host=127.0.0.1 --port=8080
```

Evidence: L7 event 1177, 7 November 14:18:55 UTC; service output at event 1180. This was inspected using:

```bash
/usr/bin/ustreamer --version
systemctl show argus-camera.service --property=ExecStart --value | sed -E 's/--(password|user) [^ ]+/--\1 [hidden]/g' | cut -c1-300
```

The complete original `argus-camera.service` unit and original camera installation procedure were not recovered in this audit. A new unit built around the observed command would be a **reconstruction**, rather than an exact copy of that original unit. The camera was verified online at 640 × 480; one early observation reported 60 captured frames/s. That is a dated capture observation, not a guaranteed processing rate.

## 2. Add the two ROS preview components

7 November 13:11:26 UTC, L7 event 603. This installed Collision Monitor and its lifecycle manager into the existing Humble installation. Five packages were added, approximately 7.6 MB. It did not install ROS itself.

```bash
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends --no-upgrade -o Acquire::Retries=0 -o Acquire::http::Timeout=8 -o Acquire::https::Timeout=8 install ros-humble-nav2-collision-monitor ros-humble-nav2-lifecycle-manager >/tmp/argus-setup.CFuv5z0f/nav2-install.log 2>&1
apt_result=$?
grep -E 'upgraded,|Need to get|After this operation|^Setting up|^E:' /tmp/argus-setup.CFuv5z0f/nav2-install.log | tail -9
printf 'Package installation exit %s\n' "$apt_result"
```

`/tmp/argus-setup.CFuv5z0f` was a session-specific transfer directory that had already been created. Do not assume it exists on another machine. The useful installation request is the `apt-get ... install` argument list; logging to this exact old directory is historical detail.

After the checked source ZIP was transferred and extracted into the new workspace, the recorded build was:

```bash
cd ~/argus/avoidance && colcon --log-base .ros/log build --base-paths . --packages-select argus_avoidance --build-base .ros/build --install-base .ros/install && source .ros/install/local_setup.bash && ros2 pkg prefix argus_avoidance
echo "Build exit $?"
```

Evidence: L7 event 665, 7 November 13:15:16 UTC. The terminal already had the ROS environment available. In a fresh terminal, `source /opt/ros/humble/setup.bash` is required first, as explained in `START-HERE.md`.

The first deployment ran `./argus status`, `./argus demo` and `./argus check`; 44 tests passed at that stage. A later isolated ROS test used `ROS_DOMAIN_ID=84` and `ROS_LOCALHOST_ONLY=1`, synthetic scans and synthetic transforms. All sampled command outputs remained zero. This is ROS preview verification, not a physical lidar or drive test.

## 3. Resolve the CH340 / BRLTTY USB conflict

8 November 08:59:44 UTC, L7 event 1799. BRLTTY was claiming the ESP32's CH340 USB interface. The recorded change preserved the vendor rule file and created a local copy with only the generic CH340 product match disabled.

```bash
systemctl stop argus-bridge.service brltty-udev.service
python3 - <<'ARGUSPY'
from pathlib import Path
vendor = Path('/usr/lib/udev/rules.d/85-brltty.rules')
override = Path('/etc/udev/rules.d/85-brltty.rules')
lines = vendor.read_text().splitlines(keepends=True)
matches = [i for i, line in enumerate(lines) if 'ENV{PRODUCT}=="1a86/7523/*"' in line]
assert len(matches) == 1, 'Expected one specific CH340 mapping'
assert not override.exists(), 'Existing local override needs review'
lines[matches[0]] = '# Argus ESP32 CH340 exception: ' + lines[matches[0]]
override.write_text('# Argus ESP32: vendor rules with the generic CH340 Braille match excluded.\n' + ''.join(lines))
print('Specific CH340 conflict override installed')
ARGUSPY
udevadm control --reload-rules
printf '%s' '7-1:1.0' > /sys/bus/usb/drivers/ch341/bind
udevadm settle
ls -l /dev/ttyUSB* /dev/serial/by-id/* 2>/dev/null
```

`7-1:1.0` was the USB interface present at that moment. It is not a universal CH340 identifier. The script deliberately refuses to overwrite an existing local override. A later `/dev/argus_esp32` alias was tied to a particular Pi USB socket. Current driving uses GPIO serial, so this alias is no longer the control link.

## 4. Prepare esptool 4.8.1 on the Pi

First an Ubuntu package install was attempted, 8 November 09:06:49 UTC, L7 event 1898:

```bash
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends --no-upgrade -o Acquire::Retries=0 -o Acquire::http::Timeout=8 install esptool > /tmp/argus-flashtool-apt.log 2>&1
echo "Flash tool install exit $?"
grep -E 'Need to get|After this operation|Setting up|^E:' /tmp/argus-flashtool-apt.log | tail -7
```

The later working flashing commands used a project-local copy of **esptool 4.8.1**, rather than relying on the first package's command-line entry point. The exact source download/extraction was recorded at L7 event 1952, 09:10:02 UTC:

```bash
python3 - <<'ARGUSPY'
import urllib.request, tarfile, io, json, importlib.util
from pathlib import Path
dest = Path('/home/orangepi/argus/.tools/esptool-src')
dest.mkdir(exist_ok=True)
meta = json.load(urllib.request.urlopen('https://pypi.org/pypi/esptool/4.8.1/json', timeout=8))
url = next(x['url'] for x in meta['urls'] if x['packagetype'] == 'sdist')
data = urllib.request.urlopen(url, timeout=10).read()
with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
    for member in archive.getmembers():
        if member.isfile() and '/esptool/' in member.name:
            relative = member.name.split('/esptool/', 1)[1]
            target = dest / 'esptool' / relative
            assert dest.resolve() in target.resolve().parents
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.extractfile(member).read())
print({x: bool(importlib.util.find_spec(x)) for x in ('serial', 'ecdsa', 'pyaes', 'bitstring', 'reedsolo', 'cryptography', 'yaml', 'intelhex')})
ARGUSPY
PYTHONPATH=/home/orangepi/argus/.tools/esptool-src python3 -m esptool version
```

The extra dependencies were then installed into that local directory, L7 event 1971, 09:10:29 UTC:

```bash
python3 -m pip --disable-pip-version-check install --only-binary=:all: --target /home/orangepi/argus/.tools/esptool-src 'bitstring==3.1.9' 'reedsolo==1.7.0' 'intelhex==2.3.0' > /tmp/argus-flash-deps.log 2>&1 && PYTHONPATH=/home/orangepi/argus/.tools/esptool-src python3 -m esptool version
echo "Vendor flasher setup exit $?"
```

This is the recovered historical installation method. Its download command pins a version but does not check a source-archive hash. It also relies on dependencies already supplied by the existing system/package installation. A new clean-install recipe can use a normal isolated Python environment, but must label that as a new recipe rather than claim it was the method originally used.

## 5. Enable the Pi's header UART

8 November 10:08:17 UTC, L7 event 3091. The existing boot file was backed up; the script checked that no `overlays=` line was already present before adding UART0 M2.

```bash
cp -n /boot/orangepiEnv.txt /home/orangepi/argus/.tools/live-flash/orangepiEnv-before-uart0.txt
python3 -c "from pathlib import Path; p=Path('/boot/orangepiEnv.txt'); t=p.read_text(); assert not any(s.startswith('overlays=') for s in t.splitlines()); p.write_text(t.rstrip()+'\noverlays=uart0-m2\n'); print('Enabled only uart0-m2')"
systemctl reboot
```

After reboot, `/dev/ttyS0` existed and UART0 was enabled in the live device tree. This exact command is not appropriate if another image already has overlays: its assertion should fail rather than erase them.

The final corrected wiring is Pi **physical 8 TX → ESP32 GPIO25 RX**, Pi **physical 10 RX ← ESP32 GPIO26 TX**, and Pi **physical 6 GND ↔ ESP32 GND**, at 115200 baud. Earlier notes copied incorrect TX/RX names from `gpio readall`; those instructions were corrected later. Use `PI-ESP32-WIRING.md` for the corrected map. Pi and ESP32 header signals are 3.3 V; none of these three wires supplies power.

## 6. Identify the programming target and test the installed Python code

9 November 13:19:07 UTC, L8 event 2633. Motor power had been confirmed OFF, the bridge had been stopped, and the ESP32 was connected by USB for upload.

```bash
PYTHONPATH=/home/orangepi/argus/.tools/esptool-src /usr/bin/python3 -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 115200 read_mac
```

The response identified the expected ESP32. A CH340 chip name alone was not treated as device identification. The three matching test files were copied from the staged phone-start bundle, then the actual system interpreter ran:

```bash
cd /home/orangepi/argus/avoidance
sudo -u orangepi /usr/bin/python3 -m unittest discover -s tests
```

88 tests passed at that point. This resolved the previous attempt to use a nonexistent virtual-environment interpreter. Later changes increased the test count; the latest recorded assisted-manual version passed 103 tests locally and on the Pi.

## 7. Install the assisted-manual Pi update

9 November 14:27:43 UTC, L8 event 3782. The reviewed ZIP had already been copied into the private staging directory. It contained changed files, not an entire fresh system image.

```bash
cd /home/orangepi/argus/.tools/obstacle-stage
unzip -oq assist-pi-stage-20261109.zip -d reviewed
cp -a /home/orangepi/argus/avoidance/argus_avoidance/usb_bridge.py /home/orangepi/argus/avoidance/argus_avoidance/serial_control.py /home/orangepi/argus/.tools/obstacle-stage/
install -o orangepi -g orangepi -m 644 reviewed/argus_avoidance/*.py /home/orangepi/argus/avoidance/argus_avoidance/
install -o orangepi -g orangepi -m 644 reviewed/tests/*.py /home/orangepi/argus/avoidance/tests/
install -o orangepi -g orangepi -m 755 reviewed/argus /home/orangepi/argus/avoidance/argus
cd /home/orangepi/argus/avoidance
sudo -u orangepi /usr/bin/python3 -m unittest discover -s tests
```

The camera observer service was installed at 14:29:18 UTC, L8 event 3801:

```bash
systemctl stop argus-obstacle-preview.service
install -m 644 /home/orangepi/argus/.tools/obstacle-stage/reviewed/systemd/argus-obstacle-preview.service /etc/systemd/system/argus-obstacle-preview.service
systemctl daemon-reload
systemctl enable --now argus-obstacle-preview.service
systemctl show argus-obstacle-preview.service -p FragmentPath -p ActiveState
cp -a /etc/systemd/system/argus-bridge.service.d/avoidance-usb.conf /home/orangepi/argus/.tools/obstacle-stage/avoidance-usb.before.conf
```

`install` copies a file and sets ownership/mode. `daemon-reload` makes systemd reread service definitions. `enable --now` arranges startup at boot and starts it immediately. The observer produces camera status; the bridge sends its reports to the ESP32, whose firmware enforces the manual-drive gate.

## 8. Flash the final assisted-manual application

9 November 14:36:12 UTC, L8 event 3903. The bridge had again been stopped. This writes firmware and resets the ESP32; it is not a status check. Motor power was OFF during commissioning.

```bash
PYTHONPATH=/home/orangepi/argus/.tools/esptool-src /usr/bin/python3 -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 115200 write_flash --flash_mode dio --flash_freq 80m --flash_size 4MB 0x10000 /home/orangepi/argus/.tools/obstacle-stage/esp32_wifi_controlcam_auto.ino.bin > /home/orangepi/argus/.tools/obstacle-stage/flash-assisted.log 2>&1
result=$?
tail -n 8 /home/orangepi/argus/.tools/obstacle-stage/flash-assisted.log
echo FLASH_EXIT=$result
```

The final application was 941568 bytes with SHA-256 `fbc4e7bc6b32263d2866c546ff624dbcaebe4598dac0179ac8768f2fbec5ddba`. The write completed with hash verification and exit 0. Firmware binaries and full flash backups are excluded because they can contain private hotspot settings. Build from the included source and your own private configuration instead.

An earlier first installation also wrote the bootloader at `0x1000`, partition table at `0x8000`, boot helper at `0xe000` and application at `0x10000` (L7 event 2103). The later command above updates the application on that already prepared board; it is not a complete blank-flash procedure.

## 9. Activate the matching bridge and calibrate the stationary view

9 November 14:38:04 UTC, L8 event 3923:

```bash
install -m 644 /home/orangepi/argus/.tools/obstacle-stage/argus-bridge-avoidance.conf /etc/systemd/system/argus-bridge.service.d/avoidance-usb.conf
systemctl daemon-reload
systemctl start argus-bridge.service
```

The existing base `argus-bridge.service`, read at L8 event 2629, was:

```ini
[Unit]
Description=Argus Vac ESP32 Camera Bridge
Requires=argus-camera.service
After=argus-camera.service

[Service]
Type=simple
User=orangepi
SupplementaryGroups=dialout
ExecStart=/usr/bin/python3 -u /home/orangepi/argus/camera_sender.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

The installed drop-in clears that original `ExecStart` and replaces it with:

```ini
[Unit]
Description=Argus ESP32 serial control bridge
Wants=argus-obstacle-preview.service
After=argus-obstacle-preview.service

[Service]
WorkingDirectory=/home/orangepi/argus/avoidance
ExecStart=
ExecStart=/usr/bin/python3 -u -m argus_avoidance.usb_bridge --serial /dev/ttyS0 --no-phone-preview --manual-guard
Restart=on-failure
RestartSec=2
```

The full drop-in and observer unit are included with the Pi source. The original `camera_sender.py` was superseded by the drop-in and was not recovered as a reviewed source file in this audit. The module name `usb_bridge` remains for compatibility even though its current serial port is the GPIO UART.

With the robot stopped and motor power OFF, the recorded calibration command was L8 event 3929, 14:38:12 UTC:

```bash
cd /home/orangepi/argus/avoidance
sudo -u orangepi /usr/bin/python3 -m argus_avoidance.obstacles --profile .state/floor.json --calibrate --sample .04 .86 .25 .98
```

The four sample numbers are normalized image coordinates for the small floor patch chosen in that scene. They are not a universal floor sample. The resulting `.state/floor.json` is a scene-dependent calibration with an expiry; a new session needs an appropriate clear patch. This is a floor-appearance detector, not a trained object-recognition model or a measured distance sensor.

The real phone showed the new assisted/manual controls and refused assisted driving while the camera reported blocked/unavailable. Later a paper-covered view reported CLEAR. A held-joystick object-placement stop test had been requested but no user result was recorded before this documentation task. Do not describe obstacle braking on the floor as validated.

## 10. Reusable checks present in the source

These are current documented commands, rather than a claim that every line below was issued together in one recorded event:

```bash
cd /home/orangepi/argus/avoidance
./argus status
./argus check
./argus obstacle-status
curl --max-time 5 -sS http://127.0.0.1:8766/state
systemctl is-active argus-camera.service argus-obstacle-preview.service argus-bridge.service
journalctl -u argus-bridge.service -n 30 --no-pager
systemctl show argus-bridge.service -p NRestarts -p ExecMainStatus
```

`./argus line-preview --seconds 3` reads the camera and prints decisions without starting a drive session. `./argus preview` launches the isolated ROS lidar preview with output disabled. The actual line follower and assisted-manual serial bridge currently work without ROS in their drive path.

## What still needs an honest reconstruction label

- Installing the original SD-card Linux image, creating its accounts and the original ROS 2 Humble installation: already present at first connection.
- Installing OpenCV, NumPy, uStreamer 4.9, the original camera unit, VS Code Server and existing lidar workspaces: present, but their original installation commands were not recovered here. Do not claim they were newly installed by this work.
- Replacing a lost camera unit: the exact observed uStreamer executable and arguments are preserved above; surrounding unit permissions/restart settings would be a newly authored service.
- Rebuilding a fresh Pi from the current complete source: the old staged update ZIPs were incremental. Use the handbook's clean-install recipe and mark it as reconstructed from the installed layout and current source.
- The Mega currently driving Argus was deliberately not reflashed during these Pi/ESP32 changes. Its exact installed sketch must be distinguished from plausible historical copies.
- ROS lidar preview tests used synthetic scans. The RPLIDAR C1 was reported faulty and real `/scan` reception was not established. Tape steering, ROS preview and manual camera assistance are separate evidence trails.

No hardware connection or robot command was made while preparing this ledger.
