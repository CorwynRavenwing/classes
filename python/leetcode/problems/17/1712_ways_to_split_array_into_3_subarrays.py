class Solution:
    def waysToSplit(self, nums: List[int]) -> int:

        mod = 10 ** 9 + 7
        answer = 0

        # if len(nums) < 3:
        #     return 0
        
        # if len(nums) == 3:
        #     (A, B, C) = nums
        #     return (
        #         1
        #         if (A <= B <= C)
        #         else
        #         0
        #     )

        sums = list(itertools.accumulate(nums))
        # print(f'{sums=}')
        Total = sums[-1]
        OneThird = Total // 3
        # print(f'{Total=} {OneThird=}')
        minLwall = 0
        maxLwall = bisect_right(sums, OneThird)
        if maxLwall > 0:
            maxLwall -= 1
        maxLwall = min(maxLwall, len(nums) - 2) # mid and right must not be empty
        if minLwall <= maxLwall:
            print(f'L wall in [{minLwall}..{maxLwall}]')
        else:
            print(f'L wall impossible')
            return 0
        
        for Lwall in range(minLwall, maxLwall + 1):
            left = sums[Lwall]
            print(f'  {Lwall=} {left=}')
            twiceLeft = 2 * left
            remaining = Total - left
            halfRemaining = remaining // 2
            # print(f'    {twiceLeft=} {remaining=} {halfRemaining=}')
            minRwall = bisect_left(sums, twiceLeft)
            minRwall = max(minRwall, Lwall + 1)  # Left must not be empty
            maxRwall = bisect_right(sums, left + halfRemaining)
            maxRwall = min(maxRwall, len(nums) - 1) # right must not be empty
            if maxRwall > 0:
                maxRwall -= 1
            if minRwall <= maxRwall:
                print(f'    R wall in [{minRwall}..{maxRwall}]')
                answer += maxRwall - minRwall + 1
            else:
                print(f'    R wall impossible')
        
        return answer % mod
# NOTE: Runtime 1002 ms; Beats 44.07%
# NOTE: Memory 29.98 MB; Beats 55.37%
