@echo off
setlocal enabledelayedexpansion

echo [1/4] Pulling latest changes from GitHub...
:: Added origin main explicitly to avoid tracking errors
git pull origin main --allow-unrelated-histories
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Pull failed. Please check for conflicts.
    pause
    exit /b %errorlevel%
)

echo.
echo [2/4] Staging all changes...
git add .

echo.
set /p commit_msg="[3/4] Enter commit message (or press Enter for 'Auto-update'): "
if "!commit_msg!"=="" set commit_msg=Auto-update: %date% %time%

git commit -m "!commit_msg!"
if %errorlevel% neq 0 (
    echo.
    echo [INFO] No changes to commit.
    pause
    exit /b 0
)

echo.
echo [4/4] Pushing to GitHub...
:: Added origin main explicitly
git push origin main
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Push failed.
    pause
    exit /b %errorlevel%
)

echo.
echo [SUCCESS] Site updated and pushed to GitHub!
pause
