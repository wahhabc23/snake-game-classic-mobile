from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
snake = Snake()
food = Food()
score = Score() 
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xpersia")
screen.tracer(0)
screen.listen()
screen.onkey(snake.north,"Up")
screen.onkey(snake.south,"Down")
screen.onkey(snake.west,"Left")
screen.onkey(snake.east,"Right")
game_on = True

while game_on:
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) <15:
        snake.add_snake()
        food.refresh()
        score.increase_score()
    screen.update()
    
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        game_on = False
        score.game_over()
    
    for snake_tail in snake.list[1:]:
        if snake.head.distance(snake_tail) < 10:
            game_on =False
            score.game_over()

screen.exitonclick()
