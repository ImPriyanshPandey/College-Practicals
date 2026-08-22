#!/bin/bash
#Function to calculate length
length(){
    num=$1
    len=0
    while [ $num -gt 0 ]
    do
        num=$((num/10))
    done
    len=$((len+1))
    echo $len
}
#Function to check if a number is Armstrong number
check_armstrong(){
    num=$1
    sum=0
    len=$(length $num)
    temp=$num
    while [ $temp-gt 0]
    do
        digit=$((temp %10))
        sum=$((sum + digit**len))
        temp=$((temp/10))
    done
    if [ $sum -eq $num]
    then
        echo "$num is an Armstrong Number."
    else
        echo "$num is not an Armstrong Number."
    fi
}
    
#Read number
echo "Enter a number:"
read num
#Calculate function
check_armstrong $num