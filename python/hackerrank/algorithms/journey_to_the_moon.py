#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# INT n
# INT[][] astronaut
# return INT
def journeyToMoon(n, astronaut):
    print(f"#{n=} {astronaut=}")
    countries = []
    known_astronauts = []
    while astronaut:
        this_country = []
        add_to_country = astronaut.pop(0)
        while add_to_country:
            print(f"#{add_to_country=}")
            this_country.extend(add_to_country)
            print(f"#{this_country=}")
            astronaut_links = [
                [A, B]
                for A, B in astronaut
                if A in add_to_country and B not in this_country
            ] + [
                [A, B]
                for A, B in astronaut
                if B in add_to_country and A not in this_country
            ]
            add_to_country = []
            for AL in astronaut_links:
                astronaut.remove(AL)
                print(f"#{AL=} {astronaut=}")
                for X in AL:
                    if X not in this_country:
                        add_to_country.append(X)
        countries.append(this_country)
        known_astronauts.extend(this_country)
    print(f"#{countries=}")
    print(f"#{known_astronauts=}")
    for A in range(n):
        if A not in known_astronauts:
            countries.append([A])
    print(f"#{countries=}")
    counts = list(map(len, countries))
    print(f"#{counts=}")
    answers = [
        A * B
        for i, A in enumerate(counts)
        for j, B in enumerate(counts)
        if i < j
    ]
    print(f"#{answers=}")
    return sum(answers)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    p = int(first_multiple_input[1])
    astronaut = []
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))
    result = journeyToMoon(n, astronaut)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

