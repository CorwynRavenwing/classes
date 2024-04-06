#!/bin/python3

# import math
import os
# import random
# import re
# import sys

#  INT n
#  INT m
#  INT k
#  INT[][] track
# return INT
def gridlandMetro(n, m, k, track):
    city = {
        i: set(range(1, m+1))
        for i in range(1, n+1)
    }
    print(f"#{city=}")
    for (row, start, end) in track:
        T = set(range(start, end+1))
        print(f"#{row=} {start}-{end} {T=}")
        city[row] = city[row] - T
    print(f"#{city=}")
    lamps = [
        len(row)
        for row in city.values()
    ]
    print(f"#{lamps=}")
    return sum(lamps)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    track = []
    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))
    result = gridlandMetro(n, m, k, track)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

