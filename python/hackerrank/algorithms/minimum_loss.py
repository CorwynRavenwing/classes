#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# return INT
# LONGINT[] price
def minimumLoss(price):
    # loss = [
    #     buy - sell
    #     for i, buy in enumerate(price[:-1])
    #     for j, sell in enumerate(price[i+1:])
    #     # if i < j
    #     if buy > sell
    # ]
    # return min(loss)

    min_loss = None
    # for i, buy in enumerate(price[:-1]):
    L = len(price)
    for i in range(L-1):
        buy = price[i]
        print("#I", i)
        # for j, sell in enumerate(price[i+1:]):
        for j in range(i+1, L):
            sell = price[j]
            # if i >= j:
            #     continue
            # print("#J", i, j)
            if buy <= sell:
                continue
            loss = buy - sell
            # print("#L", i, j, loss)
            if min_loss is None or min_loss > loss:
                min_loss = loss
                print("#M", i, j, min_loss, "*" * 20)
    return min_loss

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    price = list(map(int, input().rstrip().split()))
    result = minimumLoss(price)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

