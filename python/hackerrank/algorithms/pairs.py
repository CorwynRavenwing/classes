#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# this project is basically the same as
# the other one that is timing out
# due to combinatorial explosion

# UPDATE: look in list for x+k instead of
# checking each x-y for equality to k

# UPDATE: use set intersection instead of manual comparison

# return INT
# INT k
# INT[] arr
def pairs(k, arr):
    # answer = 0
    # L = len(arr)
    # for i in range(L):
    #     x = arr[i]
    #     for j in range(i+1, L):
    #         y = arr[j]
    #         if abs(x - y) == k:
    #             answer += 1

    # for x in arr:
    #     if (x + k) in arr:
    #         answer += 1

    # return answer
    
    # target = [
    #     x + k
    #     for x in arr
    # ]
    # answer = [
    #     t
    #     for t in target
    #     if t in arr
    # ]
    # return len(answer)
    
    sArr = set(arr)
    sTarget = set([
        x + k
        for x in arr
    ])
    sAnswer = sArr & sTarget  # intersection
    
    return len(sAnswer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()

