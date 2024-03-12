#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STRING s
# INTEGER k
# return STRING
def caesarCipher(s, k):
    print("#cC()", s, k)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    k = k % len(alphabet)
    print("#k", k)
    cypher = alphabet[k:] + alphabet[:k]
    pairs = zip(alphabet, cypher)
    lookup = dict(pairs)
    # print("#", alphabet)
    print("#", cypher)
    # print("#", lookup)
    r = []
    for c in s:
        if c.islower():
            d = lookup[c]
        elif c.isupper():
            d = lookup[
                c.lower()
            ].upper()
        else:
            d = c
        r.append(d)
    # print("#r", r)
    return ''.join(r)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    # fptr.write(result + '\n')
    print(result)
    # fptr.close()

