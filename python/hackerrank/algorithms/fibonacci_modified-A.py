#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# The function is expected to return an INTEGER.
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
def fibonacciModified(t1, t2, n):
    print(f"#t1: {t1}")
    print(f"#t2: {t2}")
    (t_i_minus_2, t_i_minus_1) = (t1, t2)
    for i in range(3, n+1):
        t_i = t_i_minus_2 + t_i_minus_1 * t_i_minus_1
        print(f"#t{i}: {t_i}")
        (t_i_minus_2, t_i_minus_1) = (t_i_minus_1, t_i)
    return t_i

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

