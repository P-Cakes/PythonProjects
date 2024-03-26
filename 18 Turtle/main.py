from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
#colors can be set as defined by tkinter (tk color specification strings)
timmy_the_turtle.color('firebrick')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


def draw_circle(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

#draw_circle(timmy_the_turtle)

def draw_dashed_line(turtle,distance):
    for i in range(distance):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

#draw_dashed_line(timmy_the_turtle,15)

def draw_shape(turtle, num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)



directions = [90,180,270,0]
colors = ['Red','Green','Blue','Orange','LawnGreen','LimeGreen','Teal','Coral']
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed('fastest')

for shape in range(3,10):
    draw_shape(timmy_the_turtle,shape)
    timmy_the_turtle.color(random_color())

for i in range(200):
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random_color())


screen = Screen()
screen.exitonclick()

