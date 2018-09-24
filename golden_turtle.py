from turtle import *

# use the golden ration and turtle to draw shapes, start with rectangles

GOLDEN_RATIO = 1.618

turtle = Turtle()
turtle.speed(6)
turtle_on_screen = True
screen = Screen()
screen.setup(400, 400)

def golden_rectangle(short_side, long_side):
    turtle_on_screen = True
    while turtle_on_screen:
        turtle.forward(short_side)
        turtle.right(90)
        turtle.forward(long_side)
        turtle.right(90)
        turtle.forward(short_side)
        turtle.right(90)
        short_side = long_side
        long_side = short_side * GOLDEN_RATIO
        if turtle.ycor() > 400 or turtle.xcor() > 400:
            turtle_on_screen = False

def golden_spiral():
    turtle_on_screen = True
    radius = 1
    while turtle_on_screen:
        turtle.circle(radius, extent=90)
        radius *= GOLDEN_RATIO
        if turtle.ycor() > 400 or turtle.xcor() > 400:
            turtle_on_screen = False


def turtle_home():
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.pendown()
    turtle_on_screen = True


short_side = 1
long_side = GOLDEN_RATIO
golden_rectangle(short_side, long_side)
turtle_home()
turtle.right(90)
golden_spiral()
turtle_home()
turtle.right(180)
golden_rectangle(short_side, long_side)
turtle_home()
turtle.right(270)
golden_spiral()
turtle_home()
turtle.right(90)
golden_rectangle(short_side, long_side)
turtle_home()
turtle.right(180)
golden_spiral()
turtle_home()
turtle.right(270)
golden_rectangle(short_side, long_side)
turtle_home()
turtle.right(360)
golden_spiral()


input()
