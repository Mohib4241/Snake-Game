import turtle
from time import sleep
from turtle import Turtle,Screen

#
#
#
#
# screen = Screen()
# screen.bgcolor("black")

ALIGNMENT = "center"
FONT = ('courier', 24 ,'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.highscore= 0
        self.hideturtle()
        self.goto(-200,300 - 10)
        self.color("white")
        self.write(arg=f"Score : {0}",align=ALIGNMENT,font=FONT)


    def add_score(self,score):
        self.clear()
        self.score = score
        self.goto(-200,300 - 10)
        self.write(arg=f"Score : {score}",align=ALIGNMENT,font=FONT)
        self.High_Score(self.highscore)

    def High_Score(self,high_score):
        if high_score < self.score:
            self.highscore = self.score
        else:
            self.highscore = high_score

        self.goto(40,300-10)
        self.write(arg=f"High Score : {self.highscore}",align='center',font=FONT)
        return self.highscore


    def gameOver(self):
        self.goto(0,0)
        self.write(arg="Game Over",align=ALIGNMENT,font=FONT)




# Scoreboard = ScoreBoard(100)
# screen.exitonclick()
