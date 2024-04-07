
# import math
import os
# import random
# import re
# import sys

directions = (
    (-1, +0),
    (+1, +0),
    (+0, -1),
    (+0, +1),
)

def neighbors_of(cell):
    (x, y) = cell
    return tuple(
        (x+i, y+j)
        for (i, j) in directions
    )

#  STR[] matrix
#  INT k
# return STR
def countLuck(matrix, k):
    points = tuple(
        (x, y)
        for x, row in enumerate(matrix)
        for y, val in enumerate(row)
        if val in ['.', 'M', '*']
    )
    endpoints = {
        val: (x, y)
        for x, row in enumerate(matrix)
        for y, val in enumerate(row)
        if val in ['M', '*']
    }
    print(f"#{points=}")
    print(f"#{endpoints=}")
    paths = {
        point: tuple(
            N
            for N in neighbors_of(point)
            if N in points
        )
        for point in points
    }
    eStart = endpoints['M']
    eEnd = endpoints['*']
    paths['M'] = (eStart,)
    paths[eStart] = tuple(
        list(
            paths[eStart]
        ) + ['M']
    )
    # print(f"#{paths=}")
    for point, neighbors in paths.items():
        print(f"#{point} -> {' '.join(map(str, neighbors))}")
    print("#" + "=" * 60)
    digraph = {}
    begin = 'M'
    current = ''
    inprog = []
    while paths:
        if not current:
            current = begin
        print(f"#{begin=} {current=}")
        if current not in paths:
            print(f"#{current=} NOT IN {paths=}")
            exit(1)
        neighbors = paths[current]
        del paths[current]
        print(f"#  {neighbors=}")
        relevant = [
            neighbor
            for neighbor in neighbors
            if neighbor in paths
        ]
        R = len(relevant)
        print(f"# {R}:{relevant=}")
        if R == 1 and current != eEnd:
            print("#R=1")
            current = relevant.pop()
            continue
        digraph.setdefault(begin, [])
        digraph[begin].append(current)
        if current == eEnd:
            print(f"#END {eEnd}")
            # stop here: don't create new inprog records
            (begin, current) = (None, None)
        elif R > 1:
            print("#R>1")
            inprog.extend([
                (current, R)
                for R in relevant
            ])
            print(f"#A {inprog=}")
            (begin, current) = (None, None)
        else:
            assert R == 0
            (begin, current) = (None, None)
        if inprog:
            (begin, current) = inprog.pop(0)
            print(f"#B {inprog=}")
        if not begin:
            print("#OUT OF DATA")
            break
    print(f"#{paths=}")
    print(f"#{digraph=}")
    path_taken = []
    current = eEnd
    while current:
        print(f"#{current=}")
        path_taken.append(current)
        previous = [
            key
            for key, value in digraph.items()
            if current in value
        ]
        print(f"#{previous=}")
        if previous:
            current = previous.pop()
        else:
            current = None
    print(f"#{path_taken=}")
    turns = len(path_taken) - len(['M', eEnd])
    if turns == k:
        retval = 'Impressed'
    else:
        retval = 'Oops!'
    print(f"#{retval=} {turns=} {k=}")
    return retval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        matrix = []
        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)
        k = int(input().strip())
        result = countLuck(matrix, k)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

