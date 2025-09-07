class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        # NOTE 0:
        # if the number is already zero, it can be "made" zero
        # in zero operations.
        if num1 == 0:
            return 0
        
        # NOTE 1:
        # If we were just subtracting powers of 2, seeking zero,
        # we could use any number of subtractions between:
        #   min = number of 1's (set bits) in num1
        #       (always subtract 2^B for a set bit B)
        #   max = num1 itself
        #       (always subtract 2^0 === 1)

        def can_become_zero_in_N_binary_moves(num1: int, N: int) -> bool:
            if num1 < 0:
                return False
            boolean = f'{num1:b}'
            bitCounts = Counter(boolean)
            setBits = bitCounts['1']
            # print(f'{num1=} {boolean=} {setBits=}')
            return (
                setBits <= N <= num1
            )

        # NOTE 2:
        # Since instead, we're needing to discover whether
        # or not we can reach zero by subtracting
        # (any power of 2, plus num2) any number of times.

        # NOTE 3:
        # This is equivalent to subtracting num2 any number
        # of times, and seeing if we can reach zero by then
        # subtracting (a power of 2) exactly that many times.

        moves = 0
        print(f'{moves}: {num1}')
        while num1 > 0:
            moves += 1
            num1 -= num2
            print(f'{moves}: {num1}')
            if can_become_zero_in_N_binary_moves(num1, moves):
                return moves
            if moves > 60:
                break
        return -1

# NOTE: Acceptance Rate 30.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 6 ms Beats 8.20%
# NOTE: Memory 17.65 MB Beats 91.80%

# NOTE: re-ran for challenge:
# NOTE: Runtime 7 ms Beats 0.00%
# NOTE: Memory 17.81 MB Beats 44.30%
# NOTE: Wow, I've never had a "beats 0%" score before :-/
