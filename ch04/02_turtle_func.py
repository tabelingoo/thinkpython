import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / 50
    polygon(t, n, length)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle /360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)



if __name__ == '__main__':
    t = turtle.Turtle()
    # square(t, 200)
    polygon(t, 7, 30)
    # circle(t, 100)
    # arc(t, 100, 120)
    # arc(t, 100, 120)