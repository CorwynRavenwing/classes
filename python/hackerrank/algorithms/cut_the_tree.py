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
    while edges:
        print(f"#edges={len(edges)}")
        # print(f"#{list(zip(*edges))[:10]=}")
        # print(f"#{list(map(list, zip(*edges)))[:10]=}")
        E = list(map(list, zip(*edges)))
        endpoints = E[0] + E[1]
        # print(f"#{endpoints[:10]=}")
        endpoint_counter = Counter(endpoints)
        # print(f"#{tuple(endpoint_counter)[:10]=}")
        leaf_nodes = [
            node
            for node, count in endpoint_counter.items()
            if count == 1
        ]
        print(f"#\tleaf_nodes={len(leaf_nodes)}")
        leaf_edges = {
            node: edge
            for node in leaf_nodes
            for edge in edges
            if node in edge
        }
        # print(f"#{list(leaf_edges)[:10]=}")
        # print(f"# B ##{edges[:10]=}")

        # PASS 1: every leaf edge -> answers
        for node, edge in leaf_edges.items():
            value = data[node-1]
            other_half = total_tree_value - value
            answers.append(
                abs(other_half - value)
            )

        # PASS 2: leaf edge data -> other node
        for node, edge in leaf_edges.items():
            (A, B) = edge
            other_node = (
                A if node == B else B
            )
            # print(f"#{node=} {other_node=} {edge=}")
            # print(
            #     f"#data {data[node-1]} ",
            #     f"{data[other_node-1]}", end=" -> "
            # )
            data[other_node-1] += data[node-1]
            data[node-1] = 0
            # print(
            #     f"# {data[node-1]} ",
            #     f"{data[other_node-1]}"
            # )

        # pass 3: delete edge
        for node, edge in leaf_edges.items():
            if edge in edges:
                # last pair will both be leaf nodes
                # can't delete edge twice
                edges.remove(edge)

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

