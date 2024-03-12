#!/bin/python3

import math
import os
import random
import re
import sys

def space(match):
    # print("#M", match)
    return " "

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
# print("#n,m", n, m)
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
# print("#M", matrix)
buffer = []
for i in range(m):
    for j in range(n):
        c = matrix[j][i]
        buffer.append(c)
# print("#B", buffer)
script = ''.join(buffer)
# print("#S0", script)
script = re.sub(
    r"(?<=[A-Za-z])[^A-Za-z]+(?=[A-Za-z])",
    space,
    script
)
print(script)

