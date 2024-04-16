#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# The function is expected to return a STRING.
#  1. STRING a
#  2. STRING b
def morganAndString(a, b):
    print(f"#{a=} {b=}")
    check = [('', a, b)]
    while check:
        check.sort()
        T = check.pop(0)
        # print(f"#  {T=}")
        output, jack, daniel = T
        # if check:
        #     check = [
        #         (O, J, D)
        #         for O, J, D in check
        #         if O == output
        #     ]
        LC = len(check)
        print(f"# {LC}: ({output[:20]},{jack[:20]},{daniel[:20]})")
        if not jack and not daniel:
            print(f"#  -> YES {output}")
            return output
        if not jack:
            T = (output + daniel, jack, '')
            check.append(T)
            continue
        if not daniel:
            T = (output + jack, '', daniel)
            check.append(T)
            continue
        J = jack[0]
        D = daniel[0]
        if J <= D:
            T = (output + J, jack[1:], daniel)
            check.append(T)
        # YES, when J == D, these will both fire
        if J >= D:
            T = (output + D, jack, daniel[1:])
            check.append(T)
    pass
    return 'XYZ'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        a = input()
        b = input()
        result = morganAndString(a, b)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()

