#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

def possible_moves_from(pos):
    (i, j) = pos
    return {
        'UL': (i-2, j-1),
        'UR': (i-2, j+1),
        'R': (i, j+2),
        'LR': (i+2, j+1),
        'LL': (i+2, j-1),
        'L': (i, j-2),
    }

def legal_position(pos, n):
    # print(f"#DEBUG: {pos=}")
    (i, j) = pos
    return (0 <= i <= n-1) and (0 <= j <= n-1)

def distance_between(pos1, pos2):
    (i1, j1) = pos1
    (i2, j2) = pos2
    return abs(i1 - i2) + abs(j1 - j2)

#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
# no return value
def printShortestPath(n, i_start, j_start, i_end, j_end):
    begin = (i_start, j_start)
    endpoint = (i_end, j_end)
    
    paths = [
        (0, [], begin)
    ]
    short_paths = []
    shortest_path = None    # might pull this all back out now
    while paths:
        path = paths.pop(0)
        # print(f"#[{len(paths)}] ({shortest_path}) {path}")
        (moves, move_list, current) = path
        assert moves == len(move_list)
        if shortest_path is not None:
            if shortest_path < moves:
                # print(f"#  TOO LONG {moves} > {shortest_path}")
                continue
        if current == endpoint:
            # print(f"#  FOUND PATH {moves} {move_list}")
            short_paths.append(tuple(move_list))
            shortest_path = moves
            break
            # continue
        current_distance = distance_between(current, endpoint)
        possible_moves = possible_moves_from(current)
        for move, new_position in possible_moves.items():
            # label = f"#  {move} {new_position}"
            if not legal_position(new_position, n):
                # print(f"#  {label} OOB!")
                continue
            new_distance = distance_between(new_position, endpoint)
            if new_distance >= current_distance:
                # print(f"#  {label} FARTHER {current_distance} <= {new_distance}")
                continue
            new_move = (moves + 1, move_list + [move], new_position)
            paths.append(new_move)
            # print(f"#  {label} *** YES *** {current_distance} -> {new_distance}")
    # print(f"#{short_paths=}")
    if short_paths:
        shortest = short_paths.pop()
        print(len(shortest))
        print(' '.join(shortest))
    else:
        print("Impossible")
    pass

if __name__ == '__main__':
    n = int(input().strip())
    first_multiple_input = input().rstrip().split()
    i_start = int(first_multiple_input[0])
    j_start = int(first_multiple_input[1])
    i_end = int(first_multiple_input[2])
    j_end = int(first_multiple_input[3])
    printShortestPath(n, i_start, j_start, i_end, j_end)

