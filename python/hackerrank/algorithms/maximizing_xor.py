#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# INT L
# INT R
# return INT
def maximizingXor(L, R):
    answers = [
        i ^ j   # xor
        for i in range(L, R)
        for j in range(i+1, R+1)
    ]
    print("#A", answers)
    return max(answers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingXor(l, r)
    fptr.write(str(result) + '\n')
    fptr.close()

