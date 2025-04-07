@echo off
cls
REM Change to the directory where the .bat file is located
cd /d "%~dp0"

REM Check if Python is installed
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed or not added to PATH.
    pause
    exit /b
)

REM Run the Python script
python ts-gui_boot_lanpack_eng.py || (
    echo Failed to execute the Python script using the default Python command.
    REM Fallback to a specific Python path
    set PYTHON_PATH=C:\Users\tadeo\AppData\Local\Programs\Python\Python313\python.exe
    if exist "%PYTHON_PATH%" (
        "%PYTHON_PATH%" ts-gui_boot_lanpack_eng.py
    ) else (
        echo Python executable not found at %PYTHON_PATH%.
        pause
        exit /b
    )
)

pause