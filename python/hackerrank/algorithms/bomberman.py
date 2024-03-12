#!/bin/python3

# import math
import os
# import random
# import re
# import sys

hashes = {}

def show_grid(i, G):
    global hashes
    grid = tuple([
            ''.join(G[i][:40])
            for i in range(len(G[:40]))
    ])
    H = hash(grid)
    hashes[H] = hashes.get(H, [])
    hashes[H].append(i)
    print("#N", i, H, hashes[H])
    print("#" + '\n#'.join(grid))
    return

def show_hashes():
    global hashes
    print("#hashes")
    for h, seconds in hashes.items():
        print("#", h, seconds)
    return

def clean_grid(G):
    G = [
        [
            'O' if e == 'N' else e
            for e in row
        ]
        for row in G
    ]
    grid = [
        ''.join(row)
        for row in G
    ]
    return grid

# INT n
# STR[] grid
# return STR[]
def bomberMan(n, grid):
    print("#bomberMan()", n)
    G = [
        list(s)
        for s in grid
    ]
    G_LEN = range(len(G))
    G_WID = range(len(G[0]))
    del grid
    show_grid(0, G)
    # shortcut:
    # there are only 6 possible states:
    # [0, 1]
    # [2]
    # [3, 7, 11, ...
    # [4, 8, 12, ...
    # [5, 9, 13, ...
    # [6, 10, 14, ...
    # therefore we can cut off after a very small number
    # of rounds and still see the same final state
    equivalent_n = (
        n
        if n <= 6
        else ((n-3) % 4) + 3
    )
    # for sec in range(1, n+1):
    for sec in range(1, equivalent_n+1):
        if sec > 50:
            show_hashes()
            return clean_grid(G)
        if sec % 2 == 0:
            G = [
                [
                    'N' if e == '.' else e
                    for e in row
                ]
                for row in G
            ]
        elif sec % 2 == 1 and sec != 1:
            bombs = [
                (i, j)
                for i in G_LEN
                for j in G_WID
                if G[i][j] == 'O'
            ]
            neighbors = [
                (-1, 0), (+1, 0),
                (0, -1), (0, +1),
            ]
            destroyed = set(bombs)
            for (i, j) in bombs:
                for (x, y) in neighbors:
                    destroyed.add(
                        tuple([i+x, j+y])
                    )
            G = [
                [
                    '.' if (i, j) in destroyed else G[i][j]
                    for j in G_WID
                ]
                for i in G_LEN
            ]
            G = [
                [
                    'O' if e == 'N' else e
                    for e in row
                ]
                for row in G
            ]
        elif sec == 1:
            pass
        # no 'else'
        show_grid(sec, G)
    return clean_grid(G)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)
    result = bomberMan(n, grid)
    print('\n'.join(result))
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    # fptr.close()

