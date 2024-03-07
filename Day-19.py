## Day 19 - Section 19: Intermediate - Instances, State and Higher Order Functions

# Task - Make an etch sketch app
# Objective : adding event listeners and using inputs from hardware

from turtle import Turtle, Screen

turtle_obj = Turtle()
screen_obj = Screen()

def moveFwd() :
    return turtle_obj.forward(100)

def movebkwd():
    return turtle_obj.backward(100)

def counterclock():
    return turtle_obj.right(90)

def clockwise():
    return turtle_obj.left(90)

screen_obj.listen()
screen_obj.onkey(key="w", fun=moveFwd)
screen_obj.onkey(key="s", fun=movebkwd)
screen_obj.onkey(key="a", fun=counterclock)
screen_obj.onkey(key="d", fun=clockwise)

screen_obj.exitonclick()


# Task 2 - Develope a turtle racing game


from turtle import Turtle, Screen
from random import randint

list_of_turtles_in_race = []
screen_obj = Screen()
user_input = screen_obj.textinput("Make your bet", "Who do you think would win")

turte_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_index = [-110, -80, -50, -20, 10, 40]

for index in range(0,6):
    turte_obj = Turtle(shape="turtle")
    turte_obj.color(turte_colors[index])
    turte_obj.penup()
    turte_obj.goto(x=-250, y=y_index[index])
    list_of_turtles_in_race.append(turte_obj)
    
is_still_racing = True    
while is_still_racing:
    
    for turtle in list_of_turtles_in_race:
        if turtle.xcor() > 200:
            is_still_racing = False
            if turtle.pencolor() == user_input:
                print("Congratulations, you won!")
            else:
                print(f"Sorry, you lose. The {turtle.pencolor()} won")
        turtle.forward(randint(0,100))


screen_obj.exitonclick()