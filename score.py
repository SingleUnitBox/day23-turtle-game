from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220, 200)
        self.score_level = 0
        self.update_score()


    def update_score(self):
        self.write(f"Level: {self.score_level}", font=('Arial', 20, 'normal'))
    def increase_score(self):
        self.clear()
        self.score_level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 25, 'normal'))
