@echo off
echo ========================================================
echo   Starting Exam Timetable Generator Web Service
echo ========================================================
echo.

cd /d "%~dp0"

REM Build frontend if dist doesn't exist
if not exist "frontend\dist\index.html" (
    echo [1/2] Building frontend web interface...
    cd frontend
    call npm.cmd run build
    cd ..
) else (
    echo [1/2] Frontend build verified.
)

echo.
echo [2/2] Launching server on http://0.0.0.0:8000 ...
echo.
echo --------------------------------------------------------
echo   Web Application is now active!
echo   - Local Access:   http://localhost:8000
echo   - API / Swagger:  http://localhost:8000/docs
echo --------------------------------------------------------
echo.
echo Opening browser...
start http://localhost:8000

cd backend
py -m uvicorn app.main:app --host 0.0.0.0 --port 8000
pause
