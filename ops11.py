# Today we are going to create a random password generator using for loops and arrays in python
# Make sure to print you password to the screen
#Can you randomize your password generated

import random
import string
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = string.ascii_letters
# american standard code for information interchange 
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = string.digits
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
symbols = string.punctuation

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# What is line 15 doing?
#Line 15 initializes an empty list called password. 
#This list will be used to store the characters of the generated password. 
#The subsequent for loops will append characters to this list based on the user's input for the number of letters, symbols, and numbers.
password = []

# Below is the guide how to write the for loop you need to write for symbols and numbers
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))


# for _ in range(nr_letters):
#     password.append(random.choice(letters))
# for _ in range(nr_numbers):
#     password.append(random.choice(numbers))
# for _ in range(nr_symbols):
#     password.append(random.choice(symbols))



random.shuffle(password)

final_pass = ""
for char in password:
    final_pass += char
print(f"Your password is {final_pass}")