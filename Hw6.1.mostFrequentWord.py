#
#   Template for 15-110 Homework #6
#
#   Problem #1: 1.mostFrequentWord.py
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moo Suk Kim (moosukk)
#
#   15-110 section: N

import copy



def mostFrequentWord(text):
    if len(text) == 0:
        return None
    text = text.upper()
    space = " "
    text = text + space
    word = []
    for x in range(len(text)):
        listOfWords = []
        if text[x] == space:
            listOfWords += word
            word = []
        else:
            word += text[x]
            word = ''.join(word)
    listOfWords.sort()
    listOfWords.append(" ")
    countA = 1
    countB = 0
    mostCommonSoFar = listOfWords[0]
    nextMostCommon = ""
    for x in range(len(listOfWords)-1):
        if mostCommonSoFar == listOfWords[x+1]:
            countA +=1
        elif (countA < countB):
            mostCommonSoFar = nextMostCommon
            countA = countB
            countB = 0
        elif listOfWords[x] != listOfWords[x+1]:
            nextMostCommon = listOfWords[x+1]
        elif listOfWords[x] == nextMostCommon:
            countB += 1
    return mostCommonSoFar


################## You may ignore below this line #################

print "Testing mostFrequentWord()...",

assert(mostFrequentWord("") == None)
assert(mostFrequentWord("This is a test!") == "A")
joke = """
You can say any foolish thing to a dog,
and the dog will give you this look that says,
"My God, you are right! I never would've thought of that!"
Dave Barry
"""
assert(mostFrequentWord(joke) == "YOU")
assert(mostFrequentWord("wow gosh wow!!! gosh!!!! wow.  No way.  Yes way.  Way!  gosh.") == "GOSH")

print "Passed!"
