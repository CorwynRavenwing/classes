class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        # we borrow some code from #3224:

        REV = lambda x: tuple(reversed(tuple(x)))

        LEN = len(nums)
        HALF = LEN//2
        firstHalf = tuple(nums[:HALF])
        secondRev = REV(nums[HALF:])
        # print(f'{firstHalf=}')
        # print(f'{secondRev=}')

        pairs = tuple(zip(firstHalf, secondRev))
        sums = tuple([A + B for (A, B) in pairs])
        # print(f'{pairs=}')
        # print(f'{sums=}')

        sumCounts = Counter(sums)
        # print(f'{sumCounts=}')

        def movesRequiredToReachX(X: int, pair: Tuple[int,int]) -> int:
            # nonlocal limit
            (A, B) = pair
            total = A + B
            if total == X:
                # print(f'  checkX({X},{pair}): {0}')
                return 0
            needed = [
                N
                for AB in pair
                for N in [X - AB]   # yes, only one thing being looped over
            ]
            allowed = [
                N
                for N in needed
                if 1 <= N <= limit
            ]
            if allowed:
                # print(f'  checkX({X},{pair}): {1}, {allowed=}')
                return 1
            else:
                # print(f'  checkX({X},{pair}): {2}, invalid {needed=}')
                return 2

        def movesRequiredToReachXEverwhere(X: int) -> int:
            # nonlocal pairs
            return sum([
                movesRequiredToReachX(X, pair)
                for pair in pairs
            ])

        movesRequired = []
        for X, count in sumCounts.most_common(100):
            print(f'Trying {X=} ({count=}):')
            moves = movesRequiredToReachXEverwhere(X)
            print(f'  {moves=}')
            movesRequired.append(moves)
        for X, count in [(limit, '=limit')]:
            print(f'Trying {X=} ({count=}):')
            moves = movesRequiredToReachXEverwhere(X)
            print(f'  {moves=}')
            movesRequired.append(moves)

        print(f'{movesRequired=}')
        return min(movesRequired)

# NOTE: timeout for large inputs
