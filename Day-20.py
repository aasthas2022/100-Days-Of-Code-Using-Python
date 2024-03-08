# Day 20: Section 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates

# Snake game.

from turtle import Turtle, Screen
import time

direction_change_degree = {
    "right": 0,
    "up": 90,
    "left": 180,
    "down": 270
}

def create_turtle_obj(position):
    turtle_obj = Turtle("square")
    turtle_obj.color("white")
    turtle_obj.penup()
    turtle_obj.goto(position)
    return turtle_obj

def create_snake():
    return [create_turtle_obj(position) for position in [(0, 0), (-20, 0), (-40, 0)]]

def move():
    global turtle_objs
    for seg_num in range(len(turtle_objs) - 1, 0, -1):
        new_x = turtle_objs[seg_num - 1].xcor()
        new_y = turtle_objs[seg_num - 1].ycor()
        turtle_objs[seg_num].goto(new_x, new_y)
    head.forward(20)

def up():
    global head
    if head.heading() != direction_change_degree["down"]:
        head.setheading(direction_change_degree["up"])

def down():
    global head
    if head.heading() != direction_change_degree["up"]:
        head.setheading(direction_change_degree["down"])

def left():
    global head
    if head.heading() != direction_change_degree["right"]:
        head.setheading(direction_change_degree["left"])

def right():
    global head
    if head.heading() != direction_change_degree["left"]:
        head.setheading(direction_change_degree["right"])

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

turtle_objs = create_snake()
head = turtle_objs[0]

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    move()

screen.exitonclick()
