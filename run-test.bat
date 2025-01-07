@echo off

start "" cmd.exe /k pytest %1 --html=report.html --dashboard --archive-logs --recorder -v -s --junit-xml=junit/test-results.xml --headless

if not exist "dashboard.html" (
timeout /t 3
)

start "" python -m http.server 1948

start "" http://localhost:1948/dashboard.html