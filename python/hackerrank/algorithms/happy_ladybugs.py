#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

# STRING b
# return STRING
def happyLadybugs(b):
    bugs = Counter()
    for color in b:
        bugs[color] += 1
    currently_not_okay = [
        color
        for i, color in enumerate(b)
        if (
            i <= 0 or color != b[i-1]
        ) and (
            i >= len(b)-1 or color != b[i+1]
        )
    ]
    print("#CNO", currently_not_okay)
    problems = [
        color
        for color, count in bugs.items()
        if (
            # singletons that aren't blanks
            count == 1 and color != '_'
        )
    ]
    if bugs['_'] == 0:
        # lack of blank spaces at all
        if len(currently_not_okay):
            # no blank spaces only a problem
            # if not already in right places
            problems.append('_')
    print("#P", problems)
    return "YES" if len(problems) == 0 else "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

