import numpy
(N, M) = map(int, input().split())
print("N", N, "M", M)
A = []
for i in range(N):
    Ai = tuple(map(int, input().split()))
    A.append(Ai)

print("A", A)
nA = numpy.array(A)
print("nA", nA)
sA = numpy.sum(nA, axis=0)
print("sA", sA)
pA = numpy.product(sA)
print("pA", pA)

