import turtle
from turtle import Turtle,Screen
import random
my_screen=Screen()
timmy = Turtle()
timmy.speed("fastest")
turtle.colormode(255)


def colours():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  c = (r, g, b)
  return c


for i in range(int(360/5)):
  timmy.color(colours())
  timmy.circle(100)
  timmy.right(5)















Screen().exitonclick()