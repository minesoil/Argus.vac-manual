# Linux, SSH and VS Code without guessing

The Pi is a separate computer running Linux. SSH opens a terminal on that
computer over the network. VS Code Remote SSH gives you a file editor and
terminal on the same remote computer. Opening `localhost` in your laptop's
browser alone does not prove a connection to the Pi.

## Connect later, when Argus is available

The recorded Ethernet address was `192.168.137.195`. It may change. From
Windows PowerShell, the historical connection shape is:

```powershell
ssh root@192.168.137.195
```

Enter your private password when SSH asks. It is deliberately not in this
guide. The initial maintenance sessions used root; routine file work and
services use `orangepi`. If that account's SSH login is configured, prefer
`ssh orangepi@192.168.137.195`. This guide has not created a new login or key.
Check an unexpected SSH host-key change before accepting it.

In VS Code, choose **Remote-SSH: Connect to Host**, select the Pi, and open
`/home/orangepi/argus/avoidance`. The bottom-left remote indicator should name
the SSH host. **Terminal → New Terminal** then runs commands on the Pi.

Verify where you are:

```bash
hostname
whoami
pwd
```

`root` is the administrator. `orangepi` is the everyday account. `pwd` prints
the current folder. `~` is the home folder of the current user: for root it
is `/root`, so `~/argus` is not the robot folder when logged in as root.
The commands below therefore use absolute `/home/orangepi/...` paths.

## Commands you will keep using

| Example | Meaning |
|---|---|
| `cd /home/orangepi/argus/avoidance` | Change the terminal's current folder. |
| `ls -la` | List files, including hidden files. |
| `cat package.xml` | Print a text file. |
| `less START-HERE.md` | Read a long file; press `q` to leave. |
| `./argus check` | Run the `argus` script in this folder with argument `check`. |
| `/usr/bin/python3 -m argus_avoidance.obstacles --help` | Run a Python module and show its options. |
| `sudo systemctl status argus-bridge.service --no-pager` | Ask Linux about the background bridge. |
| `journalctl -u argus-bridge.service -n 50 --no-pager` | Read its last 50 log entries. |
| `source /opt/ros/humble/setup.bash` | Load ROS command paths into this terminal. |

`sudo` runs one command with administrator privileges. `systemd` is the
background-program manager; a `.service` file tells it what to run.
`enable` arranges startup on future boots; `start` starts it now; `restart`
stops and starts it. Services running does not mean the robot should move.
Current firmware starts stopped until a person selects a mode.

`Ctrl+C` interrupts a foreground program. It does not necessarily stop a
separate system service. Use the phone STOP and switch motor power off before
maintenance; don't depend on closing an SSH window to stop the robot.

## Ports and localhost

| Address as seen **on the Pi** | Purpose |
|---|---|
| `http://127.0.0.1:8080` | Camera server |
| `http://127.0.0.1:8766/state` | Serial bridge state |
| `http://127.0.0.1:8767/status` | Obstacle preview status |
| `http://192.168.4.1` on a phone joined to ESP hotspot | ESP32 phone controls |

`127.0.0.1` means the machine making the request. To see the Pi preview from
a Windows laptop, a tunnel forwards a laptop port to a Pi port:

```powershell
ssh -L 127.0.0.1:18767:127.0.0.1:8767 -L 127.0.0.1:18080:127.0.0.1:8080 root@192.168.137.195
```

Keep that SSH window open, then visit `http://127.0.0.1:18767` on the laptop.
The second forward exposes the camera at laptop port18080. It does not make
these services public on the internet. A low-resolution or paused phone image
does not establish the resolution or freshness of the Pi's own processing.
