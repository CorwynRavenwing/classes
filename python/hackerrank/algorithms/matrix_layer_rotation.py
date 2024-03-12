#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# INT[][] matrix
# return INT[][]
def unrollMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    unrolled = []
    for L in range(min(m, n) // 2):
        # print("#loop", L, "top", (L,), (L, n-L))
        this_row = matrix[L][L:n-L]
        # print("#loop", L, "right", (L+1, m-L-1), (n-L-1,))
        for j in range(L+1, m-L-1):
            this_row.append(matrix[j][n-L-1])
        # print("#loop", L, "bottom", (m-L-1,), (n-L, L))
        this_row += reversed(matrix[m-L-1][L:n-L])
        # print("#loop", L, "left", (m-L-1, L+1), (L,))
        for j in reversed(range(L+1, m-L-1)):
            this_row.append(matrix[j][L])
        # print("#row", this_row)
        unrolled.append(this_row)
    return unrolled

# INT[][] unrolled
# INT m
# INT n
# return INT[][]
def rollMatrix(unrolled, m, n):
    inner = []
    for L, block in reversed(list(enumerate(unrolled))):
        # print("#dealing with block", L, block)
        width = n - 2*L
        height = m - 2*L - 2
        TR = 0 + width
        BR = TR + height
        BL = BR + width
        TL = BL + height
        top = block[0:TR]
        right = block[TR:BR]
        bottom = list(reversed(block[BR:BL]))
        left = list(reversed(block[BL:TL]))
        sides = list(zip(left, right))
        # print("#broken", top, bottom, sides)
        outer = []
        outer.append(top)
        for i, side in enumerate(sides):
            row = [] if inner == [] else inner[i]
            (L, R) = side
            row = [L] + row + [R]
            outer.append(row)
        outer.append(bottom)
        inner = outer[:]
    return outer

def rotateArray(row, r):
    # print("#rotateArray()", row, r)
    answer = row[r:] + row[:r]
    # print("#RA", answer)
    return answer

def rotateUnrolled(unrolled, r):
    # print("#rotateUnrolled()", r)
    answer = [
        rotateArray(row, r % len(row))
        for row in unrolled
    ]
    # print("#RU", answer)
    return answer

# INT[][] matrix
# INT r
# return VOID
def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    # print("#matrixRotation() M N R matrix", m, n, r, matrix)
    unrolled = unrollMatrix(matrix)
    # print("#unrolled", unrolled)
    check = rollMatrix(unrolled, m, n)
    # print("#check", check)
    if matrix != check:
        print("FAIL: roll(unroll(x)) != x")
    rotated = rotateUnrolled(unrolled, r)
    answer = rollMatrix(rotated, m, n)
    print('\n'.join([
        ' '.join(map(str, row))
        for row in answer
    ]))
    return

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    r = int(first_multiple_input[2])
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))
    matrixRotation(matrix, r)

