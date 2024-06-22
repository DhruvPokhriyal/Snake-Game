from turtle import Turtle


class Snake:
    """Create a Snake Object that can perform Specific Actions."""

    def __init__(self):
        """Initializing the variables and Creating the Snake"""
        self.snake = []
        self.distance = 0
        for i in range(3):
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.speed("normal")
            snake_body.teleport(self.distance, 0)
            self.distance -= 20
            self.snake.append(snake_body)
        self.head = self.snake[0]

    def move(self):
        """Moving The Snake"""
        for s_id in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[s_id - 1].xcor()
            new_y = self.snake[s_id - 1].ycor()
            self.snake[s_id].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        """Direct Snake in Upward Direction"""
        if self.snake[0].heading() == 270:
            return
        self.snake[0].seth(90)

    def down(self):
        """Direct Snake in Downward Direction"""
        if self.snake[0].heading() == 90:
            return
        self.snake[0].seth(270)

    def right(self):
        """Direct Snake in Right Direction"""
        if self.snake[0].heading() == 180:
            return
        self.snake[0].seth(0)

    def left(self):
        """Direct Snake in Left Direction"""
        if self.snake[0].heading() == 0:
            return
        self.snake[0].seth(180)

    def new_segment(self):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.speed("normal")
        direction = self.head.heading()
        head_x_cor = self.head.xcor()
        head_y_cor = self.head.ycor()
        if direction == 0:
            snake_body.teleport(head_x_cor-self.distance,head_y_cor)
        elif direction == 180:
            snake_body.teleport(head_x_cor+self.distance,head_y_cor)
        elif direction == 90:
            snake_body.teleport(head_x_cor,head_y_cor-self.distance)
        elif direction == 270:
            snake_body.teleport(head_x_cor,head_y_cor+self.distance)
        self.distance -= 20
        self.snake.append(snake_body)
    def extend(self):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.speed("normal")
        snake_body.goto(self.snake[-1].position())
        self.snake.append(snake_body)







