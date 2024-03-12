#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# A B C -> B C A
def rotateArrayAt(i, A):
    if A is None:
        return None
    # print("#rotateArrayAt()     ", i, "-", "\t", A)
    # print("#I", i, i+3, len(A))
    if i+3 > len(A):
        return None
    left = A[:i]        # everything before I
    pivot = [A[i]]      # I itself
    mid = A[i+1:i+3]    # I+1 and I+2
    right =A[i+3:]      # I+3 and everything after
    # print("#split", left, pivot, mid, right)
    A = left + mid + pivot + right
    return A

# A B C -> C A B
def rotateArrayBackwardAt(i, A):
    if A is None:
        return None
    # print("#rotateArrayBackardAt", i, "-", "\t", A)
    # print("#I", i, i+3, len(A))
    if i+3 > len(A):
        return None
    left = A[:i]        # everything before I
    mid = A[i:i+2]      # I and I+1
    pivot = [A[i+2]]    # I+2 itself
    right =A[i+3:]      # I+3 and everything after
    # print("#split", left, mid, pivot, right)
    A = left + pivot + mid + right
    return A

# moves thing J to location I and moves I..J-1 forward by one
# but uses rotateArrayAt if distance < 3
# and can only teleport between pairs of even or odd indices
def rotateArrayBetween(i, j, A):
    if A is None:
        return None
    # print("#rotateArrayBetween()", i, j, "\t", A)
    if i+3 > len(A):
        return None
    diff = j - i
    if diff == 0:
        # print("#\t\t", "return A\t", A)
        return A
    if diff == 1:
        A = rotateArrayAt(i, A)
        # print("#\t\t", "return B\t", A)
        return A
    if diff == 2:
        A = rotateArrayBackwardAt(i, A)
        # print("#\t\t", "return C\t", A)
        return A
    if diff % 2 == 1:
        pivot = i+1
        A = rotateArrayBetween(pivot, j, A)
        A = rotateArrayAt(i, A)
        # print("#\t\t", "return D\t", A)
        return A
    left = A[:i]        # everything before I
    mid = A[i:j]        # I and everything before J
    pivot = [A[j]]      # J itself
    right =A[j+1:]      # J+1 and everything after
    # print("#split", left, mid, pivot, right)
    A = left + pivot + mid + right
    # print("#\t\t", "return E\t", A)
    return A

def isSorted(A):
    if A is None:
        return False
    B = sorted(A)
    return A == B

# INT[] A
# return BOOL
def larryA(A):
    # print("#" + "-" * 40)
    for i in range(len(A)):
        looping = True
        while looping:
            # might need to run each pivot multiple times
            # print("#A", i, A)
            if isSorted(A):
                # print("#SUCCESS 1", i)
                return True
            Right = A[i:]
            minR = min(Right)
            minI = A.index(minR, i)
            # print("#?  ", [i], minR, [minI])
            if i == minI:
                looping = False
                # print("#    OK")
                continue
            pivotI = max(i, minI - 2)
            B = rotateArrayBackwardAt(pivotI, A)
            if B is None:
                looping = False
                # print("#    BAD")
                continue
            A = B
    # print("#A", 0, A)
    if isSorted(A):
        # print("#SUCCESS 2")
        return True
    # print("#FAIL")
    return False

# INT[] A
# return BOOL
def larryB(A):
    # print("#" + "-" * 40)
    for i in range(len(A)):
        if isSorted(A):
            # print("#SUCCESS 1", i)
            return True
        Right = A[i:]
        minR = min(Right)
        minI = A.index(minR, i)
        # print("#A", i, A)
        # print("#?  ", [i], minR, [minI])
        if i == minI:
            # print("#    OK")
            continue
        B = rotateArrayBetween(i, minI, A)
        if B is None:
            # print("#    BAD")
            continue
        A = B
    # print("#A", 0, A)
    if isSorted(A):
        # print("#SUCCESS 2")
        return True
    # print("#FAIL")
    return False

# INT[] A
# return STRING
def larrysArray(A):
    # print("#" + "=" * 50)
    answer_A = larryA(A)
    answer_B = larryB(A)
    if answer_A != answer_B:
        print("DIFFERENT!", answer_A, answer_B)
        exit()
    return 'YES' if answer_A else 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

