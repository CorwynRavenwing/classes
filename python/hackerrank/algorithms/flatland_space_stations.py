#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def flatlandSpaceStations(n, ss_list):
    print("#fSS()", n, len(ss_list))
    ss_list.sort()
    # print("#SS", ss_list)
    ss_index = -1
    # max_distance = 0
    distances = []
    for city in range(n):
        low_high = []
        while len(low_high) == 0:
            low = (
                ss_list[ss_index]
                if ss_index > -1
                else None
                )
            high = (
                ss_list[ss_index+1]
                if ss_index < len(ss_list)-1
                else None
                )
            # print("#?", ss_index, low, city, high)
            if (low is None or low <= city):
                if (high is None or city < high):
                    low_high = [low, high]
                    continue
            ss_index += 1
            # continue
        # print("#!", ss_index, low, city, high)
        if city in low_high:
            distance = 0
        else:
            distance = min([
                abs(city - ss)
                for ss in low_high
                if ss is not None
            ])
        distances.append(distance)
        print("#C", city, distance)
    print("#D", len(distances))
    return max(distances)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    # fptr.write(str(result) + '\n')
    print(str(result))
    # fptr.close()

