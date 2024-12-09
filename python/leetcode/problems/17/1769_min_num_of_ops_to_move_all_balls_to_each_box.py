class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        # SHORTCUT 1: the total number of moves, is the number of moves
        # for all balls left of here, plus the number of moves for all
        # balls right of here.  The current box, if non-empty, does not
        # contribute to the total.

        # SHORTCUT 2: these two sets of numbers can be pre-computed.

        def moves_from_one_side(balls: List[int]) -> List[int]:
            answer = []
            total = 0
            moves = 0
            for index, B in enumerate(balls):
                moves += total
                total += B
                answer.append(moves)
            return tuple(answer)

        REV = lambda x: tuple(reversed(tuple(x)))

        nums = tuple(map(int, boxes))

        moves_from_left = moves_from_one_side(nums)
        moves_from_right = REV(moves_from_one_side(REV(nums)))
        print(f'{nums            =}')
        print(f'{moves_from_left =}')
        print(f'{moves_from_right=}')

        answer = tuple(map(sum, zip(moves_from_left, moves_from_right)))
        print(f'{answer          =}')

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 48.45%
# NOTE: Memory 17.97 MB Beats 6.95%
