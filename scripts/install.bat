@echo off
echo ========================================
echo KOSA Document & Image Translator Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Python found. Checking version...
python --version

echo.
echo Installing required packages...
echo This may take a few minutes...
echo.

REM Upgrade pip first
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install some packages
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo To start the application:
echo 1. Open Command Prompt or PowerShell
echo 2. Navigate to this folder
echo 3. Run: streamlit run app.py
echo.
echo Or simply double-click on 'run_app.bat'
echo.
pause
