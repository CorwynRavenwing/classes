#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# INTEGER p
# INTEGER d
# INTEGER m
# INTEGER s
# return INTEGER

def howManyGames(p, d, m, s):
    print("#hMG()", p, d, m, s)
    games = 0
    money = s
    price = p
    while price <= money:
        print("#G", games, money, price)
        games += 1
        money -= price
        price -= d
        if price < m:
            price = m
    print("#G", games, money, price)
    return games

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])
    answer = howManyGames(p, d, m, s)
    print(str(answer))
    # fptr.write(str(answer) + '\n')
    # fptr.close()

