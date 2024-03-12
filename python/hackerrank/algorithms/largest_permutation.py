#!/bin/python3

# import math
import os
# import random
# import re
# import sys
''
# INT k
# INT[] arr
# return INT[]
def largestPermutation(k, arr):
    # print("#lP()", k, len(arr))
    L = len(arr)
    for i in range(L):
        maxA = max(arr[i:])
        this = arr[i]
        if this != maxA:
            maxI = arr.index(maxA, i)
            arr[maxI] = this
            arr[i] = maxA
            # print("#I", i, maxI, arr[:7], '...')
            k -= 1
            if k <= 0:
                break
        # else:
            # print("#M", i, i, maxA)
    return arr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(' '.join(map(str, result)))
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

