#Pong game

import turtle
import os
import random

# Screen
wn = turtle.Screen()
wn.title('Pong by Andres Araya')
wn.bgcolor('black')
wn.setup(width=1200, height=400)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-550, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(550, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = 6

# Live score
li_sc = turtle.Turtle()
li_sc.speed(0)
li_sc.color('white')
li_sc.penup()
li_sc.hideturtle()
li_sc.goto(0, 160)
li_sc.write('Player A: 0  Player B: 0', align='center', font=('Courier', 24, 'normal'))

# Paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
#wn.onkeypress(paddle_b_up, 'Up')
#wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:

    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # CPU reaction
    if ball.xcor()>400:
        x = random.randint(50,90)
        if paddle_b.ycor() > (ball.ycor() + x):
            paddle_b_down()

        if paddle_b.ycor() < (ball.ycor() - x):
            paddle_b_up()

    if ball.xcor()<490:
        if paddle_b.ycor() > 40:
            paddle_b_down()
        if paddle_b.ycor() < -40:
            paddle_b_up()

    # Border bounce
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1
        os.system('afplay bounce.wav&')

    if ball.ycor() < -180:
        ball.sety(-180)
        ball.dy *= -1
        os.system('afplay bounce.wav&')

    # Scoring system
    if ball.xcor() > 580:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        li_sc.clear()
        li_sc.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -580:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        li_sc.clear()
        li_sc.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    # Paddle bounce
    if (ball.xcor() > 540 and ball.xcor() < 550) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor()-60):
        ball.setx(540)
        ball.dx *= -1
        os.system('afplay bounce.wav&')

    if (ball.xcor() < -540 and ball.xcor() > -550) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor()-60):
        ball.setx(-540)
        ball.dx *= -1
        os.system('afplay bounce.wav&')

    # Winner
    if score_a > 5 and score_a > score_b +1:
        li_sc.clear()
        li_sc.goto(0, 0)
        li_sc.write('Player A wins {} points to {} vs Player B'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        ball.dx = 0
        ball.dy = 0
        ball.goto(0, -100)

    if score_b > 5 and score_b > score_a +1:
        li_sc.clear()
        li_sc.goto(0, 0)
        li_sc.write('Player B wins {} points to {} vs Player A'.format(score_b, score_a), align='center', font=('Courier', 24, 'normal'))
        ball.dx = 0
        ball.dy = 0
        ball.goto(0, -100)
