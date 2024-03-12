#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def NextMoves(pile):
    # print("#Next", pile)
    moves = [
        pile[:column] + tuple([i]) + pile[column+1:]
        for column, value in enumerate(pile)
        for i in range(value)
    ]
    moves = [
        tuple(sorted(p))
        for p in moves
    ]
    # print("#M", moves)
    return moves

def ReachableGames(pile):
    answer = set()
    current = [pile]
    while len(current) > 0:
        current = [
            NextMoves(g)
            for g in current
        ]
        # flatten
        current = [
            f
            for g in current
            for f in g
        ]
        # print("#SET", current)
        current_set = set(current)
        current = list(current_set)
        answer = answer.union(current_set)
    answer = list(answer)
    answer.sort(key=lambda x: sum(x))
    return answer

def nim_data(pile):
    if sum(pile) == 0:
        # print("#LOST", pile)
        return None
    # loser takes last stone, instead of loser has no stones to take
    if sum(pile) == 1:
        # print("#FALSE", pile)
        return False
    moves = NextMoves(pile)
    answers = [
        nim_cache(m)
        for m in moves
    ]
    falses = [
        a
        for a in answers
        if not a
    ]
    if len(falses) > 0:
        # print("#TRUE", pile)
        return True
    else:
        # print("#FALSE", pile)
        return False

cache = {}

def nim_cache(pile):
    global cache
    if pile not in cache:
        print("ERROR: pile not in cache", pile)
        return None
    return cache[pile]

def nim(pile):
    global cache
    if pile not in cache:
        all_reachable = ReachableGames(pile)
        for g in all_reachable:
            if g not in cache:
                cache[g] = nim_data(g)
        cache[pile] = nim_data(pile)
    return cache[pile]

# INT[] s
# return STRING
def misereNim(s):
    players = {True: 'First', False: 'Second', None: 'WRITE ME'}
    s = tuple(s)
    answer = nim(s)
    return players[answer]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        s = list(map(int, input().rstrip().split()))
        result = misereNim(s)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

