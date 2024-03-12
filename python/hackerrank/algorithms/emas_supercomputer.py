#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def show_answer(grid, p1, p2):
    # print("#show_answer()", grid, p1, p2)
    grid = [
        [
            '.'
            if e == 'B'
            else 'O'
            if e == 'G'
            else '?'
            for e in row
        ]
        for row in grid
    ]
    grid = [
        ''.join(row)
        for row in grid
    ]
    G = [
        [
            '1'
            if (i, j) in p1
            else '2'
            if (i, j) in p2
            else e
            for j, e in enumerate(row)
        ]
        for i, row in enumerate(grid)
    ]
    G = [
        ''.join(row)
        for row in G
    ]
    G = [
            '    '.join(row)
            for row in zip(grid, G)
    ]
    print("#G " + '\n#G '.join(G))
    return

# STRING[] grid
# return INT
def twoPluses(grid):
    print("#twoPluses()")
    G_WID = range(len(grid))
    G_HGT = range(len(grid[0]))
    good = [
        (i, j)
        for i in G_WID
        for j in G_HGT
        if grid[i][j] == 'G'
    ]
    # print("#G", good)
    P = {}
    # figures will contain data of this sort:
    # (size, (i, j)): {(set) (of) (all) (points) (in) (figure)}
    figures = dict([
        (
            (1, pt),
            {pt}
        )
        for pt in good
    ])
    # print("#figures", figures)
    current = good
    N = 1
    P[N] = current
    # print("#N", N, P[N])
    while len(current) > 0:
        N += 1
        new_current = []
        for (i, j) in current:
            print("#N IJ", N, (i, j))
            x = N - 1
            arm_ends = [
                (i-x, j),
                (i+x, j),
                (i, j-x),
                (i, j+x),
            ]
            obstacles = False
            for ae in arm_ends:
                # print("#AE", ae)
                if ae not in good:
                    print("#AE    ", ae, "BAD")
                    obstacles = True
                else:
                    print("#AE    ", ae, "ok")
            if obstacles:
                continue
            prior = figures[(N-1, (i, j))]
            figures[(N, (i, j))] = prior.union(set(arm_ends))
            # print("#FN-", N-1, figures[(N-1, (i, j))])
            # print("#FN+", N, figures[(N, (i, j))])
            print("#add        ", N, figures[(N, (i, j))])
            new_current.append((i, j))
        current = new_current
        P[N] = current
        print("#check", len(current))
    # print("#F", figures)
    available = list(figures.keys())
    available.sort(reverse=True, key=lambda x: x[0])
    # print("#AV", available)
    pairs = []
    for id1 in range(len(available)):
        key1 = available[id1]
        if key1[0] > 1: print("#?", key1)
        points1 = figures[key1]
        score1 = len(points1)
        for id2 in range(id1 + 1, len(available)):
            key2 = available[id2]
            if key2[0] > 1: print("#?  ", key2)
            points2 = figures[key2]
            inter = points1.intersection(points2)
            if len(inter) > 0:
                # the figures intersect: skip this pair
                print("#?    INTERSECT", inter)
                continue
            score2 = len(points2)
            score = score1 * score2
            pairs.append(
                (score, (points1, points2))
            )
    # print("#pairs", pairs)
    pairs.sort(reverse=True, key=lambda x: x[0])
    answer = pairs[0]
    (p1, p2) = answer[1]
    show_answer(grid, p1, p2)
    print("#answer", answer)
    return answer[0]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = twoPluses(grid)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

