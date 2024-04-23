#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def factorial(N):
    if not N:
        return 1
    retval = N
    for i in range(1, N):
        retval *= i
        # print("#I", i, retval)
    return retval

def line_number_0_basis(x):
    N = len(x)
    if N == 0:
        return 0
    x0 = x[0]
    assert x0 not in x[1:]
    xRest = list([
        (
            Xn - 1
            if Xn > x0
            else Xn
        )
        for Xn in x[1:]
    ])
    # print(f"#{x0=} {xRest=}")
    line = (x0 - 1) * factorial(N - 1)
    return line + line_number_0_basis(xRest)

def line_number(x):
    return line_number_0_basis(x) + 1

# TEST
# print(f"#{line_number([4, 3, 2, 1])=}")
# print(f"#{line_number([1, 2, 3, 4])=}")
# exit()

# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY x as parameter.
def solve(x):
    N = len(x)
    print(f"#{N=} {x=}")
    possibilities = [x]
    # Note: *each* possibility will contain the same number of zeros
    while 0 in possibilities[0]:
        new_list = []
        for attempt in possibilities:
            index = attempt.index(0)
            allowed_values = list([
                val + 1
                for val in range(N)
                if (val + 1) not in attempt
            ])
            # print(f"#{attempt=} {index=} {allowed_values=}")
            for val in allowed_values:
                new_attempt = attempt[:index] + [val] + attempt[index+1:]
                # print(f"#  -> {new_attempt}")
                new_list.append(new_attempt)
        possibilities = new_list
    print(f"#{possibilities=}")
    lines = [
        line_number(x)
        for x in possibilities
    ]
    print(f"#{lines=}")
    mod = 10 ** 9 + 7
    return sum(lines) % mod

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = solve(a)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

