## Day 9 - Section 9: Beginner - Dictionaries, Nesting and the Secret Auction

# Dictionary = {key:value}
# Remember = List = []; Dictionary = {}
# Add item to dictionary

already_exisiting_dict = {} 
already_exisiting_dict["new_key"] = "new_value"

# looping through dict
for key in already_exisiting_dict :
    print(key) #prints key
    print(already_exisiting_dict[key]) # prints value


'''Instructions:
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

This is the scoring criteria:
- Scores 91 - 100: Grade = "Outstanding"
- Scores 81 - 90: Grade = "Exceeds Expectations"
- Scores 71 - 80: Grade = "Acceptable"
- Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

def check_grade(score):
    if score < 100 and score > 90:
        return "Outstanding"
    elif score <= 90 and score > 80:
        return "Exceeds Expectations"
    elif score <=80 and score > 70:
        return "Acceptable"
    else:
        return "Fail"

for key in student_scores:
    student_grades[key] = check_grade(student_scores[key])
   
print(student_grades)

# Nested dict : dict_example = {"key1": [List], "key2": {Dict}}
# Lists are ordered viz each item is accessed via position in the list


''' Instructions
You are going to write a program that adds to a travel_log. 
You can see a travel_log which is a List that contains 2 Dictionaries. 
Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.
DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

Example Input
Brazil
5
["Sao Paulo", "Rio de Janeiro"]
Example Output
I've been to Brazil 5 times.
My favourite city was Sao Paulo. 

'''

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
    travel_log.append({"country": country, "visits": visits, "cities": list_of_cities})
    
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")


''' Secret Auction:
Write a Python program for a secret auction. 
The program should prompt each bidder for their name and bid amount, and it should continue asking if there are any other bidders until there are no more. 
Then, it should determine and print the winner's name and bid amount.
'''


print("Welcome to secret auction program!")

bool_other_bidders = 'yes'
names_with_bid = []
max_bid_name = ''
max_bid = 0

while bool_other_bidders != 'no':
     name = str(input("What is your name? "))
     bid = int(input("What is your bid? "))
     bool_other_bidders = str(input("Are there any other bidders? Type 'yes' or 'no'! "))
     names_with_bid.append({'name': name, 'bid': bid})
     
for elem in names_with_bid:
    if int(elem['bid']) > max_bid:
        max_bid_name, max_bid = elem['name'], elem['bid']
        
print(f"The winner is {max_bid_name} with a bid of ${max_bid}")

