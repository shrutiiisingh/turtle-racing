import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=650)
screen.tracer(0)
screen.title("Turtle Capstone ")
timmy = Player()
screen.listen()
screen.onkey(timmy.move, "Up")
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()


    if timmy.ycor() > 380:
        timmy.refresh()
        score.increase_level()
        car.level_up()

    for cars in car.all_cars:
        if timmy.distance(cars) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()







