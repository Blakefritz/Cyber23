#.!/bin/bash
# Bob is back at it again! Now he needs us to script something that if user inserts between 2 to 5, it will print out “Valid Number” and “your number is ___”.
# And if the user input is not between 2 and 5, it will print out “not valid!”


echo "Enter a number:"
read number

if (( number >= 2 && number <= 5 )); then
  echo "Valid Number"
  echo "Your number is $number"
else
  echo "Not valid!"
fi