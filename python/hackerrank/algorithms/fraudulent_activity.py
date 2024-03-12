#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def median(H):
    # print("#median()", H)
    H = sorted(H)
    # print("#sorted", H)
    L = len(H)
    M = L // 2
    if L % 2 == 0:
        # even size: average middle two
        answer = sum(H[M-1:M+1]) / 2
        # print("#even", L, [M-1, M], H[M-1:M+1], answer)
    else:
        # odd size: return middle one
        answer = H[M]
        # print("#odd", L, [M], H[M], answer)
    return answer

# INT[] expenditure
# INT d
# return INT
def activityNotifications(expenditure, d):
    warnings = 0
    for i in range(d, len(expenditure)):
        H = expenditure[i-d:i]
        M = median(H)
        E = expenditure[i]
        # print("#?", E, M, H)
        if (E >= 2 * M):
            warnings += 1
            print("#warning", i)
    return warnings

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

