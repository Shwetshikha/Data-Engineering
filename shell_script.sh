#! /usr/bin/bash
# This is a comment
echo "Hello World"  # This is also a comment

# Variables -- containers for storing data -- (System Variables and user defined variables)
#
echo Our shell name is $BASH
echo The version of bash is $BASH_VERSION
echo Our home directory is $HOME
echo Our current working directory is $PWD

name=Shwet
echo The name is $name
# Variable number should not start with number
VALUE=10
echo value $VALUE

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

# Logical AND operator
age=25
if [ "$age" -gt 18 ] && [ "$age" -lt 50 ]
then
  echo "Valid age"
  else
  echo "Age not valid"
fi

if [ "$age" -gt 18 ] || [ "$age" -lt 50 ]
then
  echo "Age is valid"
  else
  echo "Age is not valid"
fi
