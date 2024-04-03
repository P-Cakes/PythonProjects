from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_dir = 'right'
        self.y_dir = 'up'

    def move(self):
        if self.y_dir == 'up':
            new_y = self.ycor() + 10
        if self.y_dir == 'down':
            new_y = self.ycor() - 10
        if self.x_dir == 'right':
            new_x = self.xcor() + 10
        if self.x_dir == 'left':
            new_x = self.xcor() - 10
        self.goto(x=new_x, y=new_y)

    def reset_position(self):
        time.sleep(1)
        self.goto(0,0)
