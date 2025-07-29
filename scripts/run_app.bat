@echo off
echo ========================================
echo Starting KOSA Document Translator
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Streamlit is not installed
    echo Please run install.bat first
    pause
    exit /b 1
)

echo Starting the application...
echo The app will open in your default browser
echo.
echo Press Ctrl+C to stop the application
echo.

streamlit run app.py
