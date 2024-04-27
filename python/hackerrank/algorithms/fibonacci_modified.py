#!/bin/python3

# import math
import os
# import random
# import re
# import sys

block_exponent = 10
block_size = 10 ** block_exponent

def normalize(a):
    while max(a) >= block_size:
        # print(f"#NA:{a=}")
        if a[0] >= block_size:
            a = [0] + a
            # print(f"# 0 {a=}")
        for i in range(1, len(a)):
            if a[i] >= block_size:
                transfer = a[i] // block_size
                a[i-1] += transfer
                a[i] -= block_size * transfer
                # print(f"# {i} {a=}")
    return a

def add(a, b):
    # print(f"#{a=} + {b=}")
    # print("# ADD:")
    a = [0] * (len(b) - len(a)) + a
    b = [0] * (len(a) - len(b)) + b
    # print(f"#{a=}")
    # print(f"#{b=}")
    # print(f"#zip={list(zip(a, b))}")
    # print(f"#map={list(map(sum, zip(a, b)))}")
    return normalize(list(map(sum, zip(a, b))))

def multiply_int(a, integer):
    b = [
        val * integer
        for val in a
    ]
    return normalize(list(b))

def multiply(a, b):
    # print(f"#{a=} x {b=}")
    answer = [0]
    # b_len = len(b)
    for index, val in enumerate(reversed(b)):
        # print(f"#  {index=}/{b_len} {val=}")
        partial = multiply_int(a, val) + [0] * index
        answer = add(answer, partial)
    return answer

def int2list(a):
    return normalize([a])
    # return list(map(int, list(str(a))))

def list2int(b):
    # make each number a string,
    # then pad left with zeros
    # to width 'block_exponent'
    strings = map(lambda x: str(x).zfill(block_exponent), b)
    return int(''.join(strings))

# The function is expected to return an INTEGER.
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
def fibonacciModified(t1, t2, n):
    print(f"#t1: {int2list(t1)}")
    print(f"#t2: {int2list(t2)}")
    (t_i_minus_2, t_i_minus_1) = (int2list(t1), int2list(t2))
    for i in range(3, n+1):
        t_i = add(
            t_i_minus_2,
            multiply(
                t_i_minus_1,
                t_i_minus_1
            )
        )
        print(f"#t{i}: {t_i}")
        (t_i_minus_2, t_i_minus_1) = (t_i_minus_1, t_i)
    return list2int(t_i)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    t1 = int(first_multiple_input[0])
    t2 = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    result = fibonacciModified(t1, t2, n)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

