from turtle import Turtle

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.goto(0, -230)


    def move_forward(self):
        self.forward(20)