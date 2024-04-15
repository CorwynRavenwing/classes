#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    print(f"#rSM(): {s=}")
    counts = Counter(s)
    print(f"#{counts=}")
    groups = [
        letter * (count // 2)
        for letter, count in counts.items()
    ]
    letters = ''.join(groups)
    reversed_letters = ''.join(reversed(groups))
    reversed_s = ''.join(list(reversed(s)))
    print(f"#  {letters=} {reversed_letters=} {reversed_s=}")
    check = [('', letters, reversed_s)]
    while check:
        print(f"#CHECK:{len(check)}")
        T = check.pop()
        (before, after, string) = T
        print(f"#  {T}")
        if not after:
            # print(f"#  --> OK '{before}'")
            return before
        if len(after) > len(string):
            # print("#  --> NOPE")
            continue
        # if after and not string:
        #     print("#  --> NOPE")
        #     continue
        if set(after) - set(string):
            print(f"# {set(after) - set(string)}")
            continue
        count_after = Counter(after)
        count_string = Counter(string)
        too_many = [
            letter + ':' + str(count - count_string[letter])
            for letter, count in count_after.items()
            if count > count_string[letter]
        ]
        if too_many:
            print(f"# {too_many}")
            continue
        for letter in sorted(set(after), reverse=True):
            # print(f"#  L={letter}")
            if letter not in string:
                # print(f"    -> {None}")
                continue
            string_index = string.index(letter)
            after_index = after.index(letter)
            new_before = before + letter
            new_after = after[:after_index] + after[after_index+1:]
            new_string = string[string_index+1:]
            T = (new_before, new_after, new_string)
            check.append(T)
            # print(f"#    -> {T}")
        pass
    return ''

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = reverseShuffleMerge(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()

