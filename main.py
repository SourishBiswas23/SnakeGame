from turtle import Screen,  tracer
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH_OF_SCREEN = 800
HEIGHT_OF_SCREEN = 800
CRITICAL_DISTANCE_OF_FOOD_FROM_SNAKE = 15
BOUNDARY_X = 380
BOUNDARY_Y = 360

my_screen = Screen()
my_screen.setup(width=800, height=800)
my_screen.title("Snake Game")
my_screen.bgcolor("black")
tracer(0)

snake = Snake()
my_screen.setup(width=WIDTH_OF_SCREEN, height=HEIGHT_OF_SCREEN)
my_screen.listen()
my_screen.onkey(key="Up", fun=snake.move_head_up)
my_screen.onkey(key="Down", fun=snake.move_head_down)
my_screen.onkey(key="Left", fun=snake.move_head_left)
my_screen.onkey(key="Right", fun=snake.move_head_right)

food = Food()
scoreboard = Scoreboard()
game_over = False
while not game_over:
    time.sleep(0.1)
    snake.move_segments()
    game_over = snake.bit_the_tail()
    if food.distance(snake.segments[0]) < CRITICAL_DISTANCE_OF_FOOD_FROM_SNAKE:
        food.refresh_food()
        scoreboard.update_score()
        snake.extend_snake()
    if snake.segments[0].xcor() > BOUNDARY_X or snake.segments[0].xcor() < (-1)*BOUNDARY_X or snake.segments[0].ycor() > BOUNDARY_Y or snake.segments[0].ycor() < (-1)*BOUNDARY_Y:
        game_over = True

scoreboard.game_over()
my_screen.mainloop()
