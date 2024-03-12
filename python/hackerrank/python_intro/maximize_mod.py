def F(x):
    return x**2

def G(A, B):
    # print("G:", A, B)
    retval = []
    for a in A:
        def add_a(b):
            return a + b
        R = list(map(add_a, B))
        retval += R
    # print("G=", retval)
    return retval

(K, M) = tuple(map(int, input().split()))
# print(K, M)
X = []
for i in range(K):
    temp = list(map(int, input().split()))
    Xi = tuple(temp[1:])
    X.append(Xi)
# print(X)

Squares = []
for i in range(len(X)):
    Square_i = tuple(map(F, X[i]))
    Squares.append(Square_i)
# print(Squares)

while len(Squares) > 1:
    A = Squares.pop()
    B = Squares.pop()
    C = G(A, B)
    Squares.append(C)
# print(Squares[0])

def mod_M(a):
    return a % M

Sums = tuple(map(mod_M, Squares[0]))
# print(Sums)

print(max(Sums))

