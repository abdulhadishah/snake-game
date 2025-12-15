from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 18, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("#fdd835")
        self.hideturtle()
        self.penup()
        self.goto(0, 287)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} \t\t High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over.", move=False, align=ALIGNMENT, font=FONT)

class BoundaryLine(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(4)
        self.hideturtle()
        self.color("#00bcd4")
        self.penup()
        self.goto(-280, -280)
        self.pendown()
        for _ in range(4):
            self.forward(560)  # length of one side
            self.left(90)  # turn 90 degrees

