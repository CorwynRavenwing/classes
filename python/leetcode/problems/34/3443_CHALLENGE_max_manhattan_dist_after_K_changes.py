class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        def nextPosition(position: Tuple[int,int], direction: str) -> Tuple[int,int]:
            (X, Y) = position
            locations = {
                'N': (X - 1, Y),
                'S': (X + 1, Y),
                'E': (X, Y + 1),
                'W': (X, Y - 1),
            }
            return locations[direction]
        
        def manhattan(position: Tuple[int,int]) -> int:
            (X, Y) = position
            return abs(X) + abs(Y)

        origin = (0, 0)
        position = origin
        dist = manhattan(position)
        # print(f'0: ({dist}) {position}')

        distances = []
        moves = Counter()
        opposite = {
            'N': 'S',
            'E': 'W',
        }
        for move in s:
            position = nextPosition(position, move)
            dist = manhattan(position)
            # print(f'{move}: ({dist}) {position}')
            # distances.append(dist)
            moves[move] += 1
            could_fix = 0
            for direction, inverse in opposite.items():
                could_fix += min(moves[direction], moves[inverse])
            # print(f'  {could_fix=} {k=}')
            could_fix = min(could_fix, k)
            if could_fix:
                dist += (2 * could_fix)
                # print(f'    new {dist=}')
            distances.append(dist)
        # print(f'{distances=}')
        return max(distances)

# NOTE: Acceptance Rate 31.4% (medium)

# NOTE: Accepted on third Run (variable typo, needed "* 2")
# NOTE: Accepted on third Submit (Output Exceeded twice)
# NOTE: Runtime 5474 ms Beats 11.72%
# NOTE: Memory 22.26 MB Beats 6.25%
