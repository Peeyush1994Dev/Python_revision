from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(F"score:{self.score}",align="center",font= ("Arial",8,"normal"))
        self.hideturtle()


    def increment(self):
        self.score += 1
        self.clear()
        self.write(F"score:{self.score}",align="center",font= ("Arial",20,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAMEOVER",align = "center",font=("Arial",20,"normal"))


