#
#   Template for 15-110 Homework #3
#
#   Problem #5: The number guessing game strikes again
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

# Implement the function numberGuessingGame(lowerBound, upperBound) after this line

def numberGuessingGame(lowerBound, upperBound):
    guess = (upperBound + lowerBound) / 2
    print "guess ",guess
    A = raw_input("high/low/right:")
    if A == "high":
        lowerBound = guess
        numberGuessingGame(lowerBound, upperBound)
    elif A == "low":
        upperBound = guess
        numberGuessingGame(lowerBound, upperBound)
    elif A == "right":
        print guess, "is your number"
