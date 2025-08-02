#! /bin/bash
<<COMMENT
a=10
b=20
c=30
echo $a $b $c
: '
read -p "Enter your number: " num #-p means prompt
echo "You entered: $num"
'
#echo "working"
# cmd input --> ./main.sh mitran 26
#echo "file name is $0"
read -p "Enter a number: " abc
if [ $abc -gt 10 ]
then
# if [$abc -gt 10]; then
    echo "The number is grater than 10."
elif [ $abc -eq 10 ]
then 
    echo "The number is not grater than 10."
fi
COMMENT
#nested if





