#!/bin/bash

#Input from User
echo "Enter a number:"
read num

#Initialising i with 1
factorial=1

#Looping i - i should be less than or equal to num and increases by 1
for ((i = 1; i <= num; i++)); 
do
    factorial=$((factorial * i))
done

#Printing the console
echo "Factorial of $num is: $factorial"