from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Pong Game")

l_paddle = Paddle(x_start=-350, y_start=0)
r_paddle = Paddle(x_start=350, y_start=0)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = Ball()
scoreboard = Scoreboard()


# Detect collision with wall and bounce
# Detect collision with paddle and bounce
# detect when paddle misses the ball scoring a point
# keep score
timer = 0.1
game_is_on = True
while game_is_on:
    time.sleep(timer)
    screen.update()
    ball.move()
    # Detect collisions with walls
    if ball.ycor() > 280:
        ball.y_dir = 'down'
    if ball.ycor() < -280:
        ball.y_dir = 'up'
    if ball.xcor() > 380:
        ball.reset_position()
        ball.x_dir = 'left'
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        timer = 0.1
    if ball.xcor() < -380:
        ball.reset_position()
        ball.x_dir = 'right'
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        timer = 0.1


    # Detect collisions with paddle:
    if ball.distance(r_paddle) < 60 and ball.xcor() < 340:
        ball.x_dir = 'left'
        timer *= 0.9
    if ball.distance(l_paddle) < 60 and ball.xcor() > -340:
        ball.x_dir = 'right'
        timer *= 0.9


screen.exitonclick()
