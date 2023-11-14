# Day 5 - Section 5: - Beginner - Python Loops

## For loop - do something to each item - indentation is extremely imp - if indented, its inside for loop

# Example usage:

fruits = ["apple", "peach", "pear"] 
for fruit in fruits:
    print(fruit + " pie") # Indented - Inside for loop
print(fruits) # Not indented - Outside for loop


'''Instructions: AVERAGE HEIGHT
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input 1
156 178 165 171 187
Example Output 1
total height = 857
number of students = 5
average height = 171

Example Input 2
151 145 179
Example Output 2
total height = 475
number of students = 3
average height = 158'''

# Solution:

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
total_students = 0
for student_height in student_heights:
    total_height += student_height
    total_students += 1
average_height = round(total_height / total_students)
    
print(f"total height = {total_height}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")

'''Instructions:  HIGH SCORE
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91'''

# Solution

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_score = 0
for student_score in student_scores:
    if student_score > max_score:
        max_score = student_score
print(f'The highest score in the class is: {max_score}')

## Range : range(a,b, c) : a -> starting digit, b -> ending digit, not inclusive, c -> step viz difference between items

'''Instructions: ADDING EVEN NUMBERS

You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Example Input 1
10
Example Output 1
30

Example Input 2
52
Example Output 2
702''' 

# Solution - Approach 1

target = int(input()) # Enter a number between 0 and 1000
sum = 0
for i in range(1, target+1):
    if i % 2 == 0:
        sum += i     
print(sum)


# Solution - Approach 2

target = int(input()) # Enter a number between 0 and 1000
sum = 0
for i in range(2, target+1, 2):
    sum += i
        
print(sum)


'''
Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100.
- When the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

e.g. it might start off like this:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...etc
'''

# Solution: 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
'''Instructions - Password Generator : Easy Version - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

The program will ask:
- How many letters would you like in your password?
- How many symbols would you like?
- How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password. 
Use your knowledge about Python lists and loops to complete the challenge.

Generate the password in sequence. If the user wants
4 letters
2 symbols and
3 numbers
then the password might look like this:

fgdx$*924

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.'''

# Solution : Approach 1 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ''
for i in range(0,nr_letters):
    password += letters[random.randint(0, len(letters)-1)]  
for i in range(0,nr_symbols):
    password += random.choice(symbols)
for i in range(0,nr_numbers):
    password += random.choice(numbers)
print(password)

# Solution : Approach 2 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ''
for i in range(0,nr_letters):
    password += random.choice(letters) 
for i in range(0,nr_symbols):
    password += random.choice(symbols)
for i in range(0,nr_numbers):
    password += random.choice(numbers)
print(password)

''' Instructions - Password Generator : Hard Version - Order randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

The program will ask:
- How many letters would you like in your password?
- How many symbols would you like?
- How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password. 
Use your knowledge about Python lists and loops to complete the challenge.

In the advanced version of this project the final password does not follow a pattern. 
So the example above might look like this: x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different.
'''

# Solution

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''
for i in range(0,nr_letters):
    password += random.choice(letters) 
for i in range(0,nr_symbols):
    password += random.choice(symbols)
for i in range(0,nr_numbers):
    password += random.choice(numbers)
print(''.join(random.sample(password,len(password))))
