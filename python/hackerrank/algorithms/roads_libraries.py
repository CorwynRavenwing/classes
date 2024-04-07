#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# INT n
# INT c_lib
# INT c_road
# INT[][] cities
# return LONG_INT
def roadsAndLibraries(number_of_cities, c_lib, c_road, possible_roads):
    # ensure each road-endpoint pair is ordered [lower, higher]
    possible_roads = list(map(sorted, possible_roads))
    price = 0
    if c_lib <= c_road:
        price = number_of_cities * c_lib
        return price
    print(f"#{number_of_cities=} {possible_roads=}")
    connected_cities = {}
    for city in range(1, number_of_cities+1):
        print(f"#{city=}")
        roads_to_here = [
            (A, B)
            for A, B in possible_roads
            if B == city and A in connected_cities
        ]
        print(f"#  {roads_to_here}")
        if not roads_to_here:
            print(f"#    LIBRARY {c_lib}")
            price += c_lib
            connected_cities[city] = "LIB"
        else:
            print(f"#    ROAD {c_road}")
            price += c_road
            connected_cities[city] = roads_to_here.pop(0)
    print(f"#{connected_cities}")
    return price

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        c_lib = int(first_multiple_input[2])
        c_road = int(first_multiple_input[3])
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

