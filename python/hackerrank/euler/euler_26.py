
def check_loop(X):
    R_list = []
    R = 1
    while True:
        # print("#R", R)
        if R == 0:
            # print("#R0", R)
            return 0
        while R < X:
            R *= 10
            # print("#R*", R)
        if R in R_list:
            index = R_list.index(R)
            # print("#I", index, len(R_list))
            return len(R_list) - index
        else:
            R_list.append(R)
        # Q = R // X
        R = R % X
        # print("#Q", R, Q)
    pass

def euler_26(N):
    d_max = 0
    d_cycle = 0
    for i in range(1, N):
        i_cycle = check_loop(i)
        if d_cycle < i_cycle:
            print("#cycle", (d_max, d_cycle), (i, i_cycle))
            d_max = i
            d_cycle = i_cycle
    return d_max

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_26(N))

