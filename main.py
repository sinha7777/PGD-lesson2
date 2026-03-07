import pgzrun
import random

WIDTH=300
HEIGHT=300
TITLE="Rectangles"

#draw() - inbuilt function gets called itself.helps to render animations/shapes/texts
def draw():
    screen.fill("black")
    width=WIDTH
    height=HEIGHT-200

    r = 255
    g = 0
    b = random.randint(120,255)
    
    for i in range(20):
        myRect= Rect((0,0),(width,height))
        myRect.center=150,150
        screen.draw.rect(myRect,(r,g,b))
        width = width-10
        height = height+10
        r = r-5
        g = g+13

pgzrun.go()