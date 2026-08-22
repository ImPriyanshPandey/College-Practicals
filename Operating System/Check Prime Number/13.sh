#!/bin/bash
read -p "Enter a number:" number
if [ $number -lt 2]; then
    echo "$number is not a prime number."
    exit 1
fi 
if [ $number -eq 2 ]; then
    echo "$number is a prime number."
    exit 0
fi
if [ $((number % 2)) -eq 0 ]; then
    echo "$number is not a prime number."
    exit 1
fi
for ((i=3; i <= $number/2; i+=2)); do
    if [ $((number % i)) -eq 0 ]; then
        echo "$number is not a prime number."
        exit 1
    fi
done

echo "$number is a prime number."