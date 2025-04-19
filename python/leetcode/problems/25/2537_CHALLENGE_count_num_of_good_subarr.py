class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        numberCounts = Counter()
        pairs = 0
        answer = 0
        L = R = 0
        MAX = len(nums)
        while L <= R <= MAX:
            if pairs < k:
                # print(f'A={answer} [{L}:{R}] {pairs} < {k}: no')
                try:
                    B = nums[R]
                except IndexError:
                    # print(f'  OOB')
                    break
                R += 1
                # print(f'  +{B=}')
                pairs += numberCounts[B]
                numberCounts[B] += 1
                # print(f'  DEBUG C={numberCounts}')
            else:
                # print(f'A={answer} [{L}:{R}] {pairs} >= {k}: YES')
                # add all possible subarrays from L to R or farther right
                answer += 1 + MAX - R
                try:
                    A = nums[L]
                except IndexError:
                    # print(f'  OOB')
                    break
                L += 1
                # print(f'  -{A=}')
                numberCounts[A] -= 1
                pairs -= numberCounts[A]
                # print(f'  DEBUG C={numberCounts}')

        return answer

# NOTE: Accepted on second Run (math error)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 199 ms Beats 14.24%
# NOTE: Memory 34.38 MB Beats 82.85%
