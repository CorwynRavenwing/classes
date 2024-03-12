import numpy
N = int(input())
print("N",N)

A = []
for i in range(N):
    Ai = tuple(map(int, input().split()))
    A.append(Ai)
print("A", A)

B = []
for i in range(N):
    Bi = tuple(map(int, input().split()))
    B.append(Bi)
print("B", B)

nA = numpy.array(A)
print("nA", nA)

nB = numpy.array(B)
print("nB", nB)

C = []
for i in range(N):
    Ci = []
    for j in range(N):
        Ai = nA[i,:]
        Bj = nB[:,j]
        print("Ai", Ai)
        print("Bj", Bj)
        Cij = numpy.dot(Ai, Bj)
        print("Cij", Cij)
        Ci.append(Cij)
    C.append(Ci)
print("C", C)
nC = numpy.array(C)
print("nC", nC)

