## Day 10 - Section 10: Beginner - Functions with Outputs


'''Convert the is_leap() functtion - In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

Create a new function called days_in_month() - You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2) - And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.'''

def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                 return True
            else:
                return False
    else:
        return False
    
def days_in_month(year, month):
    days_in_month = {
        1:31,
        2: 29 if is_leap(year) else 28 ,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 30,
        12: 31
    }
    
    return days_in_month[month]
    
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)


# Doc strings - multiline comments, used to add documentation to function, etc


'''Write a Python program that implements a simple calculator using functions for addition, subtraction, multiplication, and division. 
The program should prompt the user to enter the first number, then display a menu of operations (+, -, *, /), and finally prompt for the second number. 
After performing the calculation, it should ask if the user wants to continue with the result or start a new calculation. 
Use the provided logo from the "art" module and clear the screen after each calculation using the "replit" module.'''


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    if num1 == 0 or num2 == 0:
        return "Invalid input"
    
def calculator(num1, opr, num2):
    opr_map = {
        "+": add(num1, num2),
        "-": sub(num1, num2),
        "*": mult(num1, num2),
        "/": div(num1, num2)
    }
    
    return opr_map[opr]
    

print(logo)
num1 = float(input("What is the first number? "))
opr = str(input("Pick an operation "))
num2 = float(input("What is the second number? "))
result = calculator(num1, opr, num2)
print(f"{num1} {opr} {num2} =  {result}")
continue_bool = input("Type Y to continue ")

while continue_bool == 'Y':
    opr = str(input("Pick an operation "))
    num2 = float(input("What is the second number? "))
    num1 = result
    result = calculator(num1, opr, num2)
    print(f"{num1} {opr} {num2} =  {result}")
    continue_bool = input("Type Y to continue ")
