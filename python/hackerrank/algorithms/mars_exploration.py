#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STRING s
# return INTEGER
def marsExploration(s):
    SOS = 'SOS'
    checksum = [
        c
        for i, c in enumerate(s)
        if c != SOS[i % 3]
    ]
    print("#CS", checksum)
    return len(checksum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()

