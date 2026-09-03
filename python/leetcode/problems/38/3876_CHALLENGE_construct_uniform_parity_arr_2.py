class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        parity = tuple([
            N % 2
            for N in nums1
        ])
        print(f'{parity=}')

        sum_parity = sum(parity)
        if sum_parity == 0:
            print(f'YES: all even')
            return True
        if sum_parity == len(parity):
            print(f'YES: all odd')
            return True
        min_num = min(nums1)
        min_parity = min_num % 2
        print(f'{min_num=} {min_parity=}')

        if min_parity:
            print(f'YES: minimum is odd')
            return True
        
        print(f'NO:  minimum is even')
        return False

# NOTE: Acceptance Rate 52.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 57 ms Beats 62.80%
# NOTE: Memory 35.78 MB Beats 10.37%
