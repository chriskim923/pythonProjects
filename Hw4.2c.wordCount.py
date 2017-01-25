#
#   Template for 15-110 Homework #3
#
#   Problem #2c: wordCount
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk Kim , moosukk
#
#   15-110 section: N

# Implement the function  wordCount(string) after this line

def wordCount(string):
    space = " "
    count = 0
    string = space + string
    for x in range(len(string)):
        if string[x] != space:
            if string[x-1] == space:
                count += 1
    return count

# These assertions are here for your benefit.  They are not exhaustive:
# the CA's will use more tests when grading your final submissions.
# Feel free to add/remove tests here, just be careful!

assert(wordCount("This is a test") == 4)
assert(wordCount("This   is   a    test!!!!!") == 4)
assert(wordCount("") == 0)
assert(wordCount("Wahoo42!??!?!") == 1)
assert(wordCount("  try this") == 2)
      
print("Passed all tests!")

