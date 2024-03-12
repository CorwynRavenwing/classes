#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

# INT[] A
# INT[] B
# return INT
def beautifulPairs(A, B):
    aC = Counter(A)
    bC = Counter(B)
    # print("#aC", aC)
    # print("#bC", bC)
    answer = 0
    for e, aCount in aC.items():
        bCount = bC[e]
        minCount = min(aCount, bCount)
        if minCount > 0:
            answer += minCount
            aC[e] -= minCount
            bC[e] -= minCount
    print("#ans", answer)
    # print("#aC", aC)
    # print("#bC", bC)
    aLeft = [
        e
        for e, count in aC.items()
        if count > 0
    ]
    bLeft = [
        e
        for e, count in bC.items()
        if count > 0
    ]
    print("#LEFT", aLeft, bLeft)
    if len(aLeft) > 0 and len(bLeft) > 0:
        answer += 1
    elif len(bLeft) == 0:
        answer -= 1
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    result = beautifulPairs(A, B)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

