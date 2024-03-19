# Enter your code here. Read input from STDIN. Print output to STDOUT

def number_word_under_20(n):
    values = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
    ]
    return values[n]

def number_word_multiple_of_10(n):
    values = [
        "", "ten", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety",
    ]
    return values[n]

def number_word_2digits(nn):
    L = []
    if nn == 0:
        pass
    elif nn < 20:
        value = number_word_under_20(nn)
        L.append(value)
        # print("#check", nn, L)
    else:
        tens = nn // 10
        ones = nn % 10
        if tens > 0:
            value_tens = number_word_multiple_of_10(tens)
            L.append(value_tens)
        if ones > 0:
            value_ones = number_word_under_20(ones)
            L.append(value_ones)
        # print("#check", nn, tens, ones, L)
    return L

def number_word_3digits(nnn):
    L = []
    if nnn > 1000:
        raise ValueError(f"Invalid input: nnn {nnn} > 1000")
    hundreds = nnn // 100
    nn = nnn % 100
    if hundreds > 0:
        H = number_word_under_20(hundreds)
        L.extend([H, "hundred"])
    TO = number_word_2digits(nn)
    L.extend(TO)
    # print("#check", nnn, hundreds, nn, L)
    return L

def number_word(N):
    L = []
    while N > 0:
        group = N % 1000
        # print("#group", group)
        L.append(group)
        N //= 1000
    # print("#L", L)
    answer = [
        ' '.join(number_word_3digits(g))
        for g in L
    ]
    # print("#ANS", answer)
    groupnames = [
        '',
        'thousand',
        'million',
        'billion',
        'trillion',
        'quadrillion',
        'quintillion',
        'sextillion',
        'septillion',
        'octillion',
        'nonillion',
        'decillion',
    ]
    relevant_names = groupnames[:len(answer)]
    merge = list(reversed(list(zip(answer, relevant_names))))
    # print("#merge", merge)
    fixed = [
        (a,) if b == '' else None if a == '' else (a, b)
        for (a, b) in merge
    ]
    fixed = [
        ' '.join(T)
        for T in fixed
        if T is not None
    ]
    # print("#fixed", fixed)
    return ' '.join(fixed)

def euler_17(N):
    return number_word(N).title()
    

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_17(N))

