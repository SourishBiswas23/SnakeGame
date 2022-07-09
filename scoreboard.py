from turtle import Turtle, update
from pathlib import Path

WIDTH_OF_SCREEN = 800
HEIGHT_OF_SCREEN = 800
COLOR = "white"
TEXT_ALIGNMENT = "center"
FONT = ("Fantasque Sans Mono", 16, "normal")
HIGHSCORE_FOLDER = "highscore.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        update()
        self.color(COLOR)
        self.goto(y=HEIGHT_OF_SCREEN/2-25, x=0)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        highscore = self.get_highscore()
        if self.score > highscore:
            self.update_highscore(self.score)
            highscore = self.score

        self.write(f"Score: {self.score}   Highscore:{highscore}",
                   False, TEXT_ALIGNMENT, FONT)
        update()

    def game_over(self):
        self.clear()
        highscore = self.get_highscore()
        self.write(f"Game Over. Score: {self.score} Highscore:{highscore}",
                   False, TEXT_ALIGNMENT, FONT)
        update()

    def get_highscore(self):
        script_location = Path(__file__).absolute().parent
        highscore_file_location = script_location / HIGHSCORE_FOLDER
        highscore = 0
        with open(highscore_file_location) as file:
            highscore = int(file.read())
        return highscore

    def update_highscore(self, highscore):
        script_location = Path(__file__).absolute().parent
        highscore_file_location = script_location / HIGHSCORE_FOLDER
        with open(highscore_file_location, "w") as file:
            file.write(str(highscore))
