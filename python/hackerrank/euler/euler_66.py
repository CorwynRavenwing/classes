
def sqrt(S):
    return int(S ** 0.5)

def is_square(S):
    root = sqrt(S)
    return (root * root == S)

def euler_66(N):
    answers = []
    # D of 0 or 1 makes no sense
    for D in range(2, N+1):
        print(f"#{D=}")
        if is_square(D):
            print("#   ignore square D")
            continue
        X = 0
        while True:
            X += 1
            X2 = X * X
            Y2 = (X2 - 1) // D
            Y = sqrt(Y2)
            if Y == 0:
                # ignore trivial solutions of X=1 Y=0 D=irrelevant
                continue
            check = X2 - D * (Y * Y)
            if check == 1:
                print(f"#{X}^2 - {D} {Y}^2 = {X2} - {D * Y2} = {check}")
                answers.append((X, D))
                break
    answers.sort(reverse=True)
    print(f"#{answers=}")
    return answers[0][1]

N = int(input().strip())
print(euler_66(N))

