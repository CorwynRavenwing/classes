
word = "abcdefghijklm"

def factorial(N):
    retval = N
    for i in range(1, N):
        retval *= i
        # print("#I", i, retval)
    return retval

def euler_24(N):
    retval = []
    rest = list(word)
    while rest != []:
        F = factorial(len(rest) - 1)
        print("#F", F)
        index = (
            (N-1) // F
            if F > 0
            else 0
        )
        print(f"#x {''.join(retval)} {''.join(rest)}", end=" ")
        print(f"{len(rest)} {F=} {N-1=} i={index}", end=" ")
        print(f"{rest[index]}")
        char = rest.pop(index)
        retval.append(char)
        N -= index * F
    return ''.join(retval)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_24(N))

