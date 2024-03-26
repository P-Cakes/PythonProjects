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
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed('fastest')

"""
for shape in range(3,10):
    draw_shape(timmy_the_turtle,shape)
    timmy_the_turtle.color(random_color())

for i in range(200):
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random_color())
"""

def draw_spirograph(turtle, size):
    for i in range(int(360/size)):
        turtle.circle(100)
        turtle.color(random_color())
        turtle.right(size)

#draw_spirograph(timmy_the_turtle,5)

def move_timmy_forward():
    timmy_the_turtle.forward(10)

def move_timmy_up():
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(10)

def move_timmy_down():
    timmy_the_turtle.setheading(270)
    timmy_the_turtle.forward(10)

def move_timmy_left():
    timmy_the_turtle.setheading(180)
    timmy_the_turtle.forward(10)

def move_timmy_right():
    timmy_the_turtle.setheading(0)
    timmy_the_turtle.forward(10)
 

screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_timmy_forward)
screen.onkey(key="w",fun=move_timmy_up)
screen.onkey(key="a",fun=move_timmy_left)
screen.onkey(key="s",fun=move_timmy_down)
screen.onkey(key="d",fun=move_timmy_right)
screen.exitonclick()

