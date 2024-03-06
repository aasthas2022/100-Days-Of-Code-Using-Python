## Day 18 - Section 18 Intermediate - Turtle & the Graphical User Interface (GUI)


# Task 1 - Use turtle module to draw a square
from turtle import Turtle, Screen

tutle_obj = Turtle()
screen_obj = Screen()

for _ in range(4):
    tutle_obj.forward(100)
    tutle_obj.right(90)

screen_obj.exitonclick()

# Task 2 - Use turtle module to draw a line of 10 paces and then a gap of 10 paces (basically a dotted line)

from turtle import Turtle, Screen

tutle_obj = Turtle()
screen_obj = Screen()

for _ in range(15):
    tutle_obj.pendown()
    tutle_obj.forward(10)
    tutle_obj.penup()
    tutle_obj.forward(10)


screen_obj.exitonclick()

# Task 3 -Use turtle module to be drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon. So from three-sided shape to ten-sided shape and each of those shapes is going to be drawn with a random color, and each of the sides are going to be 100 in terms of length. All of these shapes overlaid on each other and drawn out in sequence.

import turtle
import random
screen_obj = turtle.Screen()

def draw_polygon(n, length):
    angle = 360 / n
    for _ in range(n):
        turtle.forward(length)
        turtle.right(angle)

shapes = ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon"]
sides = [3, 4, 5, 6, 7, 8, 9, 10]

turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

for shape, num_sides in zip(shapes, sides):
    turtle.color(random.random(), random.random(), random.random())  # Random color
    draw_polygon(num_sides, 100)

turtle.done()

screen_obj.exitonclick()

# Task 4 - Use turtle module to generate a random walk

from turtle import Turtle, Screen
import random

turtle_obj = Turtle()
screen_obj = Screen()

degree_of_turn = [0, 90, 180, 360]

for _ in range(100):
    turtle_obj.color(random.random(), random.random(), random.random())
    turtle_obj.forward(20)
    turtle_obj.setheading(degree_of_turn[random.randint(0,3)])

screen_obj.exitonclick()

# Task 5 - Make spriopgraph:

from turtle import Turtle, Screen
import random

turtle_obj = Turtle()
screen_obj = Screen()

for i in range(15,100, 2):
    turtle_obj.circle(i)
    turtle_obj.left(30)

screen_obj.exitonclick()
