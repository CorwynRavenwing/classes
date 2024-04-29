#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from bisect import bisect_left

def climbingLeaderboard(ranked, player):
    retval = []
    print(f"#{ranked[:10]=}")
    nodups = set(ranked)
    ranked_nodups = list(nodups)
    ranked_nodups.sort()
    print(f"#{ranked_nodups[:10]=}")
    for P in player:
        if P in ranked_nodups:
            index = ranked_nodups.index(P)
        else:
            index = bisect_left(ranked_nodups, P)
            nearest_value = (
                ranked_nodups[index]
                if index < len(ranked_nodups)
                else "EOL"
            )
            print(f"#  {P=} {nearest_value=}")
            # if P < nearest_value:
            #     index += 1
            ranked_nodups.insert(index, P)
            print(f"#  {index=} {ranked_nodups[:10]=}")
        rank = len(ranked_nodups) - index
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

