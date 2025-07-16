@echo off

echo Running main.py to download and clean data...
py main.py

if %ERRORLEVEL% neq 0 (
    echo Error occurred running main.py
    pause
    exit /b %ERRORLEVEL%
)

echo Launching Streamlit dashboard...
py -m streamlit run titanic_dashboard.py

pause
