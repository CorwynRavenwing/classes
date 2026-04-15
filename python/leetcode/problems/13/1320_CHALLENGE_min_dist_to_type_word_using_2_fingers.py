class Solution:
    def minimumDistance(self, word: str) -> int:
        
        keyboard = [
            'ABCDEF',
            'GHIJKL',
            'MNOPQR',
            'STUVWX',
            "YZ",
        ]
        coords = {
            letter: (x, y)
            for x, row in enumerate(keyboard)
            for y, letter in enumerate(row)
        }
        # print(f'{coords=}')

        @cache
        def manhattan_distance(p1: Tuple[int,int], p2: Tuple[int,int]) -> int:
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)

        def DIST(c1: str, c2: str) -> int:
            if None in (c1, c2):
                return 0
            return manhattan_distance(
                coords[c1],
                coords[c2]
            )

        # print(f'{manhattan_distance((2,3),(5,2))=}')
        # print(f'{DIST('A','Z')=}')
        # print(f'{DIST('X','B')=}')

        @cache
        def DP_moveleft(index: int, leftChar: str, rightChar: str) -> int:
            nextChar = word[index]
            move = DIST(leftChar, nextChar)
            return move + DP(index + 1, nextChar, rightChar)

        @cache
        def DP_moveright(index: int, leftChar: str, rightChar: str) -> int:
            nextChar = word[index]
            move = DIST(rightChar, nextChar)
            return move + DP(index + 1, leftChar, nextChar)

        @cache
        def DP(index: int, leftChar: str, rightChar: str) -> int:
            try:
                _ = word[index]
            except IndexError:
                return 0
            return min([
                DP_moveleft(index, leftChar, rightChar),
                DP_moveright(index, leftChar, rightChar),
            ])

        return DP(0, None, None)

# NOTE: Acceptance Rate 59.7% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Limit Exceeded: added cache)
# NOTE: Runtime 393 ms Beats 15.25%
# NOTE: Memory 77.80 MB Beats 7.91%
