from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, BoundaryLine
import time


screen = Screen()
screen.setup(650, 650)
screen.bgcolor("#1a1a1a")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
BoundaryLine()

KEY_MAP = {
    snake.up: ["Up", "w", "W"],
    snake.down: ["Down", "s", "S"],
    snake.left: ["Left", "a", "A"],
    snake.right: ["Right", "d", "D"],
}


screen.listen()

for action, keys in KEY_MAP.items():
    for key in keys:
        screen.onkey(action, key)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.12)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 279 or snake.head.xcor() < -279 or snake.head.ycor() > 279 or snake.head.ycor() < -279:
        scoreboard.reset()
        snake.reset()

    # Detect collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # snake.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
