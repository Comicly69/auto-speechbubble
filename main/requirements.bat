@echo off

echo Installing pillow...
pip install pillow
if errorlevel 1 (
    echo Failed to install pillow. Please try again.
    pause
    exit /b 1
)

echo Installing requests...
pip install requests
if errorlevel 1 (
    echo Failed to install requests. Please try again.
    pause
    exit /b 1
)

echo Installing pyperclip...
pip install pyperclip
if errorlevel 1 (
    echo Failed to install pyperclip. Please try again.
    pause
    exit /b 1
)

echo All requirements have been installed.
pause
exit /b 0
