import numpy

(N, M) = tuple(map(int, input().split()))
A = []
for i in range(N):
    Ai = tuple(map(int, input().split()))
    A.append(Ai)
nA = numpy.array(A)

B = []
for i in range(N):
    Bi = tuple(map(int, input().split()))
    B.append(Bi)
nB = numpy.array(B)
print(nA + nB)
print(nA - nB)
print(nA * nB)
print(nA // nB)
print(nA % nB)
print(nA ** nB)

