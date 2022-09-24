from turtle import Turtle
import random
MOVE = 10


class Car(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE


    def create_car(self):
        random_choice = random.randint(1,4)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_car.shapesize(stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(250, random.randint(-230, 230))
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def refresh(self):
        self.goto(250, random.randint(-230, 230))

    def level_up(self):
        self.car_speed += MOVE


