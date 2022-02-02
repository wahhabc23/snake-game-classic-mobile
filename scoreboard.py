from turtle import Turtle
ALIGN = 'center'
FONT = ['Arial', 12, 'normal']


class Score(Turtle):
    """Creates a score-board."""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        self.speed(0)
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER\nFinal Score = {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
