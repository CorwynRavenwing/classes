#!/bin/python3

# import math
import os
# import random
# import re
# import sys

directions = tuple(
    (i, j)
    for i in [-1, 0, 1]
    for j in [-1, 0, 1]
    if (i, j) != (0, 0)
)
# print(f"#{list(directions)=}")
# print(f"#{list(directions)=}")

def cell_neighbors(T):
    (x, y) = T
    # retval = tuple(
    #     (x + i, y + j)
    #     for (i, j) in directions
    # )
    # print(f"#CN({T}) = {retval}")
    # return retval
    return tuple(
        (x + i, y + j)
        for (i, j) in directions
    )

# INT[][] matrix
# return INT
def connectedCell(matrix):
    cells = [
        (x, y)
        for x, row in enumerate(matrix)
        for y, V in enumerate(row)
        if V == 1
    ]
    print(f"#{cells=}")
    groups = []
    this_group = []
    check_neighbors = []
    while cells or this_group or check_neighbors:
        print(
            "#while:",
            [
                'C', len(cells),
                'CN', check_neighbors,
                'TG', this_group,
                'G', len(groups),
            ]
        )
        if not check_neighbors:
            if this_group:
                print("#   STORE TG -> G")
                groups.append(this_group)
                this_group = []
            if cells:
                this = cells.pop(0)
                print(f"# {this} cells -> CN")
                check_neighbors.append(this)
        if not check_neighbors:
            print("#   NOTHING TO CHECK")
            continue
        this = check_neighbors.pop(0)
        print(f"# {this} CN -> this")
        for N in cell_neighbors(this):
            # print(f"#   N in neighbors: {N}")
            if N in cells:
                print(f"# {N} cells -> CN")
                cells.remove(N)
                if N in check_neighbors:
                    print(f"#    // {N} in CN")
                    continue
                elif N in this_group:
                    print(f"#    // {N} in TG")
                    continue
                else:
                    check_neighbors.append(N)
        this_group.append(this)
        print(f"# {this} this -> TG")
        this = None
    # Write your code here
    print(f"#{groups=}")
    lengths = tuple(map(len, groups))
    print(f"#{lengths=}")
    return max(lengths)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    m = int(input().strip())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    result = connectedCell(matrix)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

