#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def climbingLeaderboard(ranked, player):
    retval = []
    print(f"#{ranked[:10]=}")
    nodups = set(ranked)
    ranked_nodups = list(nodups)
    ranked_nodups.sort(reverse=True)
    print(f"#{ranked_nodups[:10]=}")
    for P in player:
        if P not in ranked_nodups:
            nearest_value = min(
                ranked_nodups,
                key=lambda x: abs(x - P)
            )
            print(f"#  {P=} {nearest_value=}")
            index = ranked_nodups.index(nearest_value)
            if P < nearest_value:
                index += 1
            ranked_nodups.insert(index, P)
            print(f"#  {index=} {ranked_nodups[:10]=}")
        rank = ranked_nodups.index(P) + 1
        print(f"#  {P=} {rank=} LEN={len(ranked_nodups)}")
        retval.append(rank)
    return retval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    print('\n'.join(map(str, result)))
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

