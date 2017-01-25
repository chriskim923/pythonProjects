#   Template for 15-110 Homework #5
#
#   Problem 4: fractalMickeyMouse.py
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk Kim
#
#   15-110 section: N
#

from Tkinter import *
import math

#implement your code after this line

def mickeyFace(canvas, xc, yc, r):
    canvas.create_oval((xc-r),(yc+r),(xc+r),(yc-r), fill="white")
    canvas.create_arc((xc-(0.7*r)),(yc+(0.2*r)),(xc+(0.7*r)),(yc+(0.7*r)), extent=-180, style=ARC)
    canvas.create_oval((xc-(0.4*r)),(yc-(0.5*r)),(xc-(0.2*r)),yc, fill="black")
    canvas.create_oval((xc+(0.4*r)),(yc-(0.5*r)),(xc+(0.2*r)),yc, fill="black")
    canvas.create_oval((xc-(0.2*r)),(yc-(0.1*r)),(xc+(0.2*r)),(yc+(0.1*r)), fill="black")

def fractalMickeyMouse(canvas,xc,yc,r,level):
    if level ==0:
        mickeyFace(canvas,xc,yc,r)
    else:
        mickeyFace(canvas,xc,yc, r)
        fractalMickeyMouse(canvas, xc-r, yc-r*1.12, r/2.0, level-1)
        fractalMickeyMouse(canvas, xc+r, yc-r*1.12, r/2.0, level-1)
        




# DO NOT CHANGE THE CODE BELOW THIS LINE
root = Tk()
myCanvas = Canvas(root, width=800, height=600, background="darkgreen")
myCanvas.pack()
#fractalMickeyMouse(myCanvas, 400, 400, 150, 6)
#to test just the mickeyFace() function, replace the line above with
#mickeyFace(myCanvas, 400, 400, 150)
fractalMickeyMouse(myCanvas, 400,400,150,10)
root.mainloop()
