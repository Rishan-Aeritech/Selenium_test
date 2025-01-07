@echo off

start "" pytest %1 --html=report.html --dashboard --archive-logs --recorder -v -s --junit-xml=junit/test-results.xml --headless

start "" python -m http.server 1948

start "" http://localhost:1948/dashboard.html