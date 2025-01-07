echo off

pytest %1 --html=report.html --dashboard --archive-logs --recorder -v -s --junit-xml=junit/test-results.xml --headless