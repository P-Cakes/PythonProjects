from turtle import Turtle, Screen

screen_height = 400
screen_width = 500
heights = [-70,-40,-10,20,50,80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(screen_width/-2, heights[turtle_index] )
    tim.setheading(0)
    tim.color(colors[turtle_index])
    all_turtles.append(tim)

is_race_on = False

screen = Screen()
screen.setup(screen_width, screen_height)
user_bet = screen.textinput(title= 'Make a bet',prompt= 'Which turtle is going to win the race?  Enter your color:  ')
if user_bet:
    is_race_on = True

from random import randint
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.color()
            is_race_on=False
            print(f"The winner was {winner[0]}.")
            if str(winner[0]).lower() == user_bet.lower():
                print("Your bet wins!")
            else:
                print ("Your bet lost!")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()
