#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# does not return '1' among the factors
def primeFactors(n):
    # print("#pF()", n)
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            print("#F", i)
            factors.append(i)
            n //= i
        i += 1
        if i > n:
            break
    return factors

def reachable_games(G):
    answer = [
        sorted(G[:column] + tuple([new_val]) + G[column+1:])
        for column in range(len(G))
        for new_val in range(G[column])
    ]
    # answer = [
    #     tuple([
    #         c
    #         for c in game
    #         if c != 0
    #     ])
    #     for game in answer
    # ]
    answer = [
        tuple(game)
        for game in answer
    ]
    return answer

# g = (2, 1, 3)
# print("#RG", g, reachable_games(g))
# g = (5,)
# print("#RG", g, reachable_games(g))

# returns each game reachable from this one
# in any number of moves, sorted by points
# and then number of columns
def all_lesser_games(G):
    answer = set()
    current = [G]
    while current != []:
        current = [
            reachable_games(g)
            for g in current
        ]
        # flatten
        current = [
            g
            for group in current
            for g in group
        ]
        current_set = set(current)
        answer = answer.union(current_set)
        current = list(current_set)
    answer = list(answer)
    answer.sort(key=lambda x: (sum(x), len(x)))
    return answer

# g = (3, 1, 2)
# print("#ALG()", g, all_lesser_games(g))

def tB_data(G):
    # print("#tB_data()", G)
    if G == ():
        print("#FALSE", G)
        return False
    reachable = reachable_games(G)
    # print("#tB_data reachable", reachable)
    results = [
        tB_cache(r)
        for r in reachable
    ]
    # print("#tB_data results", results)
    falses = [
        r
        for r in results
        if not r
    ]
    # print("#tB_data falses", falses)
    if len(falses) > 0:
        print("#TRUE", G)
        return True
    else:
        print("#FALSE", G)
        return False

cache = {}

def tB_cache(G):
    global cache
    if G not in cache:
        return None
    return cache[G]

def tB(G):
    global cache
    if G not in cache:
        lesser = all_lesser_games(G)
        for game in lesser:
            if game not in cache:
                cache[game] = tB_data(game)
                print("#-", game, cache[game])
        answer = tB_data(G)
        cache[G] = answer
        print("#+", G, cache[G])
    return cache[G]

# INT n, number of towers
# INT m, height of each tower
# return INT
def towerBreakers(n, m):
    print("#towerBreakers()", n, m)
    pf = primeFactors(m)
    # print("#primeFactors", pf)
    game = tuple([
        len(pf)
        for i in range(n)
        if pf != []
    ])
    print("#Game", game)
    players = {True: 1, False: 2, None: 'WRITE ME'}
    player_one_wins = tB(game)
    print("#player 1 wins:", player_one_wins)
    return players[player_one_wins]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = towerBreakers(n, m)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

