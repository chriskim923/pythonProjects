#make board alternate colors
#after move, unhighlight stuff <= Completed!
#indicate king piece with K
import random
from Tkinter import *
from time import sleep

def timedHighlightsAndMove(canvas):
    #Does the pauses, highlights the piece computer will move, and where
    checkerBoard = canvas.data["checkerBoard"]
    rowClicked = canvas.data["rowClicked"]
    colClicked = canvas.data["colClicked"]
    rowClickedBefore = canvas.data["rowClickedBefore"]
    colClickedBefore = canvas.data["colClickedBefore"]
    canvas.data["rowClicked"] = rowClickedBefore
    canvas.data["colClicked"] = colClickedBefore
    drawCheckerCell(canvas, checkerBoard, rowClickedBefore, colClickedBefore)
    canvas.update()
    sleep(1)
    checkerBoard[rowClicked][colClicked] = 3
    drawCheckerCell(canvas, checkerBoard, rowClicked, colClicked)
    canvas.update()
    sleep(1)
    canvas.data["rowClicked"] = rowClicked
    canvas.data["colClicked"] = colClicked
    moveCheckerPiece(canvas, rowClickedBefore, colClickedBefore, rowClicked, colClicked)

def canProtect(canvas):
    if isThreatened(canvas) == True:
        checkerBoard = canvas.data["checkerBoard"]
        rowList = canvas.data["rowList"]
        colList = canvas.data["colList"]
        rows = len(checkerBoard)
        cols = len(checkerBoard[0])
        found = False
        #Going through all the pieces to check if their possible move spots corresponds with
        #the spot they need to get to in order to protect
        for row in range(rows):
            for col in range(cols):
                if checkerBoard[row][col] > 0:
                    findPossibleRedMoves(canvas, row, col)
                    if len(rowList) > 0:
                        for x in range(len(rowList)):
                            if checkerBoard[rowList[x]][colList[x]] == 3:
                                canvas.data["rowClicked"] = rowList[x]
                                canvas.data["colClicked"] = colList[x]
                                canvas.data["rowClickedBefore"] = row
                                canvas.data["colClickedBefore"] = col
                                canvas.data["checkerBoard"] = checkerBoard
                                found = True
                    clearHighlight(canvas)
        if found == True: return True
        else: return False
    else: return False

def isThreatened(canvas):
    checkerBoard = canvas.data["checkerBoard"]
    rows = len(checkerBoard)
    cols = len(checkerBoard[0])
    up = -2
    down = +2
    right = +2
    left = -2
    rowList = [ ] #collects row&col to which a red piece must go
    colList = [ ]
#Now searching for spots where a blue piece would land if it were to jump a red piece
    for rowClicked in range(rows):
        for colClicked in range(cols):
            if checkerBoard[rowClicked][colClicked] < 0:
                findPossibleBlueMoves(canvas, rowClicked, colClicked)
                if rowClicked + up >= 0:
                    if colClicked + left >= 0:
                        if checkerBoard[rowClicked+up][colClicked+left] == 3:
                            rowList.append(rowClicked+up)
                            colList.append(colClicked+left)
                    if colClicked + right <= cols-1:
                        if checkerBoard[rowClicked+up][colClicked+right] == 3:
                            rowList.append(rowClicked+up)
                            colList.append(colClicked+right)
                if rowClicked + down <= rows-1:
                    if colClicked + left >= 0:
                        if checkerBoard[rowClicked+down][colClicked+left] == 3:
                            rowList.append(rowClicked+down)
                            colList.append(colClicked+left)
                    if colClicked + right <= cols-1:
                        if checkerBoard[rowClicked+down][colClicked+right] == 3:
                            rowList.append(rowClicked+down)
                            colList.append(colClicked+right)
                clearHighlight(canvas)
    if len(rowList) > 0:
        canvas.data["rowList"] = rowList
        canvas.data["colList"] = colList
        return True
    else: return False


def canEat(canvas):
    checkerBoard = canvas.data["checkerBoard"]
    rows = len(checkerBoard)
    cols = len(checkerBoard[0])
    up = -2
    down = +2
    right = +2
    left = -2
    found = False
    for rowClickedBefore in range(rows):
        for colClickedBefore in range(cols):
            if checkerBoard[rowClickedBefore][colClickedBefore] > 0:
                findPossibleRedMoves(canvas, rowClickedBefore, colClickedBefore)
                removeAdjacentMoves(canvas, rowClickedBefore, colClickedBefore)
                #After removing all adjacent moves, all that remains are jump / take-piece moves
                for rowClicked in range(rows):
                    for colClicked in range(cols):
                        if checkerBoard[rowClicked][colClicked] == 3:
                            found = True
                            canvas.data["rowClickedBefore"] = rowClickedBefore
                            canvas.data["colClickedBefore"] = colClickedBefore
                            canvas.data["rowClicked"] = rowClicked
                            canvas.data["colClicked"] = colClicked
                            canvas.data["checkerBoard"] = checkerBoard
                clearHighlight(canvas)
    if found == True: return True
    else: return False

def canGoToSide(canvas):
    checkerBoard = canvas.data["checkerBoard"]
    rows = len(checkerBoard)
    cols = len(checkerBoard[0])
    tempList = [0,cols-1] #the col representing left side and right side
    found = False
    for rowClickedBefore in range(rows):
        for colClickedBefore in range(cols):
            if checkerBoard[rowClickedBefore][colClickedBefore] > 0:
                findPossibleRedMoves(canvas, rowClickedBefore, colClickedBefore)
                for rowClicked in range(rows):
                    for colClicked in tempList:
                        if checkerBoard[rowClicked][colClicked] == 3:
                            found = True
                            canvas.data["rowClickedBefore"] = rowClickedBefore
                            canvas.data["colClickedBefore"] = colClickedBefore
                            canvas.data["rowClicked"] = rowClicked
                            canvas.data["colClicked"] = colClicked
                            canvas.data["checkerBoard"] = checkerBoard
                clearHighlight(canvas)
    if found == True: return True
    else: return False

def mediumMode(canvas):
    if canEat(canvas) == True:
        print "I can eat you!"
        timedHighlightsAndMove(canvas)
    else:
        print "Doing a random move!"
        doRandomMove(canvas)
    mustTake = canvas.data["mustTake"]
    rowClicked = canvas.data["rowClicked"]
    colClicked = canvas.data["colClicked"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    checkerBoard = canvas.data["checkerBoard"]
    while mustTake == True:
        redrawAll(canvas)
        canvas.update()
        sleep(1)
        while True:
            row = random.randint(0,rows-1)
            col = random.randint(0,cols-1)
            if (checkerBoard[row][col] == 3):
                break
        rowClickedBefore = rowClicked
        colClickedBefore = colClicked
        rowClicked = row
        colClicked = col
        canvas.data["rowClicked"] = rowClicked
        canvas.data["colClicked"] = colClicked
        moveCheckerPiece(canvas, rowClickedBefore, colClickedBefore, rowClicked, colClicked)
        mustTake = canvas.data["mustTake"]

def hardMode(canvas):
    if canEat(canvas) == True:
        print "I can eat you!"
        timedHighlightsAndMove(canvas)
    elif canProtect(canvas) == True:
        print "I'll save you!"
        timedHighlightsAndMove(canvas)
    elif canGoToSide(canvas) == True:
        print "Can't hurt me here!"
        timedHighlightsAndMove(canvas)
    else:
        print "Doing a random move!"
        doRandomMove(canvas)
    mustTake = canvas.data["mustTake"]
    rowClicked = canvas.data["rowClicked"]
    colClicked = canvas.data["colClicked"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    checkerBoard = canvas.data["checkerBoard"]
    while mustTake == True:
        redrawAll(canvas)
        canvas.update()
        sleep(1)
        while True:
            row = random.randint(0,rows-1)
            col = random.randint(0,cols-1)
            if (checkerBoard[row][col] == 3):
                break
        rowClickedBefore = rowClicked
        colClickedBefore = colClicked
        rowClicked = row
        colClicked = col
        canvas.data["rowClicked"] = rowClicked
        canvas.data["colClicked"] = colClicked
        moveCheckerPiece(canvas, rowClickedBefore, colClickedBefore, rowClicked, colClicked)
        mustTake = canvas.data["mustTake"]


def doRandomMove(canvas):
    checkerBoard = canvas.data["checkerBoard"]
    mustTake = canvas.data["mustTake"]
    rows = len(checkerBoard)
    cols = len(checkerBoard[0])
    rowList = [ ]
    colList = [ ]
    for rowClicked in range(rows):
        for colClicked in range(cols):
            if checkerBoard[rowClicked][colClicked] > 0:
                    findPossibleRedMoves(canvas, rowClicked, colClicked)
                    for x in range(-2, 3):
                        if rowClicked + x >= 0 and rowClicked + x <= rows-1:
                            if checkerBoard[rowClicked+x].count(3) > 0:
                                rowList.append(rowClicked)
                                colList.append(colClicked)
                    clearHighlight(canvas)
    if len(rowList) > 0:
        if len(rowList)-1 > 0:
            piece = random.randint(0,len(rowList)-1)
        if len(rowList) == 1: piece = 0
        rowClicked = rowList[piece]
        colClicked = colList[piece]
        canvas.data["rowClicked"] = rowClicked
        canvas.data["colClicked"] = colClicked
        drawCheckerCell(canvas, checkerBoard, rowClicked, colClicked)
        canvas.update()
        sleep(1)
        findPossibleRedMoves(canvas, rowClicked, colClicked)
        while True:
            row = random.randint(0,rows-1)
            col = random.randint(0,cols-1)
            if (checkerBoard[row][col]) == 3:
                break
        rowClickedBefore = rowClicked
        colClickedBefore = colClicked
        rowClicked = row
        colClicked = col
        canvas.data["rowClicked"] = rowClicked
        canvas.data["colClicked"] = colClicked
        drawCheckerCell(canvas, checkerBoard, rowClicked, colClicked)
        canvas.update()
        sleep(1)
        moveCheckerPiece(canvas, rowClickedBefore, colClickedBefore, rowClicked, colClicked)
        mustTake = canvas.data["mustTake"]
        while mustTake == True:
            redrawAll(canvas)
            canvas.update()
            sleep(1)
            while True:
                row = random.randint(0,rows-1)
                col = random.randint(0,cols-1)
                if (checkerBoard[row][col] == 3):
                    break
            rowClickedBefore = rowClicked
            colClickedBefore = colClicked
            rowClicked = row
            colClicked = col
            canvas.data["rowClicked"] = rowClicked
            canvas.data["colClicked"] = colClicked
            moveCheckerPiece(canvas, rowClickedBefore, colClickedBefore, rowClicked, colClicked)
            mustTake = canvas.data["mustTake"]
    else:
        print "Congrats, you won"
        canvas.data["isGameOver"] = True
        redrawAll(canvas)


def removeAdjacentMoves(canvas, rowClicked, colClicked):
    checkerBoard = canvas.data["checkerBoard"]
    rows = canvas.data["rows"]
    up = -1
    down = +1
    if rowClicked+up >= 0:
        for x in range(checkerBoard[rowClicked+up].count(3)):
            index = checkerBoard[rowClicked+up].index(3)
            checkerBoard[rowClicked+up].remove(3)
            checkerBoard[rowClicked+up].insert(index,0)
    if rowClicked+down <= rows-1:
        for x in range(checkerBoard[rowClicked+down].count(3)):
            index = checkerBoard[rowClicked+down].index(3)
            checkerBoard[rowClicked+down].remove(3)
            checkerBoard[rowClicked+down].insert(index,0)
    canvas.data["checkerBoard"] = checkerBoard

def checkGameOver(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    checkerBoard = canvas.data["checkerBoard"]
    blueTurn = canvas.data["blueTurn"]
    redPieces = 0
    bluePieces = 0
    noRedMoves = True
    noBlueMoves = True
    for rowClicked in range(rows):
        for colClicked in range(cols):
            if blueTurn == True:
                if checkerBoard[rowClicked][colClicked] < 0:
                    findPossibleBlueMoves(canvas, rowClicked, colClicked)
                    for x in range(-2, 3):
                        if rowClicked + x >= 0 and rowClicked + x <= rows-1:
                            if checkerBoard[rowClicked+x].count(3) > 0:
                                noBlueMoves = False
                    clearHighlight(canvas)
            else:
                if checkerBoard[rowClicked][colClicked] > 0:
                    findPossibleRedMoves(canvas, rowClicked, colClicked)
                    for x in range(-2, 3):
                        if rowClicked + x >= 0 and rowClicked + x <= rows-1:
                            if checkerBoard[rowClicked+x].count(3) > 0:
                                noRedMoves = False
                    clearHighlight(canvas)
    if blueTurn == True and noBlueMoves == True:
        print "No Moves!!! Red Wins!!!"
        canvas.data["isGameOver"] = True
    if blueTurn == False and noRedMoves == True:
        print "No Moves!!! Blue Wins!!!"
        canvas.data["isGameOver"] = True



def endTurn(canvas):
    print "Turn Ended!!!"
    checkerBoard = canvas.data["checkerBoard"]
    canvas.data["rowClicked"] = None
    canvas.data["colClicked"] = None
    mode = canvas.data["mode"]
    blueTurn = canvas.data["blueTurn"]
    clearHighlight(canvas)
    if blueTurn == True:
        canvas.data["blueTurn"] = False
    else: canvas.data["blueTurn"] = True
    checkGameOver(canvas)
    redrawAll(canvas)
    canvas.data["mustTake"] = False
    isGameOver = canvas.data["isGameOver"]
    blueTurn = canvas.data["blueTurn"]
    if isGameOver == False:
        if mode == "easyComp" and blueTurn == False:
            print "Easy Computer's Turn!!!"
            redrawAll(canvas)
            doRandomMove(canvas)
        elif mode == "mediumComp" and blueTurn == False:
            redrawAll(canvas)
            mediumMode(canvas)
        elif mode == "hardComp" and blueTurn == False:
            print "Hard Computer's Turn!!!"
            redrawAll(canvas)
            hardMode(canvas)


def makeKingPiece(canvas, rowClicked, colClicked):
    blueTurn = canvas.data["blueTurn"]
    checkerBoard = canvas.data["checkerBoard"]
    if blueTurn == True:
        checkerBoard[rowClicked][colClicked] = -2
    else:
        checkerBoard[rowClicked][colClicked] = 2
    canvas.data["checkerBoard"]


def moveCheckerPiece(canvas, rowClickedBefore, colClickedBefore, rowClicked, colClicked):
    blueTurn = canvas.data["blueTurn"]
    checkerBoard = canvas.data["checkerBoard"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    checkerBoard[rowClicked][colClicked] = checkerBoard[rowClickedBefore][colClickedBefore]
    checkerBoard[rowClickedBefore][colClickedBefore] = 0
    canvas.data["checkerBoard"] = checkerBoard
    if checkerBoard[rowClicked][colClicked] == 1 and rowClicked == rows-1:
        makeKingPiece(canvas, rowClicked, colClicked)
    if checkerBoard[rowClicked][colClicked] == -1 and rowClicked == 0:
        makeKingPiece(canvas, rowClicked, colClicked)
    up = -1
    down = +1
    noMovesUp = True
    noMovesDown = True
    if abs(rowClickedBefore - rowClicked) == 1 and abs(colClickedBefore - colClicked) == 1:
        endTurn(canvas)
    else:
        print "Ate A Piece!!!"
        checkerBoard[(rowClicked+rowClickedBefore)/2][(colClicked+colClickedBefore)/2] = 0
        canvas.data["checkerBoard"] = checkerBoard
        clearHighlight(canvas)
        if blueTurn == True:
            findPossibleBlueMoves(canvas, rowClicked, colClicked)
            removeAdjacentMoves(canvas, rowClicked, colClicked)
            if rowClicked+up*2 >= 0:
                if checkerBoard[rowClicked+up*2].count(3) > 0:
                    noMovesUp = False
                    redrawAll(canvas)
                    canvas.data["mustTake"] = True
            if rowClicked+down*2 <= rows-1:
                if checkerBoard[rowClicked+down*2].count(3) > 0:
                    noMovesDown = False
                    redrawAll(canvas)
                    canvas.data["mustTake"] = True
        else:
            findPossibleRedMoves(canvas,rowClicked, colClicked)
            removeAdjacentMoves(canvas, rowClicked, colClicked)
            if rowClicked+up*2 >= 0:
                if checkerBoard[rowClicked+up*2].count(3) > 0:
                    noMovesUp = False
                    redrawAll(canvas)
                    canvas.data["mustTake"] = True
            if rowClicked+down*2 <= rows-1:
                if checkerBoard[rowClicked+down*2].count(3) > 0:
                    noMovesDown = False
                    redrawAll(canvas)
                    canvas.data["mustTake"] = True
        if noMovesUp == True and noMovesDown == True: endTurn(canvas)




def findPossibleBlueMoves(canvas, rowClicked, colClicked):
    checkerBoard = canvas.data["checkerBoard"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    up = -1
    down = +1
    left = -1
    right = +1
    if checkerBoard[rowClicked][colClicked] == -1:
        if rowClicked + up >= 0:
            if colClicked + left >= 0:
                if checkerBoard[rowClicked+up][colClicked+left] == 0:
                    checkerBoard[rowClicked+up][colClicked+left] = 3
#The following code identifies spaces that piece would jump to after eating a piece.
                elif checkerBoard[rowClicked+up][colClicked+left] > 0:
                    if rowClicked + up*2 >= 0:
                        if colClicked + up*2 >=0:
                            if checkerBoard[rowClicked+up*2][colClicked+left*2] == 0:
                                checkerBoard[rowClicked+up*2][colClicked+left*2] = 3
            if colClicked + right <= cols-1:
                if checkerBoard[rowClicked+up][colClicked+right] == 0:
                    checkerBoard[rowClicked+up][colClicked+right] = 3
                elif checkerBoard[rowClicked+up][colClicked+right] > 0:
                    if rowClicked + up*2 >= 0:
                        if colClicked + right*2 <= cols-1:
                            if checkerBoard[rowClicked+up*2][colClicked+right*2] == 0:
                                checkerBoard[rowClicked+up*2][colClicked+right*2] = 3
    if checkerBoard[rowClicked][colClicked] == -2: #just a combination of red and blue moves (copy&pasted)
        if rowClicked + up >= 0:
            if colClicked + left >= 0:
                if checkerBoard[rowClicked+up][colClicked+left] == 0:
                    checkerBoard[rowClicked+up][colClicked+left] = 3
                elif checkerBoard[rowClicked+up][colClicked+left] > 0:
                    if rowClicked + up*2 >= 0:
                        if colClicked + up*2 >=0:
                            if checkerBoard[rowClicked+up*2][colClicked+left*2] == 0:
                                checkerBoard[rowClicked+up*2][colClicked+left*2] = 3
            if colClicked + right <= cols-1:
                if checkerBoard[rowClicked+up][colClicked+right] == 0:
                    checkerBoard[rowClicked+up][colClicked+right] = 3
                elif checkerBoard[rowClicked+up][colClicked+right] > 0:
                    if rowClicked + up*2 >= 0:
                        if colClicked + right*2 <= cols-1:
                            if checkerBoard[rowClicked+up*2][colClicked+right*2] == 0:
                                checkerBoard[rowClicked+up*2][colClicked+right*2] = 3
        if rowClicked + down <= rows-1:
            if colClicked + left >= 0:
                if checkerBoard[rowClicked+down][colClicked+left] == 0:
                    checkerBoard[rowClicked+down][colClicked+left] = 3
                elif checkerBoard[rowClicked+down][colClicked+left] > 0:
                    if rowClicked + down*2 <= rows-1:
                        if colClicked + left*2 >= 0:
                            if checkerBoard[rowClicked+down*2][colClicked+left*2] == 0:
                                checkerBoard[rowClicked+down*2][colClicked+left*2] = 3
            if colClicked + right <= cols-1:
                if checkerBoard[rowClicked+down][colClicked+right] == 0:
                    checkerBoard[rowClicked+down][colClicked+right] = 3
                elif checkerBoard[rowClicked+down][colClicked+right] > 0:
                    if rowClicked + down*2 <= rows-1:
                        if colClicked + right*2 <= cols-1:
                            if checkerBoard[rowClicked+down*2][colClicked+right*2] == 0:
                                checkerBoard[rowClicked+down*2][colClicked+right*2] = 3
    canvas.data["checkerBoard"] = checkerBoard

def findPossibleRedMoves(canvas, rowClicked, colClicked):
    checkerBoard = canvas.data["checkerBoard"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    up = -1
    down = +1
    left = -1
    right = +1
    if checkerBoard[rowClicked][colClicked] == 1:
        if rowClicked + down <= rows-1:
            if colClicked + left >= 0:
                if checkerBoard[rowClicked+down][colClicked+left] == 0:
                    checkerBoard[rowClicked+down][colClicked+left] = 3
                elif checkerBoard[rowClicked+down][colClicked+left] < 0:
                    if rowClicked + down*2 <= rows-1:
                        if colClicked + left*2 >= 0:
                            if checkerBoard[rowClicked+down*2][colClicked+left*2] == 0:
                                checkerBoard[rowClicked+down*2][colClicked+left*2] = 3
            if colClicked + right <= cols-1:
                if checkerBoard[rowClicked+down][colClicked+right] == 0:
                    checkerBoard[rowClicked+down][colClicked+right] = 3
                elif checkerBoard[rowClicked+down][colClicked+right] < 0:
                    if rowClicked + down*2 <= rows-1:
                        if colClicked + right*2 <= cols-1:
                            if checkerBoard[rowClicked+down*2][colClicked+right*2] == 0:
                                checkerBoard[rowClicked+down*2][colClicked+right*2] = 3
    if checkerBoard[rowClicked][colClicked] == 2:
        if rowClicked + up >= 0:
            if colClicked + left >= 0:
                if checkerBoard[rowClicked+up][colClicked+left] == 0:
                    checkerBoard[rowClicked+up][colClicked+left] = 3
                elif checkerBoard[rowClicked+up][colClicked+left] < 0:
                    if rowClicked + up*2 >= 0:
                        if colClicked + up*2 >=0:
                            if checkerBoard[rowClicked+up*2][colClicked+left*2] == 0:
                                checkerBoard[rowClicked+up*2][colClicked+left*2] = 3
            if colClicked + right <= cols-1:
                if checkerBoard[rowClicked+up][colClicked+right] == 0:
                    checkerBoard[rowClicked+up][colClicked+right] = 3
                elif checkerBoard[rowClicked+up][colClicked+right] < 0:
                    if rowClicked + up*2 >= 0:
                        if colClicked + right*2 <= cols-1:
                            if checkerBoard[rowClicked+up*2][colClicked+right*2] == 0:
                                checkerBoard[rowClicked+up*2][colClicked+right*2] = 3
        if rowClicked + down <= rows-1:
            if colClicked + left >= 0:
                if checkerBoard[rowClicked+down][colClicked+left] == 0:
                    checkerBoard[rowClicked+down][colClicked+left] = 3
                elif checkerBoard[rowClicked+down][colClicked+left] < 0:
                    if rowClicked + down*2 <= rows-1:
                        if colClicked + left*2 >= 0:
                            if checkerBoard[rowClicked+down*2][colClicked+left*2] == 0:
                                checkerBoard[rowClicked+down*2][colClicked+left*2] = 3
            if colClicked + right <= cols-1:
                if checkerBoard[rowClicked+down][colClicked+right] == 0:
                    checkerBoard[rowClicked+down][colClicked+right] = 3
                elif checkerBoard[rowClicked+down][colClicked+right] < 0:
                    if rowClicked + down*2 <= rows-1:
                        if colClicked + right*2 <= cols-1:
                            if checkerBoard[rowClicked+down*2][colClicked+right*2] == 0:
                                checkerBoard[rowClicked+down*2][colClicked+right*2] = 3
    canvas.data["checkerBoard"] = checkerBoard


def clearHighlight(canvas):
    checkerBoard = canvas.data["checkerBoard"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    for row in range(rows):
        for col in range(cols):
            if checkerBoard[row][col] > 2:
                checkerBoard[row][col] = 0
    canvas.data["checkerBoard"] = checkerBoard

#def timerFired(canvas):
     #moveBadGuys(canvas)
     #Level = canvas.data["Level"]
     #delay = int(250 * (0.8) ** (Level)) # milliseconds
     #print delay
     #canvas.after(delay, timerFired, canvas)


def highlightMoves(canvas):
    checkerBoard = canvas.data["checkerBoard"]
    rowClicked = canvas.data["rowClicked"]
    colClicked = canvas.data["colClicked"]
    blueTurn = canvas.data["blueTurn"]
    if blueTurn == True and checkerBoard[rowClicked][colClicked] < 0:
        findPossibleBlueMoves(canvas, rowClicked, colClicked)
    elif blueTurn == False and checkerBoard[rowClicked][colClicked] > 0:
        findPossibleRedMoves(canvas, rowClicked, colClicked)
    redrawAll(canvas)



def mousePressed(event):
    canvas = event.widget.canvas
    checkerBoard = canvas.data["checkerBoard"]
    margin = canvas.data["margin"]
    cellSize = canvas.data["cellSize"]
    rowClickedBefore = canvas.data["rowClicked"]
    colClickedBefore = canvas.data["colClicked"]
    mustTake = canvas.data["mustTake"]
    #convert coordinates into rows & cols
    x = event.x
    y = event.y
    colClicked = (x - margin)/cellSize
    rowClicked = (y - margin)/cellSize
    if checkerBoard[rowClicked][colClicked] != 0:
        canvas.data["colClicked"] = colClicked
        canvas.data["rowClicked"] = rowClicked
    if mustTake == True and checkerBoard[rowClicked][colClicked] != 3:
        rowClicked = rowClickedBefore
        colClicked = colClickedBefore
        canvas.data["rowClicked"] = rowClicked
        canvas.data["colClicked"] = colClicked
    #if player clicked a non-highlighted box, delete the old highlights and then make new ones
    if checkerBoard[rowClicked][colClicked] != 3 and mustTake == False: clearHighlight(canvas)
    if mustTake == False: highlightMoves(canvas)
    if rowClickedBefore != None:
        if checkerBoard[rowClicked][colClicked] == 3:
            moveCheckerPiece(canvas, rowClickedBefore, colClickedBefore, rowClicked, colClicked)
            redrawAll(canvas)
    elif checkerBoard[rowClicked][colClicked] != 0:
        drawCheckerCell(canvas, checkerBoard, rowClicked, colClicked)




def drawCheckerCell(canvas, checkerBoard, row, col):
    margin = canvas.data["margin"]
    cellSize = canvas.data["cellSize"]
    colClicked = canvas.data["colClicked"]
    rowClicked = canvas.data["rowClicked"]
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    if row == rowClicked and col == colClicked:
        canvas.create_rectangle(left, top, right, bottom, fill="yellow")
    else: canvas.create_rectangle(left, top, right, bottom, fill="cyan")
    if checkerBoard[row][col] == 3:
        #highlight possible moves
        canvas.create_rectangle(left, top, right, bottom, fill="magenta")
    elif checkerBoard[row][col] > 0:
        #draw red piece
        canvas.create_oval(left, top, right, bottom, fill="red")
        canvas.create_oval(left+3, top+3, right-3, bottom-3, fill="red")
        canvas.create_oval(left+6, top+6, right-6, bottom-6, fill="red")
    elif checkerBoard[row][col] < 0:
        #blue piece
        canvas.create_oval(left, top, right, bottom, fill="blue")
        canvas.create_oval(left+3, top+3, right-3, bottom-3, fill="blue")
        canvas.create_oval(left+6, top+6, right-6, bottom-6, fill="blue")
    if abs(checkerBoard[row][col]) == 2:
        canvas.create_rectangle(left+13, top+13, right-13, bottom-13, fill="black")


def drawCheckerBoard(canvas):
    checkerBoard = canvas.data["checkerBoard"]
    rows = len(checkerBoard)
    cols = len(checkerBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawCheckerCell(canvas, checkerBoard, row, col)


def redrawAll(canvas):
    canvas.delete(ALL)
    drawCheckerBoard(canvas)
    if (canvas.data["isGameOver"] == True):
        cx = canvas.data["canvasWidth"]/2
        cy = canvas.data["canvasHeight"]/2
        canvas.create_text(cx, cy, text="Game Over!", font=("Helvetica", 32, "bold"))

def loadCheckerBoard(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    checkerBoard = [ ]
    for row in range(rows): checkerBoard += [[0] * cols]
    #for the top row
    for col in range(0,cols):
        if col%2 == 0:
            checkerBoard[rows-1][col] = -1
            checkerBoard[rows-3][col] = -1
            checkerBoard[1][col] = 1
        else:
            checkerBoard[rows-2][col] = -1
            checkerBoard[0][col] = 1
            checkerBoard[2][col] = 1
    canvas.data["checkerBoard"] = checkerBoard

def init(canvas):
    #printInstructions()
    loadCheckerBoard(canvas)
    canvas.data["isGameOver"] = False
    canvas.data["blueTurn"] = True
    canvas.data["rowClicked"] = None
    canvas.data["colClicked"] = None
    canvas.data["mustTake"] = False
    redrawAll(canvas)

def run(mode):
    # create the root and the canvas
    root = Tk()
    cellSize = 90
    margin = 10
    cols = 8
    rows = 8
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    # Set up canvas data and call init
    root.canvas = canvas.canvas = canvas
    canvas.data = { }
    canvas.data["canvasWidth"] = canvasWidth
    canvas.data["canvasHeight"] = canvasHeight
    canvas.data["cellSize"] = cellSize
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    canvas.data["margin"] = margin
    canvas.data["mode"] = mode
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    #root.bind("<Key>", keyPressed)
    #timerFired(canvas)
    # and launch the app
    root.mainloop()

def easyPressed():
    # accesses canvas as a global variable
    global canvas
    canvas.delete(ALL)
    run("easyComp")

def mediumPressed():
    global canvas
    canvas.delete(ALL)
    run("mediumComp")


def hardPressed():
    global canvas
    canvas.delete(ALL)
    run("hardComp")

def redrawAllMenu2(canvas):
    canvas.delete(ALL)
    # background (fill canvas)
    canvas.create_rectangle(0,0,300,300,fill="cyan")
    # print buttons in window
    b1 = canvas.data["Easy"]
    canvas.create_window(150, 50, window=b1)
    b2 = canvas.data["Medium"]
    canvas.create_window(150, 100, window=b2)
    b3 = canvas.data["Hard"]
    canvas.create_window(150, 150, window=b3)

def initMenu2(root, canvas):

    b1 = Button(canvas, text="Easy", command=easyPressed)
    canvas.data["Easy"] = b1
    b2 = Button(canvas, text="Medium", command=mediumPressed)
    canvas.data["Medium"] = b2
    b3 = Button(canvas, text="Hard", command=hardPressed)
    canvas.data["Hard"] = b3
    canvas.pack() # moved canvas packing to here (before button packing!)
    redrawAllMenu2(canvas)

def runMenu2():
    # create the root and the canvas
    root = Tk()
    global canvas # make canvas global for button1Pressed function
    canvas = Canvas(root, width=300, height=300)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    initMenu2(root, canvas)
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

from Tkinter import *

def onePlayerPressed():
    global canvas
    canvas.delete(ALL)
    runMenu2()


def twoPlayerPressed():
    global canvas
    canvas.delete(ALL)
    run("twoPlayer")

def redrawAllMenu1(canvas):
    canvas.delete(ALL)
    # background (fill canvas)
    canvas.create_rectangle(0,0,300,300,fill="cyan")
    # print buttons in window
    b1 = canvas.data["1 Player"]
    canvas.create_window(150, 100, window=b1)
    b2 = canvas.data["2 Players"]
    canvas.create_window(150, 200, window=b2)

def initMenu1(root, canvas):
    b1 = Button(canvas, text="1 Player", command=onePlayerPressed)
    canvas.data["1 Player"] = b1
    b2 = Button(canvas, text="2 Players", command=twoPlayerPressed)
    canvas.data["2 Players"] = b2
    canvas.pack() # moved canvas packing to here (before button packing!)
    redrawAllMenu1(canvas)



def runMenu1():
    # create the root and the canvas
    root = Tk()
    global canvas # make canvas global for button1Pressed function
    canvas = Canvas(root, width=300, height=300)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    initMenu1(root, canvas)
    root.mainloop()

runMenu1()
