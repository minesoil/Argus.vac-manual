@echo off
"C:\Program Files\WSL\wsl.exe" -d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws --exec python3 tools/run_sim.py
pause
