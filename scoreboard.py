from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.color("Black")
        self.penup()
        self.goto(-350, 280)
        self.update_level()


    def update_level(self):
        self.write(f"Level  = {self.level}", False, "center", ('Courier', 20, 'bold'))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Courier", 44, "normal"))
