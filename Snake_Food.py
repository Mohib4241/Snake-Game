from time import sleep
from  turtle import Turtle,Screen
from random import random, randint, uniform

width = 300
height = 300
# screen  = Screen()
# screen.tracer(0)
# screen.setup(width*2,height*2)

class Snake_food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        # screen.update()
        sleep(0.1)

    def refresh(self):
        x = randint(-width + 30, width - 30)
        y = randint(-height + 30, height - 30)
        self.teleport(x,y)




# food = Snake_food()
# screen.exitonclick()