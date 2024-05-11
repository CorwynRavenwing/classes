#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from typing import Dict

thingy: Dict[str,Dict] = {}
# print(f"#I {thingy=}")

def insert_string_into_thingy(s: str) -> int:
    global thingy
    ptr = thingy
    # print(f"#insert_thingy({s})")
    retval = 0
    # print(f"#T {ptr=}")
    while s:
        retval += 1
        firstchar = s[0]
        s = s[1:]
        # print(f"#  '{firstchar}'+'{s}'")
        ptr.setdefault(firstchar, {})
        ptr = ptr[firstchar]
        # print(f"#S {ptr=}")
    # print(f"#E {thingy=}")
    return retval

def numberize_pointer(ptr: dict, level=0) -> int:
    if not ptr:
        # returned value DOES include the top level
        return 1
    ptr.setdefault('#', 0)
    # this count DOES NOT include the top level
    answer = 0
    # print(f"#{' ' * level}?{answer}")
    for (char, subPtr) in ptr.items():
        if char == '#':
            continue
        # print(f"#{' ' * (level+1)}'{char}'")
        answer += numberize_pointer(subPtr, level+1)
        # print(f"#{' ' * (level+1)}={answer}")
    # print(f"#{' ' * level}={ptr['#']}->{answer}")
    ptr['#'] = answer
    # answer DOES include top level
    return answer + 1

def numberize_thingy():
    global thingy
    print("#numberize_thingy()")
    # print(f"#0 {thingy=}")
    total = numberize_pointer(thingy)
    print(f"#{total=}")
    # print(f"#N {thingy=}")
    return

def show_detail(ptr, level):
    if not ptr:
        return
    total = None
    for (val, subPtr) in ptr.items():
        if val == '#':
            total = subPtr
            continue
        print(f"#{' ' * level}'{val}'")
        show_detail(subPtr, level + 1)
    print(f"#{' ' * level}#: {total}")
    return

def show_thingy():
    global thingy
    show_detail(thingy, 0)
    pass

def all_strings(ptr=None, parent=""):
    global thingy
    if ptr is None:
        ptr = thingy
    retval = []
    for (val, subPtr) in sorted(ptr.items()):
        if val == '#':
            continue
        this_string = parent + val
        retval.append(this_string)
        if subPtr:
            retval.extend(all_strings(subPtr, this_string))
    return retval

def Nth_string_recurse(N, ptr=None, parent=""):
    print(f"#{N=}")
    for (val, subPtr) in sorted(ptr.items()):
        if val == '#':
            continue
        N -= 1
        this_string = parent + val
        if N == 0:
            return (0, this_string)
        if subPtr:
            count = subPtr['#']
            if count < N:
                N -= count
                print(f"#Skipping '{this_string}' {count}: {N}")
                continue
            else:
                retval = (Nth_string_recurse(N, subPtr, this_string))
                (newN, string) = retval
                if newN == 0:
                    return retval
                else:
                    N = newN
    return (N, '')

def Nth_string(N):
    global thingy
    print(f"#Nth_string({N}):")
    retval = Nth_string_recurse(N, thingy, '')
    (N, answer) = retval
    if N == 0:
        return answer
    else:
        return "INVALID"

# The function is expected to return a STR[]
#  1. STR[] w
#  2. INT[] queries
def findStrings(w, queries):
    w.sort()
    for s in w:
        while s:
            insert_string_into_thingy(s)
            s = s[1:]
    # print(f"#X {thingy=}")
    numberize_thingy()
    # show_thingy()
    # strings = all_strings()
    # print(f"#{strings=}")
    retval = list([
        Nth_string(Q)
        # (
        #     strings[Q - 1]
        #     if (Q - 1) < len(strings)
        #     else 'INVALID'
        # )
        for Q in queries
    ])
    return retval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    w_count = int(input().strip())
    w = []
    for _ in range(w_count):
        w_item = input()
        w.append(w_item)
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = findStrings(w, queries)
    print('\n'.join(result))
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    # fptr.close()

