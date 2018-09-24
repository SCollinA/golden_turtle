from turtle import *

# use the golden ration and turtle to draw shapes, start with rectangles

GOLDEN_RATIO = 1.618

turtle = Turtle()
turtle.speed(0)
turtle_on_screen = True
screen = Screen()
screen.setup(400, 400)

def most_of_a_rectangle(short_side, long_side):
    turtle.forward(short_side)
    turtle.right(90)
    turtle.forward(long_side)
    turtle.right(90)
    turtle.forward(short_side)
    turtle.right(90)

short_side = 1
long_side = GOLDEN_RATIO

while turtle_on_screen:
    most_of_a_rectangle(short_side, long_side)
    short_side = long_side
    long_side = short_side * GOLDEN_RATIO
    if turtle.ycor() > 400 or turtle.xcor() > 400:
        turtle_on_screen = False

turtle.penup()
turtle.goto(0,0)
turtle_on_screen = True
input()
