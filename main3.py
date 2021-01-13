from math import sqrt
from random import randrange

def f(x, y):
    return 6 * (x ** 6) + 2 * (x ** 4) * (y ** 2) + 10 * (x ** 2) + 6 * x * y + 10 * (y ** 2) - 6 * x + 4

def dervX(x, y):
    delta = 0.000001
    f1 = f(x, y)
    f2 = f(x + delta, y)
    return (f2 - f1) / delta

def dervY(x, y):
    delta = 0.000001
    f1 = f(x, y)
    f2 = f(x, y + delta)
    return (f2 - f1) / delta

def grad(x, y):
    dx = dervX(x, y)
    dy = dervY(x, y)
    ln = sqrt(dx ** 2 + dy ** 2)
    return (-(dx / ln), -(dy / ln))

def go(x, y):
    g = grad(x, y)
    step = 0.001
    mn = (f(x, y), (x, y))
    '''
    for i in range(200000):
        mn = min(mn, (f(x + g[0] * step * i, y + g[1] * step * i), (x + g[0] * step * i, y + g[1] * step * i)))
    '''
    return (x + g[0] * step, y + g[1] * step)
    #return mn[1]


global_mn = (99999999999999999, (999, 999))
while (1):
    x = randrange(-100, 100)
    y = randrange(-100, 100)
    for i in range(200000):
        x, y = go(x, y)
        global_mn = min(global_mn, (f(x, y), (x, y)))
    print(global_mn)
