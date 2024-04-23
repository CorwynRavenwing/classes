#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def all_neighbors(T):
    (i, j) = T
    return (
        (i-1, j),
        (i+1, j),
        (i, j-1),
        (i, j+1),
    )

# STR s1
# STR s2
# return INT
def gridlandProvinces(s1, s2):
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
        (T,)
        for T in cities
    ]
    # print(f"#{paths}")
    full_paths = []
    while paths:
        # print(f"#{len(paths)=}")
        path = paths.pop(0)
        # print(f"#  {path=}")
        if len(path) == 2 * N:
            # print("#    SUCCESS")
            full_paths.append(path)
            continue
        endpoint = path[-1]
        neighbors = all_neighbors(endpoint)
        for neighbor in neighbors:
            if neighbor not in cities:
                # print(f"#    {neighbor} OOB")
                pass
            elif neighbor in path:
                # print(f"#    {neighbor} CROSS")
                pass
            else:
                # print(f"#    {neighbor} ADD")
                new_path = path + (neighbor,)
                paths.append(new_path)
    # print(f"#{full_paths=}")
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

