## Day 3 - Section 3: Beginner - Control Flow and Logical Operators

'''Instructions : Rollercoaster height checker
Here is a draw.io flowchart : https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%201#R1VfbcpswEP0apk%2FJAAJfHmM7aR%2FSjlt3ps2jYm1ArUCukC%2Fk67sywqDgJM7Eub0w6Ggl7Z49uwKPjLPNZ0UX6VfJQHihzzYemXhhOIhCfBqgrICIkApIFGcVFDTAjN%2BCBX2LLjmDwjHUUgrNFy44l3kOc%2B1gVCm5ds1upHBPXdAEOsBsTkUX%2FcWZTm1YYb%2FBvwBP0vrkoDesZjJaG9tIipQyuW5B5NwjYyWlrt6yzRiE4a7mpVp3cc%2FszjEFuT5kwTQf3Pz8rmYwjVc%2FVmxzyf%2FJExtGocs6YGAYvx1KpVOZyJyK8wYdKbnMGZhdfRw1NpdSLhAMEPwDWpc2mXSpJUKpzoSdRYdV%2BdusP%2B2RsAauEDjxT%2F1%2BXCOTjT2jGpXt0RQUz0CDsmAVh3H%2BXnosVMilmsMDnNQyoyoB%2FYBdvEsiih8keqNKXKdAUM1Xrh%2FUyjDZ2dmlZ0rRsmWwkDzXRWvnqQHQwBYUIbagbD0FcdzOOr5UO9ajlmsNtFXGE1QyfGOVREHUVon%2FQQQSHUMgHQUEkSuAoe%2FuULllFzXKeKrQer3X15nlYkXF0rJje6tpbT2aoXBGid4m0w%2Bw52ceuehIU6Uyu15ilKN1yjXMFnSbzDVeT67A7GGgNGwe1kQ3h%2FWCoO%2ByVF9b6%2BauCHoWS1v3xN2ktdPe4vjpFJK3KNUj1lZ4YG3dk5eDa%2BtZJIcdnc7QYd2V4o7Y4HE53nAhxlJItV1LWAwDZtpeoZX8C62ZQXhNsDqPI2DiCjjco99wj36jl9Jv1KF2TPNPpgPg5yE8j%2BEj8EV8l6499T7ovyJd8T663gtZYb%2F%2Fvtiqz2%2FR9U12aMKAtcsFFTzJ8X2OgZsPipGhheNPwpmdyDhjVSuFgt%2FS6%2B1WppnaWxb3jUdePDF7YfcsqkZ6JJoHd%2B4gMuywTPaUcPhiLHev8SsoPjzN%2BC%2F7KM%2FRcXjGYfNfWH1cNT%2FX5Pw%2F
Write a Python program that greets users entering a rollercoaster and checks whether they meet the height requirement. 
If the user's height is greater than 120 cm, the program should output "can't ride"; 
otherwise, it should output "can ride."
'''

MAX_HEIGHT = 120
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > MAX_HEIGHT:
    print("Can ride")
else:
    print("cant ride")
    
# Comparison operators : +, - , >, <, >=, <=, ==, !-
# Remember: = - Assinment operator, == equality checker

''' Instructions : Odd or Even number

Write a program that works out whether if a given number is an odd or even number.

Example 1 Input
43
Example 1 Output
This is an odd number.
Example 2 Input
94
Example 2 Output
This is an even number.'''

number = int(input())
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    
    
'''Instructions: BMI 2.0
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height. It should tell them the interpretation of their BMI based on the BMI value.
- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Equal to or over 25 but below 30 they are slightly overweight
- Equal to or over 30 but below 35 they are obese
- Equal to or over 35 they are clinically obese.

Important: you do not need to round the result to the nearest whole number. 
It's fine to print out a floating point number for this exercise. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

Example Input 1
1.50
63
Example Output 1
Your BMI is 28.0, you are slightly overweight.
since 63 ÷ (1.50 x 1.50) = 28

The testing code will check for print output that is formatted like one of the lines below:

"Your BMI is 18.28678, you are underweight."
"Your BMI is 22.0, you have a normal weight."
"Your BMI is 28.50752, you are slightly overweight."
"Your BMI is 32.56189, you are obese."
"Your BMI is 37.50000, you are clinically obese."

Example Input 2
1.60
96
Example Output 2
Your BMI is 37.49999999999999, you are clinically obese.
Example Input 3
1.71
73
'''

height = float(input())
weight = int(input())

BMI = float(weight) / (float(height) ** 2)

if BMI < 18.5:
    print(f'Your BMI is {BMI}, you are underweight.')
elif 18.5 < BMI and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
    
    
'''Instructions : Leap year

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.
This is how you work out whether if a particular year is a leap year.
on every year that is divisible by 4 with no remainder
except every year that is evenly divisible by 100 with no remainder
unless the year is also divisible by 400 with no remainder
If english is not your first language or if the above logic is confusing, try using this flow chart .

e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)

Example Input 1
2400
Example Output 1
Leap year
Example Input 2
1989
Example Output 2
Not leap year'''

year = int(input())
LEAP_BOOLEAN = False

if year % 4 == 0:
    if year % 100 != 0:
        LEAP_BOOLEAN = True
    else:
        if year % 400 == 0:
            LEAP_BOOLEAN = True
        else:
            LEAP_BOOLEAN = False
else:
    LEAP_BOOLEAN = False
    
if(LEAP_BOOLEAN == True):
    print("Leap year")
else:
    print("Not leap year")  
    
'''Instructions: 
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.'''

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_med_large = 3
extra_cheese_required = 1
final_cost = 0

if size == 'S':
    final_cost += small_pizza
    if add_pepperoni == 'Y':
        final_cost += pepperoni_small
    if extra_cheese == 'Y':
        final_cost += extra_cheese_required
elif size == 'M':
    final_cost += medium_pizza
    if add_pepperoni == 'Y':
        final_cost += pepperoni_med_large
    if extra_cheese == 'Y':
        final_cost += extra_cheese_required
elif size == 'L':
    final_cost += large_pizza
    if add_pepperoni == 'Y':
        final_cost += pepperoni_med_large
    if extra_cheese == 'Y':
        final_cost += extra_cheese_required

print(f"Your final bill is: ${final_cost}.")


# Logical Operators: and, or, not

'''  Instructions : Love Calculator

You are going to write a program that tests the compatibility between two people. To work out the love score between two people:
- Take both people's names and check for the number of times the letters in the word TRUE occurs.
- Then check for the number of times the letters in the word LOVE occurs.
- Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be: Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be: "Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.: "Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times

Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
'''

# Approach 1:
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name_to_iterate = name1 + " " + name2

love_cal_str_1 = list('true')
love_cal_str_2 = list('love')

count_1 = 0
count_2 = 0

for i in name_to_iterate.lower():
    if i in love_cal_str_1:
        count_1 = count_1 + 1
    if i in love_cal_str_2:
        count_2 = count_2 + 1

final_score = int(str(count_1)+str(count_2))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
    print (f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
    

# Approach 2:
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name_to_iterate = name1.lower() + " " + name2.lower()


count_1 = name_to_iterate.count('t') + name_to_iterate.count('r') + name_to_iterate.count('u') + name_to_iterate.count('e')
count_2 = name_to_iterate.count('l') + name_to_iterate.count('o') + name_to_iterate.count('v') + name_to_iterate.count('e')

final_score = int(str(count_1)+str(count_2))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
    print (f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
    
    
'''  Instructions : Text based advanture Game

Write a Python script for a text-based adventure game. The game should start with the following message:

The player should be prompted to make a series of choices using `input()` statements. Here is the scenario:

1. The player starts at a crossroad and must choose to go "left" or "right."
2. If they choose "left," they come to a lake and must choose to "wait" for a boat or "swim" across.
3. If they choose to "wait," they arrive at an island with a house containing three doors (red, yellow, and blue). The player must choose a door.
   - If they choose the "red" door, it's a room full of fire, and the game is over.
   - If they choose the "yellow" door, they find the treasure and win the game.
   - If they choose the "blue" door, they enter a room of beasts, and the game is over.
   - If they choose any other option, they chose a door that doesn't exist, and the game is over.
4. If, at any point, the player chooses to "swim" across the lake, they get attacked by an angry trout, and the game is over.
5. If the player initially chooses "right" at the crossroad, they fall into a hole, and the game is over.

Write the complete Python script for this text-based adventure game based on the given scenario.

'''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"")

if direction.lower() == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")

    if action.lower() == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color = input("One red, one yellow and one blue. Which colour do you choose?")
        if color.lower == "red":
            print("It's a room full of fire. Game Over.")
        elif color.lower == "blue":
            print("You enter a room of beasts. Game Over.")
        elif color.lower == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
    