class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:

        REV = lambda x: tuple(reversed(tuple(x)))

        LEN = len(nums)
        HALF = LEN//2
        firstHalf = tuple(nums[:HALF])
        secondRev = REV(nums[HALF:])
        # print(f'{firstHalf=}')
        # print(f'{secondRev=}')

        pairs = tuple(zip(firstHalf, secondRev))
        diffs = tuple([abs(A - B) for (A, B) in pairs])
        # print(f'{pairs=}')
        # print(f'{diffs=}')

        diffCounts = Counter(diffs)
        # print(f'{diffCounts=}')

        def movesRequiredToReachX(X: int, pair: Tuple[int,int]) -> int:
            # nonlocal k
            (A, B) = pair
            diff = abs(A - B)
            if diff == X:
                # print(f'  checkX({X},{pair}): {0}')
                return 0
            needed = [
                N
                for AB in pair
                for N in (AB - X, AB + X)
            ]
            allowed = [
                N
                for N in needed
                if 0 <= N <= k
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
        for X, count in diffCounts.most_common(2):
            print(f'Trying {X=} ({count=}):')
            moves = movesRequiredToReachXEverwhere(X)
            print(f'  {moves=}')
            movesRequired.append(moves)
        
        print(f'{movesRequired=}')
        return min(movesRequired)

# NOTE: Runtime 1266 ms Beats 18.94%
# NOTE: Memory 31.57 MB Beats 29.22%
