# Project Euler: Problem 4

## Largest Palindrom Product:
# A palindromic number reads the same both ways.
# The largest palendrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Solving with Python (3.8.1)

############################################################################

# Practice Work

def checkPal(value):
    value = str(value)
    palLength = len(value) // 2
    match = 0
    check = 0

    while match < palLength and value[check] == value[-check - 1]:
        match = match + 1
        check = check + 1

    palStatus = match == palLength
    return palStatus


############################################################################
############################################################################

## Official Solution Used



############################################################################
############################################################################

## Optimized Solution Notes
