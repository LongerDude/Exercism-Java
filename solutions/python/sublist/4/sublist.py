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
    n = len(l2)
    m = len(l1)
    if m > n:
        for i in range(m - n + 1):   #looks for all possible starting positions to compare.
            if l1[i:i + n] == l2:    #checks current position in l1, uses slice operator to isolate same length of elements as l2, compares two lists.
                return SUPERLIST
    #able to merge superlist and sublist coniditionals, but keeping it this way for readabillity. 
    if m < n : 
        for i in range(n - m + 1):
            if l2[i:i + m] == l1:
                return SUBLIST
    return UNEQUAL
    
        
    
 