from random import randint, choice
from time import sleep
from turtle import Turtle,Screen


screen = Screen()
# width = 600
# height = 600
# screen.setup(width= width , height= height)
# screen.bgcolor("black")
# screen.title("Snake Game")
# screen.tracer(0)


class Snake:


    def __init__(self,shape="square",color="white"):
        self.position = (0, -20, -40)
        self.Snake_Block = []
        for i in range(3):
            self.Snake_Block.append(Turtle(shape))
            self.Snake_Block[i].color(color)
            self.Snake_Block[i].speed("slowest")
            self.Snake_Block[i].penup()
            self.Snake_Block[i].goto(x =self.position[i],y=0)
        self.head = self.Snake_Block[0]



    def add_tail(self):
        tail = Turtle(shape= "square")
        tail.color("white")
        tail.speed("slowest")
        tail.penup()
        co_ord =  self.Snake_Block[len(self.Snake_Block)-1].position()
        x = co_ord[0]
        y = co_ord[1]
        tail.goto(x-20,y-20)
        # screen.tracer(0)

        self.Snake_Block.append(tail)
    #
    def move_forward(self):
        for seg_num in range(len(self.Snake_Block) - 1, 0, -1):
            location = self.Snake_Block[seg_num - 1].position()  # print(location)
            self.Snake_Block[seg_num].goto(location[0], location[1])

        # self.Snake_Block[0].setheading(0)
        self.Snake_Block[0].forward(20)
        screen.update()
        sleep(0.1)


    def move_Up(self):
        pre_angle = self.Snake_Block[0].heading()
        up_angle = 90
        if  pre_angle == 270 :
            return

        for seg_num in range(len(self.Snake_Block) - 1, 0, -1):
            location = self.Snake_Block[seg_num - 1].position()  # print(location)
            self.Snake_Block[seg_num].goto(location[0], location[1])

        self.Snake_Block[0].setheading(up_angle)
        self.Snake_Block[0].forward(20)
        screen.update()
        sleep(0.1)


    def move_left(self):
        left_angle = 180
        pre_angle = self.Snake_Block[0].heading()
        if pre_angle == 0 :
            return

        for seg_num in range(len(self.Snake_Block) - 1, 0, -1):
            location = self.Snake_Block[seg_num - 1].position()            # print(location)
            self.Snake_Block[seg_num].goto(location[0], location[1])

        self.Snake_Block[0].setheading(left_angle)
        self.Snake_Block[0].forward(20)
        screen.update()
        sleep(0.1)

    def move_right(self):
        right_angle = 0
        pre_angle = self.Snake_Block[0].heading()
        if pre_angle == 180 :
            return

        for seg_num in range(len(self.Snake_Block) - 1, 0, -1):
            location = self.Snake_Block[seg_num - 1].position()  # print(location)
            self.Snake_Block[seg_num].goto(location[0], location[1])

        self.Snake_Block[0].setheading(right_angle)
        self.Snake_Block[0].forward(20)
        screen.update()
        # sleep(0.1)

    def move_down(self):
        down_angle = 270
        pre_angle = self.Snake_Block[0].heading()
        if pre_angle == 90 :
            return

        for seg_num in range(len(self.Snake_Block) - 1, 0, -1):
            location = self.Snake_Block[seg_num - 1].position()  # print(location)
            self.Snake_Block[seg_num].goto(location[0], location[1])

        self.Snake_Block[0].setheading(down_angle)
        self.Snake_Block[0].forward(20)
        screen.update()
        sleep(0.1)

#
# snake = Snake(shape="square",color= "white")
#
# screen.listen()
# game = True
# while game:
#     snake.move_forward()
#
#     screen.onkey(snake.move_Up,"Up")
#     screen.onkey(snake.move_left,"Left")
#     screen.onkey(snake.move_right,key="Right")
#     screen.onkey(snake.move_down,key="Down")

#
# sNake = Snake()
# sNake.Detect_Tail_Collision()
# screen.exitonclick()