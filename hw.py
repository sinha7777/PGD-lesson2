import pgzrun
import random

WIDTH = 300
HEIGHT = 300
TITLE = "Circles"

def draw():
    screen.fill("black")

    radius = 100 

    r = 0
    g = random.randint(0, 255)
    b = 255

    for i in range(20):
        screen.draw.circle((150, 150), radius, (r, g, b))

        radius -= 4
        b -= random.randint(1, 13)
        r += random.randint(1, 13)

pgzrun.go()