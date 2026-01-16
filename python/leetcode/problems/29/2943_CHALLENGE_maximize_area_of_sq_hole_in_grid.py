class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def maximumAdjacentNumbers(bars: List[int]) -> int:
            bars.sort()
            print(f'maxAN({bars}):')
            adjacent = [
                'Y' if A + 1 == B else 'n'
                for A, B in zip(bars, bars[1:])
            ]
            print(f'  {adjacent=}')
            joined = ''.join(adjacent)
            print(f'  {joined=}')
            divided = joined.split('n')
            print(f'  {divided=}')
            lengths = tuple(map(len, divided))
            print(f'  {lengths=}')
            return max(lengths) + 1     # zip pairs into length of subarray

        H = maximumAdjacentNumbers(hBars)
        V = maximumAdjacentNumbers(vBars)
        
        print(f'{H=} {V=}')
        S = min(H, V)   # make it square
        S += 1          # fenceposts (bars) into fences (regions)
        return S * S

# NOTE: Accepted on first Submit
# NOTE: Runtime 48 ms Beats 80.67%
# NOTE: Memory 16.69 MB Beats 20.67%

# NOTE: Acceptance Rate 41.0% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 3 ms Beats 52.31%
# NOTE: Memory 19.53 MB Beats 13.85%
