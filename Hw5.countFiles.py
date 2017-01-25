#   Template for 15-110 Homework #5
#
#   Problem 2A: countFiles.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:
#


import os
#implement your code after this line










# DO NOT CHANGE THE CODE BELOW THIS LINE

assert(countFiles("hw5TestFolder/folderB/folderF/folderG") == 0)
assert(countFiles("hw5TestFolder/folderB/folderF") == 0)
assert(countFiles("hw5TestFolder/folderB") == 2)
assert(countFiles("hw5TestFolder/folderA/folderC") == 4)
assert(countFiles("hw5TestFolder/folderA") == 6)
assert(countFiles("hw5TestFolder") == 10)
print "Passed all tests!"
