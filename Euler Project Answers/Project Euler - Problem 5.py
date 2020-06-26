# Project Euler: Problem 5

## Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?


# Solving with Python (3.8.1)

############################################################################

## Practice Work

# Identify prime numbers <= target
# Identify clean roots of remaining numbers <= target
# Multiply all identified factors together


# Identify prime numbers <= target
def isPrime(number):
    import math
    workingNum = number
    primeNum = True

    # Checks for 2 as a factor (if number is 2, skips and returns prime)
    if workingNum > 2 and workingNum % 2 == 0:
        primeNum = False
        while workingNum % 2 == 0:
            workingNum = workingNum / 2

    # Checks for other factors
    maxFactor = math.sqrt(workingNum)
    factor = 3
    while primeNum and workingNum > 1 and factor <= maxFactor:
        if workingNum % factor == 0:
            primeNum = False
            while workingNum % factor == 0:
                workingNum = workingNum / factor
            maxFactor = math.sqrt(workingNum)
        factor = factor + 2

    return primeNum


def primesUpTo(target):
    if target <1:
        primeList = []
    elif target == 1:
        primeList = [1]
    else:
        primeList = []
        for num in range(2, target+1):
            if isPrime(num):
                primeList.append(num)
    return primeList


print(primesUpTo(10))



# Identify clean roots of remaining numbers <= target
import math
test = [1, 2, 3, 4, 5, 9, 16, 25, 32]
test2 = [4, 9]
target = 10

#for n in test:
#    if n in test2:
#        continue

# Identifies roots to check
checkRoots = []
for root in range(int(math.sqrt(target)), 1, -1):
    checkRoots.append(root)
print(checkRoots)

# Determines if target list has a clean int root
rootFactors = []
for n in range(4, target+1):
##    if n in primeFactors(target):
##        # Skips numbers already identified as factors (b/c prime)
##        continue
    for root in checkRoots:
        if ((n ** (1/root)) % 1) == 0:
            rootFactors.append(int(n ** (1/root)))
            break
print(rootFactors)


# Multiply all identified factors together


############################################################################
############################################################################

# Official Solution Used


############################################################################
############################################################################

## Optimized Solution Notes

