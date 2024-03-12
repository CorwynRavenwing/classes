#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# This question is identical to the one called
# "Running Time of Algorithms"
# ... and ironically runs out of running time

# INTEGER[] arr
# return INTEGER
def insertionSort(arr):
    # assumes each number only appears once
    # *** turns out not to be true
    print("#ARR", arr)
    arr_dict = dict()
    for i, e in enumerate(arr):
        arr_dict[e] = arr_dict.get(e, [])
        arr_dict[e].append(i)
    print("#DICT", arr_dict)
    sorted_arr = sorted(arr)
    print("#SORT", list(sorted_arr))
    sorted_dict = dict()
    for i, e in enumerate(sorted_arr):
        sorted_dict[e] = sorted_dict.get(e, [])
        sorted_dict[e].append(i)
    print("#SD", sorted_dict)
    diffs = []
    for e, L in arr_dict.items():
        for i in L:
            sde = sorted_dict[e][0]
            sorted_dict[e] = sorted_dict[e][1:]
            if sde > i:
                diffs.append(sde - i)
    print("#DIFFS", diffs)
    return sum(diffs)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = insertionSort(arr)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

