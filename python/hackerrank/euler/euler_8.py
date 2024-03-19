#!/bin/python3

# import sys
from typing import List

def multiply_list(L: List[int]):
    if 0 in L:
        return 0
    retval = 1
    for d in L:
        retval *= d
    return retval

def euler_8(num: str, k: int):
    # print("#euler_8()", num, k)
    numL = list(map(int, list(num)))
    M = []
    for i in range(len(num) - k + 1):
        digits = numL[i:i+k]
        mul = multiply_list(digits)
        # print("#i", i, digits, mul)
        M.append(mul)
    # print("#answers", M)
    return max(M)

t = int(input().strip())
for a0 in range(t):
    n0, k0 = input().strip().split(' ')
    n, k = [int(n0), int(k0)]
    num = input().strip()
    print(euler_8(num, k))

