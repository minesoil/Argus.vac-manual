# Rebuilding and understanding Argus

Prepared 10 November 2026. This is a dated source snapshot and a practical
rebuild guide, written while Justin is away from the robot. No robot was
connected, powered, flashed or driven for this documentation session.

Start with [what works and what remains](00_CURRENT_STATE.md), then
[how the boards connect](01_HOW_IT_WORKS.md). For commands, open
[the Pi setup walkthrough](03_PI_SETUP.md) and the separate
[recorded command ledger](commands/RECORDED_PI_COMMANDS.md).

## Read in this order

| File | What it answers |
|---|---|
| [00_CURRENT_STATE.md](00_CURRENT_STATE.md) | What is actually installed or tested? |
| [01_HOW_IT_WORKS.md](01_HOW_IT_WORKS.md) | What does each board do? Where does a stop go? |
| [02_LINUX_AND_VSCODE.md](02_LINUX_AND_VSCODE.md) | Which computer am I typing on? What do Linux commands mean? |
| [03_PI_SETUP.md](03_PI_SETUP.md) | How would I put the Pi files and services back? |
| [04_FIRMWARE.md](04_FIRMWARE.md) | How do I build the ESP32 code, and which Mega sketch do I have? |
| [05_CODE_TOUR.md](05_CODE_TOUR.md) | Which source file should I read or change? |
| [06_CHECKS_AND_FIRST_TESTS.md](06_CHECKS_AND_FIRST_TESTS.md) | What can I check at school, and what needs the robot? |
| [07_ROS_2_WITH_ARGUS.md](07_ROS_2_WITH_ARGUS.md) | What is ROS 2, and how could it join this project? |
| [08_KEEPING_RECORDS.md](08_KEEPING_RECORDS.md) | How do I keep the guide, code and GitHub in sync? |

## Included code

`code/robot_control/` contains the reviewed Pi package, ESP32 sketch, tests,
configuration examples and existing reports. `code/mega-reference/` contains
the best recovered Mega baseline and its original source, clearly marked as
references because the exact running Mega firmware has not been identified.
`code/dashboard/` contains the file dashboard source. See
[the file-by-file index](inventory/FILES.md) and [hash manifest](inventory/manifest.json).

The code copies are a **snapshot**. The maintained public source is
[robot_control on GitHub](https://github.com/minesoil/Argus.vac-manual/tree/main/robot_control).
Edit that source first, then regenerate this snapshot. Each inventory entry
records where its file came from and its SHA-256 hash.

The [offline verification record](evidence/OFFLINE_CHECKS_2026-11-10.md)
includes 103 passing Python tests, host/browser checks and an ESP32 target
compile from the included source with dummy settings.

Historical Obsidian notes, saved Gemini chats and images remain in the
[reviewed public archive](https://github.com/minesoil/Argus.vac-manual/tree/main/archive).
They are not needed in a fresh Pi installation. Unknown initial Linux setup,
private passwords, actual Wi-Fi configuration, calibration data and compiled
firmware are intentionally absent. Third-party libraries are dependencies,
not project-authored source.

## How exact is this?

The recorded ledger quotes recovered commands with private values removed.
The walkthrough is an ordered recipe assembled from those commands and the
current source; reconstructed steps are labeled. The complete original Linux
image, initial ROS installation history and exact Mega binary were not saved,
so this is not a claim of a bit-for-bit disk recovery. A fresh rebuild has not
been run on spare hardware.

This guide records the integration Justin built and tested with AI assistance.
It explains the work rather than inventing a personal command history. Being
able to trace a camera reading to a motor stop, change a setting deliberately,
and explain a test result is a useful way to show ownership of the project.
