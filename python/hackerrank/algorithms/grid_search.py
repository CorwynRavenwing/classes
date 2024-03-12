#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STRING[] G
# STRING[] P
# return STRING
def gridSearch(G, P):
    g_height = len(G)
    p_height = len(P)
    g_width = len(G[0])
    p_width = len(P[0])
    # print("#G H,W", g_height, g_width)
    # print("#P H,W", p_height, p_width)
    pattern = ':'.join(P)
    # print("#P", pattern)
    for i in range(g_height - p_height +1):
        if P[0] not in G[i]:
            print("#SKIP", i)
            continue
        print("#I", i)
        for j in range(g_width - p_width +1):
            T = [
                G[i+x][j:j+p_width]
                for x in range(p_height)
            ]
            test = ':'.join(T)
            # print("#T", i, j, test)
            if test == pattern:
                # print("#FOUND!", i, j)
                return "YES"
    return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        second_multiple_input = input().rstrip().split()
        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

