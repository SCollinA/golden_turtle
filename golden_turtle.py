from turtle import *

def square(side):
    for i in range(4):
        forward(side)
        right(90)

def fractal(rotate, increase):
    side = 50
    while True:
        square(side)
        right(rotate)
        side += increase

fractal(30, 50)