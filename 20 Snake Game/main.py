from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

food = Food()
snake = Snake()
screen.listen()
score = Scoreboard()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()

    # detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # detect collision with tail.
    # if head collides with any segment in tail:
       # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
