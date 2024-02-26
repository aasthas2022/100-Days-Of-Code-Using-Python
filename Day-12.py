## Day 12 - Section 12: Beginner - Scope & Number Guessing Game

# local scope applicable only within function/etc vs global scope applicable throughout
# python does not have blocked scope
# without "global" keyword we cant modify a global variable value in local scope


'''
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


'''
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)

import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
final_ans = random.randint(1,100)

if difficulty.lower() == 'easy':
    attempt = 10
elif difficulty.lower() == 'hard':
    attempt = 5
else:
    attempt = 0
    
print(f"You have {attempt} attempts remaining to guess the number.")

while attempt > 0:
    guess = int(input("Make a guess: "))
    if guess == final_ans:
        print(f"You got it! The answer was {final_ans}.")
        break
    
    if attempt == 0:
        print("You have no attempts left. You lose!")
        print(f"The correct ans was {final_ans}")
        break
    
    if guess > final_ans:
        attempt -= 1
        print("Too high. \n Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number")
    else:
        attempt -= 1
        print("Too low. \n Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number")
        