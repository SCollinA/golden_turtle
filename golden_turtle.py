from turtle import *

# use the golden ration and turtle to draw shapes, start with rectangles

GOLDEN_RATIO = 1.618

turtle = Turtle()
screen = Screen()
screen.setup(1000, 1000)

def most_of_a_rectangle(short_side, long_side):
    turtle.forward(short_side)
    turtle.right(90)
    turtle.forward(long_side)
    turtle.right(90)
    turtle.forward(short_side)
    turtle.right(90)

short_side = 1
long_side = GOLDEN_RATIO

while True:
    most_of_a_rectangle(short_side, long_side)
    short_side = long_side
    long_side = short_side * GOLDEN_RATIO



