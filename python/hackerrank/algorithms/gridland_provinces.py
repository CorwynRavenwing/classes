#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def is_at_edge(T, N):
    (i, j) = T
    return i in [0, N-1]

def is_cross(T1, T2):
    (i1, j1) = T1
    (i2, j2) = T2
    return j1 != j2

def all_neighbors(T, may_cross):
    (i, j) = T
    non_crossing = (
        (i-1, j),
        (i+1, j),
    )
    crossing = (
        (i, j-1),
        (i, j+1),
    )
    neighbors = (
        non_crossing + (
            crossing
            if may_cross
            else ()
        )
    )
    return neighbors

def get_new_mode(mode, crossing, to_edge):
    new_mode = None
    if mode == 'NO':
        if to_edge:
            new_mode = 'MAY'
        else:
            new_mode = 'NO'
    elif mode == 'MAY':
        if crossing:
            new_mode = 'CROSSED'
        elif to_edge:
            new_mode = 'MAY'
        else:
            new_mode = 'NO'
    elif mode == 'CROSSED':
        new_mode = 'MAY'

    if new_mode is not None:
        print(f"#get_new_mode({mode},{crossing},{to_edge}):{new_mode}")
        return new_mode
    else:
        raise Exception(
            ' '.join(
                f"#ERROR: get_new_mode({mode},{crossing},{to_edge})"
                "has no allowed answer"
            )
        )

# STR s1
# STR s2
# return INT
def gridlandProvinces(s1, s2):
    print("#" * 60)
    print(f"#gridlandProvinces({s1},{s2})")
    N = len(s1)
    assert N == len(s2)
    cities = list(sorted([
        (i, j)
        for i in range(N)
        for j in range(2)
    ]))
    print(f"#{cities=}")
    paths = [
        ('START', (T,))
        for T in cities
    ]
    print(f"#{paths}")
    full_paths = []
    while paths:
        print(f"#{len(paths)=}")
        (mode, path) = paths.pop(0)
        print(f"#  {mode} {path=}")
        if len(path) == 2 * N:
            print("#    SUCCESS")
            full_paths.append(path)
            continue
        from_point = path[-1]
        from_edge = is_at_edge(from_point, N)
        if mode == 'START':
            if from_edge:
                mode = 'MAY'
            else:
                mode = 'NO'
        may_cross = (mode == 'MAY')

        neighbors = all_neighbors(from_point, may_cross)
        for to_point in neighbors:
            if to_point not in cities:
                print(f"#    {to_point} OOB")
                pass
            elif to_point in path:
                print(f"#    {to_point} CRASH")
                pass
            else:
                new_path = path + (to_point,)
                crossing = is_cross(from_point, to_point)
                # print(f"#is_cross({from_point},{to_point}):{crossing}")
                to_edge = is_at_edge(to_point, N)
                # print(f"#is_at_edge({to_point}, {N}):{to_edge}")
                new_mode = get_new_mode(mode, crossing, to_edge)
                print(f"#    {to_point} ADD ({new_mode})")
                paths.append(
                    (new_mode, new_path)
                )
                # if new_path == ((0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0)):
                #     raise Exception("die here")

    full_paths_string = '\n#'.join(map(str, full_paths))
    print(f"#full_paths=\n#{full_paths_string}")
    strings = [
        ''.join([
            (
                s1[i]
                if j == 0
                else
                s2[i]
            )
            for i, j in path
        ])
        for path in full_paths
    ]
    print(f"#{strings=}")

    answers = set(strings)
    print(f"#{answers=}")
    return len(answers)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p = int(input().strip())
    for p_itr in range(p):
        n = int(input().strip())
        s1 = input()
        s2 = input()
        result = gridlandProvinces(s1, s2)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

