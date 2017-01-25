#   Template for 15-110 Homework #5
#
#   Problem 5: fractalSun.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):Moosuk Kim    moosukk
#
#   15-110 section:N
#


from Tkinter import *
import math

#implement your code after this line

def fractalSun(canvas,xc,yc,r,level):
    blue = 0
    red = 255
    green = (255/(level+1)*level)
    color = "#%02x%02x%02x" % (red, green,  blue)
    if level == 0:
        canvas.create_oval(xc-r,yc-r,xc+r,yc+r, fill = color, width = 0)
        for n in range(0,8):
            canvas.create_line(xc, yc, xc+(2*r*math.cos(n*math.pi/4)), yc+(2*r*math.sin(n*math.pi/4)), fill = color, width = 0)
    else:
        for n in range (0,8):
            canvas.create_line(xc, yc, xc+(2*r*math.cos(n*math.pi/4)), yc+(2*r*math.sin(n*math.pi/4)), fill = color, width = 0)
            canvas.create_oval(xc-r,yc-r,xc+r,yc+r, fill = color, width = 0)
        for n in range (0,8):
            fractalSun(canvas,xc+(2*r*math.cos(n*math.pi/4)), yc+(2*r*math.sin(n*math.pi/4)),r*0.25, level-1)








# DO NOT CHANGE THE CODE BELOW THIS LINE
    
root = Tk()
myCanvas = Canvas(root, width=600, height=600, background="black")
myCanvas.pack()
fractalSun(myCanvas, 300, 300, 100, 5)
root.mainloop()
