
def euler_28(N):
    X = 1
    diag = X    # we already have "1", the middle number
    # print("#add", X)
    jump = 0
    size = 1
    while size < N:
        jump += 2
        size += 2
        for corner in range(4):
            X += jump
            diag += X
            # print("#add", X)
    return diag

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_28(N))

