#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def nextMove(pos):
    (x, y) = pos
    moves = [
        (x - 2, y + 1),
        (x - 2, y - 1),
        (x + 1, y - 2),
        (x - 1, y - 2),
    ]
    moves = [
        (x, y)
        for (x, y) in moves
        if 1 <= x <= 15
        if 1 <= y <= 15
    ]
    return moves

def reachable(pos):
    # print("#reachable()", pos)
    answer = []
    current = [pos]
    while len(current) > 0:
        current = [
            nextMove(c)
            for c in current
        ]
        # flatten
        current = [
            c
            for group in current
            for c in group
        ]
        # uniq
        current = sorted(list(set(current)))
        # move repeated items to front of 'answer'
        answer = [
            a
            for a in answer
            if a not in current
        ]
        # sorted in this order
        answer = current + answer
        # print("#C", current)
    # print("#A", answer)
    return answer

def cbg_data(pos):
    # print("#cbg_data()", pos)
    moves = nextMove(pos)
    # print("#M", moves)
    answers = [
        cbg_cache(m)
        for m in moves
    ]
    # print("#A", answers)
    if answers == []:
        # print("#FALSE", pos)
        return False
    falses = [
        a
        for a in answers
        if not a
    ]
    # print("#F", falses)
    if len(falses) > 0:
        # print("#TRUE", pos)
        return True
    else:
        # print("#FALSE", pos)
        return False

cache = {}

def cbg_cache(pos):
    if pos not in cache:
        # print("ERROR: pos not in cache", pos)
        return None
    return cache[pos]

def cbg(pos):
    global cache
    if pos not in cache:
        R = reachable(pos)
        for p in R:
            cache[p] = cbg_data(p)
        cache[pos] = cbg_data(pos)
    return cache[pos]

# INT x
# INT y
# return STRING
def chessboardGame(x, y):
    players = {True: 'First', False: 'Second', None: 'WRITE ME'}
    pos = (x, y)
    return players[cbg(pos)]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        x = int(first_multiple_input[0])
        y = int(first_multiple_input[1])
        result = chessboardGame(x, y)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

