#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def str_rev(S):
    return ''.join(reversed(list(S)))

# The function is expected to return a STRING.
#  1. STRING a
#  2. STRING b
def buildPalindrome(a, b):
    reversed_b = str_rev(b)
    checksum = 2 * min(len(a), len(b)) + 1
    print(f"#{a=} {reversed_b=}")
    best_answer = ''
    to_check = [(checksum, '', a, reversed_b)]
    while to_check:
        # print(f"#{to_check=}")
        to_check.sort()
        print(f"#{len(to_check)=}")
        check = to_check.pop(0)
        print(f"#  ({len(best_answer)}) {check=}")
        (checksum, palin, a_part, b_part) = check
        if not a_part and not b_part:
            if not palin:
                # print(f"#    X '{palin}' N:''")
                continue
            result = palin + str_rev(palin)
            # print(f"#    ANSWER: {result}")
            if len(result) < len(best_answer):
                # print(f"#    FAIL: {len(result)=} < {len(best_answer)=}")
                continue
            if len(result) == len(best_answer):
                if result > best_answer:
                    # print(f"#    FAIL: {result} > {best_answer}")
                    continue
            print(f"#    SUCCESS: {result}:{best_answer}")
            best_answer = result
            continue
        if a_part and not b_part:
            if not palin:
                # print(f"#    X '{palin}' A:{a_part}")
                continue
            result = palin + min(list(a_part)) + str_rev(palin)
            # print(f"#    ANSWER: {result}")
            if len(result) < len(best_answer):
                # print(f"#    FAIL: {len(result)=} < {len(best_answer)=}")
                continue
            if len(result) == len(best_answer):
                if result > best_answer:
                    # print(f"#    FAIL: {result} > {best_answer}")
                    continue
            print(f"#    SUCCESS: {result}:{best_answer}")
            best_answer = result
            continue
        if b_part and not a_part:
            if not palin:
                # print(f"#    X '{palin}' B:{b_part}")
                continue
            result = palin + min(list(b_part)) + str_rev(palin)
            # print(f"#    ANSWER: {result}")
            if len(result) < len(best_answer):
                # print(f"#    FAIL: len({result}) < len({best_answer})")
                continue
            if len(result) == len(best_answer):
                if result > best_answer:
                    # print(f"#    FAIL: {result} > {best_answer}")
                    continue
            print(f"#    SUCCESS: {result}:{best_answer}")
            best_answer = result
            continue
        if checksum < len(best_answer):
            print(f"#    XXXX {checksum=} < {len(best_answer)}")
            continue
        letters_in_a = list(set(a_part))
        # print(f"#    {letters_in_a=}")
        for letter in letters_in_a:
            if letter not in b_part:
                # print(f"#    {letter} not in B")
                continue
            new_palin = palin+letter
            a_index = a_part.index(letter)
            b_index = b_part.index(letter)
            new_a = a_part[a_index+1:]
            new_b = b_part[b_index+1:]
            new_checksum = 2 * (len(new_palin) + min(len(new_a), len(new_b))) + 1
            new_check = (new_checksum, new_palin, new_a, new_b)
            # print(f"#    -> {new_check}")
            to_check.append(new_check)
        new_checksum = 2 * len(palin) + 1
        if new_checksum < len(best_answer):
            print(f"#    ZZZZ {checksum=} < {len(best_answer)}")
            continue
        # min(len(''),len(b_part)) === 0, therefore this term falls out
        new_check = (new_checksum, palin, '', b_part)
        # print(f"#    => {new_check}")
        to_check.append(new_check)
        pass
    print(f"#{best_answer=}")
    if not best_answer:
        return str(-1)
    return best_answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        a = input()
        b = input()
        result = buildPalindrome(a, b)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

