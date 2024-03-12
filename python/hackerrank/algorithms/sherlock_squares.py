#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def squares(a, b):
    # print("#A,B", a, b)
    sqrt_a = int(pow(a, 1/2))
    sqrt_b = int(pow(b, 1/2))+1
    # print("#SQRT", sqrt_a, sqrt_b)
    squares_list = [
        n ** 2
        for n in range(sqrt_a, sqrt_b+1)
    ]
    # print("#SQUARES", squares_list)
    answer = [
        i
        for i in squares_list
        if a <= i <= b
    ]
    # answer = [
    #     i
    #     for i in range(a, b+1)
    #     if i in squares_list
    # ]
    # print("#ANS", answer)
    return len(answer)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        print(result)
        # fptr.write(str(result) + '\n')
    # fptr.close()

