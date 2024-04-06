
def euler_63(N):
    answers = []
    I_pow_N = ""
    i = 0
    while len(I_pow_N) <= N:
        I_pow_N = str(i ** N)
        if len(I_pow_N) == N:
            answers.append(I_pow_N)
        # print(f"# {i} {I_pow_N} {len(I_pow_N)}")
        i += 1
    return answers

N = int(input().strip())
print('\n'.join(map(str, euler_63(N))))

