
def card_value_index(x):
    CVO = 'AKQJT98765432:CHSD'
    return CVO.index(x)

def by_card_value(x):
    return card_value_index(x)

def by_card_count_then_value(T):
    count, value = T
    return (-count, card_value_index(value))

def by_number_then_values(T):
    answer = [
        (
            v
            if (i == 0) or (len(v) > 1)
            else card_value_index(v)
        )
        for i, v in enumerate(T)
    ]
    return tuple(answer)

def card_suits(C):
    return sorted([
        card[1]
        for card in C
    ])

def card_values(C):
    return sorted([
        card[0]
        for card in C
    ], key=by_card_value)

def card_flush(C):
    suits = card_suits(C)
    # print("#suits", suits)
    first = suits[0]
    flush = [first] * 5
    if suits == flush:
        return first
    else:
        return ''

def card_straight(C):
    values = card_values(C)
    first_card = values[0]
    indexes = [
        card_value_index(v)
        for v in values
    ]
    first = indexes[0]
    runs = [
        first+i in indexes
        for i in range(5)
    ]
    straight = [True] * 5
    if runs == straight:
        return first_card
    else:
        return ''
    pass

def card_count(C):
    values = card_values(C)
    different_values = set(values)
    counts = [
        (len([match for match in values if match == v]), v)
        for v in different_values
    ]
    counts = [
        (count, value)
        for (count, value) in counts
        if count > 1
    ]
    return sorted(
        counts,
        key=by_card_count_then_value
    )

def card_order(C):
    values = card_values(C)
    return values

def parse_cards(C):
    flush = card_flush(C)
    straight = card_straight(C)
    count = card_count(C)
    order = card_order(C)
    # print(f"#{flush=}\n#{straight=}\n#{count=}\n#{order=}\n#")
    count1 = count[0] if count and len(count) > 0 else ''
    count2 = count[1] if count and len(count) > 1 else ''
    count1_num = count1[0] if count1 else 0
    count1_val = count1[1] if count1 else ''
    count2_num = count2[0] if count2 else 0
    count2_val = count2[1] if count2 else ''
    both_nums = (count1_num, count2_num)
    both_vals = (count1_val, count2_val)
    if flush and straight == 'A':
        parsed = (1, straight, flush, 'Royal Flush')
    elif flush and straight:
        parsed = (2, straight, flush, 'Straight Flush')
    elif both_nums == (4, 0):
        parsed = (3, count1_val, '4 of a Kind')
    elif both_nums == (3, 2):
        parsed = (4, *both_vals, 'Full House')
    elif flush:
        parsed = (5, flush, 'Flush')
    elif straight:
        parsed = (6, straight, 'Straight')
    elif both_nums == (3, 0):
        parsed = (7, count1_val, '3 of a Kind')
    elif both_nums == (2, 2):
        parsed = (8, *both_vals, '2 Pair')
    elif both_nums == (2, 0):
        parsed = (9, count1_val, '1 Pair')
    else:
        parsed = (10, *order, 'High Card')
    return parsed

def euler_54(P1, P2):
    hands = [
        (*parse_cards(P1), 'Player 1'),
        (*parse_cards(P2), 'Player 2'),
    ]
    hands.sort(key=by_number_then_values)
    for h in hands:
        print("#hands", h)
    win = hands[0]
    winner = win[-1]
    return winner

T = int(input().strip())
for _ in range(T):
    cards = input().strip().split(' ')
    P1 = cards[:5]
    P2 = cards[5:]
    print(euler_54(P1, P2))

