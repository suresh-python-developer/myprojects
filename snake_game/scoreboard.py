from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as self.file:
            self.high_score= int(self.file.read())

        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            self.score = 0
            with open("data.txt", mode="w") as self.data:
                self.data.write(str(self.high_score))

            self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"game over and score is: {self.score}", align="center", font=("Arial", 24, "normal"))
    def update_score(self):
        self.clear()
        self.write(f"score : {self.score}  high score : {self.high_score}", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1

        self.update_score()


