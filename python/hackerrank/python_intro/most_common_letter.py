#!/bin/python3

import math
import os
import random
import re
import sys

from operator import itemgetter

if __name__ == '__main__':
    s = input()
    chars = list(s)
    data = {}
    for c in chars:
        if c in data:
            data[c] += 1
        else:
            data[c] = 1
    di = list(data.items())
    # first, sort by letter ASC
    di = sorted(
        di,
        key=itemgetter(0),
    )
    # second, sort by value DESC
    di = sorted(
        di,
        key=itemgetter(1),
        reverse=True
    )
    # third, cut off at three answers
    di = di[:3]
    for k, v in di:
        print(k, v)

