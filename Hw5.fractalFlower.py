#   Template for 15-110 Homework #5
#
#   Problem 3: fractalFlower.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:
#

import turtle

#implement your code after this line
def simpleFlower(size):
    turtle.forward(size)
    turtle.backward(size*1.0/3.0)
    turtle.left(180)
    for n in range (8):
        turtle.forward(size*(1.0/3.0))
        turtle.backward(size*(1.0/3.0))
        turtle.left(45)
    turtle.left(180)
    turtle.backward(size*(2.0/3.0))
    
def fractalFlower(size,level):
    if level == 1:
        simpleFlower(size)
    else:
        turtle.forward(size*(2.0/3.0))
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        fractalFlower(size*(1.0/3.0),level-1)
        turtle.left(45)
        turtle.backward(size*(2.0/3.0))

        
    


# DO NOT CHANGE THE CODE BELOW THIS LINE

turtle.delay(0)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)
simpleFlower(200)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
fractalFlower(250, 3)
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()
fractalFlower(300, 4)
turtle.done()
