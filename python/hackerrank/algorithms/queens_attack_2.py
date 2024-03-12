#!/bin/python3

# IN PROGRESS

# import math
import os
# import random
# import re
# import sys

def illegalPosition(n, pos):
    for s in pos:
        if s <= 0:
            # print("#<0", s)
            return True
        if s > n:
            # print("#>N", s)
            return True
    return False

def queensAttack(n, k, r_q, c_q, obstacles):
    print("#OBS", obstacles)
    directions = tuple(
        (r, c)
        for r in range(-1, 1+1)
        for c in range(-1, 1+1)
        if r != 0 or c != 0
    )
    # print("#dir", directions)
    # attack = []
    attack_count = 0
    Q_pos = (r_q, c_q)
    for d in directions:
        print("#DIR", d)
        square = Q_pos
        for i in range(n):
            # print("#I", i)
            square = [
                square[j] + d[j]
                for j in range(len(square))
            ]
            # print("#SQ", square)
            if illegalPosition(n, square):
                print("#BAD", i, square)
                break
            if square in obstacles:
                print("#X", i, square)
                break
            print("#SQ!", i, square)
            attack_count += 1
            # attack.append(square)
    # print("#ATT", attack)
    # return len(attack)
    return attack_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

