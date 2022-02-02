from turtle import Turtle

MOVE_DISTANCE = 20

EAST = 0
WEST = 180
NORTH = 90
SOUTH = 270

class Snake:
    """This method will creake a snake."""

    def __init__(self) -> None:
        self.list = []
        self.create_snake()
        self.head = self.list[0]

    def create_snake(self):
        x = 0
        for _ in range(0, 3):
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(x=x, y=0)
            x -= 20
            self.list.append(turtle)

    def add_snake(self):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(self.list[-1].position())
        self.list.append(turtle)   
             
        
    def move(self):
        """This will make the snake start moving."""
        length = len(self.list) - 1
        for n in range(length, 0, -1):
            new_x = self.list[n-1].xcor()
            new_y = self.list[n-1].ycor()
            self.list[n].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def north(self):
        """This will change snake direction to North"""
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def south(self):
        """This will change snake direction to South"""
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def west(self):
        """This will change snake direction to West"""
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def east(self):
        """This will change snake direction to East"""
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
            
        
