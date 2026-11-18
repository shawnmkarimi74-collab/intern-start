#!/bin/bash
LOG_FILE='app.log'
echo "=== ERROR LINES ==="
grep -n "ERROR" "$LOG_FILE"
grep -v "INFO" "$LOG_FILE" > problems.txt
echo "=== MOST FREQUENT USER ==="
grep -o 'user=[^ ]*' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 1


