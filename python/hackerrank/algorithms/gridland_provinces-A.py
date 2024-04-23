#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def str_rev(S):
    return ''.join(reversed(list(S)))

def all_rotations(S):
    return [
        S[i:] + S[:i]
        for i in range(len(S))
    ]

# STR s1
# STR s2
# return INT
def gridlandProvinces(s1, s2):
    print(f"#gridlandProvinces({s1},{s2})")
    string = s1 + str_rev(s2)
    print(f"#{string=}")
    answers_f = all_rotations(string)
    answers_r = list(map(str_rev, answers_f))
    print(f"#{answers_f=}")
    print(f"#{answers_r=}")
    answers_set = set(answers_f + answers_r)
    print(f"#{answers_set=}")
    return len(answers_set)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p = int(input().strip())
    for p_itr in range(p):
        n = int(input().strip())
        s1 = input()
        s2 = input()
        result = gridlandProvinces(s1, s2)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

