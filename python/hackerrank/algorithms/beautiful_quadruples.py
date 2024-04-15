#!/bin/python3

import os
# import sys

def beautifulQuadruples(a, b, c, d):
    print(f"#{a=} {b=} {c=} {d=}")
    (a, b, c, d) = sorted([a, b, c, d])
    print(f"#{a=} {b=} {c=} {d=}")
    yesses = 0
    nos = 0
    dups = 0
    seen = set()
    for w in range(1, a+1):
        for x in range(w, b+1):
            for y in range(x, c+1):
                for z in range(y, d+1):
                    attempt = tuple(sorted([w, x, y, z]))
                    ans = w ^ x ^ y ^ z
                    display = (
                        'NO'
                        if ans == 0
                        else 'DUP'
                        if attempt in seen
                        else 'yes'
                    )
                    # print(f"#{w=} {x=} {y=} {z=} {ans=} {display}")
                    if display == 'NO':
                        print(f"#{w=}/{a} {x=}/{b} {y=}/{c} {z=}/{d} {ans=} {display}")
                        print(f"#{w:08b}\n#{x:08b}\n#{y:08b}\n#{z:08b}")
                        print("#" * 20)
                    if not ans:
                        nos += 1
                    elif attempt in seen:
                        dups += 1
                    else:
                        yesses += 1
                    # if ans and attempt not in seen:
                    #     yesses += 1
                    seen.add(attempt)
    print(f"#{yesses=} {nos=} {dups=}")
    return yesses

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

