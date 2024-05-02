#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
def cost(B):
    b = B.pop(0)
    possibles = [
        (1, 0),
        (b, 0),
    ]
    for b in B:
        print(f"#{possibles=}")
        new_possibles = []
        for a in [1, b]:
            print(f"#  try {a=}")
            scores = []
            for (prev_a, prev_score) in possibles:
                new_score = prev_score + abs(a - prev_a)
                print(f"#    {new_score=}")
                scores.append(new_score)
            new_score = max(scores)
            new_poss = (a, new_score)
            print(f"#  {new_poss=}")
            new_possibles.append(new_poss)
        possibles = new_possibles
    print(f"#{possibles=}")
    scores = [
        score
        for prev_a, score in possibles
    ]
    max_score = max(scores)
    print(f"#{max_score=}")
    return max_score

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        B = list(map(int, input().rstrip().split()))
        result = cost(B)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

