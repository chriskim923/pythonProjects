#   Template for 15-110 Homework #5
#
#   Problem 2B: findFile.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:
#

import os

#implement your code after this line










# DO NOT CHANGE THE CODE BELOW THIS LINE

assert(findFile("hw5TestFolder", "fishing.txt"   ) == "hw5TestFolder/folderA/fishing.txt")
assert(findFile("hw5TestFolder", "tree.txt"      ) == "hw5TestFolder/folderA/folderC/folderE/tree.txt")
assert(findFile("hw5TestFolder", "driving.txt"   ) == "hw5TestFolder/folderB/folderH/driving.txt")
assert(findFile("hw5TestFolder", "mirror.txt"    ) == "hw5TestFolder/mirror.txt")
assert(findFile("hw5TestFolder", "noSuchFile.txt") == "")
print "Passed all tests!"
