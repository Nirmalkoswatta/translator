@echo off
title KOSA Document Translator - Quick Launcher
color 0A

echo.
echo     ╔═══════════════════════════════════════════════════╗
echo     ║          🌍 KOSA Document Translator 🌍           ║
echo     ║                 Quick Launcher                   ║
echo     ╚═══════════════════════════════════════════════════╝
echo.
echo     Choose your version:
echo.
echo     [1] Basic Version (Current - Ready to use!)
echo     [2] Full Version (Requires additional packages)
echo     [3] Install Required Packages
echo     [4] Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto basic
if "%choice%"=="2" goto full
if "%choice%"=="3" goto install
if "%choice%"=="4" goto exit
goto menu

:basic
echo.
echo Starting Basic Version...
echo ✅ Ready to use with demo features
echo 🌐 Will open in your browser shortly
echo.
streamlit run app_basic.py
goto end

:full
echo.
echo Starting Full Version...
echo ⚠️  Make sure you've installed all packages first
echo 🌐 Will open in your browser shortly
echo.
streamlit run app.py
goto end

:install
echo.
echo Installing Required Packages...
echo This may take a few minutes...
echo.
pip install easyocr googletrans==4.0.0-rc1 PyMuPDF opencv-python
echo.
if errorlevel 1 (
    echo ❌ Installation failed. Please check errors above.
) else (
    echo ✅ Installation completed successfully!
    echo You can now use the Full Version
)
echo.
pause
goto menu

:exit
echo.
echo Thanks for using KOSA Translator! 👋
echo.
pause
exit

:end
echo.
echo Press any key to return to menu...
pause >nul
goto menu

:menu
cls
goto start
