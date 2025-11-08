class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        @cache
        def DP(nums: List[int]) -> int:
            # print(f'DP({nums})')
            M = min(nums)
            next_level = tuple([
                N - M
                for N in nums
            ])
            answer = M
            if next_level == (0,):
                # print(f'  END')
                return answer
            # print(f'  {next_level=}')
            while next_level:
                if 0 in next_level:
                    index = next_level.index(0)
                    first = next_level[:index]
                    next_level = next_level[index + 1:]
                    if first:
                        # print(f'    {first=}')
                        answer += DP(first)
                else:
                    last = next_level
                    # print(f'    { last=}')
                    answer += DP(last)
                    next_level = []
            return answer

        return DP(tuple(target))

# NOTE: Acceptance Rate 73.0% (HARD)

# NOTE: Output Exceeded; Memory Exceeded.
