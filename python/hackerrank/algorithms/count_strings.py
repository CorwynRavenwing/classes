#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def regex_to_parsed(R):
    assert R
    first = R[0]
    rest = R[1:]
    if first == 'a':
        return (('a',), rest)
    if first == 'b':
        return (('b',), rest)
    if first == '(':
        first_obj, rest = regex_to_parsed(rest)
        assert rest
        second = rest[0]
        if second == '|':
            command = 'PIPE'
            second_obj, rest = regex_to_parsed(rest[1:])
        elif second == '*':
            command = 'STAR'
            second_obj, rest = None, rest[1:]
        else:
            command = 'CONCAT'
            # note: next line is NOT rest[1:]
            second_obj, rest = regex_to_parsed(rest)
        assert rest
        third = rest[0]
        assert third == ')'
        rest = rest[1:]
        retval = (command, first_obj, second_obj)
        return (retval, rest)
    raise Exception(f"Invalid first character '{first}' in parseRegex()")
    pass

cache_state: int = 0

def clear_state():
    global cache_state
    cache_state = 0

def next_state():
    global cache_state
    cache_state += 1
    return str(cache_state)

def parsed_to_NFA_transitions(parsed, fromState, toState):
    if parsed is None:
        # shouldn't actually be called anymore
        return []
    if len(parsed) == 1:
        letter = parsed[0]
        return [(fromState, letter, toState)]
    (command, first_obj, second_obj) = parsed

    if command == 'PIPE':
        first_detail = parsed_to_NFA_transitions(first_obj, fromState, toState)
        second_detail = parsed_to_NFA_transitions(second_obj, fromState, toState)
        return (
            first_detail + second_detail
        )
    elif command == 'STAR':
        first_detail = parsed_to_NFA_transitions(first_obj, fromState, toState)
        epsilon = [(toState, '', fromState)]
        return (
            first_detail + epsilon
        )
    elif command == 'CONCAT':
        midState = next_state()
        first_detail = parsed_to_NFA_transitions(first_obj, fromState, midState)
        second_detail = parsed_to_NFA_transitions(second_obj, midState, toState)
        return (
            first_detail + second_detail
        )
    else:
        raise Exception(f"Invalid command '{command}' in regexCount")

def parsed_to_NFAe(parsed):
    initialState = 'S'
    finalState = 'E*'
    clear_state()
    transitions = parsed_to_NFA_transitions(parsed, initialState, finalState)
    NFAe = (transitions, initialState)
    return NFAe

def updateStateNames(transitions, oldStateName, newStateName):
    transitions = [
        (
            (newStateName if fromState == oldStateName else fromState),
            letter,
            (newStateName if toState == oldStateName else toState),
        )
        for (fromState, letter, toState) in transitions
    ]
    return list(transitions)

def NFA_remove_epsilons(NFAe):
    (transitions, initialState) = NFAe
    epsilons = list([
        (fromState, link, toState)
        for (fromState, link, toState) in transitions
        if link == ''
    ])
    transitions = list([
        T
        for T in transitions
        if T not in epsilons
    ])
    while epsilons:
        (oldName, link, newName) = epsilons.pop(0)
        # print(f"#EPSILON {oldName} {newName}")
        transitions = updateStateNames(transitions, oldName, newName)
        epsilons = updateStateNames(epsilons, oldName, newName)
        if initialState == oldName:
            initialState = newName
        if '*' in oldName:
            if '*' not in newName:
                oldName2 = newName
                newName2 = newName + '*'
                if initialState == oldName2:
                    initialState = newName2
                # print(f"#EPSILON2 {oldName2} {newName2}")
                transitions = updateStateNames(transitions, oldName2, newName2)
                epsilons = updateStateNames(epsilons, oldName2, newName2)
    return (transitions, initialState)

def NFA_letters_available(NFA_transitions, fromStates):
    letters = [
        L
        for (fS, L, tS) in NFA_transitions
        if fS in fromStates
    ]
    letters = list(sorted(list(set(letters))))
    return letters

def NFA_destination_states(NFA_transitions, fromStates, letter):
    toStates = [
        tS
        for fromState in fromStates
        for (fS, L, tS) in NFA_transitions
        if fS == fromState and L == letter
    ]
    toStates = tuple(sorted(list(set(toStates))))
    return toStates

def NFA_to_DFA(NFA):
    (NFA_transitions, initialState) = NFA
    DFA_transitions = []
    known_states = {initialState}
    work_states = [(initialState, (initialState,))]
    while work_states:
        this_work = work_states.pop(0)
        (fromStateName, fromStates) = this_work
        # print(f"#FROM: {fromStateName} {fromStates}")
        letters = NFA_letters_available(NFA_transitions, fromStates)
        # print(f"#  {letters=}")
        for letter in letters:
            # print(f"#  {letter}:")
            toStates = NFA_destination_states(NFA_transitions, fromStates, letter)
            # print(f"#    {toStates=}")
            toStateName = ','.join(toStates)
            DFA_transitions.append(
                (fromStateName, letter, toStateName)
            )
            if toStateName not in known_states:
                known_states.add(toStateName)
                work_states.append(
                    (toStateName, toStates)
                )
    return (DFA_transitions, initialState)

def DFA_possible_destinations(DFA_transitions, fromState):
    dest = [
        tS
        for (fS, L, tS) in DFA_transitions
        if fS == fromState
    ]
    return list(dest)

def DFA_count_strings(DFA, L):
    (DFA_transitions, initialState) = DFA
    states = {initialState: 1}
    for i in range(L):
        # print(f"#{i+1}/{L} {len(states)=}")
        print(f"#{i+1}/{L} {states=}")
        new_states = {}
        for fromState, count in states.items():
            print(f"#  FROM {fromState} {count}")
            toStates = DFA_possible_destinations(DFA_transitions, fromState)
            for toState in toStates:
                new_states.setdefault(toState, 0)
                new_states[toState] += count
                print(f"#    TO {toState} {new_states[toState]}")
        states = new_states
    print(f"#{states=}")
    terminal_states = tuple([
        count
        for state, count in states.items()
        if '*' in state
    ])
    print(f"#{terminal_states=}")
    return sum(terminal_states)

def print_machine(label, machine):
    (transitions, initialState) = machine
    print(f"#**{label}**")
    print(f"#Initial: {initialState}")
    print("#" + "\n#".join(map(str, transitions)))
    pass

# The function is expected to return an INTEGER.
#  1. STRING R
#  2. INTEGER L
def countStrings(R, L):
    print(f"#{R=} {L=}")
    parsed, rest = regex_to_parsed(R)
    print(f"#  {parsed=} {rest=}")

    NFAe = parsed_to_NFAe(parsed)
    # print_machine('NFAe', NFAe)

    NFA = NFA_remove_epsilons(NFAe)
    # print_machine('NFA', NFA)

    DFA = NFA_to_DFA(NFA)
    print_machine('DFA', DFA)

    count_strings = DFA_count_strings(DFA, L)
    return count_strings

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

