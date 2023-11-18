#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

user=y

while [ $user = y ]
do
echo "pick an number to do one of the following"
echo enter 1 for a special note
echo enter 2 to ping your self
echo enter 3 to show you network configuration

read input

sleep 2

if [ $input = 1 ]
    then echo "Hello World"
elif [ $input = 2 ]
    then ping -c 3 192.168.1.71
    
elif [ $input = 3 ]
    then ifconfig
else echo "invalid entry"

fi

echo "Do you want to choose another option? y/n"
read user
done
