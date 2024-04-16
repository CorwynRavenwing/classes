#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

def count_times_found(S, t):
    if S not in t:
        return 0
    count = 0
    index = -1
    while index is not None:
        try:
            index = t.index(S, index+1)
            count += 1
        except ValueError:
            index = None
    return count

# The function is expected to return an INTEGER.
# The function accepts STRING t as parameter.
def maxValue(t):
    answers = []
    retval = 0
    for i in range(len(t)):
        max_len = len(t) - i
        print(f"# {i=} {max_len=}")
        for j in range(i+1, len(t)+1):
            S = t[i:j]
            if S in answers:
                continue
            count = count_times_found(S, t)
            if max_len * count <= retval:
                # print(f"##### {max_len} * {count} <= {retval}")
                # break J, next I
                break
            if count > 1 and len(S) <= 10:
                answers.append(S)
            retval = max(retval, len(S) * count)
            # print(f"#{i,j} '{S[:20]}' len={len(S)}/{max_len} {count=} {retval}")
    return retval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = input()
    result = maxValue(t)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

