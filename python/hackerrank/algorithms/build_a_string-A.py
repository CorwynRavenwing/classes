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
    # add one letter cost: A
    # copy any substring cost: B
    cost = 0
    string = ''
    index = 0
    while len(string) < len(s):
        print(f"#'{string}'")
        char = s[index]
        if char not in string:
            print(f"#append '{char}' for ${a}")
            cost += a
            string += char
            index += 1
        else:
            length = 0
            while s[index:index+length+1] in string:
                length += 1
            block = s[index:index+length]
            print(f"#copy '{block}' for ${b}")
            cost += b
            string += block
            index += len(block)
    if string != s:
        print(f"#ERROR: '{string}' != '{s}'")
        exit()
    return cost

if __name__ == '__main__':
    print("#0")
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    print(f"#1 {t=}")
    for t_itr in range(t):
        print("#2")
        # first_multiple_input = input().rstrip().split()
        n, a, b = map(int,input().rstrip().split(' '))
        # print(f"#3 {first_multiple_input=}")
        # n = int(first_multiple_input[0])
        # a = int(first_multiple_input[1])
        # b = int(first_multiple_input[2])
        print(f"#4 {n=} {a=} {b=}")
        s = input().strip()
        print(f"#5 {s=}")
        result = buildString(a, b, s)
        print(f"#6")
        print(result)
        print("#7")
        # fptr.write(result + '\n')
    # fptr.close()
    print("#8")

