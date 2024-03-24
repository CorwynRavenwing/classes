def char_value(C):
    return ord(C) - ord('A') + 1

def word_value(W):
    return sum(map(char_value, list(W)))

euler_data = {}

def euler_22_setup(L):
    global euler_data
    L.sort()
    for i, W in enumerate(L):
        print("#word", i, W, end=" ")
        value = word_value(W)
        print("#", value, end=" ")
        value *= (i + 1)
        print("#", value)
        euler_data[W] = value
    return

def euler_22(W):
    global euler_data
    return euler_data[W]

N = int(input().strip())
L = [
    input().strip()
    for _ in range(N)
]
euler_22_setup(L)
Q = int(input().strip())
for _ in range(Q):
    word = input().strip()
    print(euler_22(word))

