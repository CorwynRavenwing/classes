class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        
        size = len(nums)
        nums.sort()
        max_answer = 0
        i = 0
        j = 0
        while 0 <= i <= j < size:
            A = nums[i]
            B = nums[j]
            if A * k >= B:
                # print(f'[{i},{j}]: {A}*{k} >= {B}: grow right')
                answer = j - i + 1
                max_answer = max(answer, max_answer)
                # print(f'  {answer=} max={max_answer}')
                j += 1
            else:
                # print(f'[{i},{j}]: {A}*{k} < {B}: shrink left')
                i += 1

        return size - max_answer

# NOTE: Acceptance Rate 41.3% (medium)

# NOTE: Accepted on second Run (forgot to sort)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 159 ms Beats 39.72%
# NOTE: Memory 34.81 MB Beats 6.74%
