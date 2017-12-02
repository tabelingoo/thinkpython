import math

def say_hello(name):
    return "Hello " + name

def calc_future_value(rate, year):
    return math.pow(1 + 0.01 * rate, year)


print(say_hello("Ryan"))

print(calc_interest(5, 10))

