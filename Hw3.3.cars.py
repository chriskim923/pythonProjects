#
#   Template for 15-110 Homework #3
#
#   Problem #3: Let's buy a new car
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

# Implement the function compareCars(years) after this line

def compareCars (years):
    print "year\tA\tB"
    x = 0
    A = 0
    B = 0
    while ((x - 1) < years):
        A = 15000 + ((12000 / 25.0) * x * 2.7) + (300 * 1.15 * x)
        B = 18000 + ((12000 / 33.0) * x * 2.7) + (300 * 1.1 * x)
        print "%d\t%d\t%d" % (x, A, B)
        x += 1
    if (A < B):
        print "Car A is cheaper"
    elif (B < A):
        print "Car B is cheaper"
    else:
        print "It's a tie!"

# comparing car prices in 5 and 10 years:

compareCars (5) # Car A is cheaper
compareCars (10) # Car B is cheaper
        
        
        
