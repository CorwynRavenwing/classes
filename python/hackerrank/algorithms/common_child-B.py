#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STR s1
# STR s2
# return INT

def show_strings(s1, s2, points):
    if points == []:
        return
    print("#    pts", points)
    p1 = [
        x
        for (x, y, ignore, isgood) in points
    ]
    p2 = [
        y
        for (x, y, ignore, isgood) in points
    ]
    print("#    p1,2", p1, p2)
    c1 = [
        s1[i]
        for i in p1
    ]
    c2 = [
        s2[i]
        for i in p2
    ]
    print("#    c1,2", c1, c2)
    c1 = ''.join(c1)
    c2 = ''.join(c2)
    print("#    c1,2 '{}' '{}'".format(c1, c2))
    return

def commonChild(s1, s2):
    P = (-1, 0, 0, False)
    # -1 here means "just before start of string"
    points = []
    L = len(s1)  # === len(s2)

    max_A = None
    while P is not None or len(points) > 0:
        show_strings(s1, s2, points)
        # print("#LOOP", P)
        if P is None:
            P = points.pop()
            # print("#POP", P)
        (i1, i2, j, is_good) = P
        if is_good:
            i1 += 1
            i2 += 1
            j = i2
        else:
            i1 += 1
            i2 = j
        if i1 >= L:
            # print("#>", i1, L)
            # string s1 ran out
            A = len(points)
            max_A = A if max_A is None else max(A, max_A)
            P = None
            print("#maxA", max_A)
            continue
        try:
            # print("#TRY", i1, i2)
            c1 = s1[i1]
            i2 = s2.index(c1, i2)
            c2 = s2[i2]
            is_good = True
        except IndexError:
            print("#IndexError")
            # i1 not in s1
            c1 = None
            c2 = None
            i2 = None
            is_good = False
        except ValueError:
            # print("#not_found", c1, s2[i2:])
            # not found
            c2 = None
            i2 = None
            is_good = False
        # except Exception:
        #     print("Other exception happened")
        #     pass
        print(
            "#P",
            P,
            (i1, j, i2, is_good),
            (c1, c2),
            (len(points),)
        )
        P = (i1, i2, j, is_good)
        if is_good:
            points.append(P)

    print("#A", max_A)
    return max_A

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

