## Day 13 - Section 13: Beginner - Debugging: How to Find and Fix Errors in your Code

''' Suggested steps:
- Describe the problem in your head - Untangle the problem
- Reproduce the bug
- Fix errors in IDE befre you continue
- Squash bugs with a print() statement
- Use a debugger
- Take a break and come back
- Ask for an external perspective
- Run your code often - after every little code execution
- Ask stackoverflow
'''

'''Instructions
Read this the code in main.py
Spot the problems 🐞.
Modify the code to fix the program.
Fix the code so that it works and passes the tests when you submit.

number = int(input()) # Which number do you want to check?

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
'''

number = int(input()) # Which number do you want to check?

if number % 2 == 0: # learnt about = vs ==
  print("This is an even number.")
else:
  print("This is an odd number.")
  
  
'''Instructions
Read this the code in main.py
Spot the problems 🐞.
Modify the code to fix the program.
No shortcuts - don't copy-paste to replace the code entirely with a working solution.
Fix the code so that it works and when you hit submit it should pass all the tests.

# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
'''

# Which year do you want to check?
year = int(input()) # Learnt about type errors

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
'''Instructions
Read this the code in main.py
Spot the problems 🐞.
Modify the code to fix the program.
No shortcuts - don't copy-paste to replace the code entirely with a working solution.
The code needs to print the solution to the FizzBuzz game.

Your program should print each number from 1 to x where x is the input number.

However when the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
'''


target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
