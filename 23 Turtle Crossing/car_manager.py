from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


# screen is 600 px
# top 50 and bottom 50 are safe zone so generate cars between (-250,250)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.level = 1
        self.move_speed = self.STARTING_MOVE_DISTANCE + ( (self.level -1) * self.MOVE_INCREMENT )

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.randint(-250, 250)
        new_car.goto(x=300, y=random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)
