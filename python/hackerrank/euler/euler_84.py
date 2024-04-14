
from collections import Counter

def euler_84(N, K):
    squares = [
        'GO', 'A1', 'CC1', 'A2', 'T1',
        'R1', 'B1', 'CH1', 'B2', 'B2',
        'JAIL', 'C1', 'U1', 'C2', 'C3',
        'R2', 'D1', 'CC2', 'D2', 'D3',
        'FP', 'E1', 'CH2', 'E2', 'E3',
        'R3', 'F1', 'F2', 'U2', 'F3',
        'G2J', 'G1', 'G2', 'CC3', 'G3',
        'R4', 'CH3', 'H1', 'T2', 'H2',
    ]
    SIZE = 40
    assert len(squares) == SIZE

    square_indexes = {
        name: i
        for i, name in enumerate(squares)
    }
    print(f"# {square_indexes=}")

    named = {
        'R': [
            'R1', 'R2', 'R3', 'R4',
        ],
        'U': [
            'U1', 'U2',
        ],
        'CC': [
            'CC1', 'CC2', 'CC3',
        ],
        'CH': [
            'CH1', 'CH2', 'CH3',
        ],
    }

    CC_template = [
        'GO', 'JAIL',
    ]

    CH_template = [
        'GO', 'JAIL', 'C1', 'E3', 'H2',
        'R1', 'R+', 'R+', 'U+', '-3'
    ]

    CARDS = 16
    moves = {
        'G2J': ['JAIL'] * CARDS,
    }
    for cc_id in named['CC']:
        moves[cc_id] = CC_template.copy()
        moves[cc_id] += [''] * (CARDS - len(CC_template))

    def next_of_type_after(source_id, type_id):
        index = square_indexes[source_id]
        indexes = [square_indexes[N] for N in named[type_id]]
        # print(f"#  {type_id}_indexes={indexes}")
        after = [i for i in indexes if i > index]
        # print(f"#    {after=}")
        if not after:
            after = indexes
            # print(f"# >> {after=}")
        r_index = min(after)
        retval = squares[r_index]
        # print(f"#      -> {retval}")
        return retval

    def move_N(source_id, N):
        index = square_indexes[source_id]
        new_index = (index + N) % SIZE
        return squares[new_index]

    for ch_id in named['CH']:
        print(f"#  {ch_id=}")
        moves[ch_id] = CH_template.copy()
        moves[ch_id] += [''] * (CARDS - len(CH_template))
        this_index = square_indexes[ch_id]
        print(f"#  {this_index=}")
        details = {}
        details['R+'] = next_of_type_after(ch_id, 'R')
        details['U+'] = next_of_type_after(ch_id, 'U')
        details['-3'] = move_N(ch_id, -3)
        for i, val in enumerate(moves[ch_id]):
            # print(f"#    {i=} {val=}")
            if val in details:
                # print(f"#      -> {details[val]=}")
                moves[ch_id][i] = details[val]
        print(f"#        {moves[ch_id]}")

    def roll_2_dice(N):
        # possibilities = [
        #     a + b
        #     for a in range(1, N+1)
        #     for b in range(1, N+1)
        # ]
        possibilities = [
            a
            for a in range(40)
        ]
        # print(f"#roll_2_dice({N}):")
        counts = Counter(possibilities)
        # print(f"#  -> {counts}")
        denominator = len(possibilities)
        # assert denominator == N * N
        retval = {
            number: (count, denominator)
            for number, count in counts.items()
        }
        return retval

    def lowest_form_fraction(frac):
        print(f"#lff({frac}", end=" -> ")
        num, den = frac
        factors = [2, 3, 5, 7, 11, 13, 17, 19]
        for factor in factors:
            while num % factor == 0 and den % factor == 0:
                num //= factor
                den //= factor
        print(f"# {(num, den)}")
        return (num, den)

    def add_fractions(f1, f2):
        n1, d1 = f1
        n2, d2 = f2
        if d1 == d2:
            num = n1 + n2
            den = d1
        else:
            num = n1 * d2 + n2 * d1
            den = d1 * d2
        frac = (num, den)
        return lowest_form_fraction(frac)

    def multiply_fractions(f1, f2):
        n1, d1 = f1
        n2, d2 = f2
        num = n1 * n2
        den = d1 * d2
        frac = (num, den)
        return lowest_form_fraction(frac)

    def fraction_to_float(frac):
        num, den = frac
        return num / den

    start = 'GO'
    start_index = square_indexes[start]
    dice = roll_2_dice(N)
    # print(f"#{dice=}")
    this_level = [
        (move_N(start, number), odds)
        for number, odds in dice.items()
    ]
    # print(f"#{this_level=}")
    changed = True
    while changed:
        # print(f"#Change loop:\n#{this_level}")
        changed = False
        next_level = []
        for FL in this_level:
            square, odds = FL
            if square not in moves:
                next_level.append(FL)
                continue
            changed = True
            moves_from_here = moves[square]
            for new_square in moves_from_here:
                new_odds = (1, len(moves_from_here))
                if new_square == '':
                    new_square = square.lower()
                new_odds = multiply_fractions(odds, new_odds)
                move = (new_square, new_odds)
                next_level.append(move)
        this_level = next_level
    # print(f"#Change loop done:\n#{this_level}")
    this_level = [
        (square.upper(), odds)
        for square, odds in this_level
    ]
    this_level.sort()
    print(f"#Change loop upper:\n#{this_level}")
    squares = [
        square
        for square, odds in this_level
    ]
    # print(f"#  {squares=}")
    squares = set(squares)
    # print(f"#  {squares=}")
    this_level = [
        (this_square, [
            odds
            for square, odds in this_level
            if square == this_square
        ])
        for this_square in squares
    ]
    print(f"#Change loop join:\n#{this_level}")
    next_level = []
    for FL in this_level:
        square, odds_list = FL
        print(f"#{square} {odds_list}")
        if len(odds_list) == 1:
            odds = odds_list.pop()
            print(f"#  odds 1 {odds}")
        else:
            odds = odds_list.pop()
            print(f"#  odds 0 {odds}")
            while odds_list:
                next_odds = odds_list.pop()
                print(f"#  odds + {next_odds}")
                odds = add_fractions(odds, next_odds)
                print(f"#    odds = {odds}")
        NL = (square, odds)
        next_level.append(NL)
    this_level = sorted(next_level)
    print(f"#Change loop merge:\n#{this_level}")
    this_level = [
        (square, fraction_to_float(odds))
        for square, odds in this_level
    ]
    this_level.sort(key=lambda x: x[1], reverse=True)
    print(f"#Change loop calculate:\n#{this_level}")
    squares = [
        square
        for square, odds in this_level
    ]
    print(f"#  {squares=}")
    squares = squares[:K]
    print(f"#  {squares=}")
    return ' '.join(squares)

(N, K) = map(int, input().strip().split(' '))
print(euler_84(N, K))

