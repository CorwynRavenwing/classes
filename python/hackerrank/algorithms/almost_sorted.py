#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

def isSorted(A):
    if A is None:
        return False
    B = sorted(A)
    return A == B

def sortedness(A):
    return ''.join([
        (
            's' if A[i+1] > A[i]
            else 'X' if A[i+1] < A[i]
            else 's'
            # equal items are also sorted
        )
        for i in range(len(A)-1)
    ])

def countX(S):
    T = [
        1
        for c in S
        if c == 'X'
    ]
    return len(T)

def countXGroups(S):
    T = S.split("s")
    print("#cXG", T)
    T = [
        e
        for e in T
        if e != ''
    ]
    print("#cXG", T)
    return len(T)

def testSort(S):
    S = S + 's'     # add a final 's' so search never fails
    X = countX(S)
    print("#X", X)
    if X == 0:
        return ('yes',)
    if X == 1:
        L = S.index('X')
        R = S.index('s', L)   # should be L+1
        print("#1: LR", L, R)
        return ('swap', L, R)
    if X == 2:
        L = S.index('X')      # first X
        N = S.index('X', L+1) # second X
        R = S.index('s', N)   # should be N+1
        return ('swap', L, R)
    # else
    XG = countXGroups(S)
    print("#XG", XG)
    if XG == 1:
        L = S.index('X')      # beginning of X group
        R = S.index('s', L)   # end of X group
        return ('reverse', L, R)
    return ('no',)

def doSwap(arr, L, R):
    arr = arr[:L] + [arr[R]] + arr[L+1:R] + [arr[L]] + arr[R+1:]
    return arr

def doReverse(arr, L, R):
    arr = arr[:L] + list(reversed(arr[L:R+1])) + arr[R+1:]
    return arr

# INT[] arr
# return VOID
def almostSorted(arr):
    if isSorted(arr):
        print("yes")
        return
    S = sortedness(arr)
    print("#S", S)
    T = testSort(S)
    print("#T:'", T)
    action = T[0]
    if action in ['yes', 'no']:
        print(action)
        return
    print("#T len:", len(T))
    (L, R) = T[1:]
    if action == 'swap':
        arr = doSwap(arr, L, R)
        print("#?", arr)
        if isSorted(arr):
            print("yes\n{} {} {}".format(action, L+1, R+1))
        else:
            print("no")
        return
    if action == 'reverse':
        arr = doReverse(arr, L, R)
        print("#?", arr)
        if isSorted(arr):
            print("yes\n{} {} {}".format(action, L+1, R+1))
        else:
            print("no")
        return
    print("no")
    return

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)

