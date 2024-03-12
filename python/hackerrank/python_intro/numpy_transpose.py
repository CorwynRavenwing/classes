import numpy

(N,M) = tuple(map(int, input().split()))
print(N,M)
A = []
for i in range(N):
    Ai = tuple(map(int, input().split()))
    A.append(Ai)
print("A", A)
nA = numpy.array(A)
print("nA", nA)

print(numpy.transpose(nA))
print(nA.flatten())

