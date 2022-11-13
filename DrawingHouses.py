"""
The program below draws three houses in different sizes and different positions.

pu()
Pick the pen up to temporarily move without drawing.

pd()
Put the pen down to resume drawing.
"""

from turtle import *


def shape(size, angle):
    turns = 360 // angle
    for i in range(int(turns)):
        forward(size)
        left(angle)


def square(size):
    shape(size, 90)


def triangle(size):
    shape(size, 120)


def house(size):
    square(size)
    left(90)
    forward(size)
    right(90)
    triangle(size)


def village():
    house(100)
    pu()
    setpos(-300, -50)
    pd()
    house(200)
    pu()
    setpos(-100, 200)
    pd()
    house(50)


village()
