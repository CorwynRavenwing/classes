#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
def isValid(s):
    print("#iV()", s)
    F1 = Counter()
    for c in s:
        F1[c] += 1
    print("#F1", F1)
    F2 = Counter()
    V1 = F1.values()
    for f in V1:
        F2[f] += 1
    print("#F2", F2)
    MIN1 = min(V1)
    MAX1 = max(V1)
    print("#M,MAX1", MIN1, MAX1)

    if len(F2) == 1:
        print("#already valid without deletion")
        return 'YES'
    elif len(F2) > 2:
        print("#>1 different letter to delete")
        return 'NO'
    elif MIN1 == MAX1 - 1: 
        if F2[MAX1] == 1:
            print("#delete one copy of a letter")
            return 'YES'
    if MIN1 == 1:
        if F2[MIN1] == 1:
            print("#delete only copy of one letter")
            return 'YES'
    # else:
    print("#>1 letter to delete")
    return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()

