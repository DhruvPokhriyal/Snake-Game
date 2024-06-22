from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")

    def display_score(self):
        self.clear()
        self.teleport(0, 260)
        self.write(f"Score : {self.score}", False, align="center", font=('Courier', 28, 'normal'))

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.teleport(0,0)
        self.write("GAME OVER", False, align="center", font=('Courier', 28, 'normal'))

