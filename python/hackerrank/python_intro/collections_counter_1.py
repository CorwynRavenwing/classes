import collections

c = collections.Counter()

N = int(input())
for i in range(N):
    word = input()
    c[word] += 1
print(len(c))
D = []
for word, count in c.items():
    D.append(str(count))
print(" ".join(D))

