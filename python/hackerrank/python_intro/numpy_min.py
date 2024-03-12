import numpy
(N,M) = tuple(map(int, input().split()))
print("N,M",N,M)
A = []
for i in range(N):
    Ai = tuple(map(int, input().split()))
    A.append(Ai)
print("A", A)

nA = numpy.array(A)
print("nA", nA)

mA = numpy.min(nA, axis=1)
print("mA", mA)

MA = numpy.max(mA)
print("MA", MA)

