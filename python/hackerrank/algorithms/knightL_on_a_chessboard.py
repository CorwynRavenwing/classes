#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def knightMoves(n, initial, ij):
    (x, y) = initial
    (i, j) = ij
    moves = (
        (i, j), (-i, j), (i, -j), (-i, -j),
        (j, i), (-j, i), (j, -i), (-j, -i),
    )
    destinations = [
        (x + h, y + v)
        for (h, v) in moves
    ]
    legal_moves = [
        (a, b)
        for (a, b) in destinations
        if 0 <= a < n and 0 <= b < n
    ]
    return legal_moves

def knightMovesGroup(n, points, ij):
    retval = [
        knightMoves(n, initial, ij)
        for initial in points
    ]
    # flatten
    retval = [
        point
        for points in retval
        for point in points
    ]
    return tuple(set(retval))

def knightMovesDistance(n, ij):
    print("#kMD()", n, ij)
    initial = (0, 0)
    final = (n-1, n-1)
    seen = set(initial)
    current = [initial]
    distance = 0
    while True:
        print("#C", distance, len(current), current)
        if final in current:
            print("#FINAL")
            return distance
        distance += 1
        current = knightMovesGroup(n, current, ij)
        print("#CURR", current)
        current = [
            point
            for point in current
            if point not in seen
        ]
        seen = seen.union(set(current))
        if len(current) == 0:
            print("#IMPOSSIBLE")
            return -1
    pass

# INTEGER n
# return INT[][]
def knightlOnAChessboard(n):
    print("#kOAC()", n)
    answers = [
        [
            knightMovesDistance(n, (i, j))
            for j in range(1, n)
        ]
        for i in range(1, n)
    ]
    # print("#ANS", answers)
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = knightlOnAChessboard(n)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()

