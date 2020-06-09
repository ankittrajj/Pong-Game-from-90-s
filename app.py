# Simple Pong Game using turtle Module
# by Ankit Raj


import turtle

wn = turtle.Screen()
wn.title("Pong by Ankit Raj")
wn.bgcolor('blue')
wn.setup(width=800, height=600)
wn.tracer(0)


# player A (set the player to the position)
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape('square')
player_a.color('black')
player_a.penup()
player_a.goto(-375, 0)
player_a.shapesize(stretch_len=1, stretch_wid=5)


# player B (set the player to the position)
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape('square')
player_b.color('white')
player_b.penup()
player_b.goto(375, 0)
player_b.shapesize(stretch_len=1, stretch_wid=5)


# ball (set the ball in the middle of the field)
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
# ball.penup()
ball.goto(0, 0)
# player_a.shapesize(stretch_len=1, stretch_wid=5)


# make the function to make player move in up and down direction for both players
def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)


def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)


def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)


def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)


# keyboard input (by pressing the keyboard keys player move in up and down direction)
wn.listen()
wn.onkeypress(player_a_up, 'w')
wn.onkeypress(player_a_down, 's')
wn.onkeypress(player_b_up, 'Up')
wn.onkeypress(player_b_down, 'Down')


# main game loop
while True:
    wn.update()