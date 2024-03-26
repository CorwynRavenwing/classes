# Enter your code here. Read input from STDIN. Print output to STDOUT

def euler_43(N):
    possibles = ['']
    retval = 0
    digits_needed = list(map(str, range(0, N+1)))
    # print("#DN", digits_needed)
    checks = (
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 7),
        (6, 11),
        (7, 13),
        (8, 17),
    )
    while len(possibles):
        # print("#len():", len(possibles))
        trial = possibles.pop()
        # print(f"#{trial=}")
        if trial == '0':
            continue
        if len(trial) < N:
            new_list = [
                trial + d
                for d in digits_needed
                if d not in trial
            ]
            # print(f"#{new_list=}")
            possibles.extend(new_list)
            continue
        print(f"#CHECK {trial}")
        failed = False
        for C in checks:
            (R, P) = C
            D = trial[R:R+3]
            i = int(D) if D != '' else 0
            if i % P != 0:
                failed = True
                break
        if not failed:
            retval += int(trial)
    return retval

N = int(input().strip())
print(euler_43(N))

