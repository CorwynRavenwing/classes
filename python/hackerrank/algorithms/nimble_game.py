#!/bin/python3

# import math
import os
# import random
# import re
# import sys

cache = {}

def reachable(G):
    # move 1 coin from i to j, 0 <= j < i
    L = len(G)
    retval = [
        tuple([
            (
                G[j]+1
                if col == j
                else G[i]-1
                if col == i
                else e
            )
            for col, e in enumerate(G)
        ])
        for i in range(1, L)
        for j in range(i)
        if G[i] > 0
    ]
    return retval

# g = (0, 1, 2, 0, 1)
# print("#reachable(g)", g, reachable(g))

def nimble_easy(G):
    G1 = G[1:]
    if sum(G1) == 0:
        nimble_set_cache(G, False)
        return False
    odds = len([
        e
        for e in G1
        if e % 2 == 1
    ])
    # print("#odd", odds)
    if odds == 0:
        # this was the example they gave us:
        # copy the other player's moves
        # and they will run out of coins
        nimble_set_cache(G, False)
        return False
    # otherwise, not "easy": return cached answer
    return nimble_cache(G)

def nimble_data(G):
    E = nimble_easy(G)
    if E is not None:
        return E
    R = reachable(G)
    # print("#reachable", R)
    answers = [
        nimble_easy(r)
        for r in R
    ]
    # print("#answers", answers)
    falses = [
        a
        for a in answers
        if not a
    ]
    if len(falses) > 0:
        # any winning position is reachable
        return True
    nones = [
        a
        for a in answers
        if a is None
    ]
    if len(nones) == 0:
        # all answers were 'easy' or in cache
        return False
    # get detailed answers that failed the 'easy' test
    hard = [
        r
        for r in R
        if nimble_easy(r) is None
    ]
    # print("#recursion", hard)
    answers = [
        nimble(h)
        for h in hard
    ]
    falses = [
        a
        for a in answers
        if not a
    ]
    if len(falses) > 0:
        # any winning position is reachable
        return True
    nones = [
        a
        for a in answers
        if a is None
    ]
    if len(nones) == 0:
        # all answers were 'easy' or in cache
        return False
    print("#ERROR: recursion returned None", zip(hard, answers))
    return None

def nimble_cache(G):
    global cache
    if G not in cache:
        return None
    return cache[G]

def nimble_set_cache(G, answer):
    cache[G] = answer
    return

def nimble(G):
    global cache
    if G not in cache:
        # print("#checking game", G)
        nimble_set_cache(G, nimble_data(G))
        pass
    return cache[G]

# INT[] s
# return STRING
def nimbleGame(s):
    s = tuple(s)
    # print("#nimbleGame()", s)
    players = {True: 'First', False: 'Second', None: 'WRITE ME'}
    answer = nimble(s)
    return players[answer]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        s = list(map(int, input().rstrip().split()))
        result = nimbleGame(s)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

