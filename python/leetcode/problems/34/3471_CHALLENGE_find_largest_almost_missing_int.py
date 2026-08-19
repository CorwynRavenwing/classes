class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        # according to the hints:

        n = len(nums)
        print(f'{n=}')
        freq = Counter(nums)
        print(f'{freq=}')
        occurs_once = {
            value
            for value, count in freq.items()
            if count == 1
        }
        print(f'{occurs_once=}')

        if k == 1:
            print(f'k=1 case')
            return max(occurs_once, default=-1)
        
        if k == n:
            print(f'k=n case')
            return max(nums)
        
        # else
        print(f'1<k<n case')
        answers = [
            value
            for value in (nums[0], nums[-1])
            if value in occurs_once
        ]
        print(f'{answers=}')
        return max(answers, default=-1)

# NOTE: Acceptance Rate 38.9% (easy)

# NOTE: Accepted on second Run (needed second Default= clause)
# NOTE: Accepted on first Submit
# NOTE: Runtime 12 ms Beats 5.74%
# NOTE: Memory 19.36 MB Beats 35.66%
