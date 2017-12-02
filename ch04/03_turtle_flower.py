import turtle
import math


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle /360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # for i in range(n):
    #     t.fd(step_length)
    #     t.lt(step_angle)

    polyline(t, n, step_length, step_angle)

def flower(t, n, r):
    pass

def flower_test(t):
    r = 300
    arc(t, r, 30)
    t.lt(180-30)
    arc(t, r, 30)
    t.lt(180)
    arc(t, r, 30)
    t.lt(180-30)
    arc(t, r, 30)

if __name__ == '__main__':
    t = turtle.Turtle()
    # arc(t, 100, 270)
    flower_test(t)