from turtle import Turtle
import random
WIDTH_OF_SCREEN = 800
HEIGHT_OF_SCREEN = 800
COLOR_OF_FOOD = "blue"
STRETCH_WIDTH = 0.5
STRETCH_LENGTH = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(COLOR_OF_FOOD)
        self.penup()
        self.refresh_food()
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)

    def refresh_food(self):
        xcoorinate = random.randint(-1*(WIDTH_OF_SCREEN/2-40),
                                    (WIDTH_OF_SCREEN/2-40))
        ycoordinate = random.randint(-1*(HEIGHT_OF_SCREEN/2-40),
                                     (HEIGHT_OF_SCREEN/2-40))
        self.goto(xcoorinate, ycoordinate)
