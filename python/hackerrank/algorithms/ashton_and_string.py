#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STR s
# INT k
# return CHAR
def ashtonString(s, k):
    in_progress = []
    current = [
        '',
        0,
        range(len(s))
    ]
    while current != [] or in_progress != []:
        # print("#DEBUG", in_progress)
        if current == []:
            current = in_progress[0]
            in_progress = in_progress[1:]
        (ss, L, positions) = current
        current = []
        # print("#SS", k, ss, L, positions)
        if k <= L:
            letter = ss[k-1]    # 1-indexed
            # print("#FOUND '{}' at pos {} of '{}'"
            #         .format(letter, k, ss)
            # )
            return letter
        else:
            # print("#consume L from K", L, k)
            k -= L

        ### can shortcut here if len(positions) == 1 ###

        new = dict()
        L += 1
        for pos in positions: 
            ss = s[pos:pos+L]
            # print("#found", pos, L, ss)
            new[ss] = new.get(ss, [])
            new[ss].append(pos)

        if len(ss) < L:
            # only need to check the last one
            # print("#delete SS, too short", len(ss), '<', L)
            del new[ss]

        K = new.keys()
        K = sorted(K)

        new_list = [
            [
                ss,
                L,
                new[ss]
            ]
            for ss in K
        ]
        # print("#ADD new list to front", len(new_list))
        in_progress = new_list + in_progress

    # print("#FAIL")
    return None

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        k = int(input().strip())
        res = ashtonString(s, k)
        print(str(res))
        # fptr.write(str(res) + '\n')
    # fptr.close()

