## Day 1 - Section 1: - Beginner - Working with Variables in Python to Manage Data

# First line of code - Printing Hello World

print("Hello World!")

# Question -> 1 : Printing Statement

''' Instructions
Write a program in main.py that prints the following notes on Python programming into the Output console. Your code should print all three lines.
Day 1 - Python Print Function
The function is declared like this:
print('what to print') '''

# Solution:

# Approach 1: Simply printing using diff print statements
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# Approach 2: Using 1 printing statement and leveraging escape characters
print('Day 1 - Python Print Function\nThe function is declared like this:\nprint(\'what to print\')')

# String Manipulation

print("Hellp\nWorld") # Prints hello and world on different lines
print("Hello"+"Aastha") # Concatenates two strings while printing

# Question -> 2: Debugging Pratice 

''' Instructions
Look at the code in the code editor on the left. There are errors on all 4 lines of code. Fix the code so that it runs without errors.

Code:

# Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
'''

# Solution:

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.") # Alternative alternate the quotes 
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Input function

input("Hi, how are you doing today?")
print("Hi "+ input("What is your name?")) # Can use Thonny Debugger to check step by step execution of the function

# Question 3 - Length of a string

'''Instructions
Write a program that calculates and outputs the number of characters in any name. 
The automated tests will try out lots of different names as the input. 
Your code should work for any name.'''

# Solution:

print(len(input()))

# Question 4 - Swap Variables

''' Instructions
This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.
Write a program that switches the values stored in the variables a and b.

Example Input 1
29
41
Example Output 1
a: 41
b: 29

Example Input 2
Hello
World
Example Output 2
a: World
b: Hello
'''

# Solution
a = input()
b = input()
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

'''Instruction

ou are tasked with creating a simple Band Name Generator in Python. The program should follow these steps:

Display a welcome greeting for the user.
Prompt the user to enter the city they grew up in.
Prompt the user to enter the name of their pet.
Combine the city and pet names to generate a unique band name.
Ensure that the input cursor is on a new line after each prompt.
'''

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?")
pet_name = input("What's your pet's name?")
print("Your band name could be " + city + " " + pet_name)