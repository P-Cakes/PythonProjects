from turtle import Screen, Turtle
import time

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position[0],position[1])
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)

    for seg in range(len(segments)-1 ,0,-1):
        new_x = segments[seg-1].xcor()
        new_y = segments[seg-1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)









screen.exitonclick()

