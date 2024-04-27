#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

def possible_moves_from(pos):
    (i, j) = pos
    moves_dict = {
        'UL': (i-2, j-1),
        'UR': (i-2, j+1),
        'R': (i, j+2),
        'LR': (i+2, j+1),
        'LL': (i+2, j-1),
        'L': (i, j-2),
    }
    return moves_dict

def get_move_names_in_priority_order():
    moves_dict = possible_moves_from((0, 0))
    move_names = [
        move_name
        for move_name, new_pos in moves_dict.items()
    ]
    return tuple(move_names)

def sort_moves_by_priority(move_list):
    move_names = get_move_names_in_priority_order()

    def sort_by_priority(move):
        return move_names.index(move)

    return sorted(move_list, key=sort_by_priority)

def legal_position(pos, n):
    (i, j) = pos
    return (0 <= i <= n-1) and (0 <= j <= n-1)

def distance_between(pos1, pos2):
    (i1, j1) = pos1
    (i2, j2) = pos2
    return abs(i1 - i2) + abs(j1 - j2)

def find_shortest_path(beginpos, endpos):
    paths = [
        (0, [], beginpos)
    ]
    shortest_path = None
    while paths:
        path = paths.pop(0)
        print(f"#[{len(paths)}] {path}")
        (moves, move_list, current) = path
        assert moves == len(move_list)
        if current == endpos:
            print(f"#  FOUND PATH {moves} {move_list}")
            shortest_path = move_list
            break
            # could just return it here instead
        current_distance = distance_between(current, endpos)
        possible_moves = possible_moves_from(current)
        new_move_list = []
        for move, new_position in possible_moves.items():
            label = f"{move} {new_position}"
            if not legal_position(new_position, n):
                # print(f"#  {label} OOB!")
                continue
            new_distance = distance_between(new_position, endpos)
            if new_distance >= current_distance:
                # print(f"#  {label} FARTHER {current_distance} <= {new_distance}")
                continue
            new_move = (moves + 1, move_list + [move], new_position)
            new_move_list.append(
                (new_distance, new_move)
            )
        if not new_move_list:
            print("#  NO NEW MOVES")
            continue
        new_distance_list = [
            new_distance
            for (new_distance, new_move) in new_move_list
        ]
        # print(f"#  {new_distance_list.copy()=}")
        min_new_distance = min(new_distance_list)
        short_new_moves_list = [
            (new_distance, new_move)
            for (new_distance, new_move) in new_move_list
            if new_distance == min_new_distance
        ]
        # long_new_moves_list = [
        #     (new_distance, new_move)
        #     for (new_distance, new_move) in new_move_list
        #     if new_distance > min_new_distance
        # ]
        first_short_new_move = short_new_moves_list.pop(0)
        (new_distance, new_move) = first_short_new_move
        (new_moves, new_move_list, new_position) = new_move 
        label = f"{new_move_list[-1]} {new_position}"
        dist_label = f"{current_distance} -> {new_distance}"
        print(f"#  {label} *** YES *** {dist_label}")
        paths.append(new_move)
        # for (new_distance, new_move) in short_new_moves_list:
        #     (new_moves, new_move_list, new_position) = new_move 
        #     label = f"{new_move_list[-1]} {new_position}"
        #     dist_label = f"{current_distance} -> {new_distance}"
        #     print(f"#  {label} *** NO *** {dist_label}: NOT FIRST")
        # for (new_distance, new_move) in long_new_moves_list:
        #     (new_moves, new_move_list, new_position) = new_move 
        #     label = f"{new_move_list[-1]} {new_position}"
        #     dist_label = f"{current_distance} -> {new_distance}"
        #     print(f"#  {label} *** NO *** {dist_label}: NOT NEAREST")
    return shortest_path

#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
# no return value
def printShortestPath(n, i_start, j_start, i_end, j_end):
    beginpos = (i_start, j_start)
    endpos = (i_end, j_end)

    shortest_path = find_shortest_path(beginpos, endpos)
    
    print(f"#{shortest_path=}")
    if shortest_path:
        print(len(shortest_path))
        shortest_path = sort_moves_by_priority(shortest_path)
        print(' '.join(shortest_path))
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

