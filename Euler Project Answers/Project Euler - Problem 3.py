# Project Euler: Problem 3

## Largest Prime Factor:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# Solving with Python (3.8.1)

############################################################################

## Practice Work

############################################################################
############################################################################

## Official Solution Used
# For the designated number (becasue it's odd, 2 is not a factor)

targetNum = 600851475143
nonPrimeFact = targetNum
primeNum = 3
product = 1

while product < targetNum:
    if nonPrimeFact % primeNum == 0:
        while nonPrimeFact % primeNum == 0:
            print("PrimeNum factor is %d" %primeNum)
            product = product * primeNum
            print("Product is %d" % product)
            nonPrimeFact = nonPrimeFact / primeNum
        primeNum = primeNum + 2
        print("")
    else:
        primeNum = primeNum + 2

print("The largest prime factor of %d is %d" % (targetNum, primeNum - 2))


############################################################################

# MY ANSWER
# To solve for any number > 0

##targetNum = 3747
##nonPrimeFact = targetNum
##primeNum = 3
##product = 1
##
##while product < targetNum:
##    if nonPrimeFact % 2 == 0:
##        print("number is even")
##        nonPrimeFact = nonPrimeFact / 2
##        print("Remaining is %d" % nonPrimeFact)
##        product = product * 2
##        print("product is %d" % product)
##        print("")
##    else:
##        if nonPrimeFact % primeNum == 0:
##            while nonPrimeFact % primeNum == 0:
##                print("Prime factor is %d" %primeNum)
##                nonPrimeFact = nonPrimeFact / primeNum
##                print("Remaining is %d" % nonPrimeFact)
##                product = product * primeNum
##                print("Product is %d" % product)
##                print("")
##            primeNum = primeNum + 2
##        else:
##            primeNum = primeNum + 2
##
##primeNum = primeNum - 2
##if primeNum <= 2:
##    primeNum = 2
##
##print("The largest prime factor of %d is %d" % (targetNum, primeNum))


############################################################################
############################################################################

#### OPTIMIZED VERSION (with print checks)

#### Shortens the limits of options to try each iteration
####     (i.e. 2 * 2 * 2 * 3 * 3 * 5 * 21 * 499 = 3772440
####         takes ?? lines to solve instead of ??)
####     Every number has at most one prime factor greater than its square root
####         (essentially the half-way point of products)
####         (if haven't found a factor below, not going to be matching above)

#### Educational version has each section run first iteration of prime
####     followed by while loop for multiples
#### Mine eliminates duplicate run by running initial iteration with others
####     E.g. (theirs)
####         Check if factor
####             Set new max factor
####             Process factor
####             iterate
####                 process factor
####     vs. (mine)
####         Check if factor
####             set new max factor
####             iterate
####                 process factor

##import math              # needed for square root function
##
##targetNum = 3772440
##remaining = targetNum    # reducing this number to 1 as run program
##primeNum = 3             # number to test for prime status (above 2)
##lastFactor = 1           # current highest prime factor
##maxFactor = math.sqrt(remaining) # limit for highest prime factor b/w 1 & n
##product = 1
##
##### Checks if 2 is a factor
##if remaining % 2 == 0:
##    lastFactor = 2                          # Saves current highest prime factor
##    while remaining % 2 == 0:               # Factors out all multiples of 2
##        print("Prime factor is 2")
##        remaining = remaining / 2           # Left to determine factors of
##        print("Remaining is %d" % remaining)
##        product = product * 2               # Product of identified factors
##        print("product is %d" % product)    #   could eliminate but provides
##        print("")                        #   easy way to check if working
##
##### Determines prime factors > 2
##maxFactor = math.sqrt(remaining)     # Identifies the max non-n factor of n
##print("maxFactor is %d" % maxFactor)
##
##while remaining >= 1 and primeNum <= maxFactor:
##    if remaining % primeNum == 0:
##        lastFactor = primeNum               # Saves current highest prime factor
##        while remaining % primeNum == 0:    # Factors out all multiples of PF
##            print("Prime factor is %d" %primeNum)
##            remaining = remaining / primeNum    # Left to determine factors of
##            print("Remaining is %d" % remaining)
##            product = product * primeNum    # Product of identified factors
##            print("Product is %d" % product)
##            print("")
##        primeNum = primeNum + 2             # Determines next number to check
##        print("New number to test is %d" % primeNum)
##        maxFactor = math.sqrt(remaining) # Establishes new max non-n factor of n
##        print("MaxFactor is %d" % maxFactor)
##    else:
##        primeNum = primeNum + 2
##        print("New number to test is %d" % primeNum)
##print("")
##
##### Determines which option is highest prime factor
##if remaining == 1:
##    print("The largest prime factor of %d is %d" % (targetNum, lastFactor))
##else:
##    print("The largest prime factor of %d is %d" % (targetNum, remaining))


############################################################################

#### OPTIMZED VERSION (without print checks)

##import math              # needed for square root function
##
##targetNum = 3772440
##remaining = targetNum    # reducing this number to 1 as run program
##primeNum = 3             # number to test for prime status (above 2)
##lastFactor = 1           # current highest prime factor
##maxFactor = math.sqrt(remaining) # limit for highest prime factor b/w 1 & n
##
##### Checks if 2 is a factor
##if remaining % 2 == 0:
##    lastFactor = 2                  # Saves current highest prime factor
##    while remaining % 2 == 0:       # Factors out all multiples of 2
##        remaining = remaining / 2   # Left to determine factors of
##
##### Determines prime factors > 2
##maxFactor = math.sqrt(remaining)     # Identifies the max non-n factor of n
##
##while remaining >= 1 and primeNum <= maxFactor:
##    if remaining % primeNum == 0:
##        lastFactor = primeNum               # Saves current highest prime factor
##        while remaining % primeNum == 0:    # Factors out all multiples of PF
##            remaining = remaining / primeNum    # Left to determine factors of
##        primeNum = primeNum + 2             # Determines next number to check
##        maxFactor = math.sqrt(remaining) # Establishes new max non-n factor of n
##    else:
##        primeNum = primeNum + 2
##
##### Determines which option is highest prime factor
##if remaining == 1:
##    print("The largest prime factor of %d is %d" % (targetNum, lastFactor))
##else:
##    print("The largest prime factor of %d is %d" % (targetNum, remaining))
