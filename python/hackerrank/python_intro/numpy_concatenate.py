import numpy

(N, M, P) = tuple(map(int, input().split()))
# print("NMP", N, M, P)
A = []
for i in range(N):
    Ai = tuple(map(int, input().split()))
    A.append(Ai)
# print("A", A)

B = []
for i in range(M):
    Bi = tuple(map(int, input().split()))
    B.append(Bi)
# print("B", B)

nA = numpy.array(A)
# print("nA", nA)
nB = numpy.array(B)
# print("nB", nB)
nC = numpy.concatenate((A, B), axis=0)
print(nC)

