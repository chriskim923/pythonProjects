#
#   Template for 15-110 Homework #3
#
#   Problem #2d: commonLetters
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk Kim, moosukk
#
#   15-110 section: N

# Implement the function  commonLetters(s1, s2) after this line
def commonLetters(s1, s2):
    s1 = s1.upper()
    s2 = s2.upper()
    letter = ""
    for n in range(len(s2)):
        if (s1.find(s2[n]) >= 0):
            if s2[n] != " ":
                letter += s2[n]
    return letter
        




# These assertions are here for your benefit.  They are not exhaustive:
# the CA's will use more tests when grading your final submissions.
# Feel free to add/remove tests here, just be careful!

assert(commonLetters("This is a test", "Let's go Team!!!!") == "AEST")
assert(commonLetters("Roses are red!", "Yippy!") == "")  # (the empty string)
    
print("Passed all tests!")

