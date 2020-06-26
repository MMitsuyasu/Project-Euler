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


############################################################################
############################################################################

# Official Solution Used


# Identify prime numbers
def isPrime(number):
    import math
    workingNum = number
    isPrimeNum = True

    # Checks for 2 as a factor (if number is 2, skips and returns prime)
    if workingNum > 2 and workingNum % 2 == 0:
        isPrimeNum = False
        while workingNum % 2 == 0:
            workingNum = workingNum / 2

    # Checks for other factors
    maxFactor = math.sqrt(workingNum)
    factor = 3
    while isPrimeNum and workingNum > 1 and factor <= maxFactor:
        if workingNum % factor == 0:
            isPrimeNum = False
            while workingNum % factor == 0:
                workingNum = workingNum / factor
            maxFactor = math.sqrt(workingNum)
        factor = factor + 2

    return isPrimeNum


# Collect prime numbers up to target
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


# Collect roots from numbers up to target that have Nth roots
def rootFactorsIn(target):
    import math

    # Identifies Nth roots to check
    checkRoots = []
    for root in range(int(math.sqrt(target)), 1, -1):
        checkRoots.append(root)

    # Identifies and collects clean Nth roots
    rootFactors = []
    for n in range(4, target+1):    # Start at 4 since 2 & 3 are prime
        if n in primesUpTo(target):
            # Skips prime numbers
            continue
        for root in checkRoots:
            if ((n ** (1/root)) % 1) == 0:
                rootFactors.append(int(n ** (1/root)))
                break

    return rootFactors


# Multiply all identified foundational factors
def smallestProduct(target):
    number = 1
    foundationFactors = primesUpTo(target) + rootFactorsIn(target)
    for x in foundationFactors:
        number = number * x
    return number


x = 20
print(f"The smallest number evenly divisible by all integers 1 to {x} is {smallestProduct(x)}.")



############################################################################
############################################################################

## Optimized Solution Notes

