import turtle
import sys, argparse

# def draw(t, length, n):
#     if n == 0:
#         return
#     angle = 50
#     t.fd(length*50)
#     t.lt(angle)
#     draw(t, length, n-1)
#     t.rt(2*angle)
#     draw(t, length, n-1)
#     t.lt(angle)
#     t.bk(length * n)

def draw(t, length, n):
    if n == 0:
        return
    angle = 45
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', dest='length', required=False)
    parser.add_argument('--n', dest='n', required=True)
    args = parser.parse_args()

    length = 100
    if args.length:
        length = int(args.length)

    n = int(args.n)
    t = turtle.Turtle()
    draw(t, length, n)

