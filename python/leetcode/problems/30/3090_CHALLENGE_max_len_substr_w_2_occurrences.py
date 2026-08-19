class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        # we borrow some code from #2958:
        def maxSubarrayLength(nums: List[int], k: int) -> int:
            L = R = 0
            max_size = 0
            # define window === nums[L:R], therefore length === (R - L)
            freq = Counter()
            # print(f'start  [{L}:{R}] ({R-L})')
            # print(f'  {freq=}')
            # A = nums[L]
            while L <= R < len(nums):
                B = nums[R]
                R += 1
                # print(f'grow   [{L}:{R}] ({R-L})')
                freq[B] += 1
                # print(f'  {B=} {freq=}')
                if freq[B] <= k:
                    size = R - L
                    # print(f'  Yes: {size=}')
                    max_size = max(size, max_size)
                    continue
                else:
                    # print(f'  NO! {freq[B]=} > {k}')
                    while freq[B] > k:
                        A = nums[L]
                        L += 1
                        freq[A] -= 1
                        # print(f'shrink [{L}:{R}] ({R-L}) {A=}')
                        if A == B:
                            # print(f'  FOUND')
                            assert freq[B] <= k
                            break
            return max_size
        
        return maxSubarrayLength(s, 2)

# NOTE: Acceptance Rate 66.4% (easy)

# NOTE: re-used entirety of source version
# NOTE: Accepted on second Run (typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 29.86%
# NOTE: Memory 19.28 MB Beats 60.10%
