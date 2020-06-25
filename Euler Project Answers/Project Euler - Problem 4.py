# Project Euler: Problem 4

## Largest Palindrom Product:
# A palindromic number reads the same both ways.
# The largest palendrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Solving with Python (3.8.1)

############################################################################

# Practice Work

##def checkPal(value):
##    value = str(value)
##    palLength = len(value) // 2
##    match = 0
##    check = 0
##
##    while match < palLength and value[check] == value[-check - 1]:
##        match = match + 1
##        check = check + 1
##
##    palStatus = match == palLength
##    return palStatus


##def isPal(value):
##    if str(value) == "".join(reversed(str(value))):
##        return True
##    else:
##        return False
##
##
##w = 642
##print(isPal(w))
##p = 590095
##print(isPal(p))



## Generate palindrome first and check for factors
# Products of two 3-digit factors:
#    100 x 100 =  10,000
#    999 x 999 = 998,001
# Need to test palindromes between 10000 and 998001



############################################################################
############################################################################

## Official Solution Used

found = False

# Generate and test 6-digit palindromes
for a in range(9, 0, -1):
    for b in range(9, -1, -1):
        for c in range(9, -1, -1):
            # Set largest palindrome under 998001 (max product)
            if a == 9 and b == 9 and c < 8: continue
            
            prep = [str(a), str(b), str(c), str(c), str(b), str(a)]
            pal = int("".join(prep))
            
            # Check if palindrome is product of two 3-digit factors
            x = 999
            while x >= 100:
                if pal % x == 0 and len(str(int(pal / x))) == 3:
                    found = True
                    break
                x = x - 1
                
            # Stop generating palindromes once answer is identified
            if found: break
        if found: break
    if found: break


# Generate and test 5-digit palindromes
# (only if answer has not been identified)
if found == False:
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                
                prep = [str(a), str(b), str(c), str(b), str(a)]
                pal = int("".join(prep))
                
                # Check if palindrome is product of two 3-digit factors
                x = 999
                while x >= 100:
                    if pal % x == 0 and len(str(int(pal / x))) == 3:
                        found = True
                        break
                    x = x - 1
                    
                # Stop generating palindromes once answer is identified
                if found: break
            if found: break
        if found: break


print(f"The largest palindromic product of two 3-digit factors is {pal}." \
      f"\nIt is the product of {x} and {int(pal / x)}.")


############################################################################
############################################################################

## Optimized Solution Notes
