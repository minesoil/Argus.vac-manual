@echo off
powershell.exe -NoProfile -STA -File "%~dp0Vacuum-Lab.ps1"
if errorlevel 1 pause
