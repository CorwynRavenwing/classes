# Enter your code here. Read input from STDIN. Print output to STDOUT

def euler_38(N, K):
    retval = []
    # range 2 because M=1 is a trivial success
    for M in range(2, N):
        # target = list(range(1, K+1))
        target = ''.join(map(str, (range(1, K+1))))
        # print(target)
        # attempt = []
        attempt = ""
        i = 0
        while len(attempt) < len(target):
            i += 1
            product = M * i
            attempt += str(product)
            # attempt.extend(list(str(product)))
            # print(f"#{attempt=}")
            if len(set(attempt)) != len(attempt):
                # print(f"#duplicate '{attempt}'")
                break
        if len(set(attempt)) != len(attempt):
            # print("#I said duplicate")
            continue
        # print(f"%{attempt=} {target=}")
        if set(attempt) != set(target):
            # print("#wrong digits")
            continue
        # print(f"#FOUND {M}")
        retval.append(str(M))
    return '\n'.join(retval)

N, K = map(int, input().strip().split(' '))
print(euler_38(N, K))

