#   Template for 15-110 Homework #7
#
#   Problem #3: 3.frogger.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):Moosuk Kim    moosukk
#
#   15-110 section:N

"""
Your tasks:
0. Run the program, play the game, get a sense of what the code
   is trying to do.  Then study the code to see HOW it is doing it.

1. Answer the following questions (place your answers right here!):
a) What does it mean if grid[row][col] is True?  False?
If grid[row][col] is True, then that means a bad guy is at that location.
If it is False, it means that no bad guy is at that location.
b) When shifting bad guys to the left, the code uses this loop:
            for col in range(19):
   But when shifting right, it uses this less-obvious loop:
            for col in range(19,0,-1):
   What would happen (from the user's perspective) if the code
   used the first loop (range(19)) in both cases?
The game gets alot easier for the user because the yellow circles move left and they start
on the left side. Moves off the screen right after they appear.
c) Briefly but precisely explain what this line of code is doing:
        makeNewPiece = (random.random() < 0.20)
Random.random gives a random float between 0 and 1. If the random number turns
out to be greater than 0.20, then it becomes False, which is nothing. If it is
less than 0, then it becomes True, which means a bad guy has appeared.


2. When the game is over (and the gameOverMessage is being displayed),
   the bad guys keep moving and you can still move the frog. These
   are bugs.  Fix them so that when the game is over, the bad guys
   stop moving and you cannot move the frog.  However, if the user
   presses "r" to reset the game, then movement is restored to normal.
   Done!

3. This version is hardcoded for 10 rows by 20 columns.
   Change the run function so it takes 2 parameters, rows and cols,
   and creates a Frogger game with those dimensions.
   The window should be sized to just fit the board.
   Hint:  you may want to store the dimensions in the canvas.

4. Add a simple notion of "levels":  each time the user wins,
   the next game (after "r" is pressed) should speed up
   (so the timer delay should go down, say by 20%).  Each time
   the user loses, the game should slow down (again, say by 20%).

"""


from Tkinter import *

import random 

def moveFrog(canvas, drow, dcol):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    grid = canvas.data["grid"]
    row0 = canvas.data["frogRow"]
    col0 = canvas.data["frogCol"]
    Level = canvas.data["Level"]
    (row1,col1) = (row0+drow, col0+dcol)
    if ((row1 < 0) or (row1 >= rows) or (col1 < 0) or (col1 >= cols) or
        (grid[row1][col1] == True)):
        canvas.data["gameOverMessage"] = "You crashed!  You lose!"
        Lose = True
        Level -= 1
        canvas.data["Level"] = Level
    else:
        canvas.data["frogRow"] = row1
        canvas.data["frogCol"] = col1
        if (row1 == 0):
            canvas.data["gameOverMessage"] = "You win!"
            Win = True
            canvas.data["Win"] = Win
            Level += 1
            canvas.data["Level"] = Level

def keyPressed(event):
    canvas = event.widget.canvas
    Win = canvas.data["Win"]
    Lose = canvas.data["Lose"]
    if (event.char.lower() == "r"):
        init(canvas)
    if Win == False and Lose == False:
        if (event.keysym == "Left"):
            moveFrog(canvas, 0, -1)
        elif (event.keysym == "Right"):
            moveFrog(canvas, 0, +1)
        elif (event.keysym == "Up"):
            moveFrog(canvas, -1, 0)
        elif (event.keysym == "Down"):
            moveFrog(canvas, +1, 0)
        elif (event.char.lower() == "r"):
            init(canvas)
        redrawAll(canvas)

# Note:  This redrawAll function was intentionally written without helper
# functions, with the original intention that you would as part of this hw
# change this function so that it uses helper functions.  However, we
# dropped that part of the hw.  Still, you should know that this
# function shows poor style, and should use helper functions
# in the way that Sokoban does (check it out!).
def redrawAll(canvas):
    canvas.delete(ALL)
    # paint the grid
    grid = canvas.data["grid"]
    frogRow = canvas.data["frogRow"]
    frogCol = canvas.data["frogCol"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    cellSize = 30
    for row in range(rows):
        for col in range(cols):
            left = cellSize * col
            right = left + cellSize
            top = cellSize * row
            bottom = top + cellSize
            # paint cell background
            if (row == 0):
                color = "darkBlue"
            elif (row == rows-1):
                color = "black"
            elif (row % 2 == 0):
                color = "gray"
            else:
                color = "white"
            canvas.create_rectangle(left, top, right, bottom, fill=color)
            # now paint the object in the cell
            hasBadGuy = grid[row][col]
            hasFrog = ((row == frogRow) and (col == frogCol))
            if (hasBadGuy or hasFrog):
                if (hasFrog):
                    color = "green"
                elif (row % 2 == 0):
                    color = "red"
                else:
                    color = "yellow"
                canvas.create_oval(left, top, right, bottom, fill=color)
    # finally, paint game over message, if any
    msg = canvas.data["gameOverMessage"]
    if (msg != ""):
       canvas.create_text(300, 120, text=msg, font=("Helvetica", 32))
       canvas.create_text(300, 180, text="Game Over!", font=("Helvetica", 32))
 
def moveBadGuys(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    Win = canvas.data["Win"]
    Lose = canvas.data["Lose"]
    Level = canvas.data["Level"]
    if Win == False and Lose == False:
        grid = canvas.data["grid"]
        for row in range(1,rows-1):
            makeNewPiece = (random.random() < 0.20)
            if (row % 2 == 0):
                # shift left
                for col in range(cols-1):
                    grid[row][col] = grid[row][col+1]
                grid[row][cols-1] = makeNewPiece
            else:
                # shift right
                for col in range(cols-1, 0, -1):
                    grid[row][col] = grid[row][col-1]
                grid[row][0] = makeNewPiece
        frogRow = canvas.data["frogRow"]
        frogCol = canvas.data["frogCol"]
        if (grid[frogRow][frogCol] == True):
            canvas.data["gameOverMessage"] = "You were eaten!  You lose!"
            Lose = True
            canvas.data["Lose"] = Lose
            Level -= 1
            canvas.data["Level"] = Level
        redrawAll(canvas)
    
def timerFired(canvas):
     moveBadGuys(canvas)
     Level = canvas.data["Level"]
     delay = int(250 * (0.8) ** (Level)) # milliseconds
     print delay
     canvas.after(delay, timerFired, canvas) # pause, then call timerFired again

def init(canvas):
    # make the grid and store it
    grid = [ ]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    for row in range(rows): grid += [[False] * cols]
    canvas.data["grid"] = grid
    # store the frog's initial position
    canvas.data["frogRow"] = rows - 1
    canvas.data["frogCol"] = cols / 2
    canvas.data["Win"] = False
    canvas.data["Lose"] = False
    canvas.data["gameOverMessage"] = "" # so game is not over!
    # get some bad guys going to start the game
    for move in range(50):
        moveBadGuys(canvas)
    # and display the canvas
    redrawAll(canvas)

########### copy-paste below here ###########

def run(rows, cols):
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=cols*30, height=rows*30)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    canvas.data["Level"] = 0
    init(canvas)
    # set up events
    #root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)


