from turtle import Turtle,Screen
import random

colors = ["red","green","blue"]
timmy = Turtle()
my_screen=Screen()
timmy.shape("turtle")
def draw_shape(num_of_sides):
  angle=360/num_of_sides
  for i in range(num_of_sides):
       timmy.forward(100)
       timmy.right(angle)

for i in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(i)



Screen().exitonclick()