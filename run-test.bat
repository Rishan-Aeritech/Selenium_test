echo off

pytest %1 --demo --html=report.html --archive-logs --recorder -v -s --junit-xml=junit/test-results.xml