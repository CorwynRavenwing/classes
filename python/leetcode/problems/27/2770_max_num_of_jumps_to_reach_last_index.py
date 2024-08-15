class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        adjacent = {}
        for i, A in enumerate(nums):
            # print(f'[{i}]{A}')
            adjacent.setdefault(i, set())
            for j in range(i + 1, len(nums)):
                B = nums[j]
                # print(f'  [{j}]{B}')
                if -target <= B - A <= target:
                    # print(f'    OK')
                    adjacent[i].add(j)
                # else:
                #     # print(f'    no')
        print(f'{adjacent=}')

        maxJumps = [0] * len(nums)
        for i in range(len(nums)):
            JumpsI = maxJumps[i]
            if i != 0 and JumpsI == 0:
                print(f'  Unreachable')
                continue
            for j in adjacent[i]:
                JumpsJ = maxJumps[j]
                maxJumps[j] = max(
                    JumpsI + 1,
                    JumpsJ
                )
        print(f'{maxJumps=}')
        
        answer = maxJumps[-1]
        return answer if answer else -1
# NOTE: Runtime 810 ms Beats 6.64%
# NOTE: Memory 45.85 MB Beats 5.21%
