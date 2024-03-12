#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# timeout exceeded: tests 7 - 10

# returns binary digits, reversed,
# i.e. 12 -> [0, 0, 1, 1]
def binaryArray(n):
    N_binary = []
    while True:
        N_binary.append(n % 2)
        n //= 2
        if n == 0:
            break
    return N_binary

# LONG n
# return LONG
def sumXor(n):

    # matches = 0
    # for i in range(n+1):
    #     if (n + i) == (n ^ i):
    #         print("#m", i, '/', n, round(i * 100 / n), '%')
    #         matches += 1
    # # print("#M", match)
    # return matches

    # match = [
    #     1
    #     for i in range(n+1)
    #     if (n + i) == (n ^ i)
    # ]
    # # print("#M", match)
    # return len(match)

    # both of these work, but they time out

    # shortcut #1:
    # '(n + i) == (n ^ i)'
    # ===
    # 'N and I share no 1 digits in binary'

    # shortcut #2:
    # 'all numbers < N like that'
    # ===
    # 'all numbers whose binary representation
    # has ones only where N has zeroes'
    # ===
    # 'all numbers that can be composed by
    # adding 2^Xi for some subset of Xs
    # being that list of zeros in N

    # shortcut #3:
    # 'the *count* of numbers like that'
    # ===
    # '2 ^ (count of zeros in N)'

    # shortcut #4:
    # if N is a power of 2,
    # the number of ones in N will be 1
    # and the answer will be N itself.
    # if N is zero,
    # the number of ones in N will be 0
    # and the answer will be 1
    # (the length of [0], just zero itself)

    N_binary = binaryArray(n)
    zeros = len([
        d
        for d in N_binary
        if d == 0
    ])
    ones = len(N_binary) - zeros
    if ones == 1:
        return n
    elif ones == 0:
        return 1
    else:
        return 2 ** zeros
    pass

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = sumXor(n)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

