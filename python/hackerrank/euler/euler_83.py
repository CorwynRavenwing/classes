
from with_cache import with_cache

# @with_cache
def position_after_move_cached(T):
    (pos, direction, H, W) = T
    print(f"#position_after_move({pos}, {direction})", end="")
    (x, y) = pos
    moves = {
        'L': (x, y-1),
        'R': (x, y+1),
        'U': (x-1, y),
        'D': (x+1, y),
    }
    newpos = moves[direction]
    (x1, y1) = newpos
    if 0 <= x1 < W and 0 <= y1 < H:
        print(f"# -> {newpos}")
        return newpos
    print(f"# -> {newpos} (OOB)")
    return None

def position_after_move(pos, direction, H, W):
    T = (pos, direction, H, W)
    return position_after_move_cached(T)

def VAP_generator(matrix):
    # @with_cache
    def value_at_position(pos):
        (x, y) = pos
        return matrix[x][y]
    return value_at_position

value_at_position = None

def euler_83(matrix):
    H = len(matrix)
    W = len(matrix[0])
    global value_at_position
    if value_at_position is None:
        value_at_position = VAP_generator(matrix)
    UL = matrix[0][0]
    beginpoint = (0, 0)
    endpoint = (H-1, W-1)
    value_at_point = {beginpoint: UL}
    answers = []
    to_check = [(UL, '', beginpoint)]
    while to_check:
        to_check.sort()
        (value, path, position) = to_check.pop(0)
        print("#" * 40)
        print(f"# {len(to_check)+1}: {value} '{path}' {position}")
        print("#" * 40)
        for direction in ['U', 'D', 'L', 'R']:
            new_position = position_after_move(position, direction, H, W)
            if new_position is None:
                continue
            position_value = value_at_position(new_position)
            new_value = value + position_value
            new_path = path + direction
            print(f"#{new_path=} {new_position} {new_value=}", end=" ")
            prior_value = value_at_point.get(new_position, None)
            if prior_value is None or new_value < prior_value:
                print(f"# +++ MIN < {prior_value}")
                value_at_point[new_position] = new_value
            else:
                print(f"# --- NO! > {prior_value}")
                continue
            if new_position == endpoint:
                print("#" + "=" * 30 + "\n#")
                print(f"##### '{new_path}' {new_position} {new_value}")
                print("#\n" + "#" + "=" * 30)
                answers.append(new_value)
                continue
            T = (new_value, new_path, new_position)
            print(f"#  ==> {T=}")
            to_check.append(T)
    print(f"#{answers=}")
    return min(answers)

N = int(input().strip())
matrix = [
    list(map(int, input().strip().split(' ')))
    for _ in range(N)
]
print(euler_83(matrix))

