#
#   Template for 15-110 Homework #3
#
#   Problem #4a: beninFlag
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk Kim, moosukk
#
#   15-110 section:N


# In the file 4a.beninFlag.py, include the helper function drawFlagOfBenin(canvas, left, top, right, bottom)
# along with the code required to display the flag in the 4 quadrants of a canvas, as described above.

from Tkinter import *
root = Tk()
canvas = Canvas(root, width=820, height=620)
canvas.pack()
canvas.create_rectangle(  0,   0, 820, 620, fill="black")
canvas.create_rectangle(  5,  5, 200, 300, fill="green")
canvas.create_rectangle( 200, 5, 405, 150, fill="yellow")
canvas.create_rectangle( 200, 150, 405, 300, fill="red")
canvas.create_rectangle( 415, 5, 620, 300, fill="green")
canvas.create_rectangle( 615, 5, 810, 150, fill="yellow")
canvas.create_rectangle( 615, 150, 810, 300, fill="red")
canvas.create_rectangle(  5,  315, 200, 615, fill="green")
canvas.create_rectangle( 200, 315, 405, 465, fill="yellow")
canvas.create_rectangle( 200, 465, 405, 615, fill="red")
canvas.create_rectangle( 415, 315, 615, 615, fill="green")
canvas.create_rectangle( 615, 315, 810, 465, fill="yellow")
canvas.create_rectangle( 615, 465, 810, 615, fill="red")
root.mainloop()
