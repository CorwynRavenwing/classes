#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# INT[] cost_y
# INT[] cost_x
# return INT
def boardCutting(cost_y, cost_x):
    cost_x.sort(reverse=True)
    cost_y.sort(reverse=True)
    seg_x = 1
    seg_y = 1
    price = 0
    while (len(cost_x) + len(cost_y)) > 0:
        # print("#C", cost_x, cost_y)
        this_x = (
            cost_x[0]
            if cost_x != []
            else 0
        )
        this_y = (
            cost_y[0]
            if cost_y != []
            else 0
        )
        # print("#T", this_x, this_y)
        if this_x >= this_y:
            if this_x > 0:
                price += this_x * seg_y
                seg_x += 1
                cost_x = cost_x[1:]
                # print("#X", price, [
                #     seg_x,
                #     seg_y,
                # ])
        else:
            if this_y > 0:
                price += this_y * seg_x
                seg_y += 1
                cost_y = cost_y[1:]
                # print("#Y", price, [
                #     seg_x,
                #     seg_y,
                # ])
    return price

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        m = int(first_multiple_input[0])
        n = int(first_multiple_input[1])
        cost_y = list(map(int, input().rstrip().split()))
        cost_x = list(map(int, input().rstrip().split()))
        result = boardCutting(cost_y, cost_x)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

