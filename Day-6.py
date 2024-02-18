##Day 6 -  Section 6: Beginner - Python Functions & Karel

# Def is a keyword used to define functions : Eg def function_name(): followed by core logic indented

# Note : Spaces vs tabs - according to official python documentation - spaces are preferred indentation methods (use 4 spaces per indentation level)


'''
Hurdles race 1- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json 
Reeborg has entered a hurdles race. Make him run the course, following the path shown in the image.
What we have.
The functions move() and turn_left().
A robot located at (x, y) = (1, 1) carries no objects.
Goal to achieve:
The final position of the robot must be (x, y) = (13, 1)
'''

#Solution:

def move():
    print("Predefined function")
    
def turn_left():
    print("Predefined function")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pass_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

pass_hurdle()
pass_hurdle()
pass_hurdle()
pass_hurdle()
pass_hurdle()
pass_hurdle()

'''
More advanced
You may have noticed that your solution has some repeated patterns. If you know how to define functions, define a function named jump() and use it to simplify your program.
'''

#Solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(0,6):
    jump()

# While loop: while something_is_true: do something repeatedly

'''

Huddle race 2: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
What you need to know
The functions move() and turn_left().
The condition at_goal() and its negation.
'''
#Solution:

def at_goal():
    print("Predefined function")
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
    
# Note: Use for loop when we want to do something with each item, use while loop when you dont particularly care about each item as long as logic does something as long as the conditions are met
# Be cautious while using while loop - chances of our code getting into infinite loop situation is higher

'''
Huddle race 3: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

eeborg has entered a hurdle race. Make him run the course, following the path shown.

The position and number of hurdles changes each time this world is reloaded.
What you need to know
The functions move() and turn_left().
The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
How to use a while loop and an if statement.
'''

#Solution:

def front_is_clear():
    print("Predefined function")
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if not front_is_clear():
        jump()
    else:
        move()
        
'''
Huddle 4 - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

Reeborg has entered a hurdle race.The position, the height and the number of hurdles changes each time this world is reloaded.
What you need to know
'''

#Solution:

def wall_on_right():
    print("Predefined function")
    
def wall_in_front():
    print("Predefined function")
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        

'''
Lost in a maze: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

What you need to know
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).
'''


# Solution

def right_is_clear():
    print("Predefined function")
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear(): 
    move()
turn_left()
   
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()