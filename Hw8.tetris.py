#   Template for 15-110 Homework #8
#
#   Problem #1: tetris.py
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk Kim   moosukk
#
#   15-110 section:N

from Tkinter import *

import random

    
def newFallingPiece(canvas):
    tetrisPieces = canvas.data["tetrisPieces"]
    tetrisPieceColors = canvas.data["tetrisPieceColors"]
    cols = canvas.data["cols"]
    fallingPiece = [ ]
    fallingPieceColor = ""
    randomInt = random.randint(0,5)
    fallingPiece = tetrisPieces[randomInt]
    fallingPieceColor = tetrisPieceColors[randomInt]
    fallingPieceRow = 0
    pieceCols = len(fallingPiece[0])
    fallingPieceCol = cols/2 - pieceCols/2
    canvas.data["fallingPieceColor"] = fallingPieceColor
    canvas.data["fallingPiece"] = fallingPiece
    canvas.data["fallingPieceRow"] = fallingPieceRow
    canvas.data["fallingPieceCol"] = fallingPieceCol
    drawFallingPiece(canvas)
    
    
def drawFallingPiece(canvas):
    fallingPiece = canvas.data["fallingPiece"]
    fallingPieceColor = canvas.data["fallingPieceColor"]
    fallingPieceRow = canvas.data["fallingPieceRow"]
    fallingPieceCol = canvas.data["fallingPieceCol"]
    board = canvas.data["board"]
    pieceRows = len(fallingPiece)
    pieceCols = len(fallingPiece[0])
    canvas.data["pieceRows"] = pieceRows
    canvas.data["pieceCols"] = pieceCols
    for y in range(pieceRows):
        for x in range(pieceCols):
            if fallingPiece[y][x] == True:
                row = y + fallingPieceRow
                col = x + fallingPieceCol
                board[row][col] = fallingPieceColor
                drawCell(canvas, row, col, board)
  


def drawBoard(canvas):
    board = canvas.data["board"]
    emptyColor = canvas.data["emptyColor"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, row, col, board)

    

def drawCell(canvas, row, col, board):
    CellSize = 26
    #Drawing the black outer box:
    leftSpace = 19
    topSpace = 29
    left = (CellSize * col)+leftSpace
    right = left + CellSize +1
    top = (CellSize * row)+topSpace
    bottom = top + CellSize +1
    canvas.create_rectangle(left, top, right, bottom, fill="black")
    #Drawing the colored inner box:
    leftSpace += 1
    topSpace += 1
    left = (CellSize * col) + leftSpace
    right = left + CellSize -2
    top = (CellSize * row) + topSpace
    bottom = top + CellSize -2
    canvas.create_rectangle(left, top, right, bottom, fill=board[row][col])    

def redrawAll(canvas):
    canvas.delete(ALL)
    drawBoard(canvas)

def fallingPieceIsLegal(canvas, fallingPieceRow, fallingPieceCol):
    fallingPiece = canvas.data["fallingPiece"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    pieceRows = canvas.data["pieceRows"]
    pieceCols = canvas.data["pieceCols"]
    emptyColor = canvas.data["emptyColor"]
    board = canvas.data["board"]
    isLegal = True
    isFallen = False
    #test for piece at left, right, bottom edge of board and/or touching another piece:
    if  fallingPieceRow + pieceRows > rows:
        isFallen = True
        isLegal = False
        canvas.data["isFallen"] = isFallen
        return False
    elif fallingPieceCol < 0:
        isLegal = False
        return False
    elif fallingPieceCol + pieceCols > cols:
        isLegal = False
        return False
    if isLegal != False:
        for x in range(pieceCols):
            for y in range(pieceRows):
                if fallingPiece[y][x] == True and board[fallingPieceRow + y][fallingPieceCol + x] != emptyColor:
                    isFallen = True
                    isLegal = False
                canvas.data["isFallen"] = isFallen
    if isLegal == False: return False
    
def deletePiece(canvas):
    fallingPiece = canvas.data["fallingPiece"]
    pieceRows = canvas.data["pieceRows"]
    pieceCols = canvas.data["pieceCols"]
    fallingPieceRow = canvas.data["fallingPieceRow"]
    fallingPieceCol = canvas.data["fallingPieceCol"]
    emptyColor = canvas.data["emptyColor"]
    board = canvas.data["board"]
    for y in range(pieceRows):
        for x in range(pieceCols):
            if fallingPiece[y][x] == True:
                row = y + (fallingPieceRow)
                col = x + (fallingPieceCol)
                board[row][col] = emptyColor
                drawCell(canvas, row, col, board)


def placeFallingPiece(canvas):
    fallingPiece = canvas.data["fallingPiece"]
    fallingPieceColor = canvas.data["fallingPieceColor"]
    fallingPieceRow = canvas.data["fallingPieceRow"]
    fallingPieceCol = canvas.data["fallingPieceCol"]
    board = canvas.data["board"]
    pieceRows = canvas.data["pieceRows"]
    pieceCols = canvas.data["pieceCols"]
    for y in range(pieceRows):
        for x in range(pieceCols):
            if fallingPiece[y][x] == True:
                row = y + fallingPieceRow
                col = x + fallingPieceCol
                board[row][col] = fallingPieceColor
                drawCell(canvas, row, col, board)
                canvas.data["board"] = board
    
    
def timerFired(canvas):
    delay = 250
    moveFallingPiece(canvas, +1, 0)
    isFallen = canvas.data["isFallen"]
    if isFallen == True:
        placeFallingPiece(canvas)
        newFallingPiece(canvas)
    canvas.after(delay, timerFired, canvas)
    

def moveFallingPiece(canvas, drow, dcol):
    board = canvas.data["board"]
    fallingPieceRow = canvas.data["fallingPieceRow"]
    fallingPieceCol = canvas.data["fallingPieceCol"]
    pieceRows = canvas.data["pieceRows"]
    pieceCols = canvas.data["pieceCols"]
    fallingPiece = canvas.data["fallingPiece"]
    emptyColor = canvas.data["emptyColor"]
    #starting row & col
    row0 = fallingPieceRow
    col0 = fallingPieceCol
    #proposed new row & col
    fallingPieceRow += drow
    fallingPieceCol += dcol
    #Deleting piece in old position
    deletePiece(canvas)
    if fallingPieceIsLegal(canvas, fallingPieceRow, fallingPieceCol) != False: #Accepting proposed row & col
        #Drawing piece in new position
        canvas.data["fallingPieceRow"] = fallingPieceRow
        canvas.data["fallingPieceCol"] = fallingPieceCol
        drawFallingPiece(canvas)
        return True
    else: return False
        
        
def fallingPieceCenter(canvas, pieceRows, pieceCols):
    fallingPieceRow = canvas.data["fallingPieceRow"]
    fallingPieceCol = canvas.data["fallingPieceCol"]
    fallingPiece = canvas.data["fallingPiece"]
    if fallingPiece == [[ True, True],[ True, True]]: #if it is a o piece, oldPieceCenter is the same as newPieceCenter
        oldCenterRow = fallingPieceRow + pieceRows/2
        oldCenterCol = fallingPieceCol + pieceCols/2
        oldPieceCenter = (oldCenterRow, oldCenterCol)
        newCenterRow = oldCenterRow
        newCenterCol = oldCenterCol
        newPieceCenter = (newCenterRow, newCenterCol)
        canvas.data["oldPieceCenter"] = oldPieceCenter
        canvas.data["newPieceCenter"] = newPieceCenter
    elif pieceRows == canvas.data["pieceRows"] and pieceCols == canvas.data["pieceCols"]:
        oldCenterRow = fallingPieceRow + pieceRows/2
        oldCenterCol = fallingPieceCol + pieceCols/2
        oldPieceCenter = (oldCenterRow, oldCenterCol)
        canvas.data["oldPieceCenter"] = oldPieceCenter
    else:
        newCenterRow = fallingPieceRow + pieceRows/2
        newCenterCol = fallingPieceCol + pieceCols/2
        newPieceCenter = (newCenterRow, newCenterCol)
        canvas.data["newPieceCenter"] = newPieceCenter


def rotateFallingPiece(canvas):
    pieceRows = canvas.data["pieceRows"]
    pieceCols = canvas.data["pieceCols"]
    fallingPieceRow = canvas.data["fallingPieceRow"]
    fallingPieceCol = canvas.data["fallingPieceCol"]
    fallingPiece = canvas.data["fallingPiece"]
    fallingPieceCenter(canvas, pieceRows, pieceCols)
    oldPieceCenter = canvas.data["oldPieceCenter"]
    deletePiece(canvas)
    oldCenterRow = oldPieceCenter[0]
    oldCenterCol = oldPieceCenter[1]
    rotatedPiece = [ ]
    for col in range(pieceCols): rotatedPiece += [[False] * pieceRows]
    for row in range(pieceRows):
        for col in range(pieceCols):
            rotatedPiece[col][row] = fallingPiece[row][(pieceCols-1) - col]
    #swapping the values of pieceCols and pieceRows
    pieceCols = pieceCols + pieceRows
    pieceRows = pieceCols - pieceRows
    pieceCols = pieceCols - pieceRows
    fallingPieceCenter(canvas, pieceRows, pieceCols)
    newPieceCenter = canvas.data["newPieceCenter"]
    newCenterRow = newPieceCenter[0]
    newCenterCol = newPieceCenter[1]
    fallingPieceRow += (oldCenterRow - newCenterRow)
    fallingPieceCol += (oldCenterCol - newCenterCol)
    canvas.data["pieceCols"] = pieceCols
    canvas.data["pieceRows"] = pieceRows
    if fallingPieceIsLegal(canvas, fallingPieceRow, fallingPieceCol) == True:
        canvas.data["fallingPiece"] = rotatedPiece
        canvas.data["fallingPieceRow"] = fallingPieceRow
        canvas.data["fallingPieceCol"] = fallingPieceCol
        drawFallingPiece(canvas)
    else: #swapping back the values of pieceCol and pieceRows to their pre-rotated values
        pieceCols = pieceCols + pieceRows
        pieceRows = pieceCols - pieceRows
        pieceCols = pieceCols - pieceRows
        canvas.data["pieceCols"] = pieceCols
        canvas.data["pieceRows"] = pieceRows
        drawFallingPiece(canvas)
        
    

def init(canvas):
    board = [ ]
    emptyColor = "blue"
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    canvas.data["emptyColor"] = emptyColor
    #Making 2-D list for board
    for row in range(rows): board += [[emptyColor] * cols]
    canvas.data["board"] = board
    #Defining tetris pieces:
    iPiece = [[ True,  True,  True,  True]]
    jPiece = [[ True, False, False ],[ True, True,  True]]
    lPiece = [[ False, False, True],[ True,  True,  True]]
    oPiece = [[ True, True],[ True, True]]
    sPiece = [[ False, True, True ],[True, True, False]]
    tPiece = [[ False, True, False ],[ True,  True, True]]
    zPiece = [[ True,  True, False ],[ False, True, True]]
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange"]
    canvas.data["tetrisPieces"] = tetrisPieces
    canvas.data["tetrisPieceColors"] = tetrisPieceColors
    newFallingPiece(canvas) #initial falling piece
    redrawAll(canvas)

def keyPressed(event):
    canvas = event.widget.canvas
    if (event.keysym == "Left"):
        moveFallingPiece(canvas, 0, -1)
    elif (event.keysym == "Right"):
        moveFallingPiece(canvas, 0, +1)
    elif (event.keysym == "Down"):
        moveFallingPiece(canvas, +1, 0)
    elif (event.keysym == "Up"):
        rotateFallingPiece(canvas)
    elif (event.char.lower() == "r"):
        init(canvas)
    redrawAll(canvas)


def run(rows, cols):
    root = Tk()
    canvas = Canvas(root, width=cols*30, height=rows*30)
    canvas.pack()
    root.resizable(width=0, height=0)
    root.canvas = canvas.canvas = canvas
    canvas.data = { }
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    init(canvas)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    root.mainloop()
