from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5



    def create_cars(self):
        chance = random.randint(0, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(450, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5



