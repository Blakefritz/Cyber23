# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
#Write your code below this line:

import random

while True:
    action = input("Choose (paper, rock, scissors): ")
    choices = ["paper","rock", "scissors"]
    comp_action = random.choice(choices)
    
    print("computer chose "+comp_action)
    if action == comp_action:
        print(f"\n tie")
    elif action == "paper":
        if comp_action == "rock":
            print(f"\n paper beats rock")
        else: print("scissors beats paper")
    elif action == "rock":
        if comp_action == "scissors":
            print(f"\n rock beats scissors")
        else: print(f"\n paper beats rock")
    elif action == "scissors":
        if comp_action == "paper":
            print(f"\n scissors beats paper")
        else: print("rock beats scissors")
        
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break