#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

def n_pick_2(N):
    # N pick K === (N!) / (K!)(N-K)!
    # in the case K=2:
    # N pick 2 === (N!) / 2!(N-2)!
    # === (N)(N-1)(N-2)(N-3)..(2)(1)/2(N-2)(N-3)..(2)(1)
    # === (N)(N-1)/2
    return N * (N-1) // 2
    # either N or N-1 will be even,
    # therefore N*(N-1) will be even,
    # therefore integer division by 2 is OK here

# STR s
# return INT
def sherlockAndAnagrams(s):
    master_count = Counter()
    for i in range(len(s)):
        for j in range(i, len(s)):
            # print("#ss", s[i:j+1])
            local_count = Counter(s[i:j+1])
            local_count = [
                e+str(count) if count > 1 else e
                for e, count in local_count.items()
            ]
            local_count.sort()
            count_key = ''.join(local_count)
            # print("#count", i, j, count_key)
            master_count[count_key] += 1
    master_count = dict([
        (e, count)
        for e, count in master_count.items()
        if count > 1
    ])
    print("#Master", master_count)
    
    for k in range(2, 6):
        print("#N pick 2:", k, n_pick_2(k))
    
    answer = 0
    for key, count in master_count.items():
        if count == 2:
            answer += 1
        else:
            answer += n_pick_2(count)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()

