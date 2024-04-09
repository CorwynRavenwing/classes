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
    # and that list is in order by [lower]
    # then turn it from a generator back into a list
    possible_roads = list(sorted(map(sorted, possible_roads)))
    price = 0
    if c_lib <= c_road:
        price = number_of_cities * c_lib
        return price
    # print(f"#{number_of_cities=} {possible_roads=}")
    # connected_cities = []
    disconnected_cities = list(range(1, number_of_cities+1))
    while disconnected_cities:
        city = disconnected_cities.pop(0)
        print(f"#{city=}")
        # if city in connected_cities:
        #     print("#  CONNECTED $0")
        #     continue
        print(f"#  LIBRARY #{city} ${c_lib}")
        price += c_lib
        # connected_cities.append(city)
        check_connections = [city]
        while check_connections:
            # connection = check_connections.pop(0)
            roads_from_here = set([
                B
                for A, B in possible_roads
                if A in check_connections and B in disconnected_cities
            ])
            check_connections = roads_from_here
            if roads_from_here:
                print(f"#    ROADS {len(roads_from_here)} * ${c_road}")
                price += c_road * len(roads_from_here)
                for destination in roads_from_here:
                    disconnected_cities.remove(destination)
    # print(f"#{connected_cities}")
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

