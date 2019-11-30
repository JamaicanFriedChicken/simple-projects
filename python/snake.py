# Simple Snake Game in Python

import turtle
import time

delay = 0.1

# Setting up the screen
window = turtle.Screen()
window.title("Simple Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()  # turtle module was designed for drawing lines, penup() doesn't let it draw anything
head.goto(0, 0)
head.direction = "stop"

def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Controls
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main game loop
while True:
    window.update()
    move()
    time.sleep(delay)

# Allows window to remain open by "looping" it
window.mainloop()