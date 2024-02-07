from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def reach_the_goal(self):
        self.score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.home()
        self.write("GAME OVER.", align="center", font=FONT)
