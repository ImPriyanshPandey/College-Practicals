#!/bin/bash
echo "     SYSTEM INFORMATION"
HOSTNAME=$(hostname)
DATE=$(date)

echo "Hostname : $HOSTNAME"
echo "Date     : $DATE"

echo "----- System Uptime -----"
uptime

echo ""
echo "----- Memory Usage -----"
free -h

echo ""
echo "----- Disk Usage -----"
df -h

echo "=============================="
echo "   SSH FAILED LOGIN REPORT"

LOG_FILE="/var/log/auth.log"

if [ -f "$LOG_FILE" ]; then
    echo "Log file found."

    echo ""
    echo "Total Failed SSH Login Attempts:"
    grep "Failed password" $LOG_FILE | wc -l

    echo ""
    echo "Top Failed Login IPs:"
    grep "Failed password" $LOG_FILE | awk '{print $11}' | sort | uniq -c | sort -nr | head

else
    echo "Auth log file not found!"
fi

echo ""
echo "=============================="
echo " Script Execution Completed "
echo "=============================="