#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# INT[] arr
# return INT
def lilysHomework(arr):
    # shortcut 1: a "beautiful" array
    # === "an array which is either sorted, or sorted in reverse"
    
    # shortcut 2: "number of swaps required to change A to A-prime"
    # (assuming each is doing some actual work, rather than undoing it)
    # is commutative and associative: i.e. we don't have to work to
    # discover the *best* order of swapping, we just pick one that works
    
    # shortcut 3: "number of swaps to change A to A-prime"
    # === "number of swaps to change A-prime to A"
    
    # shortcut 4: "distinct integers" means we can make a dictionary
    # of numbers to indexes without reusing any
    
    forward_array = sorted(arr)
    backward_array = list(reversed(forward_array))
    forward_index = dict()
    backward_index = dict()
    for i, e in enumerate(forward_array):
        forward_index[e] = i
    # could combine these by setting "back[e] = LEN - i" here?
    for i, e in enumerate(backward_array):
        backward_index[e] = i
    forward_swaps = 0
    backward_swaps = 0
    for i, e in enumerate(arr):
        print("#I,E", i, e)
        if forward_index[e] != i:
            e_prime = forward_array[i]
            i_prime = forward_index[e]
            forward_array[i] = e
            forward_index[e] = i
            forward_array[i_prime] = e_prime
            forward_index[e_prime] = i_prime
            forward_swaps += 1
            print("#FWD", [i, i_prime], [e, e_prime])
        if backward_index[e] != i:
            e_prime = backward_array[i]
            i_prime = backward_index[e]
            backward_array[i] = e
            backward_index[e] = i
            backward_array[i_prime] = e_prime
            backward_index[e_prime] = i_prime
            backward_swaps += 1
            print("#BACK", [i, i_prime], [e, e_prime])
    print("#SWAPS:", forward_swaps, backward_swaps)
    return min(forward_swaps, backward_swaps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = lilysHomework(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

