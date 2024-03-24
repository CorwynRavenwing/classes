#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# INT[] arr
# return INT[]
def same_sign(A, B):
    (A_neg, A_pos) = (A <= 0, A >= 0)
    (B_neg, B_pos) = (B <= 0, B >= 0)
    return (A_neg and B_neg) or (A_pos and B_pos)

def maxSubarray(arr):
    not_none = lambda x: x is not None
    # section 1: maximum subsequence (pick any set)
    positive_values = [
        v
        for v in arr
        if v > 0
    ]
    if not len(positive_values):
        # if there are no positive values:
        # pick the largest (least negative) single value
        # and return it as both answers
        M = max(arr)
        return (M, M)
    
    max_subsequence = sum(positive_values)
    
    # section 2: maximum subarray (contiguous)
    print(f"#36 {arr[0:8]=}")
    changes = True
    while changes:
        changes = False
        for i in range(len(arr)-1):
            A = arr[i]
            B = arr[i+1]
            if same_sign(A, B):
                arr[i] = None
                arr[i+1] = A + B
                print(f"#{i} {(A, B)} -> {(arr[i], arr[i+1])}")
                changes = True
        if changes:
            print(f"#48 {arr[0:8]=}")
            arr = list(filter(not_none, arr))
            print(f"#55 {arr[0:8]=}")
    if arr[0] <= 0:
        print(f"#delete negative first element {arr[0]=}")
        del arr[0]
        print(f"#63 {arr[0:8]=}")
    if arr[-1] <= 0:
        print(f"#delete negative last element {arr[-1]=}")
        del arr[-1]
        print(f"#66 {arr[0:8]=}")
    window = 3
    changes = True
    while changes:
        print(f"#{window=} / {len(arr)}")
        changes = False
        for i in range(len(arr) - window + 1):
            ABC = arr[i:i+window]
            if len(ABC) != window:
                print(f"#len too small: {i=} {len(ABC)} {window}")
                break
            if None in ABC:
                print(f"#None {i=}")
                continue
            if sum(ABC) > max(ABC):
                # newval = [None] * (window - 1) + [sum(ABC)]
                newval = [sum(ABC)]
                print(f"#{sum(ABC)}>{max(ABC)}:")
                print(f"#:: {ABC[:8]}")
                print(f"#-> {newval[-8:]}")
                # arr[i:i+window] = newval
                arr = arr[:i] + newval + arr[i+window:]
                changes = True
        # if changes:
            print(f"#77 {arr[0:8]=}")
            # arr = list(filter(not_none, arr))
            # print(f"#84 {arr[0:8]=}")
        # else:
            # window += 2
            # if window < len(arr):
                # changes = True
    max_subarray = max(arr)
    return (max_subarray, max_subsequence)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = maxSubarray(arr)
        print(' '.join(map(str, result)))
        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')
    # fptr.close()

