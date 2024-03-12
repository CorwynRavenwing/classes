#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def leaderboard_pos_b(ranked_nodups, score):
    low = 0
    if ranked_nodups[low] < score:
        return low+1
    high = len(ranked_nodups)-1
    rdh = ranked_nodups[high]
    if rdh != 0:
        print("Error: last value should be 0")
    while True:
        mid = (high + low) // 2
        print("#L,M,H", low, mid, high)
        mid_value = ranked_nodups[mid]
        print("#MID", mid_value)
        if low == mid:
            print("#LOW==MID")
            return high+1
        elif mid == high:
            print("#MID==HIGH")
            return high+1
        elif mid_value == score:
            print("#found")
            return mid+1
        elif mid_value > score:
            low = mid
            print("#LOW", low)
            continue
        elif mid_value < score:
            high = mid
            print("#HIGH", high)
            continue
        else:
            return "IMPOSSIBLE"
    return "UNREACHABLE"    

def leaderboard_pos(ranked_nodups, score):
    print("#LP()", score, ranked_nodups)
    for i, topscore in enumerate(ranked_nodups):
        print("#rwd", i+1, topscore)
        if topscore <= score:
            return i+1
    i += 1
    print("#not found", i+1)
    return i+1

def climbingLeaderboard(ranked, player):
    retval = []
    ranked_nodups = []
    for topscore in ranked:
        if topscore not in ranked_nodups:
            ranked_nodups.append(topscore)
    ranked_nodups.append(0)
    for p in player:
        pos = leaderboard_pos(ranked_nodups, p)
        posb = leaderboard_pos_b(ranked_nodups, p)
        if pos != posb:
            print("ERROR: pos != posb", pos, posb)
        retval.append(pos)
    
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

