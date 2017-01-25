#
#   Template for 15-110 Homework #6
#
#   Problem #2: 2.mastermindScore.py
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk Kim   (moosukk)
#
#   15-110 section:N

import copy

def mastermindScore(code, guess):
    Perfect = 0
    RightColor = 0
    for x in range(3):
        if code[x] == guess[x]:
            Perfect += 1
    for x in range(3):
        if (code.count(guess[x]) >0):
            RightColor += 1
    Answer = [RightColor, Perfect]
    return Answer



################## You may ignore below this line #################

print "Testing mastermindScore()...",
assert(mastermindScore([3,4,5,6], [3,3,4,6]) == [2,1])
assert(mastermindScore([3,4,5,6], [1,2,3,4]) == [0,2])
assert(mastermindScore([3,4,5,6], [3,4,3,4]) == [2,0])
assert(mastermindScore([3,4,5,6], [1,1,1,1]) == [0,0])
assert(mastermindScore([3,4,5,6], [3,3,3,3]) == [1,0])
assert(mastermindScore([3,4,5,6], [2,3,3,3]) == [0,1])
print "Passed!"
