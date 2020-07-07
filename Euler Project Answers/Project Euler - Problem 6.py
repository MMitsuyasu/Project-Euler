# Project Euler: Problem 6

## Sum Square Difference
# The sum of the squares of the first ten natural numbers is,
#        1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#        (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is
#        3025 - 385 = 2640
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.


# Solving with Python (3.8.1)

############################################################################

## Practice Work

# Because (1+2+3+...)^2 = (1^3 + 2^3 + 3^3 + ...)
# Then (1+2+3+...)^2 increases by x^3 each time.

# Also (1^2 + 2^2 + 3^2 + ...) increases by x^2 each time

# Therefore, the difference between (1+2+3+...)^2 and (1^2 + 2^2 + 3^2 +...)
# increases by (x^3 - x^2) each time.

# Thus, for any number x
# The difference can be found by iterating (x^3 - x^2)
# and adding to the previous result from 1 to x.



## Proof (1+2+3+...)^2 = (1^3 + 2^3 + 3^3 + ...)
# Note:
#    When multiplying, write the smaller number as coefficient,
#    and write squares as x(x).

# (1+2)^2
# (1+2)(1+2)
# 1(1) + 1(2) + 1(2) + 2(2)
# 1(1) + 4(2)
# 1 + 2(2)(2)
# 1^x + 2^3

# (1+2+3)^2
# (1+2+3)(1+2+3)
# 1(1) + 1(2) + 1(3) + 1(2) + 2(2) + 2(3) + 1(3) + 2(3) + 3(3)
# 1(1) + 1(2) + 1(2) + 2(2) + 1(3) + 2(3) + 1(3) + 2(3) + 3(3)
# 1(1) + 4(2) + 9(3)
# 1 + 2(2)(2) + (3)(3)(3)
# 1^x + 2^3 + 3^3

# (1+2+3+4)^2
# (1+2+3+4)(1+2+3+4)
# 1(1) + 1(2) + 1(3) + 1(4) + 1(2) + 2(2) + 2(3) + 2(4)
#         + 1(3) + 2(3) + 3(3) + 3(4) + 1(4) + 2(4) + 3(4) + 4(4)
# 1(1) + 1(2) + 1(2) + 2(2) + 1(3) + 2(3) + 1(3) + 2(3)
#         + 3(3) + 1(4) + 2(4) + 3(4) + 1(4) + 2(4) + 3(4) + 4(4)
# 1(1) + 4(2) + 9(3) + 16(4)
# 1 + 2(2)(2) + 3(3)(3) + 4(4)(4)
# 1^x + 2^3 + 3^3 + 4^3



############################################################################
############################################################################

# Official Solution Used

def sqSumLessSumSq(stop):
    difference = 0
    for x in range(1, stop+1):
        increment = x**3 - x**2
        difference = difference + increment
    return difference

x = 100
print(f"The sum of integers 1 to {x} squared \n" \
      "minus \n" \
      f"The sum of the squares of integers 1 to {x} \n" \
      "is \n" \
      f"{sqSumLessSumSq(x)}.")




############################################################################
############################################################################

## Optimized Solution Notes

# See official Project Euler "overview" explanation:
#    <webaddress>

