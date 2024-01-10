for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#In Python, the expression number % 3 == 0 checks if the remainder of the division of number by 3 is equal to 0.
#The % symbol represents the divison, which calculates the remainder of the division.
#So, number % 3 == 0 will be True if number is evenly divisible by 3, and False otherwise. 
#In the context of the FizzBuzz program, this condition is used to determine if a given number is divisible by 3.