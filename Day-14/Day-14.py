## Day 14 - Section 14: Beginner - Higher Lower Game Project

'''Create a Python program for a higher-lower game where players guess which of two randomly selected social media accounts has more followers. The game should display ASCII art for the logo and versus sign, randomly select accounts from a provided dataset, format the account data for display, allow users to guess the account with more followers, check their guess against the actual follower counts, keep track of the score, and repeat the game until the user guesses incorrectly. '''

# Solution

'''
1. Display the game logo
2. Print randomly chosen option 1 in the format : name + description + "from" + country and save value in variable A
3. Display vs logo
4. Print randomly chosen option 2 in the format : name + description + "from" + country and save value in variable B
5. Prompt user for input : Who has more followers? Type 'A' or 'B'
6. Initialize score to 0
7. While user's answers are correct (correct ans is when user guesses who has more followers):
7.1. Increment the score 
7.2. Repeat 2,3,4,5
8. When user answers are incorect
8.1 Display the score
8.2 Exit the game
'''

import art
import game_data
import random

print(art.logo)

data = game_data.data
data_length = len(game_data.data)

continue_game = True
score = 0

while continue_game:
    a, b = random.sample(data, 2)
    
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

    user_choice = str(input("Who has more followers? Type 'A' or 'B' ")).lower()
    
    if user_choice != "a" and user_choice != "b":
        print("Invalid Input")
        continue_game = False
    
    first_choice, second_choice = (a, b) if user_choice == "a" else (b, a)

    if int(first_choice['follower_count']) > int(second_choice['follower_count']):
        print("Congratulations, you're correct")
        score += 1
        continue_game = True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False 
        
        

    
