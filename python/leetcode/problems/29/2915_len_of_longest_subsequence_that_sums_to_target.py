class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        # we say "without changing the order", but summation is commutative, so:
        nums.sort()
        bestAnswers = {0: 0}     # { total: length }
        for N in nums:
            print(f'{N=}')
            for (total, length) in tuple(bestAnswers.items()):
                # print(f'  {total}: {length}')
                if total >= target:
                    # print(f'    (skip)')
                    continue
                new_length = length + 1
                new_total = total + N
                if new_total > target:
                    # print(f'    Too big')
                    continue
                bestAnswers.setdefault(new_total, 0)
                old_length = bestAnswers[new_total]
                if new_length > old_length:
                    # print(f'    Update {new_total} ({old_length} -> {new_length})')
                    bestAnswers[new_total] = new_length

        bestAnswers.setdefault(target, -1)
        return bestAnswers[target]
# NOTE: Runtime 1591 ms Beats 96.47%
# NOTE: Memory 17.05 MB Beats 49.88%
