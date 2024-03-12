import numpy

dims = tuple(map(int, input().split()))
# print(dims)

print(numpy.zeros(dims, dtype=numpy.int))
print(numpy.ones(dims, dtype=numpy.int))

