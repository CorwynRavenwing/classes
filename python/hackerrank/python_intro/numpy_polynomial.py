import numpy

P = tuple(map(float, input().split()))
x = float(input())
# print("P,x", P, x)
Px = numpy.polyval(P, x)
# print("P(x)")
print(Px)

