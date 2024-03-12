#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# return INTEGER[]
# INTEGER[] arr
def countingSort(arr):
    freq = [0] * 100
    # print(freq)
    for e in arr:
        freq[e] += 1
    result = [
        n
        for n, count in enumerate(freq)
        for i in range(count)
    ]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

