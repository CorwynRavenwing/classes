#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def update_array(arr, value, index):
    print(f"#  -> AVABI({value},{index})")
    return list([
        val + (value if i != index else 0)
        for i, val in enumerate(arr)
    ])

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
def equal(arr):
    ideas = [(0, tuple(arr))]
    min_answer = None
    answers = []
    while ideas:
        print(f"#{len(ideas)} / {min_answer}")
        # ideas.sort()
        idea = ideas.pop()
        (answer, arr) = idea
        max_arr = max(arr)
        min_arr = min(arr)
        diff = max_arr - min_arr
        print(f"#  N={answer} arr={min_arr}..{max_arr} ({diff})")
        if min_answer is not None and answer > min_answer:
            print(f"#    NOPE, {answer} > {min_answer}")
            continue
        # print(f"#  {diff=}")
        if max_arr - min_arr == 0:
            print(f"#  FOUND ANSWER {answer}")
            answers.append(answer)
            min_answer = min(answers)
            continue
        if diff >= 5:
            copies = diff // 5
            # print(f"#  {5} * {copies}")
            index = arr.index(max_arr)
            new_arr = update_array(arr, 5*copies, index)
            ideas.append((answer + copies, new_arr))
            continue
        elif diff >= 2:
            copies = diff // 2
            # print(f"#  {2} * {copies}")
            index = arr.index(max_arr)
            if copies == 2:
                # if 2 * 2, also try 5 * 1
                # print(f"#  {5} also")
                new_arr = update_array(arr, 5, index)
                ideas.append((answer + 1, new_arr))
            else:
                # if 2 * 1, also try 1 * 1
                # print(f"#  {1} also")
                new_arr = update_array(arr, 1, index)
                ideas.append((answer + 1, new_arr))
            # in any case, do the normal case last:
            new_arr = update_array(arr, 2*copies, index)
            ideas.append((answer + copies, new_arr))
            continue
        elif diff >= 1:
            copies = diff // 1
            # print(f"#  {1} * {copies}")
            index = arr.index(max_arr)
            new_arr = update_array(arr, 1*copies, index)
            ideas.append((answer + copies, new_arr))
            continue
        
    print(f"#{answers=}")
    return str(min(answers))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = equal(arr)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

