
def euler_29(N):
    retval = set()
    for A in range(2, N+1):
        for B in range(2, N+1):
            AB = A ** B
            # print(f"{A}^{B} = {AB}")
            retval.add(AB)
    return len(retval)

N = int(input().strip())
print(euler_29(N))

