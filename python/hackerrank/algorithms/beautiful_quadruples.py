#!/bin/python3

import os
# import sys

def beautifulQuadruples(a, b, c, d):
    print(f"#{a=} {b=} {c=} {d=}")
    retval = 0
    seen = set()
    for w in range(1, a+1):
        for x in range(1, b+1):
            for y in range(1, c+1):
                for z in range(1, d+1):
                    attempt = tuple(sorted([w, x, y, z]))
                    ans = w ^ x ^ y ^ z
                    display = (
                        'NO'
                        if ans == 0
                        else 'DUP'
                        if attempt in seen
                        else 'yes'
                    )
                    print(f"#{w=} {x=} {y=} {z=} {ans=} {display}")
                    if ans and attempt not in seen:
                        retval += 1
                    seen.add(attempt)
    return retval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    abcd = input().split()
    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])
    result = beautifulQuadruples(a, b, c, d)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

