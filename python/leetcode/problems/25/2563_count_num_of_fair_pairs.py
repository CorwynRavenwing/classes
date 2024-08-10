class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()
        # print(f'{nums=}')
        answer = 0
        for i, Ni in enumerate(nums):
            # lower <= Ni + Nj --> lower - Ni <= Nj
            # Ni + Nj <= upper --> Nj <= upper - Ni
            min_Nj = lower - Ni
            max_Nj = upper - Ni
            # print(f'{i}: {Ni=}  {min_Nj} <= Nj <= {max_Nj}')
            min_j = bisect_left(nums, min_Nj)
            max_j = bisect_right(nums, max_Nj)
            min_j = max(min_j, i + 1)   # because i < j
            max_j = max(max_j, i + 1)
            count_j = max_j - min_j
            if count_j:
                # print(f'  {min_j} <= j < {max_j}: {count_j=}')
                answer += count_j
            # else:
            #     print(f'  (impossible) {count_j=}')

        return answer
# NOTE: Runtime 709 ms Beats 38.08%
# NOTE: Memory 31.52 MB Beats 12.91%
