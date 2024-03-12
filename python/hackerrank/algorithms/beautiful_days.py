#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def reverse_int(i):
    # print("#i", i)
    i_str = str(i)
    # print("#i_str", i_str)
    i_list = list(i_str)
    # print("#i_list", i_list)
    r_list = list(reversed(i_list))
    # print("#r_list", r_list)
    r_str = ''.join(r_list)
    # print("#r_str", r_str)
    r_int = int(r_str)
    # print("#r_int", r_int)
    print("#rev", i, r_int)
    return r_int

def i_minus_reverse_i(i):
    return abs(i - reverse_int(i))

def beautifulDays(i, j, k):
    range_days = range(i, j+1)
    beautiful_days_in_range = [
        d
        for d in range_days
        if i_minus_reverse_i(d) % k == 0
    ]
    return len(beautiful_days_in_range)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    i = int(first_multiple_input[0])
    j = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    result = beautifulDays(i, j, k)
    # fptr.write(str(result) + '\n')
    # fptr.close()
    print(result)

