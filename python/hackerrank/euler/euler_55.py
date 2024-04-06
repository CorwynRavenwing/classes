
def reversed_int(N):
    return int(''.join(reversed(str(N))))

def reverse_and_add(N):
    return N + reversed_int(N)

def is_palindrome(N):
    return N == reversed_int(N)

def euler_55(N):
    answers = {}
    # print(f"#euler_55({N})")
    for X in range(N, 0, -1):
        Y = X
        # print(f"#{X=} {Y=}")
        for i in range(60):
            # print(f"#{X=} {Y=} {i=}")
            if Y in answers:
                break
            if is_palindrome(Y):
                answers[Y] = Y
                break
            Y = reverse_and_add(Y)
        if X not in answers:
            if Y in answers:
                answers[X] = answers[Y]
            else:
                answers[X] = Y
    # print(f"#{answers=}")
    palindromes = {}
    targets = answers.values()
    for target in targets:
        matches = [
            key
            for key, value in answers.items()
            if value == target
        ]
        palindromes[target] = len(matches)
    # print(f"#{palindromes=}")
    max_length = max(palindromes.values())
    # print(f"#{max_length=}")
    matches = [
        (key, value)
        for key, value in palindromes.items()
        if value == max_length
    ]
    # print(f"#{matches=}")
    first_match = matches[0]
    return ' '.join(map(str, first_match))

N = int(input().strip())
print(euler_55(N))

