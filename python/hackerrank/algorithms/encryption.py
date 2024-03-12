#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def encryption(s):
    print("#en()", s)
    s = s.replace(' ', '')
    # print("#s", s)
    L = len(s)
    size = pow(L, 1/2)
    floor = int(size)
    if floor ** 2 == L:
        # exactly square
        ceil = floor
    else:
        # rectangle
        ceil = floor + 1
    block_size = floor * ceil
    if block_size < L:
        # larger square
        floor = ceil
        block_size = floor * ceil
    print("#l", L, floor, ceil, block_size)
    s_list = list(s)
    while len(s_list) < block_size:
        s_list.append('')
    # print("#SL", s_list)
    s_block = [
        s_list[i*ceil:(i+1)*ceil]
        for i in range((len(s_list)+ceil-1) // ceil)
    ]
    print("#SB", s_block)
    encr = list(zip(*s_block))
    print("#ENCR", encr)
    encr = [
        ''.join(e)
        for e in encr
    ]
    # print("#ENCR", encr)
    encr = ' '.join(encr)
    print("#ENCR", encr)
    return encr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()

