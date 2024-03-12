import numpy

A = tuple(map(int, input().split()))
print("A", A)

B = tuple(map(int, input().split()))
print("B", B)

nA = numpy.array(A)
print("nA", nA)

nB = numpy.array(B)
print("nB", nB)

print(numpy.inner(A,B))
print(numpy.outer(A,B))

