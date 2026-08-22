#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <month> <year>"
    exit 1
fi

# Extract month and year from command line arguments
month=$1
year=$2

# Check if the provided month is valid
if [ $month -lt 1 ] || [ $month -gt 12 ]; then
    echo "Invalid month: Month must be between 1 and 12."
    exit 1
fi

# Display calendar for the specified month and year
echo "Calendar for Month $month, Year $year:"
cal $month $year
