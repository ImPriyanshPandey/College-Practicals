#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <start_month> <end_month>"
    exit 1
fi

# Extract start month and end month from command line arguments
start_month=$1
end_month=$2

# Check if start month is less than end month
if [ $start_month -gt $end_month ]; then
    echo "Invalid input: Start month should be less than or equal to end month."
    exit 1
fi

# Loop through the range of months and display calendar for each month
for (( month=$start_month; month<=$end_month; month++ )); do
    echo "Calendar for Month $month:"
    cal $month $(date -d "$month/1 + 1 month - 1 day" +%Y)
    echo ""
done
