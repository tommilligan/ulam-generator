#!/usr/bin/env python

from functools import reduce
import itertools
import math

from PIL import Image, ImageDraw

LENGTH = 600
HEIGHT = LENGTH
WIDTH = LENGTH

GRID = 4
DOT_RADIUS = 2

COLOR_BACKGROUND = (245, 245, 245)
COLOR_DOTS = (55, 176, 232)

def centralise(coord):
    x, y = coord
    return (x + (WIDTH / 2), y + (HEIGHT / 2))

def factor_generator(n):
    max = math.ceil(pow(n, 0.5))
    for i in range(1, max):
        if n % i == 0:
            yield [i, n//i]

def factors(n):
    return set(itertools.chain.from_iterable(factor_generator(n)))

def position(n):
    """
    For inter n returns (x, y) position
    """
    k = math.ceil((math.sqrt(n) - 1) / 2)
    t = (2 * k) + 1
    m = pow(t, 2)

    t = t - 1

    if n >= (m - t):
        return [k - (m - n), -k]

    m = m - t

    if n >= (m - t):
        return [-k, -k + (m - n)]

    m = m - t

    if n >= (m - t):
        return [-k + (m - n), k]

    return [k, k - (m - n - t)]


im = Image.new("RGB", (WIDTH, HEIGHT), color=COLOR_BACKGROUND)
draw = ImageDraw.Draw(im)
for i in range(1, 30000):
    number_factors = len(factors(i))
    #print("{}: {}: {}".format(i, number_factors, factors(i)))
    r = DOT_RADIUS
    point = centralise([c * GRID for c in position(i)])
    box = (tuple(c - r for c in point), tuple(c + r for c in point))

    if number_factors <= 2:
        fill = COLOR_DOTS
    else:
        fill = COLOR_BACKGROUND
    draw.ellipse(box, fill=fill)
    
im.save("out.png")
