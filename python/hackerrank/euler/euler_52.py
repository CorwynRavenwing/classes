
def euler_52(N, K):
    for x in range(1, N+1):
        digits_x = sorted(list(str(x)))
        # print(f"#{digits_x=}")
        answer = [x]
        for m in range(2, K+1):
            prod = m * x
            digits_p = sorted(list(str(prod)))
            # print(f"#  {m=} {digits_p=}")
            if digits_x == digits_p:
                # print("#    YES")
                answer.append(prod)
            else:
                # print("#    NO")
                answer = []
                break
        if answer:
            print(' '.join(map(str, answer)))

(N, K) = map(int, input().strip().split(' '))
euler_52(N, K)

