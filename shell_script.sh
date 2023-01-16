#! /usr/bin/bash
# This is a comment
echo "Hello World"  # This is also a comment

# Variables -- containers for storing data -- (System Variables and user defined variables)

# echo Our shell name is $BASH
# echo The version of bash is $BASH_VERSION
# echo Our home directory is $HOME
# echo Our current working directory is $PWD

# name=Shwet
# echo The name is $name
# # Variable number should not start with number
# VALUE=10
# echo value $VALUE

# READ USER INPUT
# echo "Enter name : "
# # read fname mname lname 
# echo "Entered name : $fname , $mname, $lname"

# Enter input on same line

# read -p 'username : ' user_var
# read -sp 'password : ' pass_var
# echo "username : $user_var"
# echo "password : $pass_var"

# Enter multiple inputs and store it in the form of array
# echo "Enter names : "
# # read -a names
# # echo "Names : ${names[0]} ,${names[1]}"
# read 
# echo "Name : $REPLY"

# PASS ARGUMENTS TO A BASH-SCRIPT

# echo $0 $1 $2 $3 ' > echo $1 $2 $3'
# args=("$@")
# # echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}  
# echo $@
# echo $#

# # If Statement 
# count=10
# if [ $count -eq 10 ]
# then
#     echo "Condition is true"
# fi
# if (($count >= 9 ))
# then
#     echo "Count is greater than 9"
# fi

# # String comparision =, ==, !=, <, >, -z
# word=abc

# if [ $word = 'abcd' ]
# then 
#     echo "Condition true for string"
# else
#     echo "Condition not true for string"
# fi

# # FILE TEST OPERATORS
# # -d, -e, -s

# echo -e "Enter the name of the file : \c"
# read file_name

# if [ -e $file_name ]
# then
#     echo "$file_name found"
# else 
#     echo "$file_name not found"
# fi

# APPEND OUTPUT TO THE END OF TEXT FILE

# echo -e "Enter the name of the file : \c"
# read file_name

# if [ -e $file_name ]
# then
#     echo "$file_name not empty"
# else 
#     echo "$file_name empty"
# fi


# # Loop in shell scripting
# for i in 1 2 3 4 5 6
# do
#   echo "Looping ... number $i"
# done
# for i in hello 1 * 2 goodbye 
# do
#   echo "Looping ... i is set to $i"
# done

# # While Loop
# INPUT_STRING=hello
# while [ "$INPUT_STRING" != "bye" ]
# do
#   echo "Please type something in (bye to quit)"
#   read INPUT_STRING
#   echo "You typed: $INPUT_STRING"
# done

# # Logical AND operator
# age=25
# if [ "$age" -gt 18 ] && [ "$age" -lt 50 ]
# then
#   echo "Valid age"
#   else
#   echo "Age not valid"
# fi 

# if [ "$age" -gt 18 ] || [ "$age" -lt 50 ]
# then
#   echo "Age is valid"
#   else
#   echo "Age is not valid"
# fi 

# #  changing the permissions in file and concat it  
# echo -e "Enter the name of the file : \c"
# read file_name

# if [ -f $file_name ]
# then
#   if [ -w $file_name ]
#   then 
#     echo "Type some text data. To quit press ctrl-d."
#     cat >> $file_name
#   else 
#     echo "The file do not have write permissions"
#   fi
# else
#   echo "$file_name not exists"
# fi

# # Perform arithmetic operations
# num1=20.5
# num2=5

# echo $((num1 + num2))
# echo $((num1 - num2))
# echo $((num1 * num2))
# echo $((num1 / num2))
# echo $((num1 % num2))

# # using expr

# echo $(expr $num1 + $num2)
# echo $(expr $num1 - $num2)
# echo $(expr $num1 \* $num2)  # use escape character before * for using it as multiplicative expression
# echo $(expr $num1 / $num2)
# echo $(expr $num1 % $num2)

# # Floating point math operations in bash | bc command
# # bc - basic calculator
# echo "$num1 + $num2" | bc
# echo "$num1 - $num2" | bc
# echo "20.5*5" | bc
# echo "scale=2;20.5/5" | bc
# echo "20.5%5" | bc
# num=27
# echo "scale=2;sqrt($num)" | bc -l
# echo "scale=2;3^3" | bc -l

# The Case statement
# echo -e "Enter some character : \c"
# read value

# vehicle=$1

# case $vehicle in
#   "car")
#     echo "Rent of $vehicle is 100 dollar" ;;
#   "van")
#     echo "Rent of $vehicle is 80 dollar" ;;
#   "truck")
#     echo "Rent of $vehicle is 1000 dollar" ;;
#   * )
#     echo "Unknown vehicle" ;;
# esac


# case $value in
#   [a-z] )
#     echo "user entered $value a to z" ;;
#   [A-Z] )
#     echo "user entered $value A-Z " ;;
#   [0-9] )
#     echo "user entered $value 0-9" ;;
#   ? )
#     echo "user entered $value special character" ;;
#   * )
#     echo "Unknown value" ;;
# esac
# # if cap alphabet is not working use LANG=alphabet

# # ARRAY VARIABLES 
# os=('ubuntu' 'windows' 'kali' )
# os[3]='mac'
# unset os[2]
# echo "${os[@]}"
# echo "${os[0]}"
# echo "${!os[@]}"
# echo "${#os[@]}"
# string=fgthjskkkkkkkkpioo
# echo "${string[@]}"
# echo "${string[0]}"
# echo "${string[1]}"  # here whole value is assigned to index 0

# # LOOPS IN SHELL SCRIPT
# n=1
# while [ $n -le 10 ]
# do 
#   echo "$n"
#   (( ++n ))
# done

# # use sleep 
# n=1
# while [ $n -le 10 ]
# do 
#   echo "$n"
#   (( n++ ))
#   sleep 2
# done

# # Opening the gnome terminal

# n=1
# while [ $n -le 2 ]
# do 
#   echo "$n"
#   (( n++ ))
#   gnome-terminal &
#   # xterm & 
# done

# READ FILE CONTENT IN BASH

while read p
do 
  echo $p
done < test 

# 
