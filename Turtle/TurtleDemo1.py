# Examples taken from https://www.geeksforgeeks.org/turtle-programming-python/
import turtle

def firstTurtle():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Turtle")
    t = turtle.Turtle()
    t.forward(100)
    t.done()

def turtleSquare():
    t = turtle.Turtle()
    for i in range(4):
        t.forward(50)
        t.right(90)
    turtle.done()


def turtleStar():
    t = turtle.Turtle()
    t.right(75)
    t.forward(100)
    for i in range(4):
        t.right(144)
        t.forward(100)
    turtle.done()


def turtlePolygon():
    t = turtle.Turtle()

    num_sides = 9
    side_length = 70
    angle = 360.0 / num_sides

    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)

    turtle.done()


def turtleHelix():
    for i in range(100):
        turtle.circle(5*i)
        turtle.circle(-5*i)
        turtle.left(i)

    turtle.done()


def turtleRainbowSpiral():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] # list of colors
    t = turtle.Turtle() # creates turtle
    for x in range(360): # repeats the following 360 times
        t.pencolor(colors[x%6]) # rotate choosing colors in the color list
        t.width(x//100 + 1) # slowly increase the width of the turtle line
        t.forward(x) # move forward x units (x increases each loop)
        t.left(61) # turn the turtle 61 degrees counterclockwise

    turtle.done()
