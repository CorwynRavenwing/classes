import numpy

def arrays(arr):
    print('arr', arr)
    A = arr[::-1]
    print('A', A)
    N = numpy.array(A, float)
    print('N', N)
    return N

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

