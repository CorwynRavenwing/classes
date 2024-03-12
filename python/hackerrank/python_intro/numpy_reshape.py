import numpy

A = tuple(map(int, input().split()))
# print("A", A)
N = numpy.array(A)
# print("N", N)
R = numpy.reshape(A, (3,3))
print(R)

