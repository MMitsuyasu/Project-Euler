# Project Euler: Problem 1

## Multiples of 3 and 5:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# Solving with Python (3.8.1)

############################################################################

## Practice Work
# My test work to ensure I understand the results of each action:
# The modulo operator (%) returns the remainder.
# If the remainder is 0, then x is divisible by the number specified.
# By adding x and "total" and reassigning the sum to "total,"
# "total" becomes the sum of all the divisible numbers in the set.

# total = 0

# for x in range(1,1000):
#    if x % 3 == 0:
#        print("number is divisible by 3: %d" % x)
#        total = total + x
#        print("total is %d" % total)
#    else:
#       if x % 5 == 0:
#           print("number is divisible by 5: %d" % x)
#           total = total + x
#           print("total is %d" % total)


############################################################################
############################################################################

## Official Solution Used
# The problem only needs the answer
# Since I've ensured the logic (above), no need to print each valid number

total = 0

for x in range(1,1000):
    if x % 3 == 0:
        total = total + x
    else:
       if x % 5 == 0:
           total = total + x

print(total)


############################################################################
############################################################################

## Simpler Solution
# Didn't need to set the initial value of the set,
#    including 0 does not make a difference
# Could combine both conditions with an "or" statement
#    rather than nesting the second divisor
#    in a second "if" statement in "else"

#total = 0

#for x in range(10):
#    if x % 3 == 0 or x % 5 == 0:
#        total = total + x

#print(total)


############################################################################

## Lighter Solution
# Provided by Euler Project after solution
# Avoids having to process every number (good for very large range)
# Use concept of partial sums to simplify
# For reminders, see www.mathisfun.com/algebra/partial-sums.html

# Use partial sum properties: sigma k=1 to m of k = (m(m+1))/2
#                                             or  = m/2 * (m+1)
# Floor (w/o remainder) of target / n == number of factors of n below target
#    E.g. 20//3 == 6   (3, 6, 9, 12, 15, 18)   3(1, 2, 3, 4, 5, 6)
# When summing a series multiplied by a constant, can sum series & then multiply
#    E.g. sigma k=1 to 4 of 3k = 3(1)+3(2)+3(3)+3(4) = 3(1+2+3+4) = 3(10)
# So
#    target // n = m
#    sigma k=1 to m of nk = n * sigma k = n * (m(m+1)/2

# Problem wants the sum of numbers divisble by 3 and numbers divisible by 5
# Calculate sum of those divisible by 3 and 5 separately
# Add the two sums together
# Numbers divisible by both (factors of 15) would be calculated twice
#    would be in sum of both sets
# Calculate the sum of those numbers and subtract once to correct
    

#target = 9

#def SumDivisibleBy(n):
#    p = target // n
#    return n * (p*(p+1)) // 2

#print(SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15))
