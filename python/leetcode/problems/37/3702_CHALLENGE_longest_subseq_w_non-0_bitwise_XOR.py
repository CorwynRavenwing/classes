class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        is_all_zeros = all([
            (N == 0)
            for N in nums
        ])
        if is_all_zeros:
            print(f'all zeros')
            return 0
        
        xor_of_everything = tuple(accumulate(nums, operator.xor))[-1]
        print(f'{xor_of_everything=}')

        len_of_everything = len(nums)
        if xor_of_everything:
            print(f'XOR non-zero: return length')
            return len_of_everything
        else:
            print(f'XOR zero: return one less')
            return len_of_everything - 1

# NOTE: Acceptance Rate 37.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 49 ms Beats 21.77%
# NOTE: Memory 34.48 MB Beats 14.52%
