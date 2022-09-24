import turtle
from turtle import Screen
from frog import Frog
from car import Car
from score import Score
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)

frog = Frog()
car = Car()
score = Score()
turtle.colormode(255)


screen.listen()
screen.onkeypress(key="Up", fun=frog.move_forward)

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move_forward()

    for c in car.all_cars:
        if c.distance(frog) < 20:
            game_is_on = False
            score.game_over()


    if frog.ycor() > 230:
        frog.refresh()
        score.increase_score()
        car.level_up()


screen.exitonclick()
