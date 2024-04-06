def int_len(N):
    return len(str(N))

def euler_57(N):
    AB = (1, 1)
    for i in range(N+1):
        (A, B) = AB
        # fraction = A / B
        bigger = int_len(A) > int_len(B)
        if bigger:
            print(i)
        # print(f"#{i} {AB=} {bigger} {fraction}")
        AB = (A + 2 * B, A + B)
    pass

N = int(input().strip())
euler_57(N)

