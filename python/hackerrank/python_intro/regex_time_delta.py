#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    #   Day dd Mon yyyy hh:mm:ss +xxxx"
    fmt = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(t1, fmt)
    d2 = datetime.strptime(t2, fmt)
    #print("#D1", d1)
    #print("#D2", d2)
    delta = d1 - d2
    #print("#DIFF", type(delta), delta)
    sec = delta.total_seconds()
    #print("#SEC", sec)
    return str(int(abs(sec)))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        #fptr.write(delta + '\n')
        print(delta)

    #fptr.close()

