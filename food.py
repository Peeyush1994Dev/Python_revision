from turtle import Turtle
import random


class Food(Turtle):  ##Class Inheritance ##

    ##Food Creation for Snake
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()


    ##Food location change
    def refresh(self):
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x, self.random_y)
        self.speed("fastest")


