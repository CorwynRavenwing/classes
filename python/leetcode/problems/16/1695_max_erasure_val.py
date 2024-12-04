class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        L = 0
        R = L + 1
        # represents range [L:R], L-inclusive, R-exclusive as Python standard
        A = nums[L]
        score = A
        count = Counter()
        count[A] += 1
        max_score = 0
        while 0 <= L < R <= len(nums):
            # print(f'[{L}:{R}]: {R-L=} {len(count)=} {score} {count}')
            # if max(count.values()) == 1:
            # ... much faster version without running values() and max() every loop
            if (R - L) == len(count):
                # unique: score and expand right
                max_score = max(score, max_score)
                try:
                    B = nums[R]
                except IndexError:
                    break
                score += B
                count[B] += 1
                R += 1
            else:
                # not unique: contract left
                A = nums[L]
                score -= A
                count[A] -= 1
                if not count[A]:
                    del count[A]
                L += 1

        return max_score

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded; Time Limit Exceeded)
# NOTE: Runtime 598 ms Beats 10.71%
# NOTE: Memory 28.64 MB Beats 54.18%
