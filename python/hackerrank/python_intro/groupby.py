from itertools import groupby

S = input()
data = list(S)

groups = []
keys = []
for k,g in groupby(data):
    groups.append(list(g))
    keys.append(k)

lengths = list(map(len, groups))
values = list(map(int, keys))

answer = list(zip(lengths, values))
answerStr = list(map(str, answer))

print(' '.join(answerStr))

