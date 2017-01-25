#
#   Template for 15-110 Homework #3
#
#   Problem #3: nthPerfect
#
#
#   WRITTEN BY (NAME & ANDREW ID): Moosuk Kim, moosukk
#
#   15-110 section: N


# Implement the helper function  sumOfProperFactors(n) after this line
def sumOfProperFactors(n):
    sum = 0
    for x in range(n):
        if n%(x+1) == 0:
            sum += (x+1)
    sum = sum / 2
    return sum


# Implement the helper function  isPerfect(n) after this line
def isPerfect(n):
    return sumOfProperFactors(n) == n

# Implement the function  nthPerfect(n) after this line
def nthPerfect(n):
    perfect = 0
    guess = -1
    while ((perfect - 1) <= n):
        guess += 1
        if (isPerfect(guess)):
            perfect += 1
    return guess

# These assertions are here for your benefit.  They are not exhaustive:
# the CA's will use more tests when grading your final submissions.
# Feel free to add/remove tests here, just be careful!

assert(sumOfProperFactors(-22) == 0)
assert(sumOfProperFactors(1) == 0)
assert(sumOfProperFactors(6) == 6)
assert(sumOfProperFactors(8) == 7)
       
print("Passed all tests for sumOfProperFactors!")

assert(isPerfect(-22) == False)
assert(isPerfect(5) == False)
assert(isPerfect(6) == True)
# We'll just comment this next one out for now...
#assert(isPerfect(2658455991569831744654692615953842176) == True) (eventually)

print("Passed all tests for isPerfect!")


assert(nthPerfect(0) == 6)
assert(nthPerfect(1) == 28)
assert(nthPerfect(2) == 496)
assert(nthPerfect(3) == 8128)
assert(nthPerfect(-22) == -1)

print("Passed all tests for nthPerfect!")
