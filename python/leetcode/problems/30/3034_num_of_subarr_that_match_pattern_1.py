class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        pattern = ''.join([
            (
                '+' if P == 1 else
                '=' if P == 0 else
                '-' if P == -1 else
                '?'
            )
            for P in pattern
        ])
        print(f'{pattern=}')
        assert '?' not in pattern

        nums = ''.join([
            (
                '+' if B > A else
                '=' if B == A else
                '-' if B < A else
                '?'
            )
            for A, B in pairwise(nums)
        ])
        print(f'{nums=}')
        assert '?' not in nums

        if pattern not in nums:
            return 0
        
        answer = 0
        index = -1
        while True:
            try:
                index = nums.index(pattern, index + 1)
            except ValueError:
                break
            print(f'Found at {index=}')
            answer += 1

        return answer

# NOTE: Acceptance Rate 67.4% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 8 ms Beats 27.31%
# NOTE: Memory 18.16 MB Beats 22.15%
