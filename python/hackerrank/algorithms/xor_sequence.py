#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def A_below_R(R):
    A = {}
    A[0] = 0
    # print("#A[{}]: {}".format(0, A[0]))
    for x in range(1, R+1):
        A[x] = A[x-1] ^ x
        # print("#A[{}]: {}".format(x, A[x]))
    return A

# Complete the xorSequence function below.
def xorSequence(L, R):
    A = A_below_R(R)
    ans = A[L]
    # print("#L", L, ans)
    for i in range(L+1, R+1):
        ans ^= A[i]
        # print("#I", i, ans)
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        lr = input().split()
        l = int(lr[0])
        r = int(lr[1])
        result = xorSequence(l, r)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

