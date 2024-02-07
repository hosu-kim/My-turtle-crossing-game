from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_incresement = [1]

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance in self.car_incresement:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            random_y = randint(-249, 249)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def add_more_cars(self):
        self.car_incresement = [1, 2]

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

