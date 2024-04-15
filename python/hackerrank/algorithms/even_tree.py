#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    print(f"#evenForest() {t_nodes=} {t_edges=} {t_from=} {t_to=}")
    weights = ['Z'] + [1] * t_nodes
    print(f"#{weights=}")
    endpoints = sorted(t_from + t_to)
    edges = list(zip(t_from, t_to))
    print(f"#{edges=} {endpoints=}")
    groups = []
    edges_keep = []
    edges_cut = []
    endpoint_count = Counter(endpoints)
    print(f"#{endpoint_count=}")
    edges_by_endpoint = {
        key: [
            edge
            for edge in edges
            if key in edge
        ]
        for key in endpoint_count.keys()
    }
    print(f"#{edges_by_endpoint=}")
    edges_work = edges.copy()
    while edges_work:
        print(f"#{len(edges_work)=}")
        leaf_nodes = [
            endpoint
            for endpoint, edge_list in edges_by_endpoint.items()
            if len(edge_list) == 1
        ]
        print(f"#  {leaf_nodes=}")
        for endpoint in leaf_nodes:
            print(f"#    {endpoint=}")
            weight = weights[endpoint]
            print(f"#    {weight=}")
            edge_list = edges_by_endpoint[endpoint]
            if not edge_list:
                continue
            edge = edge_list[0]
            print(f"#    {edge=}")
            other_end = sum(edge) - endpoint
            assert other_end in edge
            if weight % 2 == 0:
                edges_cut.append(edge)
            else:
                if weights[other_end] == 0:
                    continue
                edges_keep.append(edge)
                weights[other_end] += weight
                weights[endpoint] -= weight
                assert weights[endpoint] == 0
            for point in edge:
                print(f"#  {point}: remove {edge} from {edges_by_endpoint[point]}")
                edges_by_endpoint[point].remove(edge)
            edges_work.remove(edge)
    print(f"#  {weights=}")
    print(f"#  {edges_keep=}")
    print(f"#  {edges_cut=}")
    return len(edges_cut)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t_nodes, t_edges = map(int, input().rstrip().split())
    t_from = [0] * t_edges
    t_to = [0] * t_edges
    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())
    res = evenForest(t_nodes, t_edges, t_from, t_to)
    print(str(res))
    # fptr.write(str(res) + '\n')
    # fptr.close()

