@echo off
echo ========================================================
echo   Exam Timetable Generator - Instant Public Sharing
echo ========================================================
echo.

cd /d "%~dp0"

if not exist "cloudflared.exe" (
    echo Downloading Cloudflare tunnel binary...
    curl.exe -sL -o cloudflared.exe https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe
)

echo.
echo Launching public tunnel for http://localhost:8000 ...
echo.
echo NOTE: A free public HTTPS link (e.g. https://*.trycloudflare.com)
echo will appear below. Share that link with anyone on the internet!
echo Press Ctrl+C at any time to stop sharing.
echo.

.\cloudflared.exe tunnel --url http://localhost:8000
pause
