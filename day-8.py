##Day 8: Section 8 - Beginner - Function Parameters & Caesar Cipher

## Task 1 - Function without parameters:
'''# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
'''

def greet():
    print("Hi, I am Aastha")
    print("This is day 8 of my 100DaysOfCode Challenge")
    print("Good luck!")
    
greet()

## Task 2 - Function with parameter

def greet_with_name(name): ## Name is the parameter here
    print(f"Hi, how are you {name}?")
    
greet_with_name("Aastha") ## Aastha is the argument - Argument is the actual peice of data passed over to parameter

## Task 3 - Function with multiple parameters

def greet_with(name, city):
    print(f"Hi {name}, do you like in {city}?")
    
greet_with("Aastha", "Syracuse") ## name and city are positional argument - default away of calling arguments
greet_with(city="Mumbai", name="Aastha") ## name and city are keyword arguments - makes code less error prone but introduces unncessary code

''' Instructions - You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 \* 4) / 5
               = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

Example Input
3
9
Example Output
You'll need 6 cans of paint.
Hint
Stackoveflow link on how to round up a number: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python'''

import math
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / coverage
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


'''Instructions
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2. But 4 is not a prime number because you can divide it by 1, 2 or 4.

Example Input 1
73
Example Output 1
It's a prime number.
Example Input 2
75
Example Output 2
It's not a prime number.

'''

def prime_checker(number):
    counter = 0
    for i in range(2,number):
        if(number % i == 0):
            counter += 1
    if counter > 0:
        print("It's not a prime number")
    else:
        print("It's a prime number")


n = int(input()) # Check this number
prime_checker(number=n)


''' Caesar Cipher 1 - Encrypt - You are tasked with implementing a simple encryption function using the Caesar cipher technique in Python. Write a Python function called encrypt that takes three parameters:

plain_text: a string representing the message to be encrypted.
shift: an integer representing the amount by which each letter in the message should be shifted in the alphabet.
The function should return the encrypted message.
Your function should shift each letter in the plain_text forwards in the alphabet by the shift. If the shift goes beyond 'z', it should wrap around to the beginning of the alphabet.

For example, if plain_text is "hello" and shift is 5, the encrypted text should be "mjqqt".

Your task:

Write the Python function encrypt according to the specifications provided above. You can assume that the input plain_text contains only lowercase alphabetic characters and spaces. Non-alphabetic characters (like punctuation) should remain unchanged in the encrypted text.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        new_pos = (alphabet.index(letter) + shift) % 26 
        encrypted_text += (alphabet[new_pos])
        
    print(encrypted_text)

''' Caesar Cipher 2 - Decrypt - You are provided with a Python function called decrypt that decrypts a message encrypted using the Caesar cipher technique. The function takes two parameters:

text: a string representing the encrypted message.
shift: an integer representing the amount by which each letter in the message was shifted during encryption.
The decrypt function should return the decrypted message.

Your task is to complete the decrypt function so that it correctly decrypts the message according to the Caesar cipher algorithm.

The Caesar cipher shifts each letter in the alphabet backwards by the shift amount. If the shift goes beyond 'a', it should wrap around to the end of the alphabet.

For example, if the encrypted text is "def" and shift is 3, the decrypted message should be "abc".
'''

def decrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        new_pos = (alphabet.index(letter) - shift) % 26 
        encrypted_text += (alphabet[new_pos])
        
    print(encrypted_text)


''' Caesar Cipher 2 -Enhancing user experience - You are tasked with implementing a Caesar cipher program in Python. The program should take a message, a shift amount, and a direction (encode or decode) as inputs, and perform the corresponding encryption or decryption.

You are provided with a Python function called caesar that performs the encryption or decryption based on the given inputs. The function takes three parameters:

start_text: a string representing the message to be encrypted or decrypted.
shift_amount: an integer representing the amount by which each letter in the message should be shifted in the alphabet.
direction: a string representing the direction of the cipher operation, either "encode" for encryption or "decode" for decryption.
Your task is to complete the caesar function so that it correctly encrypts or decrypts the message using the Caesar cipher algorithm.

The Caesar cipher shifts each letter in the alphabet forwards (for encryption) or backwards (for decryption) by the shift_amount. If the shift goes beyond 'z' for encryption or 'a' for decryption, it should wrap around to the beginning or end of the alphabet, respectively.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  end_text = ""
  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {direction}d result: {end_text}")

should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift % 26, direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


