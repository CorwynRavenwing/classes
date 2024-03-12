from itertools import combinations

line = input().split()
S = sorted(line[0])
K = int(line[1])
for i in range(1, K+1):
    C = list(combinations(S, i))
    for c in C:
        print(''.join(c))

