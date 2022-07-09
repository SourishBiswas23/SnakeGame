import time
from tkinter import RIGHT
from turtle import Turtle, update
POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0),
             (-100, 0), (-120, 0), (-140, 0), (-160, 0), (-180, 0), (-200, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MIN_DISTANCE_OF_HEAD_FROM_BODY = 19


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.create_segments(position)
        update()

    def create_segments(self, position):
        segment = Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position[0], position[1])
        self.segments.append(segment)

    def move_segments(self):
        update()
        for i in range(len(self.segments)-1, 0, -1):
            xcoordinate = self.segments[i-1].xcor()
            ycoordinate = self.segments[i-1].ycor()
            self.segments[i].goto(xcoordinate, ycoordinate)
        self.segments[0].forward(MOVE_DISTANCE)

    def extend_snake(self):
        self.create_segments(self.segments[-1].position())

    def bit_the_tail(self):
        bit_tail = False
        for segment in self.segments[1:]:
            if segment.distance(self.segments[0]) < MIN_DISTANCE_OF_HEAD_FROM_BODY:
                bit_tail = True
                break
            else:
                bit_tail = False
        return bit_tail

    def move_head_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_head_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_head_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_head_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
