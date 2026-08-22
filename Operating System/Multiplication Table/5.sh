#!/bin/bash 

#Input from user 
echo "Enter a number: " 
read n 

#Initialising i with 1 
i=1 

#Looping i (i should be less than or equal to 10)
while [ $i -le 10 ]
do
res=$(expr $i \* $n)

#printing on console
echo "$n x $i = $res"

#Increment of i by 1
((++i))

#end of the while loop
done