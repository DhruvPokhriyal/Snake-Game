from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
game_is_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
writer = Scoreboard()
writer.display_score()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 15:
        food.refresh()
        writer.update_score()
        writer.display_score()
        snake.extend()
    # Detect Collision with wall
    if (snake.head.xcor() > -290 and
            snake.head.xcor() < 290 and
            snake.head.ycor() < 290 and
            snake.head.ycor() > -290):
        pass
    else:
        writer.game_over()
        game_is_on = False
    for body in range(3, len(snake.snake)):
        if snake.head.distance(snake.snake[body])<=20:
            writer.game_over()
            game_is_on = False




screen.exitonclick()
