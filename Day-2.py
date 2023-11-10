## Day 2 - Section 2: - Beginner - Understanding Data Types and How to Manipulate Strings

# Subscripting - method of pulling out a particular elem from a string

print("Hello"[0]) # Prints first char of string - since string is essentially array of chars

print(123_456_789) # Underscore replaces comma in tradaiton sence, so this is 123,456,789 and outputs 123456789, helps in visualization

# returns data type of the parameter passed - type checking 
print(type("Aastha")) # class str
print(type(26)) # class int

#type conversion - converting one data type to other

print(str(123)) # int -> string : "123"
print(int("123")) # string -> int :123
print(float("123")) # string -> float : 123.0

'''Instructions - Add digits in a number
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
The last line of your program should print the result.
Example 1 Input
39
Example 1 Output
12'''

# Solution:
two_digit_number = input()
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit+second_digit)

# Mathematical operations in python - Follows PE(MD)(AS) 

print(1+2) # Addition
print(1-2) # Subtraction
print(1*2) # Multiplication
print(1/2) # Divison
print(1**2) # Exponent

'''Instructions : BMI Calculator
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight (in kg) / height ^ 2 (m^2)

NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.
Example Input 1
1.75
80
means: weight = 80 and height = 1.75

Example Output 1
26
Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837

Example Input 2
1.58
57
Example Output 1
22
'''

# Solution
height = input()
weight = input()

BMI = float(weight) / (float(height) ** 2)
print(int(BMI))


# Mathematical operations

print(round(123.44444, 2)) # Rounds the floating pt number to nearest n precision
print(8//3) # floors -> converts to int -> rounds down the number

# f-String 

num = 2
# print("Hi, this is testing num: " + num)# Throws error
print(f'Hi, this is testing num: {num}') #This works

'''Instructions - Lifes in weeks
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
Example Input
56
Example Output
You have 1768 weeks left.
'''

age = input()
age_left = 90 - int(age)
age_in_weeks = int(age_left * 52)
print(f'You have {age_in_weeks} weeks left.')


'''Instructions : Tip Calculator
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
'''

total_bill = float(input("What was the total bill? $"))
total_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
total_bill_incl_tip = total_bill + (total_bill * (total_tip / 100))
per_person_cost = round(total_bill_incl_tip / total_people, 2)
print(f'Each person should pay: {per_person_cost}')