def solve(s):
    letters = list(s)
    token = True
    for i, c in enumerate(letters):
        if token and c.islower():
            c = c.upper()
            letters[i] = c
            token = False
        elif c.isalnum():
            token = False
        else:
            token = True

    return ''.join(letters)

tests = [
        'this is a test',
        'Already Correct',
        'problematic 3g issue',
        'hello   world  lol',
        ]

for t in tests:
    print(t, solve(t))

