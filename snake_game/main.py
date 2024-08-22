from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(n=0)
snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")
food = Food()
sco = Score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sco.increase_score()
    if snake.head.xcor() >280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        sco.reset()
        snake.reset_snake()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            sco.reset()
            snake.reset_snake()



screen.exitonclick()