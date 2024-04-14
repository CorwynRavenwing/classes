
from with_cache import with_cache

@with_cache
def position_after_move_cached(T):
    (pos, direction, H, W) = T
    print(f"#position_after_move({pos}, {direction}, {H}, {W})")
    (x, y) = pos
    moves = {
            'U': (x, y-1),
            'D': (x, y+1),
            'L': (x-1, y),
            'R': (x+1, y),
    }
    newpos = moves[direction]
    (x1, y1) = newpos
    if 0 <= x1 < W and 0 <= y1 < H:
        print(f"#  -> {newpos}")
        return newpos
    print(f"#  -> {None}")
    return None

def position_after_move(pos, direction, H, W):
    T = (pos, direction, H, W)
    return position_after_move_cached(T)

@with_cache
def positions_reached_by_string_cached(T):
    (S, H, W) = T
    if S == '':
        return (
            (0, 0),
        )
    positions_before = positions_reached_by_string(S[:-1], H, W)
    position_before = positions_before[-1]
    position_after = position_after_move(position_before, S[-1], H, W)
    if position_after is None:
        return None
    if position_after in positions_before:
        return None
    return positions_before + (position_after,)

def positions_reached_by_string(S, H, W):
    T = (S, H, W)
    return positions_reached_by_string_cached(T)

@with_cache
def position_after_string_cached(T):
    (S, H, W) = T
    positions = positions_reached_by_string(S, H, W)
    if positions is None:
        return None
    position = positions[-1]
    return position

def position_after_string(S, H, W):
    T = (S, H, W)
    return position_after_string_cached(T)

def VAP_generator(matrix):
    @with_cache
    def value_at_position(pos):
        (x, y) = pos
        return matrix[x][y]
    return value_at_position

value_at_position = None

def value_of_string(S, matrix):
    global value_at_position
    if value_at_position is None:
        value_at_position = VAP_generator(matrix)
    H = len(matrix)
    W = len(matrix[0])
    positions = positions_reached_by_string(S, H, W)
    if positions is None:
        return None
    values = map(value_at_position, positions)
    return sum(values)

def string_leads_to_endpoint(S, H, W):
    position = position_after_string(S, H, W)
    endpoint = (H-1, W-1)
    return position == endpoint

def euler_83(matrix):
    H = len(matrix)
    W = len(matrix[0])
    endpoint = (H-1, W-1)
    value_at_point = {}
    answers = []
    to_check = [(0, '')]
    while to_check:
        to_check.sort()
        print("#" * 70)
        print(f"#{to_check=}")
        print("#" * 70)
        (prior_value, path) = to_check.pop(0)
        value = value_of_string(path, matrix)
        print(f"#{path=} {value=}")
        if len(path) > 5:
            break
        if value is None:
            continue
        position = position_after_string(path, H, W)
        prior_value = value_at_point.get(position, None)
        if prior_value is None or value < prior_value:
            print(f"#### P:{position} V:{value} MIN < {prior_value}")
            value_at_point[position] = value
        else:
            print(f"#### P:{position} V:{value} > {prior_value}")
            continue
        if position == endpoint:
            answers.append(value)
            continue
        for direction in ['U', 'D', 'L', 'R']:
            to_check.append((value, path + direction))
    print(f"#{answers=}")
    return min(answers)

N = int(input().strip())
matrix = [
    list(map(int, input().strip().split(' ')))
    for _ in range(N)
]
print(euler_83(matrix))

