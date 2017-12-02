import turtle
import math



def koch(t, length):
    if length < 3:
        return 
    t.fd(length//3)
    t.lt(60)
    t.fd(length//3)
    koch(t, length)
    t.lt(240)
    t.fd(length)
    koch(t, length)
    t.lt(60)
    t.fd(length)
    koch(t, length)
        

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)
    
def main():
    t = turtle.Turtle()
    t.penup()
    t.goto(-400,0)
    t.pendown()
    koch(t, 1000)

if __name__ =='__main__':
    main()