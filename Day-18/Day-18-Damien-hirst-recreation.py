import colorgram
import turtle as t
from turtle import Turtle, Screen
from random import choice


colors = colorgram.extract('./Day-18/damien-hirst-severed-spots-img.jpg', 10)
colors_rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

turtle_obj = Turtle()
turtle_obj.penup()
t.colormode(255)

for i in range(10):
    turtle_obj.setpos(-225,-200 + 50 * i)
    for _ in range(10):
        turtle_obj.pendown()
        turtle_obj.dot(20, choice(colors_rgb))
        turtle_obj.penup()
        turtle_obj.forward(50) 

screen_obj = Screen()
screen_obj.exitonclick()