#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated

echo "How your day is?"
read answer

case $answer in

good|great|okay)
echo "your day is good"
;;
bad|awful)
echo "sorry to hear you had a bad day"
;;
*)
echo "i didnt understand"
;;
esac

# case expression in
#   pattern1)
#     # commands to be executed if expression matches pattern1
#     ;;
#   pattern2)
#     # commands to be executed if expression matches pattern2
#     ;;
#   pattern3)
#     # commands to be executed if expression matches pattern3
#     ;;
#   *)
#     # default commands if no patterns match
#     ;;
# esac
