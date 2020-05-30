

##n = 291
##
##if n % 2 == 0:
##    print("Number is even")
##    n = n / 2
##    print("Remaining number is %d" % n)
##    lastFactor = 2
##    print("  ")
##    while n % 2 == 0:
##        n = n / 2
##        print("Number is even")
##        print("Remaining number is %d" % n)
##        print("  ")
##else:
##    lastFactor = 1
##    print("Number is odd")
##    print("  ")
##
##factor = 3
##print("New number to try is %d" % factor)
##print("  ")
##
##while n > 1:
##    if n % factor == 0:
##        print("Prime factor is %d" % factor)
##        n = n / factor
##        print("Remaining number is %d" % n)
##        lastFactor = factor
##        print("  ")
##        while n % factor == 0:
##            print("Prime factor is %d" % factor)
##            n = n / factor
##            print("Remaining number is %d" % n)
##            print("  ")
##    factor = factor + 2
##    print("New number to try is %d" % factor)
##    print("  ")
##
##print("The largest prime factor is %d" % lastFactor)

import math

n = 3772440

if n % 2 == 0:
    print("Number is even")
    n = n / 2
    print("Remaining number is %d" % n)
    lastFactor = 2
    while n % 2 == 0:
        n = n / 2
        print(" ")
        print("Number is even")
        print("Remaining number is %d" % n)
else:
    lastFactor = 1
    print("Number is odd")

factor = 3
maxFactor = math.sqrt(n)
print(" ")
print("MaxFactor is %d" % maxFactor)
print("New number to try is %d" % factor)

while n > 1 and factor <= maxFactor:
    if n % factor == 0:
        print("Prime factor is %d" % factor)
        n = n / factor
        print("Remaining number is %d" % n)
        lastFactor = factor
        while n % factor == 0:
            n = n / factor
            print(" ")
            print("Prime factor is %d" % factor)
            print("Remaining number is %d" % n)
        maxFactor = math.sqrt(n)
        print(" ")
        print("MaxFactor is %d" % maxFactor)
    factor = factor + 2
    print("New number to try is %d" % factor)

print(" ")

if n == 1:
    print("The largest prime factor is %d" % lastFactor)
else:
    print("The largest prime factor is %d" % n)

