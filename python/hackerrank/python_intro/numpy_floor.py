import numpy
numpy.set_printoptions(legacy='1.13')

A = tuple(map(float, input().split()))

nA = numpy.array(A)

print(numpy.floor(nA))
print(numpy.ceil(nA))
print(numpy.rint(nA))

