#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STR gene
# return INT
def steadyGene(gene):
    need = len(gene) // 4
    genomes = 'GCAT'
    counter = {
        g: -need
        for g in genomes
    }
    for g in gene:
        counter[g] += 1
    print(f"#{counter}")
    too_high = {
        g: count if count > 0 else 0
        for g, count in counter.items()
    }
    min_answer = sum(too_high.values())
    print(f"#{min_answer} {too_high}")
    for answer in range(min_answer, len(gene)):
        print(f"#try {answer=}")
        for i in range(len(gene) - answer + 1):
            block = gene[i:i+answer]
            print(f"#  {block}")
            counter2 = too_high.copy()
            # print(f"#{counter2=}")
            for g in block:
                counter2[g] -= 1
            print(f"#{counter2=}")
            still_too_high = {
                g: count if count > 0 else 0
                for g, count in counter2.items()
            }
            print(f"#STH {still_too_high}")
            left_over = sum(still_too_high.values())
            if left_over <= 0:
                print(f"#FOUND {answer} {left_over} {still_too_high}")
                return answer
    assert False

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    gene = input()
    result = steadyGene(gene)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

