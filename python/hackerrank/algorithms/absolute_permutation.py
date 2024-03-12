#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def checkAbsolutePerm(P, k):
    for i_0, p in enumerate(P):
        i = i_0 + 1
        if abs(p - i) != k:
            # print("#P", k, P, "NO", i, abs(p - i))
            return False
    print("#P", k, P, "YES")
    return True

# INT n
# INT k
# return INT[]
def absolutePermutation(n, k):
    print("#" + "=" * 60)
    print("#ap()", n, k)
    P0 = list(range(1, n+1))
    PlusMinus = [-1, +1]
    iPlusK = [
        i + k
        for i in P0
    ]
    iPlusK = [
        i if i in P0 else '-'
        for i in iPlusK
    ]
    iMinusK = [
        i - k
        for i in P0
    ]
    iMinusK = [
        i if i in P0 else '-'
        for i in iMinusK
    ]
    # print("#P", P0)
    # print("#I+K", iPlusK)
    # print("#I-K", iMinusK)
    iBothK = zip(iPlusK, iMinusK)
    iNeitherK = [
        x
        for x in iBothK
        if x == ['-', '-']
        # if x[0] == '-' and x[1] == '-'
    ]
    if len(iNeitherK) > 0:
        print("#I*K", list(iNeitherK)[0])
        return [-1]
    Left = []
    Right = P0
    initial = (Left, Right)
    options = [initial]
    prev_i = None
    while len(options) > 0:
        o = options[0]
        options = options[1:]
        (Left, Right) = o
        i = len(Left) + 1
        # print("#I", i)
        # print("#TRY", len(options), o)
        if prev_i != i:
            prev_i = i
            i0 = i - 1
            R = iPlusK[i0:] + iMinusK[i0:]
            R = [
                x
                for x in R
                if x != '-'
            ]
            R = set(R)
        # else, keep prior R
        if not set(Right).issubset(R):
            # print("#Right not subset of R")
            # print("#Right", set(Right))
            # print("#R", R)
            continue
        possibles = [
            i + (direction * k)
            for direction in PlusMinus
        ]
        possibles = [
            x
            for x in possibles
            if x in Right
        ]
        possibles = sorted(list(set(possibles)))
        for x in reversed(possibles):
            if x in Right:
                new_left = Left[:]
                new_left.append(x)
                new_right = Right[:]
                new_right.remove(x)
                opt = (new_left, new_right)
                options = [opt] + options
                # print("#add", opt)
            # else:
                # print("#dont", x, Right)
        if len(Right) == 0:
            if checkAbsolutePerm(Left, k):
                print("#answer", Left)
                return Left
            else:
                print("#nope")
                break
    print("#NOPE", len(options))
    return [-1]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        result = absolutePermutation(n, k)
        print(' '.join(map(str, result)))
        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')
    # fptr.close()

