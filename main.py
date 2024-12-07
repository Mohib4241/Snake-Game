import turtle
from time import sleep
from turtle import Screen,Turtle
from turtledemo.clock import setup

from Snake_Food import  Snake_food
from snake import Snake
from ScoreBoard import ScoreBoard

high_score = None
with open("HighScore.txt",'r') as file:
    c = file.read()
    high_score = int(c)

import  time

ALIGNMENT = "center"
FONT = ('courier', 24 ,'normal')

screen = Screen()
width = 600
height = 600 + 2 *24
screen.setup(width= width , height= height )
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

food = Snake_food()
snake = Snake(shape = "square",color = "white")
scoreBoard = ScoreBoard()

screen.onkey(snake.move_Up, "Up")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, key="Right")
screen.onkey(snake.move_down, key="Down")


game = True
score = 0

while game:
    high_score = scoreBoard.High_Score(high_score=high_score)
    screen.update()

    sleep(0.1)
    snake.move_forward()

    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        snake.add_tail()
        scoreBoard.add_score(score)


    # Boundary Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.gameOver()
        print("Game Over")
        game = False

    #Tail Collision
    for block in snake.Snake_Block:
        if block == snake.head :
            pass
        elif snake.head.distance(block) < 10:
            game = False
            scoreBoard.gameOver()


with open("HighScore.txt",mode='w') as file:
    file.write(str(high_score))





























#
# starting_position = [(0,0) , (-20 , 0) ,(-40 , 0)]
#
# x = 0
# for i in range(3):
#     new_width = width / 2 - 10
#     new_height = height / 2 - 10
#     Snake_Block.append(Turtle(shape="square"))
#     Snake_Block[i].speed("slowest")
#     Snake_Block[i].color("white")
#     Snake_Block[i].penup()
#     # turtle_list[i].goto(x= x , y = 0)
#     Snake_Block[i].goto(starting_position[i])
#     # print(turtle_list[i].position())
#     # x -= 20
#
# def move_forward(turtle):
#     turtle.forward(20)
#
# def move_left(turtle):
#     location = turtle.position()
#     turtle.left(90)
#     turtle.forward(20)
#     return location
#
# # move_left(Snake_Block[0])
# # move_left(Snake_Block[1])
# # move_left(Snake_Block[2])
#
# for _ in range(1):
#     screen.update()
#     time.sleep(1)
#
#     for i in range(3):
#         # print(Snake_Block[i].position()
#         move_forward(Snake_Block[i])
#         print(Snake_Block[i].position())
#
# for _ in range(1):
#
#     location = []
#     for i in range(len(Snake_Block)):
#         location.append(Snake_Block[i].position())
#     print(location)
#
#
#     for i in range(0,3):
#         if(i == 0):
#             move_left(Snake_Block[0])
#         # print(location[i-1])
#         else:
#             Snake_Block[i].teleport(location[i-1][0],location[i-1][1])
#
#     screen.update()
#
#     time.sleep(0.3)
#
#
#
#
#
# # tim = Turtle(shape="square")
# # tim.goto(0,20)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # screen.tracer(0)

screen.exitonclick()
