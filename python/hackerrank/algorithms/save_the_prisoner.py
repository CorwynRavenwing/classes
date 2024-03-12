#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def saveThePrisoner(n, m, s):
    # print("pris={} candy={} chair={}".format(n, m, s))
    last_candy = s+m-1
    # candies = range(s, s+m)
    # print("#candies", tuple(candies))
    # print("#last candy", last_candy)
    # seats = [
    #     ((_-1) % n) + 1
    #     for _ in candies
    # ]
    last_seat = ((last_candy-1) % n) + 1
    # print("#seats", seats)
    # print("#seat", last_seat)
    # prisoner = seats[-1]
    prisoner = last_seat
    # print("#pris", prisoner)
    return prisoner

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        s = int(first_multiple_input[2])
        result = saveThePrisoner(n, m, s)
        # fptr.write(str(result) + '\n')
        print(result)
    # fptr.close()

