class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        pairs = [
            (N, i)
            for i, N in enumerate(nums)
        ]
        print(f'raw  {pairs=}')
        pairs.sort()
        print(f'sort {pairs=}')

        locations = [
            i
            for (N, i) in pairs
        ]
        print(f'{locations=}')

        maxRight = [None] * len(locations)
        maxRight[-1] = locations[-1]
        for i, location in reversed(list(enumerate(locations))):
            if i == len(locations) - 1:
                # print(f'{i}: {location} == {maxRight[i]}')
                continue
            maxRight[i] = max(location, maxRight[i + 1])
            # print(f'{i}: {location} -> {maxRight[i]}')
        print(f' {maxRight=}')

        widths = [
            B - A
            for (A, B) in zip(locations, maxRight)
        ]
        print(f'   {widths=}')
        return max(widths)

