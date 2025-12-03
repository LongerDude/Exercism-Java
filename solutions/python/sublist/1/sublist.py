"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(l1, l2):
    if l1 == l2:
        return EQUAL
    if l1 == [] and l1 != l2:
        return SUBLIST
    if l2 == [] and l1 != l2:
        return SUPERLIST
    if len(l1) > len(l2):
        n = len(l2)
        m = len(l1)
        for i in range(m - n + 1):
            if l1[i:i + n] == l2:
                return SUPERLIST
    if len(l1) < len(l2) : 
        n = len(l2)
        m = len(l1)
        for i in range(n - m + 1):
            if l2[i:i + m] == l1:
                return SUBLIST
    if l1 != l2:
        return UNEQUAL
    
        
    
 