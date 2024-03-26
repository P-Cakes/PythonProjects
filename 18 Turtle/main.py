from turtle import Turtle, Screen
import turtle as t

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
#colors can be set as defined by tkinter (tk color specification strings)
timmy_the_turtle.color('firebrick')



def draw_circle(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

draw_circle(timmy_the_turtle)

def draw_dashed_line(turtle,distance):
    for i in range(distance):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

draw_dashed_line(timmy_the_turtle,15)

screen = Screen()
screen.exitonclick()
