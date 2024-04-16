#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def parseRegex(R):
    assert R
    first = R[0]
    rest = R[1:]
    if first == 'a':
        return (('a',), rest)
    if first == 'b':
        return (('b',), rest)
    if first == '(':
        first_obj, rest = parseRegex(rest)
        assert rest
        second = rest[0]
        if second == '|':
            command = 'PIPE'
            second_obj, rest = parseRegex(rest[1:])
        elif second == '*':
            command = 'STAR'
            second_obj, rest = None, rest[1:]
        else:
            command = 'CONCAT'
            # note: next line is NOT rest[1:]
            second_obj, rest = parseRegex(rest)
        assert rest
        third = rest[0]
        assert third == ')'
        rest = rest[1:]
        retval = (command, first_obj, second_obj)
        return (retval, rest)
    raise Exception(f"Invalid first character '{first}' in parseRegex()")
    pass

def regex_pipe(thing1, thing2, L):
    return tuple(set(thing1 + thing2))

def regex_star(thing1, L):
    possibles = {''}    # empty string always matches star
    new_possibles = possibles.copy()
    while new_possibles:
        # print(f"#  {new_possibles=}")
        matches = tuple(new_possibles)
        this_matches = regex_concat(matches, thing1, L)
        this_possibles = set(this_matches)
        new_possibles = this_possibles - possibles
        possibles |= new_possibles
    return tuple(possibles)

def regex_concat(thing1, thing2, L):
    return tuple(
        T1 + T2
        for T1 in thing1
        for T2 in thing2
        if len(T1) + len(T2) <= L
    )

def regexCount(parsed, L):
    if parsed is None:
        return None
    if len(parsed) == 1:
        return parsed
    (command, first_obj, second_obj) = parsed
    first_detail = regexCount(first_obj, L)
    second_detail = regexCount(second_obj, L)
    if command == 'PIPE':
        return regex_pipe(first_detail, second_detail, L)
    elif command == 'STAR':
        return regex_star(first_detail, L)
    elif command == 'CONCAT':
        return regex_concat(first_detail, second_detail, L)
    else:
        raise Exception(f"Invalid command '{command}' in regexCount")

# The function is expected to return an INTEGER.
#  1. STRING R
#  2. INTEGER L
def countStrings(R, L):
    print(f"#{R=} {L=}")
    parsed, rest = parseRegex(R)
    print(f"#  {parsed=} {rest=}")
    strings = regexCount(parsed, L)
    strings = tuple(sorted([
        S
        for S in strings
        if len(S) == L
    ]))
    print(f"#  {strings=}")
    return len(strings)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = first_multiple_input[0]
        L = int(first_multiple_input[1])
        result = countStrings(R, L)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

