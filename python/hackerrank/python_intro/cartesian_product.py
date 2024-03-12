from itertools import product

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
# print("A", A)
# print("B", B)

AxB = tuple(product(A,B))
# print("AxB", AxB)

AxBstr = tuple(map(str, AxB))
print(' '.join(AxBstr))

