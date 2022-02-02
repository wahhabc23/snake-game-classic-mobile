from random import randint
from turtle import Turtle


class Food(Turtle):
    """Create food at random positions of screen"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed(0)
        self.refresh()

    def refresh(self):
        """This method will put food in random position"""
        random_x = randint(-280, 280)
        random_y = randint(-280, 270)
        self.goto(random_x, random_y)
