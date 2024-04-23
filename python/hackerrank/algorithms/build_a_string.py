#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# The function is expected to return an INTEGER.
#  1. INTEGER a
#  2. INTEGER b
#  3. STRING s
def buildString(a, b, s):
    print(f"#buildString({a},{b},{s})")
    # add-one-letter cost: A
    # copy-any-substring cost: B
    cost = 0
    s_built = ''
    index = 0
    while len(s_built) < len(s):
        char = s[index]
        print(f"#'{s_built}' {cost=} {index=} {char=}")
        if char not in s_built:
            print(f"#append '{char}' for ${a}")
            cost += a
            s_built += char
            index += 1
        else:
            # print(f"#    '{char}' ")
            length = 0
            while s[index:index+length+1] in s_built:
                if len(s[index:index+length+1]) != length + 1:
                    # we've hit the end of the source string 's'
                    break
                length += 1
            print(f"#  '{s[index:index+length]}' in '{s_built}'")
            block = s[index:index+length]
            LB = len(block)
            if b < a * LB:
                print(f"#copy '{block}' for ${b}")
                cost += b
                s_built += block
                index += LB
            else:
                print(f"#append '{block[0]}' for ${a} after all")
                cost += a
                s_built += char
                index += 1
    if s_built != s:
        print(f"#ERROR: '{s_built}' != '{s}'")
        exit()
    return str(cost)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        (n, a, b) = map(int, input().strip().split(' '))
        s = input()
        result = buildString(a, b, s)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

