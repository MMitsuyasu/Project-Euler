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
    elif target == 2:
        primeList = [2]
    else:
        primeList = [2]
        for num in range(3, target+1, 2):
            if isPrime(num):
                primeList.append(num)
    return primeList


# Collect roots from numbers up to target that have Nth roots
def rootFactorsIn(target):
    import math

    # Identifies Nth roots to check
    checkRoots = []
    for root in range(int(math.sqrt(target)), 1, -1):
        # Max root is sqrt(target) to limit number of roots to check
            # r such that 2 ** r <= target will be <= sqrt(target)
            # 2 is the smallest prime, so for any higher prime, r will be <=
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
print(f"The smallest number evenly divisible by all integers 1 to {x}" \
    f" is {smallestProduct(x)}.")



############################################################################
############################################################################

## Optimized Solution Notes

# See official Project Euler "overview" explanation:
#     https://projecteuler.net/overview=005

# Essentially the same idea though used logarithms instead of Nth roots
#     (I'd forgotten what logarithms are and how to use them)
#     (Logarithms are the inverse functions to exponentialism)
#     Logarithm review: https://en.wikipedia.org/wiki/Logarithm
# Could rewrite program as follows:
#    Replace "rootFactorsIn()" and "smallestProduct()" with:
#    (My adaptation of Project Euler recommendation)


# def smallestProductIntsTo(target):
#     import math
#     targetSqrt = math.sqrt(target)
#     primeFactors = primesUpTo(target)
#     number = 1

#     for x in primeFactors:
#         if x <= targetSqrt:
#             x = x ** math.floor(math.log(target) / math.log(x))
#         number = number * x

#     return number

# x = 20
# print(f"The smallest number evenly divisible by all integers 1 to {x}" \
#     f" is {smallestProductIntsTo(x)}.")
