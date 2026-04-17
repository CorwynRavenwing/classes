class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        reverses = {}
        answers = []

        for i, N in enumerate(nums):
            if N in reverses:
                diff = (i - reverses[N])    # abs() not necessary: we're increasing
                answers.append(diff)
                print(f'  Found {N}/{i}: {diff}')
                del reverses[N]     # any future match will be further away
            N_str = f'{N}'
            reverse_str = ''.join(reversed(N_str))
            reverse_N = int(reverse_str)
            print(f'{N} -> {reverse_N}')
            reverses[reverse_N] = i
        
        return min(answers, default=-1)

# NOTE: Acceptance Rate 47.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 807 ms Beats 5.04%
# NOTE: Memory 42.53 MB Beats 28.29%
