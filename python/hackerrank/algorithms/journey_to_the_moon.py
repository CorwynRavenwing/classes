#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def count_astro(A):
    nulls = len([
        a
        for a in A
        if not a
    ])
    return (len(A)-nulls, nulls)

# INT n
# INT[][] astronaut
# return INT
def journeyToMoon(n, astronaut):
    print(f"#{n=} {count_astro(astronaut)}")
    for index, A in enumerate(astronaut):
        if A:
            print(f"#  {index=} {A=} {count_astro(astronaut)}")
        running = True
        while running:
            running = False
            for val in A:
                others = list([
                    o_group
                    for o_index, o_group in enumerate(astronaut)
                    if val in o_group and o_index != index
                ])
                if others:
                    print(f"#    {val=} {others=}")
                while others:
                    running = True
                    other = others.pop(0)
                    print(f"#      {other=}")
                    while other:
                        other_val = other.pop(0)
                        print(f"#        {other_val=}")
                        if other_val not in A:
                            print("#          INSERT")
                            A.append(other_val)
            # print(f"#  {index=} {A=} {count_astro(astronaut)}")
    astronaut = list([
        A
        for A in astronaut
        if A
    ])
    # print(f"#{count_astro(astronaut)}")
    known_astronauts = list(sorted([
        val
        for A in astronaut
        for val in A
    ]))
    # print(f"#{known_astronauts=}")
    singles = 0
    for A in range(n):
        if A not in known_astronauts:
            # astronaut.append([A])
            singles += 1
            # print(f"#  SINGLE {A}")

    print(f"#{singles=}")

    counts = list(map(len, astronaut))
    print(f"#{counts=}")

    # SECTION 1: KNOWN ASTRONAUTS
    # Each known astronaut can go with any of the astronauts
    # from a different country than herself:

    answer = 0
    for i, A in enumerate(counts):
        for j, B in enumerate(counts):
            if i < j:
                answer += A * B
                # print(f"# {i=} {A=} {j=} {B=} {A*B=} {answer=}")

    # SECTION 2: KNOWN * UNKNOWN
    # Each known astronaut can go with any one of the singles:

    print(f"#{sum(counts)=}")
    print(f"#{sum(counts)*singles=}")
    answer += sum(counts) * singles

    # SECTION 3: UNKNOWN ASTRONAUTS
    # Each singleton can go with any other singleton:

    # === N choose K, N=singles, K=2
    # === N! / (N-2)!(2)!
    # === N (N-1) / 2   # the (N-2)(N-3)...(2)(1) terms all cancel
    print(f"#{singles*(singles-1)//2=}")
    answer += singles * (singles - 1) // 2

    return answer

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

