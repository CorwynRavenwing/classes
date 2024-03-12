import numpy

N = int(input())
A = []
for i in range(N):
    Ai = tuple(map(float, input().split()))
    A.append(Ai)
# print("A", A)
det = numpy.linalg.det(A)
# print("det", det)
det = round(det, 2)
print(det)

