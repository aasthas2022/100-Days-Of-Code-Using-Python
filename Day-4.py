# Day 4 - Section 4: Beginner - Randomisation and Python Lists

import random

print(random.randint(1,10)) # Generates random integer between 1 to 10
print(random.random()) # Generates random floating pt value between 0 to 1 (1 not inclusive)

# Note: Split large set of code into individual peices grouping them on the basis of functionality -> each peice is called a module

'''Instructions : Heads or Tails

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

Example Output
Heads
or
Tails'''

#Solution:

import random
outcome = random.randint(0,1)
if outcome == 1:
    print("Heads")
else:
    print("Tails")
    
# Note: List is a data structure in Python that is a mutable, or changeable, ordered sequence of elements - https://docs.python.org/3/tutorial/datastructures.html

test_of_items = ["item1", "item2", "item3"] # Example of list
print(test_of_items[0]) # Prints first item
print(test_of_items[-1]) # Prints last item - negative indices start from behind
test_of_items[0] = "item1-updated" # Alters first item in the list
test_of_items.append("Appended-item") # Adds item to the end of the list 

'''Instructions : BANKER ROULETTE

You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 1 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
'''

#Solution:

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

import random
person_paying_bill_index = random.randint(0, len(names)-1)
print(f'{names[person_paying_bill_index]} is going to buy the meal today!')

# Note: Nested List - List within a list

list_1 = ["list_1_item_1", "list_1_item_2", "list_1_item_3", "list_1_item_n"]
list_2 = ["list_2_item_1", "list_2_item_2", "list_2_item_3", "list_3_item_n"]
nested_list = [list_1, list_2] # Prints - [['list_1_item_1', 'list_1_item_2', 'list_1_item_3', 'list_1_item_n'], ['list_2_item_1', 'list_2_item_2', 'list_2_item_3', 'list_3_item_n']]

'''Instructions: Treasure map

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map. This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Your job is to write a program that allows you to mark a square on the map using a letter-number system.

Exmaple location

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
Example Input 2
B1
Example Output 2
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']

Check your formatting. This is correctly formatted:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']

'''

# Solution:

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

vertical_mapping_cordinates = {"A": 0, "B": 1, "C": 2}
horizontal_mapping_cordinates = {"1": 0, "2": 1, "3": 2}

vertical_cordinate = position[0]
horizontal_cordinate = position[1]

mapped_cordinate_vertical = vertical_mapping_cordinates.get(vertical_cordinate)
mapped_cordinate_horizontal = horizontal_mapping_cordinates.get(horizontal_cordinate)

map[mapped_cordinate_vertical][mapped_cordinate_horizontal] = 'X'

print(f"{line1}\n{line2}\n{line3}")

'''Instructions : Rock paper sissor
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.'''

# Solution: Approach 1

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
system_input = random.randint(0,2)

if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("Invalid input")
    
print("Computer chooses:")
if system_input == 0:
    print(rock)
elif system_input == 1:
    print(paper)
elif system_input == 2:
    print(scissors)
else:
    print("Invalid system input number generated")

if (user_input == system_input):
    print("Its a tie")
elif (user_input == 0 and system_input == 2) or (user_input == 2 and system_input == 1) or (user_input == 1 and system_input == 0):
    print("You win")
else:
    print("You lose!")

# Solution : Approach 2

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

graphics = [rock, paper, scissors]    
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(graphics[user_input])
system_input = random.randint(0,2)   
print("Computer chooses:\n"+graphics[system_input] )

if (user_input < 0 or user_input > 3) and (system_input < 0 or system_input > 3):
    print("Invalid input")
elif (user_input == system_input):
    print("Its a tie")
elif (user_input == 0 and system_input == 2) or (user_input == 2 and system_input == 1) or (user_input == 1 and system_input == 0):
    print("You win")
else:
    print("You lose!")
    