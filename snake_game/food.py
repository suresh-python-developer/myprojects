from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ra_x = random.randint(-280, 280)
        ra_y = random.randint(-280, 280)
        self.goto(ra_x, ra_y)
