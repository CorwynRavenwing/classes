class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        def check(i: int) -> int:
            nonlocal nums
            return (
                1
                if (nums[i] == 1)
                else -1
            )

        # if len(nums) > 1000:
        #     return -99999

        # print(f'{nums=}')
        # counts[i] === (count of "1" in nums[:i+1]) - (count of "0" in nums[:i+1])
        counts = [None] * len(nums)
        counts[0] = check(0)
        for i in range(1, len(nums)):
            counts[i] = counts[i-1] + check(i)
        # print(f'{counts=}')
        # all_counts = list(sorted(set(counts)))
        # print(f'{all_counts=}')
        # L = len(counts)
        # RC = list(reversed(counts))
        answer = 0
        first_pos = {}
        if 0 in counts:
            first_pos[0] = -1
        for last_pos, C in enumerate(counts):
            first_pos.setdefault(C, last_pos)
            A = last_pos - first_pos[C]
            if A:
                print(f'{C=} {first_pos[C]}..{last_pos} = {A}')
                answer = max(answer, A)
        # for C in all_counts:
            # if C == 0:
            #     first_pos = -1
            # else:
            #     first_pos = counts.index(C)
            # last_pos = L - 1 - RC.index(C)
            # A = last_pos - first_pos
            # print(f'{C=} {first_pos}..{last_pos} = {A}')
            # answer = max(answer, A)
        
        return answer

