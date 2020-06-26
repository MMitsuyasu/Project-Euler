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
def primeFactors(target):
    import math
    workingTarget = target
    primeList = [1]

    # Checks for 2 as a factor
    if workingTarget % 2 == 0:
        primeList.append(2)
        while workingTarget % 2 == 0:
            workingTarget = workingTarget / 2

    # Checks for other prime factors
    maxFactor = math.sqrt(workingTarget)
    factor = 3

    while workingTarget > 1 and factor <= maxFactor:
        if workingTarget % factor == 0:
            primeList.append(factor)
            while workingTarget % factor == 0:
                workingTarget = workingTarget / factor
            maxFactor = math.sqrt(workingTarget)
        factor = factor + 2

    primeList.append(int(workingTarget))

    return primeList

print(primeFactors(688500))



############################################################################
############################################################################

# Official Solution Used


############################################################################
############################################################################

## Optimized Solution Notes

