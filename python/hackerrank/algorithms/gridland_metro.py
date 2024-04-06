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
    city = {}
    print(f"#{city=}")
    for (row, start, end) in track:
        city.setdefault(row, [])
        city_row = city[row]
        if not city_row:
            city[row].append((start, end))
            print(f"#{row=} {start}-{end} +ADD+")
            continue
        overlaps = [
            (S, E)
            for S, E in city_row
            if (
                start <= S <= end
            ) or (
                start <= E <= end
            ) or (
                S <= start <= E
            ) or (
                S <= end <= E
            )
        ]
        disjoints = [
            T
            for T in city_row
            if T not in overlaps
        ]
        print(f"#{row=} {start}-{end} {overlaps=} {disjoints=}")
        for S, E in overlaps:
            start = min(start, S)
            end = max(end, E)
            print(f"# -> {start}-{end}")
        city[row] = disjoints
        city[row].append((start, end))
    print(f"#{city=}")
    count_track = [
        sum([
            E - S + 1
            for (S, E) in row
        ])
        for row in city.values()
    ]
    print(f"#{count_track=}")
    lamps = [
        m - T
        for T in count_track
    ] + [
        m * (n - len(city))
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

