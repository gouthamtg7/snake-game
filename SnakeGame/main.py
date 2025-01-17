import random
import time
from turtle import Turtle, Screen
from SnakeBody import CreateSnake
from Food import Food
from Score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)

snake = CreateSnake()
snake.create_a_snake_body()
food = Food(snake)
score = Score()
screen.tracer(0)
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move_the_snake()

    if food.did_you_eat(snake, score):
        food.deploy_food(snake)

    score.display()  # Update score display each frame
    game_over = snake.gameover()

    if game_over:
        score.score_display.clear()
        score.score_display.goto(0, 0)
        score.score_display.write("Game Over", align="center", font=("Arial", 24, "bold"), color="red")

screen.exitonclick()
