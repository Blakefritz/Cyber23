# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?


import random

def guessing_game():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    
    # Set the maximum number of turns
    max_turns = 3
    turns_taken = 0
    
    while turns_taken < max_turns:
        # Get the user's guess
        guess = int(input("Guess a number between 1 and 20: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Yes! You guessed it in {turns_taken + 1} {'guess' if turns_taken == 0 else 'guesses'}.")
            break
        else:
            # Provide hints to the user
            if guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")
            
            turns_taken += 1
    
    # If the player couldn't guess the number in the allowed turns
    if turns_taken == max_turns:
        print(f"Sorry, you couldn't guess the number. The correct number was {secret_number}.")

# Run the game
guessing_game()
