
def sqrt(X):
    return X ** 0.5

def sqrt_sum(X, P):
    Q = sqrt(X)
    INT = int(Q)
    decimal = Q - INT
    if INT * INT == X:
        # print(f"#{X} is a perfect square: {INT}")
        return 0
    string = str(decimal)
    digits = list(string)
    # print(f"#{X} {INT} {decimal} {string} {digits}")
    assert digits.pop(0) == '0'
    assert digits.pop(0) == '.'
    digits = digits[:P]
    # print(f"#{X} {P} {digits}")
    return sum(map(int, digits))

# print(sqrt_sum(2, 10))
# print(sqrt_sum(4, 10))
# exit()

def euler_80(N, P):
    answers = [
        sqrt_sum(i, P)
        for i in range(N + 1)
    ]
    return sum(answers)

N = int(input().strip())
P = int(input().strip())
print(euler_80(N, P))

