import numpy
(N,M) = tuple(map(int, input().split()))
# print("N,M",N,M)
A = []
for i in range(N):
    Ai = tuple(map(int, input().split()))
    A.append(Ai)
# print("A", A)

nA = numpy.array(A)
# print("nA", nA)

print(numpy.mean(nA, axis=1))
print(numpy.var(nA, axis=0))
nS = numpy.std(nA)
if nS == 0.0:
    print(nS)
else:
    print("{:.11f}".format(nS))

