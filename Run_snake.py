#!/usr/bin/python

import numpy as np
import turtle
import math
import random
import time

st = turtle.setup(400,400)
wb = turtle.Screen()
wb.bgcolor("black")
turtle.tracer(4)

state = False
# setting up snake body
snake = []

box_space = 20
x = 0
global size
size = 1
def init_snake():
    global body_len
    body_len = 3
    global snake
    snake = []
    for i in range(body_len):
        snake.append(turtle.Turtle())
        snake[i].hideturtle()
        snake[i].penup()
        snake[i].color("red")
        snake[i].shape("square")
        snake[i].shapesize(size,size)
        snake[i].setx(-i*box_space)
a = 0
score = turtle.Turtle()
def score_():
    global a
    a = 0
    score.clear()
    score.color("white")
    score.hideturtle()
    score.pu()
    score.setx(-100)
    score.sety(150)

speed = 2.5

def reset_speed():
    global speed
    speed = 2.5

def move_snake():
    for i in range(body_len):
        if i == 0:
            snake[i].forward(speed)
        else:
            x = snake[i-1].xcor() - snake[i].xcor()
            y = snake[i-1].ycor() - snake[i].ycor()
            diff = math.sqrt(pow(x,2)+pow(y,2))
            if(diff < 18):
                snake[i].forward(speed-(speed/2))
                continue
            snake[i].setheading(snake[i].towards(snake[i-1]))
            snake[i].forward(speed)

def move_right():
    snake[0].right(90)

def move_left():
    snake[0].left(90)

def on_enter():
    print("space pressed")
    global state
    state = True

def is_collosion():
    if snake[0].xcor() >= 100 or snake[0].xcor() <= -100:
        snake[0].right(180)
    if snake[0].ycor() >= 100 or snake[0].ycor() <= -100:
        snake[0].right(180)

def goal_collosion(goal):
    x = goal.xcor() - snake[0].xcor()
    y = goal.ycor() - snake[0].ycor()
    diff = math.sqrt(pow(x,2)+pow(y,2))
    if diff < 10:
        goal.setx(random.randint(-100,100))
        goal.sety(random.randint(-100,100))
        snake.append(turtle.Turtle())
        global body_len
        snake[body_len].penup()
        snake[body_len].color("red")
        snake[body_len].shape("square")
        snake[body_len].shapesize(size,size)
        snake[body_len].setx(snake[body_len-1].xcor()-11)
        snake[body_len].sety(snake[body_len-1].ycor()-11)
        body_len += 1
        global speed
        speed += 0.1
        if speed >= 3:
            speed = 3
        global a
        a += 1
        score.clear()
        score.write("Score: {0}".format(a),align="center",font=(10))

def bit_self():
    for i in range(2,body_len):
        x = snake[0].xcor() - snake[i].xcor()
        y = snake[0].ycor() - snake[i].ycor()
        diff = math.sqrt(pow(x,2)+pow(y,2))
        if diff < 10:
            return True
    return False

def border_setup():
    # border setup
    border = turtle.Turtle()
    border.hideturtle()
    border.color("white")
    border.penup()
    border.setx(-100)
    border.pendown()
    border.sety(-100)
    for i in range(5):
        border.forward(200)
        border.left(90)

def start_screen():
    Text = turtle.Turtle()
    Text.hideturtle()
    Text.color("white")
    Text.pu()
    Text.setx(0)
    Text.sety(0)
    Text.write("Press Space To Become Box Dragon",align="center",font=(20))
    return Text

def snake_vis():
    for i in range(body_len):
        snake[i].st()
def goal_():
    goal = turtle.Turtle()
    goal.penup()
    goal.color("green")
    goal.shape('circle')
    goal.shapesize(1,1)
    goal.setx(random.randint(-100,100))
    goal.sety(random.randint(-100,100))
    return goal
def game_over_reset():
    Text = turtle.Turtle()
    Text.hideturtle()
    Text.color("white")
    Text.pu()
    Text.setx(0)
    Text.sety(0)
    for i in range(10):
        Text.clear()
        Text.write("Game over. Resets in {0} of 10 sec".format(i),align="center",font=(20))
        time.sleep(1)

    Text.clear()

def main():
    init_snake()
    score_()

    wb.listen()
    wb.onkey(move_right,"Right")
    wb.onkey(move_left,"Left")
    wb.onkey(on_enter,"space")

    while True:
        if state == False:
            t = start_screen()
            time.sleep(0.3)
            t.clear()
        else:
            break

    t.clear()
    snake_vis()
    score.write("Score: {0}".format(a),align="center",font=(10))
    border_setup()
    #goal
    goal = goal_()

    while True:
        move_snake()
        goal_collosion(goal)
        is_collosion()
        if bit_self():
            wb.resetscreen()
            game_over_reset()
            border_setup()
            reset_speed()
            init_snake()
            score_()
            score.write("Score: {0}".format(a),align="center",font=(10))
            goal = goal_()
            snake_vis()

if __name__ == '__main__':
    main()
