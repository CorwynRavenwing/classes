class Solution:
    def trap(self, height: List[int]) -> int:
        
        print(f'{height=}')
        maxVal = max(height)
        print(f'{maxVal=}')
        MAX = lambda x: tuple(accumulate(x, max))
        REV = lambda x: tuple(reversed(x))
        leftMax = MAX(height)
        print(f'{leftMax =}')
        rightMax = REV(MAX(REV(height)))
        print(f'{rightMax=}')
        level = tuple(
            map(
                min,
                zip(leftMax, rightMax)
            )
        )
        print(f'{level   =}')
        water = [
            L - H
            for H, L in zip(height, level)
        ]
        print(f'{water   =}')

        return sum(water)

# NOTE: Acceptance Rate 63.9% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 43 ms Beats 6.22%
# NOTE: Memory 19.88 MB Beats 6.31%
