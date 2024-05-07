#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from itertools import combinations

def checkNonDivisible(k, arr):
    # print("#cND()", k, len(arr))
    count_non_divisible = len([
        x
        for x in arr
        if x % k != 0
    ])
    if count_non_divisible == 0:
        # print("#BAD")
        return False
    pairs = combinations(arr, 2)
    for pair in pairs:
        total = sum(pair)
        divisible = total % k == 0
        # print("#pair", pair, total, divisible)
        if divisible:
            return False
    return True

def nonDivisibleSubset(k, s):
    s = [
        item % k
        for item in s
    ]
    if checkNonDivisible(k, s):
        print("#WIN", s)
        return len(s)
    for L in range(len(s), 0, -1):
        subsets = combinations(s, L)
        print(f"#Checking {subsets} subsets:")
        # print("#Checking {} subsets:".format(len(subsets)))
        for ss in subsets:
            if checkNonDivisible(k, ss):
                print("#FIND", ss)
                print("#CHECK", L, len(ss))
                return len(ss)
    print("#NOPE")
    return None

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

