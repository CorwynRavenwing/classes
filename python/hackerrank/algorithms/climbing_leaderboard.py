#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def climbingLeaderboard(ranked, player):
    retval = []
    print(f"#{ranked=}")
    nodups = set(ranked)
    for P in player:
        nodups.add(P)
        ranked_nodups = list(nodups)
        ranked_nodups.sort(reverse=True)
        rank = ranked_nodups.index(P) + 1
        # print(f"#  {rank=} RND={ranked_nodups}")
        print(f"#  {rank=} LEN={len(nodups)}")
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

