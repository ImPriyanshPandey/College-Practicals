#!/bin/bash
printf "Enter the number of rows : "
read rows
for((i=0;i<=rows;i++))
do
for((j=1;j<=i;j++))
do
printf "* "
done
printf "\n"
done