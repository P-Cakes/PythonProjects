from turtle import Screen, Turtle
import time
from snake import Snake

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key= 'Up')
screen.onkey(fun=snake.down, key= 'Down')
screen.onkey(fun=snake.left, key= 'Left')
screen.onkey(fun=snake.right, key= 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move()













screen.exitonclick()

