import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

cars = CarManager()

game_tick = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_tick += 1
    if game_tick % 6 == 0:
        cars.create_car()
    cars.move_cars()
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level += 1
        cars.level += 1
        scoreboard.update_scoreboard()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()
