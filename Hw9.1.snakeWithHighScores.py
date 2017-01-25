#   Template for 15-110 Homework #9
#
#   Problem #1: 1.snakeWithHighScores.py
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk   moosukk and Abhik Bhaval
#
#   15-110 section: N
#

# Your task: implement the functions loadHighScores(canvas),
# saveHighScores(canvas), getCurrentScore(canvas), and
# updateHighScores(canvas) defined below.
# Appropriate calls to these functions and additional support code have
# already been added to gameOver(canvas), redrawAll(canvas), and init().

import random
from Tkinter import *

def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)

def keyPressed(event):
    canvas = event.widget.canvas
    canvas.data["ignoreNextTimerEvent"] = True # for better timing
    # first process keys that work even if the game is over
    if (event.char == "q"):
        gameOver(canvas)
    elif (event.char == "r"):
        init(canvas)
    elif (event.char == "d"):
        canvas.data["inDebugMode"] = not canvas.data["inDebugMode"]
    # now process keys that only work if the game is not over
    if (canvas.data["isGameOver"] == False):
        if (event.keysym == "Up"):
            moveSnake(canvas, -1, 0)
        elif (event.keysym == "Down"):
            moveSnake(canvas, +1, 0)
        elif (event.keysym == "Left"):
            moveSnake(canvas, 0,-1)
        elif (event.keysym == "Right"):
            moveSnake(canvas, 0,+1)
    redrawAll(canvas)

def moveSnake(canvas, drow, dcol):
    # move the snake one step forward in the given direction.
    canvas.data["snakeDrow"] = drow # store direction for next timer event
    canvas.data["snakeDcol"] = dcol
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = canvas.data["headRow"]
    headCol = canvas.data["headCol"]
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    if ((newHeadRow < 0) or (newHeadRow >= rows) or
        (newHeadCol < 0) or (newHeadCol >= cols)):
        # snake ran off the board
        gameOver(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] > 0):
        # snake ran into itself!
        gameOver(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] < 0):
        # eating food!  Yum!
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
        canvas.data["headRow"] = newHeadRow
        canvas.data["headCol"] = newHeadCol
        placeFood(canvas)
        score = canvas.data["score"]
        score += 1
        canvas.data["score"] = score
    else:
        # normal move forward (not eating food)
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
        canvas.data["headRow"] = newHeadRow
        canvas.data["headCol"] = newHeadCol
        removeTail(canvas)

def removeTail(canvas):
    # find every snake cell and subtract 1 from it.  When we're done,
    # the old tail (which was 1) will become 0, so will not be part of the snake.
    # So the snake shrinks by 1 value, the tail.
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1

def gameOver(canvas):
    canvas.data["isGameOver"] = True
    # update and save the high score list
    updateHighScores(canvas)
    saveHighScores(canvas)

def timerFired(canvas):
    ignoreThisTimerEvent = canvas.data["ignoreNextTimerEvent"]
    canvas.data["ignoreNextTimerEvent"] = False
    if ((canvas.data["isGameOver"] == False) and
        (ignoreThisTimerEvent == False)):
        # only process timerFired if game is not over
        drow = canvas.data["snakeDrow"]
        dcol = canvas.data["snakeDcol"]
        moveSnake(canvas, drow, dcol)
        redrawAll(canvas)
    # whether or not game is over, call next timerFired
    # (or we'll never call timerFired again!)
    delay = 150 # milliseconds
    canvas.after(delay, timerFired, canvas) # pause, then call timerFired again

def redrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)
    if (canvas.data["isGameOver"] == True):
        cx = canvas.data["canvasWidth"]/2
        cy = canvas.data["canvasHeight"]*0.2
        canvas.create_text(cx, cy, text="Game Over!", font=("Helvetica", 32, "bold"))
        # display the current score and the high score list
        highScores = canvas.data["highScores"]
        scoreText = "Your score: %d\n" % getCurrentScore(canvas)
        scoreText += "High scores:\n"
        for scoreIndex in range(len(highScores)):
            scoreText += "%d - %d\n" % (scoreIndex+1, highScores[scoreIndex])
        canvas.create_text(cx, cy+20, text=scoreText, font=("Sans 14"), anchor=N)
            
def drawSnakeBoard(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas, snakeBoard, row, col)

def drawSnakeCell(canvas, snakeBoard, row, col):
    margin = canvas.data["margin"]
    cellSize = canvas.data["cellSize"]
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] > 0):
        # draw part of the snake body
        canvas.create_oval(left, top, right, bottom, fill="blue")
    elif (snakeBoard[row][col] < 0):
        # draw food
        canvas.create_oval(left, top, right, bottom, fill="green")
    # for debugging, draw the number in the cell
    if (canvas.data["inDebugMode"] == True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,
                           text=str(snakeBoard[row][col]),font=("Helvatica", 14, "bold"))

def loadSnakeBoard(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    snakeBoard = [ ]
    for row in range(rows): snakeBoard += [[0] * cols]
    snakeBoard[rows/2][cols/2] = 1
    canvas.data["snakeBoard"] = snakeBoard
    findSnakeHead(canvas)
    placeFood(canvas)

def placeFood(canvas):
    # place food (-1) in a random location on the snakeBoard, but
    # keep picking random locations until we find one that is not
    # part of the snake!
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0):
            break
    snakeBoard[row][col] = -1

def findSnakeHead(canvas):
    # find where snakeBoard[row][col] is largest, and
    # store this location in headRow, headCol
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = 0
    headCol = 0
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > snakeBoard[headRow][headCol]):
                headRow = row
                headCol = col
    canvas.data["headRow"] = headRow
    canvas.data["headCol"] = headCol

def printInstructions():
    print "Snake!"
    print "Use the arrow keys to move the snake."
    print "Eat food to grow."
    print "Stay on the board!"
    print "And don't crash into yourself!"
    print "Press 'd' for debug mode."
    print "Press 'r' to restart."

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    canvas.data["inDebugMode"] = False
    canvas.data["isGameOver"] = False
    canvas.data["snakeDrow"] = 0
    canvas.data["snakeDcol"] = -1 # start moving left
    canvas.data["ignoreNextTimerEvent"] = False
    canvas.data["score"] = 0
    # load the high score list
    loadHighScores(canvas)
    redrawAll(canvas)

# Loads a high score list from the file "snakeHighScores.txt".
# The file "snakeHighScores.txt" should exist in the same directory of
# this program. In this file, each score (a single integer) is represented
# on a separate line.
# Stores the high scores as a list of integers in the dictionary
# entry canvas.data["highScores"]
# Parameters:
#   canvas: canvas where the data dictionary is stored
# Returns nothing
def loadHighScores(canvas):
    highScores = [ ]
    scores = [ ]
    fileHandler = open("snakeHighScores.txt", "rt")
    text = fileHandler.readlines()
    for line in text:
        scores.append(line.rstrip("\n"))
    for x in range(len(scores)):
        scores[x] = int(scores[x])
    canvas.data["highScores"] = scores # this is a list of integers
    # Hint: when you read a text file, each line is a string.
    # Make sure you convert the values you read to integers before you store
    # them into the high score list.
    return

# Writes the list of high scores contained in canvas.data["highScores"]
# to the file "snakeHighScores.txt"
# Each score is written on a separate line.
# Parameters:
#   canvas: canvas where the data dictionary is stored
# Returns nothing
def saveHighScores(canvas):
    highScores = canvas.data["highScores"]
    stringOfScores = ""
    for x in highScores:
        stringOfScores += (str(x) + "\n")
    fileHandler = open("snakeHighScores.txt", "wt")
    fileHandler.write(stringOfScores)
    fileHandler.close()
    return

# Calculates and returns the current score of the player.
# The score is the number of food items eaten by the snake
# so far, i.e., the length of the snake minus 1.
# Parameters:
#   canvas: canvas where the data dictionary is stored
# Returns: an integer representing the current score
def getCurrentScore(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    headRow = canvas.data["headRow"]
    headCol = canvas.data["headCol"]
    currentScore = snakeBoard[headRow][headCol] - 1
    return currentScore

# Updates the high score list stored in canvas.data["highScores"]
# by adding the current score.
# Only the five highest scores are retained in the high score list,
# sorted from largest to smallest.
# Parameters:
#   canvas: canvas where the data dictionary is stored
# Returns nothing
def updateHighScores(canvas):
    highScores = canvas.data["highScores"]
    currentScore = getCurrentScore(canvas)
    for line in highScores:
        if line != "\n":
            if currentScore>line:
                i = highScores.index(line)
                highScores.insert(i, currentScore)
                highScores.pop()
                break
    canvas.data["highScores"] = highScores
    saveHighScores(canvas)
    return

########### copy-paste below here ###########

def run(rows, cols):
    # create the root and the canvas
    root = Tk()
    margin = 5
    cellSize = 30
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    canvas.data["margin"] = margin
    canvas.data["cellSize"] = cellSize
    canvas.data["canvasWidth"] = canvasWidth
    canvas.data["canvasHeight"] = canvasHeight
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run(8,16)
