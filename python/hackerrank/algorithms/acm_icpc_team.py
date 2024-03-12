#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from itertools import combinations

def acmTeam(topics):
    # print("#aT()", topics)
    topic_lists = [
        list(topic)
        for topic in topics
    ]
    # print("#lists", topic_lists)
    topic_set_lists = [
        [
            j+1
            for j, t in enumerate(topic)
            if t == '1'
        ]
        for topic in topic_lists
    ]
    # print("#set_lists", topic_set_lists)
    topic_sets = [
        set(topic)
        for topic in topic_set_lists
    ]
    # print("#sets", topic_sets)
    indexes = range(len(topic_sets))
    possible_teams = list(combinations(indexes, 2))
    # print("#teams", possible_teams)
    team_subjects = [
        len(
            topic_sets[T[0]]
            .union(topic_sets[T[1]])
        )
        for T in possible_teams
    ]
    # print("#breadth", team_subjects)
    max_subjects = max(team_subjects)
    teams_at_max = [
        t
        for t in team_subjects
        if t == max_subjects
    ]
    # print("#TAM", teams_at_max)
    pass
    return [max_subjects, len(teams_at_max)]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
    print('\n'.join(map(str, result)))
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

