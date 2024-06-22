from turtle import Turtle, Screen

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# snake = []
# x_og = 0
# for i in range(3):
#     snake_body = Turtle("square")
#     snake_body.color("white")
#     snake_body.penup()
#     snake_body.teleport(x_og, 0)
#     x_og -= 20
#     snake.append(snake_body)
# # game_is_on = True
# # while game_is_on:
# #     for snake_body in snake:
# #         snake_body.fd(1)
#
#
# screen.listen()
# screen.exitonclick()

tur = Turtle("circle")
tur.turtlesize(0.5, 0.5)
screen = Screen()
tur.teleport(0, 280)
tur.write("Hello", False, align="center", font=('Arial', 28, 'normal'))

screen.exitonclick()
