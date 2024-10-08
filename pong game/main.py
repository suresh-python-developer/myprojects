import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen =Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong arcade game")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
ball= Ball()
scoreboard = Scoreboard()
game_is_on =True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()
    if ball.xcor()>320 and ball.distance(right_paddle)<50 or ball.xcor()<-320and ball.distance(left_paddle)<50:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
