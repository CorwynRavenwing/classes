#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STR s
# return INT
def stringSimilarity(s):
    answer = 0
    L = len(s)
    positions = range(0, L)
    for C in s:
        # print("#C", C)
        positions = [
            pos + 1
            for pos in positions
            if pos < L and s[pos] == C
        ]
        # print("#POS", C, positions)
        count = len(positions)
        answer += count
        if count == 0:
            break
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = stringSimilarity(s)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

