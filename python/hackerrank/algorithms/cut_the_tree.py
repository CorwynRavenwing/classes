#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

# INT[] data
# INT[][] edges
# return INT
def cutTheTree(data, edges):
    total_tree_value = sum(data)
    print(f"#{total_tree_value=}")
    answers = []
    print(f"#{edges=}")
    print(f"#{list(zip(*edges))=}")
    print(f"#{list(map(list, zip(*edges)))=}")
    E = list(map(list, zip(*edges)))
    endpoints = E[0] + E[1]
    print(f"#{endpoints=}")
    endpoint_counter = Counter(endpoints)
    print(f"#{endpoint_counter=}")
    leaf_nodes = [
        node
        for node, count in endpoint_counter.items()
        if count == 1
    ]
    print(f"#{leaf_nodes=}")
    leaf_edges = {
        node: (A, B)
        for node in leaf_nodes
        for A, B in edges
        if A == node or B == node
    }
    print(f"#{leaf_edges=}")

    exit()

    pass

    for edge in edges:
        print(f"#{edge=}")
        edges_test = edges.copy()
        edges_test.remove(edge)
        group = []
        check = [1]
        while check:
            group.extend(check)
            check = [
                B
                for A, B in edges_test
                if A in check and B not in group
            ] + [
                A
                for A, B in edges_test
                if B in check and A not in group
            ]
            print(f"#{len(group)=} {len(check)=}")
        value_without_edge = [
            data[node-1]
            for node in group
        ]
        value_without_edge = sum(value_without_edge)
        print(f"#{value_without_edge=}")
        other_half = total_tree_value - value_without_edge
        answers.append(
            abs(other_half - value_without_edge)
        )
    print(f"#{answers=}")
    return min(answers)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))
    result = cutTheTree(data, edges)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

