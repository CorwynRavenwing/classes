class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        INF = 10 ** 5   # higher than any possible nums[i]

        answers = []
        for initial in [0, 1]:
            print(f'{initial=}')
            changes = 0
            for i in range(initial, len(nums)+1+initial, 2):
                try:
                    A = (nums[i - 1] if i else INF)
                    B = nums[i]
                except IndexError:
                    continue
                # a separate try/catch because this error
                # only uses a default C value
                try:
                    C = nums[i + 1]
                except IndexError:
                    C = INF
                print(f'({i-1},{i},{i+1}): ({A},{B},{C})')
                target = min(A,C) - 1
                if B <= target:
                    print(f'  (ok)')
                    continue
                else:
                    print(f'  -{B - target}')
                    changes += B - target
            print(f'Grand total {changes=}')
            answers.append(changes)
        
        return min(answers)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was array fencepost OOB)
# NOTE: Runtime 3 ms Beats 17.86%
# NOTE: Memory 16.71 MB Beats 25.54%
