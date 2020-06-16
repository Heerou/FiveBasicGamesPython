# simple pong game in python 3
# By Julio Alvarez Pimiento


import turtle
import os
import winsound

soundDirectory = os.path.dirname(os.path.abspath(__file__))
palletsSound = os.path.join(soundDirectory, 'Sounds\_Laser_Shoot2.wav')
borderSound = os.path.join(soundDirectory, 'Sounds\_Pickup_Coin.wav')

screen = turtle.Screen()
screen.title("Pong by Julio.A.P.")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Score Table
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "bold"))

# Score
scoreA = 0
scoreB = 0


# Function
def MoveUpPaddleA():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def MoveDownPaddleA():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def MoveUpPaddleB():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def MoveDownPaddleB():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
screen.listen()
screen.onkeypress(MoveUpPaddleA, "w")
screen.onkeypress(MoveDownPaddleA, "s")
screen.onkeypress(MoveUpPaddleB, "Up")
screen.onkeypress(MoveDownPaddleB, "Down")

# Main game Loop
while True:
    screen.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    # Ball Goings up
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(borderSound, winsound.SND_ASYNC)

    # Ball Goings down
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(borderSound, winsound.SND_ASYNC)

    # Ball Goings right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound(borderSound, winsound.SND_ASYNC)

    # Ball Goings left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound(borderSound, winsound.SND_ASYNC)

    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(palletsSound, winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(palletsSound, winsound.SND_ASYNC)
