#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STRING s
# INTEGER[] queries
# return STRING[]
def weightedUniformStrings(s, queries):
    print("#wUS()", len(s), len(queries))

    # 1. FIND ALL "UNIFORM" SUBSTRINGS
    substrings = {}
    prev_c = None
    prev_c_count = 0
    for c in s:
        if prev_c != c:
            # print("#ss", prev_c, prev_c_count)
            substrings[prev_c] = max(
                prev_c_count,
                substrings.get(prev_c, 0)
            )
            prev_c = c
            prev_c_count = 1
        else:
            prev_c_count += 1
    # now add final substring
    # print("#SS", prev_c, prev_c_count)
    substrings[prev_c] = max(
        prev_c_count,
        substrings.get(prev_c, 0)
    )
    del substrings[None]
    # print("#ALL_SS", substrings)

    # 2. FIND SUBSTRING WEIGHTS
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_weights = dict([
        (c, i+1)
        for i, c in enumerate(alphabet)
    ])
    # print("#LW", letter_weights)

    # 3. CHECK QUERIES
    answers = [
        [
            c + ':' + str(count)
            for c, count in substrings.items()
            if q % letter_weights[c] == 0
            and q // letter_weights[c] <= count
        ]
        for q in queries
    ]
    print("#A", answers)
    answers = [
        'Yes' if len(a) > 0 else 'No'
        for a in answers
    ]
    return answers

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    # fptr.close()

