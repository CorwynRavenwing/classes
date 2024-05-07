#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

def nonDivisibleSubset(k, s):
    print(f"#NDS({k},{s})")
    forbid = list([
        (i, (k-i) % k)
        for i in range(k)
    ])
    print(f"#{forbid=}")
    forbid = list([
        (a, b)
        for (a, b) in forbid
        if a <= b
    ])
    print(f"#{forbid=}")
    modulos = list([
        val % k
        for val in s
    ])
    print(f"#{modulos=}")
    countM = Counter(modulos)
    print(f"#{countM=}")
    maxLen = 0
    for A in range(k):
        B = (k - A) % k
        if A > B:
            print(f"#  ({A},{B}) skip")
            continue
        countA = countM[A]
        countB = countM[B]
        print(f"#  ({A},{B}) = [{countA},{countB}]")
        M = max(countA, countB)
        if M:
            if A == B:
                print(f"#    DUP, use {1}")
                maxLen += 1
            else:
                print(f"#    use {M}")
                maxLen += M
        else:
            print("#    neither available")
    
    return maxLen

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

