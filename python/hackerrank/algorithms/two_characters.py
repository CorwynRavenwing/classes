#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from itertools import combinations

def isAlternating(s):
    if len(s) < 2:
        return False
    if s[0] == s[1]:
        return False
    evens = [
        c
        for i, c in enumerate(s)
        if i % 2 == 0
    ]
    odds = [
        c
        for i, c in enumerate(s)
        if i % 2 != 0
    ]
    different_evens = len(list(set(evens)))
    different_odds = len(list(set(odds)))
    if different_evens > 1:
        return False
    if different_odds > 1:
        return False
    return True

def filteredString(s, keep):
    # should return string 's' with
    # all characters deleted unless
    # they are in list 'keep'
    s = list(s)
    s = [
        c
        for c in s
        if c in keep
    ]
    s = ''.join(s)
    return s

# STRING s
# return INTEGER
def alternate(s):
    if isAlternating(s):
        return len(s)
    chars = sorted(list(set(s)))
    print("#C", chars)
    if len(chars) < 2:
        return 0
    answers = []
    for pair in combinations(chars, 2):
        print("#pair", pair)
        check = filteredString(s, pair)
        if isAlternating(check):
            print("#ok", check)
            answers.append(check)
    print("#answers", answers)
    lengths = list(map(len, answers))
    print("#lengths", lengths)
    return max(lengths) if len(lengths) > 0 else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    s = input()
    result = alternate(s)
    fptr.write(str(result) + '\n')
    fptr.close()
