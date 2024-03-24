#!/bin/python3

# import math
import os
# import random
# import re
# import sys
import time
from typing import Dict, List

def highest_value_less_than(V, arr):
    # shortcut if answer is highest value
    top = max(arr)
    if top < V:
        return top
    # normal way instead
    for v in range(V, 0, -1):
        if v in arr:
            return v

first_timestamp = None
previous_timestamp = None
timestamp_dict: Dict[str, List[int]] = {}

def time_profile(label = None, summation = False):
    global first_timestamp
    global previous_timestamp
    global timestamp_dict
    NS_TO_MS = 1_000_000
    MS_TO_SECONDS = 1_000
    if summation:
        if label is None:
            label = 'SUMMATION'
        print(f"#TIMER {label}")
        max_ns = max([
            data_list[0]
            for data_list in timestamp_dict.values()
        ])
        max_count = max([
            data_list[1]
            for data_list in timestamp_dict.values()
        ])
        ns_width = len(str(max_ns))
        width = len(str(max_count))
        for label, timestamp_list in timestamp_dict.items():
            diff_ms, count = timestamp_list
            diff_sec = round(diff_ms / MS_TO_SECONDS, 2)
            time_diff = f"{diff_sec:{ns_width}.2f}"
            count_diff = f"{count:{width}d}"
            print(f"#TIMER    {time_diff} {count_diff} {label}")
            # should print grand-total-time here
        return
    MIN_DIFF = 0.1
    timestamp = time.perf_counter_ns()
    if label is None:
        label = 'no label'
    if previous_timestamp is not None:
        diff_ns = timestamp - previous_timestamp
        diff_ms = diff_ns // NS_TO_MS
        diff_sec = round(diff_ms / MS_TO_SECONDS, 2)
        if diff_sec >= MIN_DIFF:
            print(f"#TIMER {diff_sec:.2f} {label}")
        timestamp_dict.setdefault(label, [0, 0])
        timestamp_dict[label][0] += diff_ms
        timestamp_dict[label][1] += 1
    previous_timestamp = timestamp
    return

# INT[] x
# INT k
# return INT
def hackerlandRadioTransmitters(x, k):
    time_profile('begin')
    time_profile('sorting')
    x.sort()
    time_profile('sort complete')
    # print(f"{k=} {x=}")
    transmitters = 0
    while len(x):
        time_profile('begin loop')
        print(f"#{k=} {len(x)=}")
        h1 = x[0]
        time_profile('calling HVLT for T')
        t = highest_value_less_than(h1+k, x)
        time_profile('got T')
        print(f"#{t=}")
        transmitters += 1

        time_profile('calling HVLT for TOR')
        top_of_range = highest_value_less_than(t+k, x)
        time_profile('got TOR')
        # print(f"{k=} {x=}")
        top_index = x.index(top_of_range)

        time_profile('split range')
        out_of_range = x[top_index:]
        time_profile('range split; popping')
        while out_of_range and out_of_range[0] == top_of_range:
            ignore = out_of_range.pop(0)
            print("#POP", ignore)
        time_profile('done popping')
        # print(f"#{in_range=}")
        print(f"#{out_of_range[0:10]=}")
        time_profile('setting x')
        x = out_of_range
        time_profile('X is set')
    print(f"#{transmitters}")
    time_profile('SUMMATION', True)
    return transmitters

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    x = list(map(int, input().rstrip().split()))
    result = hackerlandRadioTransmitters(x, k)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

