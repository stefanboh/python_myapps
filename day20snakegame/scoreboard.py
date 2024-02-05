from turtle import Turtle
ALIGNMET = "center"
FONT = ("arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMET, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))


        self.score = 0
        self.updatescoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over", align=ALIGNMET, font=FONT)

    def scoreup(self):
        self.score += 1
        # self.clear() was here in previuse part
        self.updatescoreboard()