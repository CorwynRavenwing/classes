alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = "();:,.'?-! "
possible_str = alphabet + alphabet.upper() + symbols
possible_int = [
    ord(c)
    for c in possible_str
]

def euler_59(codes):
    alphabet_int = [
        ord(c)
        for c in alphabet
    ]
    letters = [[]] * 3
    for i in range(3):
        letters[i] = alphabet_int.copy()
    for i, c in enumerate(codes):
        code_i = i % 3
        for j, L in enumerate(letters[code_i]):
            decoded = c ^ L
            if decoded not in possible_int:
                # print(f"#{i=} {code_i} {c=} {chr(L)} NO")
                letters[code_i][j] = None
        letters[code_i] = [
            L
            for L in letters[code_i]
            if L is not None
        ]
        # print(f"#? {code_i} " + ''.join(map(chr, letters[code_i])))
        
    for code_i in range(3):
        if len(letters[code_i]) != 1:
            print(f"#ERROR: letters[{code_i}]={letters[code_i]}, len != 1")
        letters[code_i] = letters[code_i][0]
    # for i, c in enumerate(codes):
    #     code_i = i % 3
    #     L = letters[code_i]
    #     decoded = c ^ L
        # print(chr(decoded), end="")
    # print("")
    return ''.join(map(chr, letters))

N = int(input().strip())
codes = tuple(map(int, input().strip().split(' ')))
print(euler_59(codes))

