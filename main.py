import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with turtle and a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.call_game_over()
            game_is_on = False

    # Detect when the turtle reaches the top edge of the screen
    if player.is_at_finish_line():
        player.return_to_start()
        scoreboard.increase_score()
        car_manager.increase_car_speed()



screen.exitonclick()